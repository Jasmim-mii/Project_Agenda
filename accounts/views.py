from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.shortcuts import redirect, render


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')
    usuario = request.POST.get('usuario')
    password = request.POST.get('password')

    user = auth.authenticate(request, username=usuario, password=password)
    if not user:
        messages.error(request, 'Usuario ou senha inválidos.')
        return render(request, 'accounts/login.html')

    elif request.session.get('usuario'):
        return redirect('login')
    else:
        auth.login(request, user)
        messages.success(request, 'Voce fez login com sucesso.')
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')
    usuario = request.POST.get('usuario')

    if not name or not lastName or not email or not usuario or not password \
            or not password2:
        messages.error(request, 'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/register.html')

    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido.')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'Senha precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if len(usuario) < 6:
        messages.error(request, 'Usuário precisa ter 6 caracteres ou mais.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(username=usuario).exists():
        messages.error(request, 'Usuário já existe.')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'E-mail já existe.')
        return render(request, 'accounts/register.html')

    messages.success(request, 'Registrado com sucesso! Agora faça login.')

    user = User.objects.create_user(username=usuario, email=email,
                                    password=password, first_name=name,
                                    last_name=lastName)
    user.save()
    return redirect('login')
