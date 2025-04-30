from django.shortcuts import render
from .forms import LivreForm
from . import models
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import LivreForm
from . import models
from django.shortcuts import render, get_object_or_404, redirect

def ajout(request):
    if request.method == "POST":
        form = LivreForm(request)
        if form.is_valid():
            Livre = form.save()
            return render(request,"appTP2/detail.html/",{"Livre" : Livre})
        else:
            return render(request,"appTP2/ajout.html/",{"form": form})
    else :
        form = LivreForm()
        return render(request,"appTP2/ajout.html/",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        lform.save()  # Sauvegarde dans la base
        return HttpResponseRedirect("/appTP2/liste/")  # Redirige vers la liste des livres
    else:
        return render(request, "appTP2/ajout.html/", {"form": lform})


def read(request, id):
    livre = get_object_or_404(models.Livre, pk=id)  # Récupération du Livre avec son ID
    return render(request, "appTP2/detail.html", {"livre": livre})  # Envoie vers le gabarit "detail.html"


def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False)
        Livre.id = id;
        Livre.save()
        return HttpResponseRedirect("/appTP2/")
    else:
        return render(request, "appTP2/update.html/", {"form": lform, "id": id})

def update(request, id):
    livre = get_object_or_404(models.Livre, pk=id)  # Récupération de l'objet
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)  # Préremplissage du formulaire
        if form.is_valid():
            form.save()  # Sauvegarde des modifications
            return redirect('/appTP2/liste/')  # Redirection vers la liste
    else:
        form = LivreForm(instance=livre)  # Formulaire prérempli
    return render(request, "appTP2/update.html", {"form": form, "id": id})


def liste(request):
    livres = models.Livre.objects.all()  # Récupère tous les objets de la table Livre
    return render(request, "appTP2/liste.html", {"livres": livres})

def delete(request, id):
    livre = get_object_or_404(models.Livre, pk=id)
    livre.delete()
    return redirect('/appTP2/liste/')
