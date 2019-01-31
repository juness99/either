from django.shortcuts import render,redirect
# Create your views here.
from .models import Choice,Answer
def index(request):
    choices = Choice.objects.all()
    
    return render(request,"choice/index.html",{'choices':choices})
    
def new(request):
    
    return render(request,"choice/new.html")
    
def create(request):
    title = request.POST.get("title")
    content = request.POST.get("content")
    content_2 = request.POST.get("content_2")
    
    Choice.objects.create(title=title, content=content ,content_2=content_2)
    
    return redirect("/choices/")
    
def read(request,id):
    choice = Choice.objects.get(pk=id)
    
    return render(request,"choice/read.html",{'choice':choice})
    

def edit(request,id):
    choice = Choice.objects.get(pk=id)
    return render(request,"choice/edit.html",{'choice':choice})
    
def update(request,id):
    
    choice = Choice.objects.get(pk=id)
    
    title = request.POST.get("title")
    content = request.POST.get("content")
    content_2 = request.POST.get("content_2")
    
    choice.title = title
    choice.content = content
    choice.content_2 = content_2
    choice.save()
    
    return redirect(f"/choices/{id}/")
    
def delete(request,id):
    choice = Choice.objects.get(pk=id)
    
    choice.delete()
    
    return redirect("/choices/")

def comment_create(request,id):
    choice = Choice.objects.get(pk=id)
    content= request.POST.get("content")
    q= request.POST.get("q")
    w= request.POST.get("W")
    if content == "1":
        choice.q +=1
        choice.save()
    else:
        choice.w +=1
        choice.save()
    
    Answer.objects.create(choice=choice,content=content)
    
    return redirect(f"/choices/{id}/")