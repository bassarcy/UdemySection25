from .models import Profile
from django import forms
from django.contrib.auth.models import User

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']

    image = forms.ImageField()
    


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].initial = self.instance.profile.image
        self.fields['first_name'].initial = self.instance.profile.first_name
        self.fields['last_name'].initial = self.instance.profile.last_name
        
        

    def save(self, commit=True):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        user = self.instance
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        profile = super().save(commit=commit)
        profiles = user.profile
        profiles.image = self.cleaned_data['image']
        if commit:
            profiles.save()
        return profile

    def clean_username(self):
        new_username = self.cleaned_data.get('username')

        return new_username


