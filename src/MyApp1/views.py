from MyApp1.forms import MyForm, CommentForm
from django.shortcuts import render, redirect
from datetime import date
from MyApp1.models import Request, Comment

def index_page(request):

    if request.method == 'POST':
        today = date.today()
        form = Request(name=request.POST['name'], mail=request.POST['mail'],
                       phone=request.POST['phone'], message=request.POST['message'],
                       date=today.strftime('%d.%m.%Y'))
        form.save()
        return redirect('index')
    else:
        form = MyForm()

    return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def contact_page(request):

    if request.method == 'POST':
        today = date.today()
        form = Request(name=request.POST['name'], mail=request.POST['mail'],
                       phone=request.POST['phone'], message=request.POST['message'],
                       date=today.strftime('%d.%m.%Y'))
        form.save()
        return redirect('contact')
    else:
        form = MyForm()

    return render(request, 'contact.html')

def events_page(request):
    return render(request, 'events.html')

def trainers_page(request):

    if request.method == 'POST':
        today = date.today()
        form = Comment(name=request.POST['name'],
                       message=request.POST['message'],
                       date=today.strftime('%d.%m.%Y'))
        form.save()
        return redirect('trainers')
    else:
        form = CommentForm()

    comms = Comment.objects.all()

    return render(request, 'trainers.html', context={'comms': comms})