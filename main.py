def calcul_moyen(notes):
    sum_notes = 0
    count_notes = 0
    for note in notes:
        sum_notes += note
        count_notes += 1
    return sum_notes / count_notes

def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif moyenne >= 10 and moyenne < 12:
        return "Passable"
    elif moyenne >= 12 and moyenne < 16:
        return "Bien"
    elif moyenne >= 16 and moyenne <= 20:
        return "Tres bien"
     
students = []

while True:    
    first_name = input("type first name: ")
    last_name = input ("type last name: ")
    notes = []
    is_valide_numbers = True
    for i in range(3):
        user_input = input(f"type num {i + 1} : ")
        try :
            note = float(user_input)
        except ValueError:
            note = "this is not a valide number"
            is_valide_numbers = False
        notes.append(note)
    
    if not is_valide_numbers:
        for note in notes:
            if isinstance(note, float):
                print(f"note accepted: {note}")
            else:
                print(note)
    
    else:
        moyen = calcul_moyen(notes)
        print(f"{first_name} {last_name} : {moyen:.2f}")


    