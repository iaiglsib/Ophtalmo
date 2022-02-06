from datetime import datetime

from Patient import Patient

class AnalysePatient(Patient):
    dico = dict()
    maladies = list()
    # def __int__(self):
    #     pass

    def __init__(self, id, nom, age, sexe, acuite_visuelle, vision_pres, vision_loin, date_consul: datetime.now(), axe_pres=0, axe_loin=0, sphere_pres=0, sphere_loin=0, cylindre_pres=0, cylindre_loin=0):
        Patient.__init__(self, id, nom, age, sexe, acuite_visuelle)
        self.vision_pres = vision_pres
        self.vision_loin = vision_loin
        self.dat_consul = date_consul
        self.axe_pres = axe_pres
        self.axe_loin = axe_loin
        self.sphere_pres = sphere_pres
        self.sphere_loin = sphere_loin
        self.cylindre_pres = cylindre_pres
        self.cylindre_loin = cylindre_loin
        self.maladies = []
        self.dico = self.resultat()

    def dateMod(self, date):
        self.dat_consul = date

    def Analyse(self):
        if (self.acuite_visuelle == 1) and (self.vision_pres == "normale") and (self.vision_loin == "floue"):
            self.maladies.append("Myopie")
            return "Myopie"
        elif (self.acuite_visuelle == 3) and (self.vision_pres == "floue") and (self.vision_loin == "normale") and (self.age < 45):
            self.maladies.append("Hypermetropie")
            return "Hypermetropie"
        elif (self.acuite_visuelle == 3) and (self.vision_pres == "floue") and (self.age >= 45):
            self.maladies.append("Presbytie")
            return "Presbytie"
        elif (self.acuite_visuelle <= 3) and (self.vision_loin == "floue") and (self.vision_pres == "floue"):
            self.maladies.append("Astigmatisme")
            return "Astigmatisme"
        else:
            self.maladies.append("Expertise medicale requise")
            return "Analyses approfondies requises"

    def resultat(self):

        dic_res = dict()
        dic_res["Date consultation"] = str(self.dat_consul)
        dic_res["Acuite_visuelle"] = self.acuite_visuelle
        dic_res["Vision de pres"] = self.vision_pres
        dic_res["Vision de loin"] = self.vision_loin
        dic_res["Axe pres"] = self.axe_pres
        dic_res["Axe loin"] = self.axe_loin
        dic_res["Sphere pres"] = self.sphere_pres
        dic_res["Sphere loin"] = self.sphere_loin
        dic_res["Cylindre pres"] = self.cylindre_pres
        dic_res["Cylindre loin"] = self.cylindre_loin
        dic_res["Troubles"] = self.maladies

        return dic_res


# (En cours d'étude)
