from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),


    #path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name=
    #"accounts/password_change_done.html"), name='password_change_done'),

]
