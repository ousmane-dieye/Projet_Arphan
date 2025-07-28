from django.db import models

# Create your models here.
class etudiant(models.Model):
    nom_utilisateur = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    mot_de_passe = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_utilisateur
    
