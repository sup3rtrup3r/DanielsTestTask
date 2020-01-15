from django import forms
from django_registration.forms import RegistrationForm
from app.models import CustomUser, Product


class CustomUserForm(RegistrationForm):

    class Meta(RegistrationForm.Meta):
        model = CustomUser
        fields = ["username", "email"]


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category',)
        widgets = {
            'category': forms.RadioSelect,
        }
