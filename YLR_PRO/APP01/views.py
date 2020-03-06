from django.shortcuts import render,redirect

# Create your views here.
def login1(request):
    if request.method=='GET':
        return render(request,'login1.html')
    else:
        return redirect('/APP01/home/')
def home(request):
    return render(request,'home.html')