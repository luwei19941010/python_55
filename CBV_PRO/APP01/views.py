from django.shortcuts import render,HttpResponse
from django.views import View
from django.utils.decorators import method_decorator

# Create your views here.

#在执行get方法前作操作
# class Login_view(View):
#     def dispatch(self, request, *args, **kwargs):
#         print('请求来了')
#         ret=super().dispatch(request, *args, **kwargs)
#         return ret
#     def get(self,request):
#         return render(request,'base.html')

def n1(f):
    def n2(*args,**kwargs):
        print('123')
        ret=f(*args,**kwargs)
        return ret
    return n2

class Login_view(View):
    @method_decorator(n1)
    def dispatch(self, request, *args, **kwargs):
        ret=super().dispatch(request,*args,**kwargs)
        return ret
    # @method_decorator(n1)#方式一
    def get(self,request):
        return render(request,'base.html')
    def post(self,request):
        print(request.POST.get('user'),request.POST.get('psd'))
        return HttpResponse('successful')

#
# @n1
# def func():
#     print('123')