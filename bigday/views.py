from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import *
from .forms import contact_form
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.shortcuts import redirect

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    if request.method == 'GET':
        form = contact_form()
    else:
        form = contact_form(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
            try:
                send_mail(contact_name, contact_message, contact_email, ['noemie.ruizhi@gmail.com'])
                messages.success(request, 'Successfully Sent The Message!')
                form = contact_form()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

    return render(request, "base.html", {'form': form})

# def contact(request):
#     if request.method == 'GET':
#         form = contact_form()
#     else:
#         form = contact_form(request.POST)
#         if form.is_valid():
#             contact_name = form.cleaned_data['contact_name']
#             contact_email = form.cleaned_data['contact_email']
#             contact_message = form.cleaned_data['contact_message']
#             try:
#                 send_mail(contact_name, contact_message, contact_email, ['noemieruizhi@gmail.com'])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('success')
#     return render(request, "contact.html", {'form': form})


def success(request):
    return HttpResponse('Success! Thank you for your message.')