from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class WasteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='category_icons/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class WasteCollectionRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE)
    address = models.TextField()
    description = models.TextField()
    quantity = models.CharField(max_length=50)
    preferred_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s {self.category.name} collection request"

class RecyclingCenter(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='recycling_centers/', null=True, blank=True)
    categories_accepted = models.ManyToManyField(WasteCategory)
    opening_hours = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    
    def __str__(self):
        return self.name

class EducationalContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='educational_content/', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

class WasteClassification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='waste_classifications/')
    predicted_category = models.ForeignKey(WasteCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='classifications')
    confidence_score = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        category_name = self.predicted_category.name if self.predicted_category else "Unknown"
        return f"Classification: {category_name} ({self.confidence_score:.2f})"

class ChatMessage(models.Model):
    MESSAGE_TYPES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=100)
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f"{self.message_type}: {self.content[:50]}..."

class RoofPlantation(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    area = models.DecimalField(max_digits=10, decimal_places=2, help_text="Area in square meters")
    plant_types = models.TextField(help_text="Types of plants used in this plantation")
    benefits = models.TextField(help_text="Environmental and social benefits of this plantation")
    implementation_date = models.DateField()
    maintenance_tips = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='roof_plantations/', null=True, blank=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class RoofPlantationProduct(models.Model):
    CATEGORY_CHOICES = [
        ('seeds', 'Seeds & Plants'),
        ('soil', 'Soil & Fertilizers'),
        ('containers', 'Containers & Planters'),
        ('tools', 'Gardening Tools'),
        ('irrigation', 'Irrigation Systems'),
        ('accessories', 'Accessories'),
    ]
    
    name = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='roof_plantation_products/')
    is_featured = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_discount_percentage(self):
        if self.discount_price:
            discount = ((self.price - self.discount_price) / self.price) * 100
            return round(discount)
        return 0
