from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='accounts/login.html',
            redirect_authenticated_user=True,
        ),
        name='login',
    ),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path(
        'password/',
        views.CambiarPasswordView.as_view(),
        name='password_change',
    ),
    path(
        'password/hecho/',
        views.CambiarPasswordHechoView.as_view(),
        name='password_change_done',
    ),
]