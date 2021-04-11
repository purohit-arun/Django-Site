from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context ={
        "variable": "This is variable"
    }
    return render(request,'index.html',context)
    
def about(request):
    if request.method == 'POST':
        name = request.POST.get('name1')
        email = request.POST.get('email1')
        desc = request.POST.get('feedback')
        contact = Contact(name=name, email=email, desc= desc)
        contact.save()
        messages.success(request, 'Your response has been submitted')
    return render(request,'about.html')
