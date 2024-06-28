from django.shortcuts import render, redirect
from .forms import ContactoForm, DonacionForm
from django.core.mail import send_mail
from .models import Inicio, Nosotros, Programas, Actividades, Historias, Articulos, Donaciones, DonacionesCBU



def inicio(request):
    inicio_data = Inicio.objects.latest('fecha_publicacion')  # Obtener el último registro
    return render(request, 'core/inicio.html', {'inicio': inicio_data})

def nosotros(request):
    try:
        nosotros_data = Nosotros.objects.latest('id')  # Obtener el último registro
    except Nosotros.DoesNotExist:
        nosotros_data = None
    
    return render(request, 'core/nosotros.html', {'nosotros': nosotros_data})

def programas(request):
    programas_data = Programas.objects.latest('id')
    return render(request, 'core/programas.html', {'programas': programas_data})

def actividades(request):
    actividades_data = Actividades.objects.all()
    return render(request, 'core/actividades.html', {'actividades': actividades_data})

def historias(request):
    historias_data = Historias.objects.all()
    return render(request, 'core/historias.html', {'historias': historias_data})

def articulos(request):
    articulos_data = Articulos.objects.all()
    return render(request, 'core/articulos.html', {'articulos': articulos_data})

#def donaciones_cbu(request):
#    donaciones_data_cbu = DonacionesCBU.objects.all()
#    return render(request, 'core/donaciones.html', {'donaciones_cbu':donaciones_data_cbu})

def donaciones(request):
    donaciones_data = Donaciones.objects.latest('id')  # Obtener el último registro de donaciones
    donaciones_data_cbu = DonacionesCBU.objects.all()
    
    mensaje_exito = False
    
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y envía el correo electrónico
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'tu_correo@example.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                ['destino@example.com'],  # Cambia esto por el correo al cual enviarás el mensaje
                fail_silently=False,
            )
            mensaje_exito = True  # Marca como enviado exitosamente
    else:
        form = ContactoForm()

    context = {
        'donaciones': donaciones_data,
        'donaciones_cbu': donaciones_data_cbu,
        'form': form,
        'mensaje_exito': mensaje_exito,
    }
    
    return render(request, 'core/donaciones.html', context)

def contacto(request):
    mensaje_exito = False  # Variable para indicar si se envió el formulario correctamente

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            # Procesa el formulario y envía el correo electrónico
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            send_mail(
                'Nuevo mensaje de contacto',
                f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}',
                'tu_correo@example.com',  # Cambia esto por el correo desde el cual enviarás el mensaje
                ['destino@example.com'],  # Cambia esto por el correo al cual enviarás el mensaje
                fail_silently=False,
            )
            mensaje_exito = True  # Marca como enviado exitosamente
    else:
        form = ContactoForm()

    return render(request, 'core/contacto.html', {'form': form, 'mensaje_exito': mensaje_exito})

