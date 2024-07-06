from django.shortcuts import render,HttpResponse
from.models import BloodDonor
from django.contrib import messages
def home(request):
    return render(request,'home.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        bloodgroup = request.POST.get("bloodgroup")
        
        city = request.POST.get("city")
        phonenumber = request.POST.get("phonenumber")
        x=BloodDonor(name=name,age=age,gender=gender,bloodgroup=bloodgroup,city=city,phonenumber=phonenumber)
        x.save()
        messages.success(request, "Donor registered successfully")
    return render(request,'form.html')

def search(request):
    y=''
    z=False
    if request.method=="POST":
        bg = request.POST.get("bg")
        y = BloodDonor.objects.filter(bloodgroup__contains=bg)
        if not y:
            z=True
    return render(request,'search.html',{'y':y,'z':z})

