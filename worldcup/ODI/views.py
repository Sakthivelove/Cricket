from ast import And
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Book,Matches
from django.contrib import messages
from django.http import JsonResponse
import logging
logger = logging.getLogger('django')





# Create your views here.
def index (request): 
     return render(request,"index.html") 

def booking (request):  # 127.0.0.1:8000/
    mydata=Matches.objects.all()
    
    if(mydata!=""):
        
        return render(request,"booking.html",{"matches":mydata})

    

def addrecord(request):
     
  a = request.POST.get('team1')
  b = request.POST.get('team2')
  c = request.POST.get('venue')
  d = request.POST.get('date')
  e = request.POST.get('adult')
  f = request.POST.get('children')
 
  list = Book(Team1=a, Team2=b, Venue=c, Date=d, Adult=e, Children=f)
  list.save()
  messages.success(request,"Ticket Booked Successfully")
  return HttpResponseRedirect(reverse('booklist'))   
 
    
def booklist (request):  # 127.0.0.1:8000/
    list=Book.objects.all()
    
    if(list!=""):
        
        return render(request,"booklist.html",{"matches":list})
     

def delete(request,id):
    list=Book.objects.get(id=id)
    list.delete()
    return HttpResponseRedirect(reverse('booklist'))

def final1 (request): 
     return render(request,"1975.html") 

def final2 (request): 
     return render(request,"1979.html") 

def final3 (request): 
     return render(request,"1983.html")

def final4 (request): 
     return render(request,"1987.html")

def final5 (request): 
     return render(request,"1992.html")

def final6 (request): 
     return render(request,"1996.html")

def final7 (request): 
     return render(request,"1999.html")

def final8 (request): 
     return render(request,"2003.html")

def final9 (request): 
     return render(request,"2007.html")

def final10 (request): 
     return render(request,"2011.html")

def final11 (request): 
     return render(request,"2015.html")

def final12 (request): 
     return render(request,"2019.html")

def get_topics_ajax(request):
    if request.method == "POST":
        teamId = request.POST['teamId']
        try:
            #team2 = Matches.objects.filter(id = teamId).first()
            matches = Matches.objects.filter(Team2 = teamId)
            
        except Exception:
            messages['error_message'] = 'error'
            return JsonResponse(messages)
        return JsonResponse(list(matches.values('id', 'Venue','Date')), safe = False) 