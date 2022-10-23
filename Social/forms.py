from django import forms
from .models import Posts, Comment


class PostForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                'rows':5, 'cols':30,
                "placeholder": " What's on your mind?",
            }
        ),
        label="",
    )

    class Meta:
        model = Posts
        exclude = ("user", )


class CommentForm(forms.ModelForm):
    body = forms.CharField(label='')
    class Meta:
        model = Comment
        fields = ('body',)
