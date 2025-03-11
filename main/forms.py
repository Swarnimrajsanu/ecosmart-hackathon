from django import forms
from .models import WasteCollectionRequest, WasteClassification, ChatMessage

class WasteCollectionRequestForm(forms.ModelForm):
    class Meta:
        model = WasteCollectionRequest
        fields = ['category', 'address', 'description', 'quantity', 'preferred_date']
        widgets = {
            'preferred_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class WasteClassificationForm(forms.ModelForm):
    class Meta:
        model = WasteClassification
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['content']
        labels = {
            'content': '',
        }
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ask a question about waste management...',
                'autocomplete': 'off'
            }),
        } 