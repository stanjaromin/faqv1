from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the question'}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the answer'}),
        }