from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

from .models import Grades, Students


def index(rquest):
    return HttpResponse("<h1 style='colour:red')>这个页面可以正常工作了</h1>")


def detail1(request,num):
    return HttpResponse("detail-%s"%num)

def detail2(request,num1,num2):
    return HttpResponse('detail-%s-%s'%(num1,num2))



def grades(request):
    # 去models取数据
    gradelist = Grades.objects.all()
    # 将数据传递给模板,由模板渲染页面再将渲染好的页面传递给浏览器
    return render(request,'myapp/grades.html',{'grades':gradelist})

def students(reques):
    studentlist = Students.objects.all()
    return render(reques,'myapp/students.html',{'students':studentlist})


def gradestudents(request,num):
    grade = Grades.objects.get(pk=num)
    studentlist = grade.students_set.all()
    return render(request,'myapp/students.html',{'students':studentlist})



def attribles(request):
    print(request.path)
    print(request.encoding)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse('this is a Attribles Object.')

def get1(request):
    a = request.GET.get('a','')
    b = request.GET.get('b', '')
    c = request.GET.get('c', '')
    return HttpResponse(a + '   ' + b + '   ' + c)


def get2(request):
    a = request.GET.getlist('a')
    a1 = a[0]
    a2 = a[1]
    b = request.GET.get('b','')
    c = request.GET.get('c','')
    return HttpResponse(a1 + ' ' + a2 + ' ' + b + ' ' + c)

def showregist(request):
    return render(request,'myapp/regist.html')

def regist(request):
    request.POST.get('name')
    return HttpResponse('您已注册成功！')
