from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.db import models
import uuid
from .models import WasteCategory, WasteCollectionRequest, RecyclingCenter, EducationalContent, WasteClassification, ChatMessage, RoofPlantation, RoofPlantationProduct
from .forms import WasteCollectionRequestForm, WasteClassificationForm, ChatMessageForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .ai_utils import classify_waste_image, get_chatbot_response

def home(request):
    categories = WasteCategory.objects.all()
    educational_content = EducationalContent.objects.all().order_by('-created_at')[:3]
    return render(request, 'main/home.html', {
        'categories': categories,
        'educational_content': educational_content
    })

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def request_collection(request):
    if request.method == 'POST':
        form = WasteCollectionRequestForm(request.POST)
        if form.is_valid():
            collection_request = form.save(commit=False)
            collection_request.user = request.user
            collection_request.save()
            messages.success(request, 'Collection request submitted successfully!')
            return redirect('my_requests')
    else:
        form = WasteCollectionRequestForm()
    return render(request, 'main/request_collection.html', {'form': form})

@login_required
def my_requests(request):
    requests = WasteCollectionRequest.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/my_requests.html', {'requests': requests})

def recycling_centers(request):
    centers = RecyclingCenter.objects.all()
    categories = WasteCategory.objects.all()
    
    # If there are no centers, create a sample one for demonstration
    if not centers.exists() and categories.exists():
        sample_center = RecyclingCenter(
            name="EcoSmart Recycling Center",
            address="123 Green Street, Eco City, 110001",
            phone="+91 98765 43210",
            email="contact@ecosmart-recycling.com",
            website="https://www.ecosmart-recycling.com",
            description="Our main recycling center accepts a wide variety of waste materials. We focus on sustainable recycling practices and community education.",
            opening_hours="Monday to Saturday: 9:00 AM - 6:00 PM, Sunday: Closed",
            latitude=28.6139,
            longitude=77.2090
        )
        sample_center.save()
        
        # Add some categories to the sample center
        for category in categories[:3]:  # Add first 3 categories
            sample_center.categories_accepted.add(category)
        
        # Refresh the centers queryset
        centers = RecyclingCenter.objects.all()
    
    return render(request, 'main/recycling_centers.html', {
        'centers': centers,
        'categories': categories
    })

def educational_content(request):
    content = EducationalContent.objects.all().order_by('-created_at')
    return render(request, 'main/educational_content.html', {'content': content})

@login_required
def cancel_request(request, request_id):
    collection_request = get_object_or_404(WasteCollectionRequest, id=request_id, user=request.user)
    if collection_request.status == 'pending':
        collection_request.status = 'cancelled'
        collection_request.save()
        messages.success(request, 'Request cancelled successfully!')
    return redirect('my_requests')

# AI Features

def waste_classifier(request):
    """View for waste classification using AI"""
    if request.method == 'POST':
        form = WasteClassificationForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form but don't commit yet
            classification = form.save(commit=False)
            
            # Associate with user if logged in
            if request.user.is_authenticated:
                classification.user = request.user
            
            # Get the uploaded image
            image_file = request.FILES['image']
            
            # Classify the image
            predicted_category, confidence = classify_waste_image(image_file)
            
            # Update the classification object
            classification.predicted_category = predicted_category
            classification.confidence_score = confidence
            classification.save()
            
            return render(request, 'main/classification_result.html', {
                'classification': classification,
                'form': WasteClassificationForm()
            })
    else:
        form = WasteClassificationForm()
    
    # Get recent classifications for the user
    recent_classifications = []
    if request.user.is_authenticated:
        recent_classifications = WasteClassification.objects.filter(
            user=request.user
        ).order_by('-created_at')[:5]
    
    return render(request, 'main/waste_classifier.html', {
        'form': form,
        'recent_classifications': recent_classifications
    })

def chatbot(request):
    """View for AI chatbot"""
    # Generate or get session ID
    if 'chat_session_id' not in request.session:
        request.session['chat_session_id'] = str(uuid.uuid4())
    
    session_id = request.session['chat_session_id']
    
    # Get chat history
    chat_history = ChatMessage.objects.filter(session_id=session_id).order_by('created_at')
    
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            # Save user message
            user_message = form.save(commit=False)
            user_message.message_type = 'user'
            user_message.session_id = session_id
            if request.user.is_authenticated:
                user_message.user = request.user
            user_message.save()
            
            # Get response from AI
            response_text = get_chatbot_response(
                user_message.content, 
                conversation_history=chat_history
            )
            
            # Save assistant response
            assistant_message = ChatMessage(
                message_type='assistant',
                content=response_text,
                session_id=session_id,
                user=request.user if request.user.is_authenticated else None
            )
            assistant_message.save()
            
            # If AJAX request, return JSON response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'user_message': user_message.content,
                    'assistant_message': response_text
                })
            
            # Otherwise redirect to refresh the page
            return redirect('chatbot')
    else:
        form = ChatMessageForm()
    
    return render(request, 'main/chatbot.html', {
        'form': form,
        'chat_history': chat_history
    })

def roof_plantation(request):
    """View for the urban roof plantation page"""
    plantations = RoofPlantation.objects.all().order_by('-is_featured', '-created_at')
    featured_plantations = plantations.filter(is_featured=True)[:3]
    
    # Get featured products for the shop section
    featured_products = RoofPlantationProduct.objects.filter(is_featured=True, is_available=True)[:4]
    
    context = {
        'plantations': plantations,
        'featured_plantations': featured_plantations,
        'featured_products': featured_products,
    }
    
    return render(request, 'main/roof_plantation.html', context)

def roof_plantation_shop(request, category=None):
    """View for the roof plantation shop page"""
    products = RoofPlantationProduct.objects.filter(is_available=True)
    
    # Filter by category if provided
    if category:
        products = products.filter(category=category)
    
    # Get all available categories for the filter
    categories = RoofPlantationProduct.CATEGORY_CHOICES
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': category,
    }
    
    return render(request, 'main/roof_plantation_shop.html', context)

def product_detail(request, product_id):
    """View for the product detail page"""
    product = get_object_or_404(RoofPlantationProduct, id=product_id, is_available=True)
    
    # Get related products in the same category
    related_products = RoofPlantationProduct.objects.filter(
        category=product.category, 
        is_available=True
    ).exclude(id=product.id)[:4]
    
    context = {
        'product': product,
        'related_products': related_products,
    }
    
    return render(request, 'main/product_detail.html', context)

def card_image_guide(request):
    """View for the card image guide page"""
    return render(request, 'main/card_image_guide.html')
