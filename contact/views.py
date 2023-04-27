from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Contact
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.core import mail
from .forms import ContactForm
# Create your views here.
# def contact(request):
#     if request.method=='POST':
#         listing=request.POST['listing']
#         listing_id=request.POST['listing_id']
#         name=request.POST['name']
#         email=request.POST['email']
#         phone=request.POST['phone']
#         message=request.POST['message']
#         user_id=request.POST['user_id']
#         if request.user.is_authenticated:
#             user_id=request.user.id
#             has_contacted=Contact.objects.filter(user_id=user_id,listing_id=listing_id)
#             if has_contacted:
#                 messages.error(request, 'already sent message')
#                 return HttpResponseRedirect(reverse('listing', args=[listing_id]))
#         contact=Contact(
#             listing=listing,
#             listing_id=listing_id,
#             name=name,
#             email=email,
#             phone=phone,
#             message=message,
#             user_id=user_id,
#         )

#         contact.save()
        
#         connection = mail.get_connection()

#         # Manually open the connection
#         connection.open()

#         # Construct an email message that uses the connection
#         email1 = mail.EmailMessage(
#             'Propriety sending inquiry',
#             'there has been an inquiry for '+listing+' sign in to admin panel to check',
#             'a_bachir@enst.dz',
#             ['arachid663@gmail.com','a_bachir@enst.dz'],
#             connection=connection,
#         )
#         email1.send() # Send the email
#         # send_mail(
#         #     'Propriety sending inquiry',
#         #     'there has been an inquiry for'+listing+'sign in to admin panel to check',
#         #     'a_bachir@enst.dz',
#         #     ['arachid663@gmail.com','a_bachir@enst.dz'],
#         #     fail_silently=True,
            
#         # )
#         messages.success(request, 'enquiry successfully sent.')
#         return HttpResponseRedirect(reverse('listing', args=[listing_id]))


def Contact(request):
    form=ContactForm
    return HttpResponseRedirect(reverse('listings'))

