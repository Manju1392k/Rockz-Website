
from django.forms import ModelForm
from django import forms
from .models import RocketBlog

class RocketBlogForm(ModelForm):
    class Meta:
        model = RocketBlog
        fields = ['Rocket_Name','Rocket_LaunchDate', 'Rocket_LandingDate', 'Rocket_Image']

    Rocket_Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputags'}))
    Rocket_LaunchDate = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputags'}))
    Rocket_LandingDate = forms.CharField(widget=forms.TextInput(attrs={'class': 'inputags'}))
    Rocket_Image = forms.FileField(widget=forms.FileInput(attrs={'class': 'imgtag'}))