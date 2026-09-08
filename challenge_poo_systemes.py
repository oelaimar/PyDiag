print("== block I==")

class ErrorDisponible(Exception):
    pass

class Livre:
    def __init__(self, titre, auteur, disponible = True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        self.disponible = False
    def rendre(self):
        self.disponible = True
    def __str__(self):
        return f"\"{self.titre}\" de {self.auteur}  -- : {"disponible" if self.disponible else "emprunte"}"

class Adherent:

    def __init__(self, nom):
        self.nom = nom
        self.livres_empruntes = []
    def emprunter_livre(self, livre : Livre):
        try:
            if not livre.disponible:
                raise ErrorDisponible
            livre.emprunter()
            self.livres_empruntes.append(livre)
        except ErrorDisponible:
            print(f"Erreur : le livre \"{livre.titre}\" n'est pas disponible.")

    def rendre_livre(self, livre : Livre):
        try:
            if livre not in self.livres_empruntes:
                raise ErrorDisponible
            livre.rendre()
            self.livres_empruntes.remove(livre)
        except ErrorDisponible:
            print(f"Erreur : le livre \"{livre.titre}\" n'est pas disponible.")
    def nombre_livres_empruntes(self):
        return len(self.livres_empruntes)

livre = Livre("Dune", "Frank Herbert")
print(livre)

livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
ali.emprunter_livre(livre)
print(livre)
print(ali.nombre_livres_empruntes())

livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
sara = Adherent("Sara")
ali.emprunter_livre(livre)
sara.emprunter_livre(livre)

livre = Livre("Dune", "Frank Herbert")
ali = Adherent("Ali")
ali.emprunter_livre(livre)
ali.rendre_livre(livre)
print(livre)
print(ali.nombre_livres_empruntes())

print("==block II==")
class CompteBancaire:

    nom_banque = "BanquePyDiag"
    nombre_comptes = 0

    def __init__(self, nom, solde_initial = 0):
        self.__sold = solde_initial
        self.nom = nom
        CompteBancaire.nombre_comptes += 1

    @property
    def solde(self):
        return self.__sold

    def deposer(self, montant):
        if montant < 0:
            print("fonds suffisants")
        self.__sold += montant

    def retirer(self, montant):
        if montant < 0:
            print("fonds suffisants")
        self.__sold -= montant

    @classmethod
    def nombre_total_comptes(cls):
        return cls.nombre_comptes

    @staticmethod
    def convertir_devise(montant, taux):
        return montant * taux


compte = CompteBancaire("Ali", solde_initial=100)
print(compte.solde)
try:
    compte.solde = 5000
except:
    print("AttributeError: can't set attribute 'solde'")

print("==block III==")

from abc import ABC, abstractmethod

class Vehicule(ABC):

    def __init__(self, marque, immatriculation):
        self.marque = marque
        self.immatriculation = immatriculation

    @abstractmethod
    def tarif_journalier(self):
        pass

class Voiture(Vehicule):
    def __init__(self, marque, immatriculation, nombre_places):
        super().__init__(marque, immatriculation)
        self.nombre_places = nombre_places

    def tarif_journalier(self):
        return 30 + self.nombre_places * 0.2

    def __str__(self):
        return f"Voiture {self.marque} {self.immatriculation} -- {self.nombre_places} places"

class Moto(Vehicule):
    def __init__(self, marque, immatriculation, cylindree):
        super().__init__(marque, immatriculation)
        self.cylindree = cylindree

    def tarif_journalier(self):
        return 10 + self.cylindree * 0.3
    def __str__(self):
        return f"Voiture {self.marque} {self.immatriculation} -- {self.cylindree} cylindrees"

class Camion(Vehicule):
    def __init__(self, marque, immatriculation, charge_utile, base):
        super().__init__(marque, immatriculation)
        self.charge_utile = charge_utile
    def tarif_journalier(self):
        return 20 + self.charge_utile * 0.1

    def __str__(self):
        return f"Voiture {self.marque} {self.immatriculation} -- {self.charge_utile} charge"

print("==bloc IV==")


