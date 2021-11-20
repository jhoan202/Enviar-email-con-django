from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def contactar(request):
	if request.method=='POST':

		
		asunto=request.POST['asunto']
		email=["jhoansebastianbarreravanegas@gmail.com"]
		mensaje=request.POST['mensaje'] +request.POST['email']
		from_email=settings.EMAIL_HOST_USER
		send_mail(asunto,mensaje,from_email,email)

		return HttpResponse('gracias')
	return render(request,'Plantilla_Formulario.html')