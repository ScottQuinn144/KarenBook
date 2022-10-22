from django import forms
from .models import Posts


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'rows':10, 'cols':30,
                "placeholder": " What's on your mind?",
            }
        ),
        label="",
    )

    class Meta:
        model = Posts
        exclude = ("user", )
