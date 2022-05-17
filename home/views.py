from django.shortcuts import render
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request): 
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')


def test(request):
    return render(request, 'test.html')

def tutoring(request):
    return render(request, "tutoring.html")

def contact(request):
    if request.method=="POST":
        name= request.POST['name']
        email= request.POST['email']
        phone= request.POST['phone']
        message= request.POST['message']
        

        if len(name)<2 or len(email)<2 or len(phone)<10 or len(message)<5:
            messages.error(request, "Message not sent")
        else:
            contact= Contact(name= name, email= email, phone= phone, message= message)
            contact.save()
    return render(request, "contact.html")