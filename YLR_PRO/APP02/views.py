from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
def base(request):
    if request.method=='GET':
        # print(request.body)
        # print(request.GET)
        print(request.META)
        print(request.path)
        # return HttpResponse('123123')
        return render(request, 'base.html')
    else:
        print(request.body)

def login2(request):
    print(request.path)
    print(request.get_full_path())
    return render(request,'login2.html')