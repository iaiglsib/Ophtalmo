import json

#from AnalysePatient import AnalysePatient
from serialisation import serialiseur_patient
from Consultation import consultation
from datetime import datetime

# Données test
liste_patient = []

# resultat=input("Voulez-vous enregistrer un patient (oui ou non)? ")
# while resultat != "oui" or resultat != "non" :
#     resultat = input("Voulez-vous enregistrer un patient (oui ou non)? ")
#     if (resultat == "oui"):
#         temp = consultation()
#         patient = temp
#         resultat = input("Voulez-vous enregistrer un patient ? ")
#         patient.Analyse()
#         liste_patient.append((patient))
#         break
#     elif (resultat == "non"):
#         print("Fin")
#     break
#


p1 = consultation()
var = datetime.now()
p1.dateMod(var)
print(var)
p1.Analyse()
# p2 = AnalysePatient(3, "Mamzelle", 22, "F", 3, "floue","normale")
# p2.Analyse()
# p4 = AnalysePatient(4, "Eleve", 30, "M", 3, "floue","floue")
# p4.Analyse()
# p4 = AnalysePatient(5, "Etudiant", 50, "F", 3, "floue","floue")
# p4.Analyse()
# p5 = AnalysePatient(6, "Mo", 25, "F", 3, "floue","normale")
# p5.Analyse()
#
#
#
liste_patient.append(p1)
# liste_patient.append(p2)
# liste_patient.append(p4)
# liste_patient.append(p4)
# liste_patient.append(p5)
#
# Ecriture

with open('fichier_patients.json', 'a', encoding='utf-8', ) as f:
    json.dump(p1, f, indent=4, default=serialiseur_patient)

# Lecture du fichier
