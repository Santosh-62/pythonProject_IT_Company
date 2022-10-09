from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from.models import user

# Create your views here.

#def index(request):
#     return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def gallery(request):
    return render(request, 'gallery.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def index(request):
    if 'user' in request.session:
        current_user=request.session['user']
        param={'current_user': current_user}
        return render(request,'index.html', param)
    else:
        return redirect('login')
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        uname=request.POST.get('uname')
        pwd=request.POST.get('pwd')
        eml=request.POST.get('eml')
        error_name=[]

        if user.objects.filter(username=uname).count() >0:
            error_name='the username already exists'
            return render(request, 'register.html', {'error_name': error_name})
        else:
            User=user(username=uname,email=eml,password=pwd)
            User.save()
            return redirect('login')
    else:
        return render(request,'register.html',)


def login(request):
    if request.method=='POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')

        check_user=user.objects.filter(username=uname,password=pwd)
        if check_user:
            request.session['user'] = uname

            return redirect('index')
        error = 'wrong username and password'

    return render(request,'login.html',locals())

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
