from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='main/logout.html'), name='logout'),
    path('request-collection/', views.request_collection, name='request_collection'),
    path('my-requests/', views.my_requests, name='my_requests'),
    path('recycling-centers/', views.recycling_centers, name='recycling_centers'),
    path('educational-content/', views.educational_content, name='educational_content'),
    path('cancel-request/<int:request_id>/', views.cancel_request, name='cancel_request'),
    
    # AI Features
    path('waste-classifier/', views.waste_classifier, name='waste_classifier'),
    path('chatbot/', views.chatbot, name='chatbot'),
    
    # Guides
    path('guides/card-images/', views.card_image_guide, name='card_image_guide'),
    
    # Urban Initiatives
    path('urban-roof-plantation/', views.roof_plantation, name='roof_plantation'),
    path('urban-roof-plantation/shop/', views.roof_plantation_shop, name='roof_plantation_shop'),
    path('urban-roof-plantation/shop/category/<str:category>/', views.roof_plantation_shop, name='roof_plantation_shop_category'),
    path('urban-roof-plantation/shop/product/<int:product_id>/', views.product_detail, name='product_detail'),
] 