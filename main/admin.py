from django.contrib import admin
from .models import WasteCategory, WasteCollectionRequest, RecyclingCenter, EducationalContent, RoofPlantation, RoofPlantationProduct

@admin.register(WasteCategory)
class WasteCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

@admin.register(WasteCollectionRequest)
class WasteCollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'status', 'preferred_date', 'created_at')
    list_filter = ('status', 'category', 'preferred_date')
    search_fields = ('user__username', 'address', 'description')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(RecyclingCenter)
class RecyclingCenterAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'has_coordinates')
    search_fields = ('name', 'address', 'phone', 'email')
    filter_horizontal = ('categories_accepted',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'image')
        }),
        ('Contact Details', {
            'fields': ('address', 'phone', 'email', 'website')
        }),
        ('Operation Details', {
            'fields': ('opening_hours', 'categories_accepted')
        }),
        ('Map Coordinates', {
            'fields': ('latitude', 'longitude'),
            'description': 'Coordinates for map placement (decimal degrees)'
        }),
    )
    
    def has_coordinates(self, obj):
        return obj.latitude is not None and obj.longitude is not None
    has_coordinates.boolean = True
    has_coordinates.short_description = 'Map Location'

@admin.register(EducationalContent)
class EducationalContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

@admin.register(RoofPlantation)
class RoofPlantationAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'area', 'implementation_date', 'is_featured')
    list_filter = ('is_featured', 'implementation_date')
    search_fields = ('title', 'description', 'location', 'plant_types', 'benefits')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'location', 'area', 'image')
        }),
        ('Plantation Details', {
            'fields': ('plant_types', 'benefits', 'implementation_date', 'maintenance_tips')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'contact_phone')
        }),
        ('Settings', {
            'fields': ('is_featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(RoofPlantationProduct)
class RoofPlantationProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'discount_price', 'stock', 'is_available', 'is_featured')
    list_filter = ('category', 'is_available', 'is_featured')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Product Information', {
            'fields': ('name', 'description', 'category', 'image')
        }),
        ('Pricing & Inventory', {
            'fields': ('price', 'discount_price', 'stock', 'is_available')
        }),
        ('Settings', {
            'fields': ('is_featured',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
