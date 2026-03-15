from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate , logout as auth_logut
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def apply_bootstrap_classes(form):
    print(form, "the form")
    for field in form.fields.values():
        print(field,'the form field')
        existing_classes = field.widget.attrs.get('class', '')
        print(existing_classes,'the form field existing class')
        field.widget.attrs['class'] = (existing_classes + ' form-control').strip()


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        apply_bootstrap_classes(form)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
        apply_bootstrap_classes(form)
    return render(request, 'registration/login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        apply_bootstrap_classes(form)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
        apply_bootstrap_classes(form)
    return render(request, 'registration/signup.html', {'form': form})

def logout(request):
    auth_logut(request)
    form = AuthenticationForm()
    return render(request, "registration/login.html" , {'form' : form })