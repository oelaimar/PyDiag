print("===MODULE I===")
#module 1
student_karim = {"name" : "Karim", "prenom" : "Ben Ali", "notes" : [12, 15, 9]}

def calculer_moyenne(notes):
    sum_notes = 0
    count_notes = 0
    for note in notes:
        sum_notes += note
        count_notes += 1
    return sum_notes / count_notes

print(f"{student_karim["name"]} moyenne : {(float(calculer_moyenne(student_karim["notes"]))):.2f}")

print("===MODULE II===")
#module 2

valeurs_test = [9.9, 10.0, 11.9, 12.0, 15.9, 16.0, 20.0]

def appreciation(moyenne):
    if moyenne < 10:
        return "Insuffisant"
    elif moyenne >= 10 and moyenne < 12:
        return "Passable"
    elif moyenne >= 12 and moyenne < 16:
        return "Bien"
    elif moyenne >= 16 and moyenne <= 20:
        return "Tres bien"
    
for value in valeurs_test:
    print(f"{value} -> {appreciation(value)}")
    
students = [
        {"nom": "Karim", "notes": [12, 15, 9]},
        {"nom": "Sara", "notes": [18, 17, 16]},
        {"nom": "Lina", "notes": [6, 8, 5]},
    ]
    
def desplay_students(students):
    bad_student = {}
    min = 20
    best_student = {}
    max = 0
    for student in students:
        moyenne =  float(calculer_moyenne(student["notes"]))
        
        if moyenne > max:
            max = moyenne
            best_student = student
        if moyenne < min:
            min = moyenne
            bad_student = student
        print(f"{student["nom"]} {moyenne:.2f} {appreciation(moyenne)}")
        
        print(f"best student is {best_student["nom"]}")
        print(f"bad student is {bad_student["nom"]}")
        
desplay_students(students)



print("==MODULE III===")

students = [
    {"nom": "Karim", "notes": [12, 15, 9]},
    {"nom": "Sara", "notes": [18, 17, 16]},
    {"nom": "Lina", "notes": [6, 8, 5]},
    ]

def construire_resultats(students):
    result = {}
    for student in students:
        moyenne = calculer_moyenne(student["notes"])
        mention = appreciation(moyenne)
        result[student["nom"]] = {"moyenne": moyenne, "mention": mention}
    return result

result = construire_resultats(students)

for value in result:
    value_dic = {value : result[value]}
    print(value_dic)

print("==result sorted==")

result_sorted = dict(sorted(result.items() , key = lambda student : student[1]["moyenne"], reverse= True))

for value in result_sorted:
    value_dic = {value : result[value]}
    print(value_dic)

students_failed = []
for student in students:
    moyenne = calculer_moyenne(student["notes"])
    if moyenne < 10:
        students_failed.append((student["nom"], moyenne))

print(students_failed)