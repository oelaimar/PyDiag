print("==chalange I==")

# 1.1
try:
    extrait_a = "print('bonjour'"
    exec(extrait_a)
except SyntaxError:
    print("extrait_a -> SyntaxError (parenthese non fermee)")
    
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("extrait_b -> ZeroDivisionError (exception a l'execution)")
    
try:    
    valeurs = [1, 2, 3]
    result = valeurs[5]
except IndexError:
    print("extrait_c -> IndexError (exception a l'execution)")

# 1.2

def division_securisee(a, b):
    try:
        result = a / b
        print(result)
    except:
        print("Erreur : division par zero impossible")
    

division_securisee(10, 2)
division_securisee(10, 0)

# 1.3

def convertir_entier(valeur):
    try:
        result = int(valeur)
        print(result)
    except ValueError:
        print(f"Erreur : \"{valeur}\" n'est pas un entier valide.")
        
convertir_entier("42")
convertir_entier("abc")


# 1.4

def acceder_element(liste, index):
    try:
        result = liste[index]
        print(result)
    except IndexError:
        print(f"Erreur : index {index} hors limites (taille de la liste : {len(liste)}).")

notes = [12, 15, 9]
acceder_element(notes, 1)
acceder_element(notes, 10)

# 1.5

def acceder_cle(dictionnaire, cle):
    try:
        result = dictionnaire[cle]
        print(result)
    except KeyError:
        print(f"Erreur : la cle \"{cle}\" n'existe pas")

eleve = {"nom": "Sara", "age": 20}
acceder_cle(eleve, "nom")
acceder_cle(eleve, "email")

# 1.6

def traiter_valeur(value):
    try:
        result = int(value)
    except ValueError:
        print(f"Erreur : \"{value}\" n’est pas convertible.")
    else:
        print(f"Conversion reussie : {result}")
    finally:
        print("Traitement termine.")
        
traiter_valeur("8")
traiter_valeur("x")

print("==CHALANGE II==")
# 2.1
def verifier_age(age):
    try:
        if age < 0:
            raise ValueError
        print(f"Age valide : {age}")
    except ValueError:
        print(f"ValueError: l'age ne peut pas etre negatif ({age}).")

verifier_age(25)
verifier_age(-3)

# 2.2

def traiter_liste_de_valeurs(list):
    for value in list:
        try:
            result = int(value)
            print(result)
        except ValueError:
            print(f"Log : valeur \"{value}\" invalide, exception relancee.")
            raise

try:
    traiter_liste_de_valeurs(["3", "9", "x", "5"])
except Exception as e:
    print(e)

# 2.3

class StockInsuffisantError(Exception):
    pass

# 2.4

def retirer_stock(stock, produit, quantite):
    try:
        if quantite > stock[produit]:
            raise StockInsuffisantError(f"stock insuffisant pour {produit}")
        stock[produit] -= quantite
    except StockInsuffisantError as e:
        print(f"StockInsuffisantError: {e}")
        print(f"(demande : {quantite}, disponible : {stock[produit]})")


stock = {"pommes": 20, "bananes": 4}
retirer_stock(stock, "pommes", 5)
retirer_stock(stock, "bananes", 10)

print("==CHALANGE III==")

# 3.1
def ecrire_liste_courses(chemin, articles):
    file = open(chemin, "w")
    file.writelines(article + "\n" for article in articles)
    file.close()

articles = ["pommes", "lait", "pain"]
ecrire_liste_courses("courses.txt", articles)
print("3.1 check the cources.txt")

# 3.2
def ajouter_article(chemin, article):
    file = open(chemin, "a")
    file.write(article)
    file.close()

ajouter_article("courses.txt", "oeufs")
print("3.2 check the cources.txt")

# 3.3

def lire_fichier(chemin):
    file = open(chemin, "r")
    lines = file.readlines()
    file.close()
    return lines
print(lire_fichier("courses.txt"))

# 3.4

def compter_lignes(chemin):
    file = open(chemin, "r")
    count = 0
    for line in file:
        count += 1
    file.close()
    return count

print(compter_lignes("courses.txt"))

# 3.5

# "r" is for read
# "w" is for write
# "a" is for append
# "x" create file if not exist if exist it'll raise an exception FileExistsError
# "rb" read binary mode
# "r+" read and write
# "w+" write and read
# the diff between "r+" and "w+" is "r+" the file must be existing


print("==chalange IV=")

def lire_fichier_securise(chemin):
    try:
        with open(chemin, "r", encoding = "utf-8") as file:
            lines = file.readlines()
            print("Contenu du fichier renvoye sous forme de liste de lignes.")
    except FileNotFoundError:
        print(f"Erreur : le fichier {chemin} n'existe pas.")

lire_fichier_securise("courses.txt")
lire_fichier_securise("inexistant.txt")

import csv
def calculer_moyenne_csv(chemin):
    sum_notes = 0
    count_notes = 0
    with open(chemin, "r", encoding = "utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            try:
                sum_notes += int(row[1])
                count_notes += 1
            except ValueError:
                print(f"Attention : note invalide pour {row[0]} (\"{row[1]}\"), ligne ignoree.")

        print(f"Moyenne calculee ({count_notes} notes valides) : {sum_notes / count_notes : .2f}")

calculer_moyenne_csv("notes.csv")

# 4.3

stock = {"pommes": 20, "bananes": 4, "oranges": 15}
commandes_brutes = [
    "pommes,5",
    "bananes,10",
    "kiwis,2",
    "oranges,abc",
    "oranges,5",
]

with open("journal.txt", "w") as journal:
    for cmd in commandes_brutes:
        produit, qte_str = cmd.split(",")
        try:
            qte = int(qte_str)
            if produit not in stock:
                raise KeyError(f"{produit} : produit inconnu")
            if stock[produit] < qte:
                raise StockInsuffisantError(
                    f"{produit} : stock insuffisant (demande {qte}, dispo {stock[produit]})"
                )
            stock[produit] -= qte
            ligne = f"[OK] {produit} : -{qte} (reste {stock[produit]})"
        except ValueError:
            ligne = f"[ERREUR] {produit} : quantite invalide (\"{qte_str}\")"
        except KeyError as e:
            ligne = f"[ERREUR] {e.args[0]}"
        except StockInsuffisantError as e:
            ligne = f"[ERREUR] {e}"

        journal.write(ligne + "\n")

with open("journal.txt", "r") as journal:
    print(journal.read())
