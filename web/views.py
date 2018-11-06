from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from web.models import Signup


def index(request):
    # id = request.POST['id']
    # pw = request.POST['pw']
    #
    # try:
    #     Signup.objects.get(id=id, pw=pw)

        # request.session['id'] = id
    return render(request, 'web/index.html', {})
        # return redirect('/index')
    # except:
    #     return redirect('/login')
    #     pass

def login(request):
    if request.method == 'GET':
        return render(request,'web/login.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        try:
            Signup.objects.get(id=id, pw=pw)
            request.session['id'] = id
        # return render(request, 'web/index.html', {})
            return redirect('/index')
        except:
            return redirect('/login')


def member(request):
    return render(request, 'web/member.html', {})

def complete(request):
    if request.method =="GET":
        return render(request, 'web/member.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']
        email = request.POST['e_mail']
        Signup(id=id, pw=pw, name=name, e_mail=email).save()
        return render(request, 'web/complete.html', {})

def starter_kit(request):
    return render(request, 'web/starter-kit.html', {})

def error(request):
    return render(request, 'web/error-404.html',{})

def form_basic(request):
    return render(request, 'web/form-basic.html',{})

def pages_profile(request):
    return render(request, 'web/pages-profile.html',{})

def table_basic(request):
    return render(request, 'web/table-basic.html', {})

def icon_material(request):
    return render(request, 'web/icon-material.html', {})