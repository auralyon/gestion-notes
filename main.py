nb = int(input("entrer le nombre d'étudiant: "))

etudiants = []

for i in range(nb):
    nom = input("entrer le nom d'étudiant: ")
    etudiants.append(nom)

print("liste des étudiants:")
for e in etudiants:
    print(e)

