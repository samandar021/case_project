from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person ,Info


# получение данных из бд
def index(request):
    people = Person.objects.all()
    return render(request, "index.html", {"people": people})


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        tom = Person()
        tom.firstname = request.POST.get("firstname")
        tom.id = request.POST.get('student_id')
        tom.phonenumber = request.POST.get('phonenumber')
        tom.email = request.POST.get('email')
        tom.studentreg_no = request.POST.get('studentreg_no')
        tom.birthdate = request.POST.get("birthdate")
        tom.lastname = request.POST.get('lastname')
        tom.save()
    return HttpResponseRedirect("/")

def take(request):
    if request.method =='POST':



# Create your views here.
