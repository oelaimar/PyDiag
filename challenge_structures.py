print("==chalange I==")
# 1.1
notes = [12, 18, 7, 15, 9, 20, 3, 14]

max_note = float("-inf")
min_note = float("inf")

for note in notes:
    if max_note < note:
        max_note = note
    if min_note > note:
        min_note = note

print(f"max note: {max_note}")
print(f"min note: {min_note}")

# 1.2
def notes_au_dessus(notes, seuil):
    return [note for note in notes if note > seuil]

notes = [8, 14, 6, 17, 11, 20]
seuil = 12

print(notes_au_dessus(notes, seuil))

# 1.3

fruits = ["pomme", "banane", "pomme", "orange", "banane", "pomme"]

fruits_unique = set()
fruits_count = {}
for fruit in fruits:
    if fruit not in fruits_unique:
        fruits_count[fruit] = 1
        fruits_unique.add(fruit)
    else:
        fruits_count[fruit] += 1
print(fruits_count)

# 1.4
liste = [1, 2, 3, 4, 5]

def inversion_list(list):
    if not list:
        return []
    return inversion_list(list[1:]) + [list[0]]

print(inversion_list(liste))

# 1.5

liste_a = [1, 4, 7]
liste_b = [2, 3, 8, 9]

def merge_sort(list_a, list_b):
    list_a_left = 0
    list_b_left = 0
    result = []
    while len(list_a) - 1 > list_a_left and len(list_b) - 1 > list_b_left:
        if list_a[list_a_left] < list_b[list_b_left]:
            result.append(list_a[list_a_left])
            list_a_left += 1
        if list_a[list_a_left] > list_b[list_b_left]:
            result.append(list_b[list_b_left])
            list_b_left += 1
    if list_a[list_a_left] < list_b[list_b_left]:
        result.append(list_a[list_a_left])
        list_a_left += 1
    else:
        result.append(list_b[list_b_left])
        list_b_left += 1
        
    while(len(list_b) > list_b_left):
        result.append(list_b[list_b_left])
        list_b_left += 1
    while(len(list_a) > list_a_left):
            result.append(list_a[list_a_left])
            list_a_left += 1
    return result
        
print(merge_sort(liste_a, liste_b))
# 1.6

numbers = [3, 12, 7, 25, 8, 19, 2]

even_number_squares = [number**2 for number in numbers if not number&1]

print(even_number_squares)

print("==chalange II==")

# 2.1
def vendre(stock, produit, quantite):
    if stock[produit] < quantite or not stock[produit]:
        print(f"Stock insuffisant pour {produit}(disponible : {stock[produit]})")
        return
    stock[produit] -= quantite
    print(f"Vente enregistree : {stock[produit]} {produit}.")

stock = {"pommes": 50, "bananes": 30, "oranges": 0}
vendre(stock, "pommes", 20)
vendre(stock, "oranges", 5)

print(stock)

# 2.2

stock = {"pommes": 30, "bananes": 0, "oranges": 0, "kiwis": 12}

def produits_epuises(stock):
    return [item for item in stock.keys() if stock[item] == 0]

print(produits_epuises(stock))

# 2.3

commandes = [
    {"client": "Ali", "produit": "pommes", "quantite": 5},
    {"client": "Sara", "produit": "bananes", "quantite": 10},
    {"client": "Ali", "produit": "oranges", "quantite": 2},
]

def total_par_client(list):
    result = {}
    for command in list:
        if not command["client"] in result:
            result[command["client"]] = command["quantite"]
        else:
            result[command["client"]] += command["quantite"]
    return result

print(total_par_client(commandes))

# 2.4

d = {"a": 1, "b": 2, "c": 3}

inversion = {value : key for key, value in d.items()}

print(inversion)

# 2.5

mots = ["chat", "elephant", "abeille", "riz"]

mote_len = {mot : len(mot) for mot in mots}

print(mote_len)

# 2.6

entreprise = {
    "IT": ["Ali", "Sara", "Omar"],
    "RH": ["Lina"],
    "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
}

employe_count = {depart : len(entreprise[depart]) for depart in entreprise}

print(employe_count)

print("==chalange III==")

# 3.1

atelier_python = ["Ali", "Sara", "Lina", "Karim"]
atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]

print(f"Inscrits aux deux ateliers : {set(atelier_python) & set(atelier_java)}") # you can do set(a).union(set(b))
print(f"Inscrits a au moins un atelier : {set(atelier_python) | set(atelier_java)}") # you can do set(a).intersection(set(b))
print(f"Uniquement Python : {set(atelier_python) - set(atelier_java)}") # you can do set(a).difference(set(b))

# 3.2

def a_des_doublons(liste):
    return len(liste) == len(list(set(liste)))

liste_1 = ["Ali", "Sara", "Lina"]
liste_2 = ["Ali", "Sara", "Ali"]

print(f"a_des_doublons(liste_1) -> {a_des_doublons(liste_1)}")
print(f"a_des_doublons(liste_2) -> {a_des_doublons(liste_2)}")


# 3.3

tags_articles = [
    ["python", "web", "api"],
    ["python", "data"],
    ["web", "css"],
]

unique_tags_articles = set()

for tag in tags_articles:
    unique_tags_articles = unique_tags_articles | set(tag) 

print(unique_tags_articles)

# 3.4

# the Mutable Objects are unhashable
# the Imutable Objects are hashable

# because the if you want to use object in set, it hash needs to be stable

print("==chalange IV==")

# 4.1

ventes = [
    {"produit": "pommes", "montant": 120},
    {"produit": "bananes", "montant": 80},
    {"produit": "pommes", "montant": 45},
    {"produit": "oranges", "montant": 60},
    {"produit": "bananes", "montant": 30},
]

total_par_pruduit = {}

for vente in ventes:
    if not vente["produit"] in total_par_pruduit:
        total_par_pruduit[vente["produit"]] = vente["montant"]
    else:
        total_par_pruduit[vente["produit"]] += vente["montant"]

Meilleur_produit = ventes[0]

for vente in ventes[1:]:
    if Meilleur_produit["montant"] < vente["montant"]:
        Meilleur_produit = vente


Produits_distincts = set([vente["produit"] for vente in ventes])

print(f"Total par produit : {total_par_pruduit}")
print(f"Meilleur produit : {Meilleur_produit["produit"]} ({Meilleur_produit["montant"]})")
print(f"Produits distincts  : {Produits_distincts}")

# 4.2

inv1 = {"pommes": 20, "bananes": 15}
inv2 = {"bananes": 10, "kiwis": 5}

def fusionner_inventaires(inv1, inv2):
    result = {}
    for (key, value) in inv1.items():
        if key in inv2:
            result[key] = inv2[key] + inv1[key]
        else:
            result[key] = value
    for (key, value) in inv2.items():
        if key in inv1:
            continue
        result[key] = value
    return result

print(fusionner_inventaires(inv1, inv2))

# 4.3
        
etudiants = [
    {"nom": "Ali", "matieres": {"maths": 14, "physique": 12}},
    {"nom": "Sara", "matieres": {"maths": 18, "physique": 16, "svt": 15}},
    {"nom": "Lina", "matieres": {"maths": 9, "physique": 11}},
]

Moyenne_par_etudiant = {}

def calcule_moyenne(matieres):
    return sum(list(matieres.values())) / len(list(matieres.values()))

for student in etudiants:
    Moyenne_par_etudiant[student["nom"]] = calcule_moyenne(student["matieres"])
    
print(Moyenne_par_etudiant)

Matieres_enseignees = set()
for student in etudiants:
    Matieres_enseignees = Matieres_enseignees | set(list(student["matieres"]))

print(Matieres_enseignees)

Notes_par_matiere = {matiere : [] for matiere in Matieres_enseignees}

for student in etudiants:
    for matieres in Matieres_enseignees:
        if matieres not in student["matieres"]:
            continue
        Notes_par_matiere[matieres].append(student["matieres"][matieres])

print(Notes_par_matiere)


def moyenne_globale(notes):
    return sum(notes) / len(notes)

Meilleure_matiere = 0

for notes in list(Notes_par_matiere.values()):
    if moyenne_globale(notes) > Meilleure_matiere:
        Meilleure_matiere = moyenne_globale(notes)

print(f"Meilleure matiere (moyenne globale) : {Meilleure_matiere}")