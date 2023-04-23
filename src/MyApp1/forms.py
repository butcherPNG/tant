from datetime import date
from django.utils import timezone

from MyApp1.models import Request, Comment
from django import forms

class MyForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('name', 'mail', 'phone', 'message', 'date')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'message', 'date')

