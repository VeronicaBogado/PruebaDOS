from django.shortcuts import render

def formulario(request):
	return render(request, 'registracion/formulario.html',{})
