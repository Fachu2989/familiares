from django.http import HttpResponse
from django.shortcuts import render
from Appfamilia.models import Family 

def family(request, nombre, edad, nacimiento):

    family = Family(nombre=nombre, edad=edad, nacimiento=nacimiento)
    family.save()
    
    return HttpResponse(f"""<p>{family.nombre} de edad  {family.edad} y su nacimiento es {family.nacimiento}. ya se ha agregado</p>
    """)

def lista_family(request):
    
    lista=Family.objects.all()

    return render(request, "familiares.html", {"familiares": lista})