from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_connected:
                messages.error(request, 'You have already made an inquiry for this listing.')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
        contact.save()

        # # Email Sending
        # send_mail(
        #     'Property Listing Industry',
        #     'There has been an inquiry for' + listing + '. Sign in to the admin panel for more info',
        #     'macmacquisel@gmail.com',
        #     [realtor_email, 'dwarfinyoloban@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your inquiry has been submitted. Just wait and check back your email or sms for the feedback of the realtor')

        return redirect('/listings/'+listing_id)