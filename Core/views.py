from django.shortcuts import render
from .models import Messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        message = request.POST.get("message")
        messageObject = Messages.objects.create(fname=fname,lname=lname,email=email,message=message)
        messageObject.save()
    return render(request,'Core/index.html')