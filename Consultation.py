from AnalysePatient import AnalysePatient


from datetime import datetime


def consultation():
    print("Informations du Patient")

    id = input("Id du patient : ")
    nom = input("Nom : ")
    age = -1
    sex = 'E'
    while (int(age) < 0):
        age = int(input("Age : "))
        if (int(age) > 0):

            while sex != 'M' or sex != 'F':
                sex = input("Sexe (M pour Homme et F pour Femme) : ")
                if (sex == 'M') or (sex == 'F'):
                    print("Donnees du patient enregistrees. \n")
                    break
            break


    print("Analyses ")
    acuite_vis = -1

    while int(acuite_vis) < 0 or int(acuite_vis) > 10:
        acuite_vis = int(input("Entrer la valeur de l'acuite visuelle "))
        if (int(acuite_vis) >= 0) and (int(acuite_vis) <= 10):
            vision_pr, vision_ln = "", ""
            while vision_pr != "floue " or vision_pr != "normale":
                vision_pr = input("Vision pres (floue ou normale) : ")
                if (vision_pr == "floue") or (vision_pr == "normale"):
                    while vision_ln != "floue " or vision_ln != "normale":
                        vision_ln = input("Vision loin (floue ou normale) : ")
                        if (vision_ln == "floue") or (vision_ln == "normale"):
                            axe_pre, axe_ln = -1, -1
                            while float(axe_pre) < 0:
                                axe_pre = float(input("Axe pres (mm) : "))
                                if float(axe_pre) >= 0:
                                    while float(axe_ln) < 0:
                                        axe_ln = float(input("Axe loin (mm) : "))
                                        if float(axe_ln) >= 0:
                                            sphere_pre, sphere_ln = -1, -1
                                            while float(sphere_pre) < 0:
                                                sphere_pre = float(input("Sphere pres(mm) : "))
                                                if float(sphere_pre) >= 0:
                                                    while float(sphere_ln) < 0:
                                                        sphere_ln = float(input("Sphere loin(mm) : "))
                                                        if float(sphere_ln) >= 0:
                                                            cylindre_pre, cylindre_ln = -1, -1
                                                            while float(cylindre_pre) < 0:
                                                                cylindre_pre = float(input("Cylindre pres(mm) : "))
                                                                if float(cylindre_pre) >= 0:
                                                                    while float(cylindre_ln) < 0:
                                                                        cylindre_ln = float(input("Cylindre loin(mm) : "))
                                                                        if float(cylindre_ln) >= 0:
                                                                            print("Resultats analyses enregistrees")

                                                                            patient = AnalysePatient(id=id,
                                                                                                     nom=nom,
                                                                                                     age=age,
                                                                                                     sexe=sex,
                                                                                                     date_consul= datetime.now(),
                                                                                                     acuite_visuelle=acuite_vis,
                                                                                                     vision_pres=vision_pr,
                                                                                                     vision_loin=vision_ln,
                                                                                                     axe_pres=axe_pre,
                                                                                                     axe_loin=axe_ln,
                                                                                                     sphere_pres=sphere_pre,
                                                                                                     sphere_loin=sphere_ln,
                                                                                                     cylindre_pres=cylindre_pre,
                                                                                                     cylindre_loin=cylindre_ln)
                                                                            return patient
                            break
                    break
