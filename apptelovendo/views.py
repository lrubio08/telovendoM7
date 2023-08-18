from django.shortcuts import render, redirect
from .forms import RegistroForm
import random
import string
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

#pagina de inicio
def index(request):
    return render (request, 'apptelovendo/index.html')

def exit(request):
    logout(request)
    return redirect('apptelovendo/index.html')
#Formulario de registro
def registro_usuario(request):
    
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = generate_random_password()
            user.set_password(password)
            user.save()

            send_registration_email(user.email, password)

            return redirect('bienvenida')
    else:
        form = RegistroForm()
    return render(request, 'apptelovendo/registro.html', {'form': form})

#gnerar contraseña aleatoria
def generate_random_password():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(6))
    return password

#Envio de contraseña la cual se recibe por consola 
def send_registration_email(email, password):
    subject = 'Bienvenido a Te lo vendo'
    message = f'Tu contraseña para ingresar a tus pedidos es: {password}'
    from_email = 'noreply@teloVendo.com' 
    recipient_list = [email]

    send_mail(subject, message, from_email, recipient_list)
    
#bienvenida al usuario registrado 
def bienvenida(request):
    return render(request, 'apptelovendo/bienvenida.html')

#Inicio de sesion
def iniciar_sesion(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de inicio de sesión
        email= request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # El inicio de sesión es exitoso, redirigir a la vista sesion_iniciada
            login(request, user)
            return redirect('sesion_iniciada')
        else:
            messages.error(request, 'Tu correo o contraseñas no son correctos. Por favor intenta nuevamente.')
    return render(request, 'apptelovendo/login.html')

def sesion_iniciada(request):
    return render(request, 'apptelovendo/sesion_iniciada.html')