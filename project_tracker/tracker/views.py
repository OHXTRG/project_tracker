from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.urls import reverse_lazy 
from django.views.generic import CreateView
from django.shortcuts import redirect

# Create your views here.

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


    

@login_required
def index(request):
    context = {"user": request.user}
    return render(request, "home.html", context)




@login_required
def logoutCont(request):
    print(request,"the request in logout")
    logout(request)
    return render(request , 'home.html' , {})
    # return redirect("index")

   
