from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Contact

# Create your views here.
def home(request):

    if request.method == 'POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phoneNumber = request.POST['phoneNumber']
        email = request.POST['email']
        message = request.POST['message']
        
        return redirect('home')
    else: 
        return render(request, "home.html")
    
    # contact = Contact.objects.all()
    # return render(request, 'home.html', {'contact': contact})

def contact(request):
    # if request.method == 'POST':
    #     pass
    # else:
    return render(request, 'contact.html')
