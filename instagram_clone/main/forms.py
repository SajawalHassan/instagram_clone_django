from django import forms
from .models import Post

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('username', 'img_url', 'description')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            'img_url': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Enter image url'}),
            'description': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
        }
