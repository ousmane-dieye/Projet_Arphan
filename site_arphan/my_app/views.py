from django.shortcuts import render
from .models import etudiant
from django.shortcuts import redirect 


# Create your views here.
def index(request):
    return render(request, 'my_app/index.html')

def inscription(request):
    if request.method == "POST":
        nom_utilisateur = request.POST.get("nom_utilisateur")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        mot_de_passe = request.POST.get("mot_de_passe")
        departement = request.POST.get("departement")


        etudiant.objects.create(
            nom=nom,
            prenom=prenom,
            nom_utilisateur = nom_utilisateur,
            departement=departement,
            mot_de_passe=mot_de_passe
        )
        return redirect('success')  # ou vers la page que tu veux
            
    return render(request, 'my_app/inscription.html')


def connexion(request):
    erreur = ""
    if request.method == "POST":
        nom_utilisateur = request.POST.get("nom_utilisateur")
        mot_de_passe = request.POST.get("mot_de_passe")

        try:
            utilisateur = etudiant.objects.get(nom_utilisateur=nom_utilisateur)

            if utilisateur.mot_de_passe == mot_de_passe:
                # Connexion réussie → aller à la page d’accueil par exemple
                return render(request, "my_app/accueil.html")
            else:
                # Mot de passe incorrect
                erreur =  "Mot de passe incorrect."

        except etudiant.DoesNotExist:
            # Nom d’utilisateur introuvable
            erreur = "Utilisateur introuvable."
    return render(request, 'my_app/connexion.html', {"erreur": erreur})


def success(request):
    return render(request, 'my_app/success.html')


