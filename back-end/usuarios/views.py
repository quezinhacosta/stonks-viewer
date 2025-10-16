from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model


def cadastro(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Aqui você pode adicionar validações, criar o usuário, etc.
        User = get_user_model()
        user = User.objects.create_user(email=email, password=password, first_name=first_name)

        # Depois do cadastro, redireciona para alguma página, por exemplo login
        return redirect('login')  # ou qualquer outra página

    return render(request, 'usuarios/cadastro.html')
