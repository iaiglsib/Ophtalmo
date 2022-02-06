import copy
from AnalysePatient import Patient
from AnalysePatient import AnalysePatient


def serialiseur_patient(obj):

    if isinstance(obj, AnalysePatient):
        obj_cpy = copy.copy(obj)
        obj_cpy.__class__ = Patient
        return {
            "Patient id": obj.id,
            "Nom": obj.nom,
            "Age": obj.age,
            "Sexe": obj.sexe,
            "Diagnostic ": obj.dico,
                },

    # if isinstance(obj, Patient):
    #     return {"__class__": "Patient",
    #             "Id": obj.id,
    #             "Nom": obj.nom,
    #             "Age": obj.age,
    #             "Sexe": obj.sexe}