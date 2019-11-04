from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect

from util.resp import resp_ok
from util.resp import resp_err
from util.resp import CODE_AUTHENTICATION_FAILED

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return HttpResponseRedirect('/login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return resp_ok()
        else:
            return resp_err(CODE_AUTHENTICATION_FAILED)
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request, 'login.html')
