from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['text', 'photo']
        
    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if not photo:
            raise forms.ValidationError("\u200B")
        return photo    
    