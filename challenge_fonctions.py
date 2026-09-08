print("==chalange I==")

# 1.1

def saluer(nom):
    print(f"Bonjour {nom} !")

saluer("Ali")

# 1.2

def puissance(base, exposant=2):
    print(base**exposant)

puissance(3)
puissance(2, 5)

# 1.3

def afficher_message(message):
    print(message)

resultat = afficher_message("Traitement termine")
print(resultat)


def diviser_avec_reste(a, b):
    if(b == 0):
        return (None, None)
    return int(round(a / b)), a % b

quotient, reste = diviser_avec_reste(17, 5)
print(f"quotient -> {quotient}")
print(f"reste -> {reste}")

def presenter(nom, age):
    return f"{nom} a {age} ans"