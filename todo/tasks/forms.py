from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New Task...'}))
    priority = forms.ChoiceField(choices=Task.priorities)

    class Meta:
        model = Task
        fields = '__all__'
