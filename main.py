nb = int(input("entrer le nombre d'étudiant: "))

etudiants = []

for i in range(nb):
    nom = input("entrer le nom d'étudiant: ")
    etudiants.append(nom)

print("liste des étudiants:")
for e in etudiants:
    print(e)

notes = []
somme = 0

for i in range(nb):
    note = float(input("entrer la note" + etudiants[i] + ": "))
    notes.append(note)
    somme = somme + note

moyenne = somme / nb
print("la moyenne est:", moyenne)

if moyenne >= 10:
    print("Admis")
else:
    print("Ajourné")
