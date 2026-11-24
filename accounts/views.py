from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import PerfilForm, RegistroForm, UserEditForm
from .models import Perfil


def registro(request):
    if request.user.is_authenticated:
        return redirect('posts:lista_posts')

    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # El perfil se crea explícitamente al registrarse (sin signals)
            Perfil.objects.create(user=user)
            messages.success(
                request, 'Cuenta creada correctamente. Ya podés iniciar sesión.'
            )
            return redirect('accounts:login')
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})


@login_required
def perfil(request):
    # get_or_create cubre usuarios sin perfil (ej: superusuarios creados por consola)
    perfil_obj, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil_obj})


@login_required
def editar_perfil(request):
    perfil_obj, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil_obj)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('accounts:perfil')
    else:
        user_form = UserEditForm(instance=request.user)
        perfil_form = PerfilForm(instance=perfil_obj)

    return render(request, 'accounts/editar_perfil.html', {
        'user_form': user_form,
        'perfil_form': perfil_form,
        'perfil': perfil_obj,
    })


class CambiarPasswordView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('accounts:password_change_done')


class CambiarPasswordHechoView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'