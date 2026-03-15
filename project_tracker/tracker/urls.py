from django.urls import path , include
from django.contrib.auth import views as auth_views
from . import views 


urlpatterns = [
    path('' , views.index , name='index' ),
    # path('signup' , views.signup ,name='signup'),
    # path('accounts/login/' , auth_views.LoginView.as_view() , name='login'),
    # path('logout' , views.logoutCont , name='custom_logout'),
    # path("", include("django.contrib.auth.urls")), 
    # path("signup/", views.SignUpView.as_view(), name="signup"),
]

