from django.forms import ModelForm, TextInput, Textarea
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'content': Textarea(attrs={'class': 'form-control'})
        }
