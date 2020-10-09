from django.shortcuts import render, redirect
from django.contrib.auth.models import User  
from django.contrib import auth, messages
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
            #회원가입시 자동으로 로그인되지 않도록. 
            #auth.login(request, user)  
            return redirect('home')
        else:
            return redirect('signup')
    return render(request, 'signup.html')

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "회원가입이 필요합니다.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout_request(request):
    auth.logout(request)
    print("로그아웃")
    return render(request, 'home.html')


