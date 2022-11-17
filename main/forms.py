from django import forms

from main.models import Shortener


class ShortenerForm(forms.ModelForm):
    full_url = forms.URLField(
        widget=forms.URLInput(attrs={"class": "form-control form-control-lg",
                                     'placeholder': 'Введите ссылку'})
    )

    class Meta:
        model = Shortener
        fields = ('full_url',)
