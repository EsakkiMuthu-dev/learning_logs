from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    """Form definition for Topic."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Topic
        fields = ['text']
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Entry
        fields = ['text']
        labels ={'text':'entry'}
        widgets ={'text':forms.Textarea(attrs={'cols':80})}
