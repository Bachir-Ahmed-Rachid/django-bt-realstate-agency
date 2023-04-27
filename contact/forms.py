from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        exclude=['user_id','listing_id','listing']
        labels={
            "property":"Property",
            "name":"Name",
            "email":"Email",
            "phone":"Phone",
            "message":"Message",
        }
        error_message={
            "property":{
                "max_length":"max 20"
            }
        }
