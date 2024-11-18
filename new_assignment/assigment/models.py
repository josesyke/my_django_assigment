
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator

class MessageForm(forms.Form):
    receiver_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    receiver_email = forms.EmailField(widget=forms.EmailInput(attrs={'readonly': 'readonly'}))
    email_title = forms.CharField(max_length=255)
    message_body = forms.CharField(widget=forms.Textarea)
    sender_name = forms.CharField(max_length=100)
    sender_email = forms.EmailField()
    sender_phone = forms.CharField(max_length=20)

    def clean_receiver_email(self):
        email = self.cleaned_data.get('receiver_email')
        
        # Using Django's built-in EmailValidator to validate email format
        email_validator = EmailValidator()
        try:
            # This will raise a ValidationError if the email is invalid
            email_validator(email)
        except ValidationError:
            raise ValidationError("Invalid email format for the recipient.")
        
        return email
