class Maladie:
    def __init__(self, description, caracteristique, patient_concernes ):
        self.id = id
        self.description = description
        self.caracteristique = {}
        self.patient_concernes = dict() #cet argument servira à repertorier les personnes touchees par la maladie (Pas encore implemente)
#Nb Pat

#Myopie

class Myopie(Maladie):
    def __init__(self, description, caracteristique, patient_concernes):
        self.id = 1
        self.description = "Trouble de la vision dont le symptôme principal pour le sujet est de voir flou au loin"
        self.caracteristique = {"Vision de loin defective, maladie souvent manifestée entre l'enfance et l'adolescence"}
        self.patient_concernes = patient_concernes



#Presbytie

class Presbytie(Maladie):
    def __init__(self, description, caracteristique, patient_concernes):
        self.id = 2
        self.description = "Défaut lié à l’âge dû à une perte d’accommodation. En vieillissant, le cristallin (organe de l’accommodation) perd de sa souplesse. Il se déforme difficilement et les objets, les textes, les détails de vision de près deviennent de plus en plus flous. Suivre les lignes d’un journal ou le passage de la vision de loin à la vision de près est compliqué"
        self.caracteristique = {"Vision de près defective, maladie  souvent dû à la vieillesse"}
        self.patient_concernes = {}

#Hypermetropie

class Hypermetropie(Maladie):
    def __init__(self, description, caracteristique, patient_concernes):
        self.id = 3
        self.description = "Défaut de réfraction de l’œil que l’on a depuis l’enfance ; l’hypermétrope est gêné de près mais il peut aussi l’être de loin."
        self.caracteristique = {"Vision de près defective, maladie souvent héréditaire"}
        self.patient_concernes = {}

#Cataracte

class Cataracte(Maladie) :
    def __init__(self, description, caracteristique, nombres_touche ):
        self.id = 4
        self.description = "Opacification partielle ou totale du cristallin, lentille convergente située à l'intérieur de l'œil. Cette opacification est responsable d'une baisse progressive de la vue, au début accompagnée de gêne à la lumière (photophobie)"
        self.caracteristique = {"vision floue", "Diminution de l'acuité visuelle","mauvaise perception des contrastes", "vision des couleurs altérée", "sensibilité à la lumière vive et des phénomènes d'éblouissement"}
        self.nombres_touche = nombres_touche

#Achromatopsie

class Achromatopsie(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 5
        self.description = "Dégénérescence des cellules en cône (celles qui sont chargées de la vision de jour) de la rétine. Il ne reste donc que les cellules en bâtonnet, qui ne permettent pas la vision des couleurs"
        self.caracteristique = {"Absence de vision des couleurs"}
        self.nombres_touche = nombres_touche

#Amblyopie
class Amblyopie(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 6
        self.description = "Atteinte des cellules du cortex occipital, qui a pour conséquence la baisse de l’acuité visuelle d’un œil (ou des deux). Elle peut aussi entrainer une baisse de perception des reliefs. Cette pathologie visuelle s’installe pendant l’enfance et persiste toute la vie"
        self.caracteristique = {"Baisse de l'acuite visuelle", "baisse de la vision des reliefs"}
        self.nombres_touche = nombres_touche


#Aniridie
class Aniridie (Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 7
        self.description = "Absence d’iris. Cette anomalie est la plupart du temps de nature congénitale mais peut également survenir après un traumatisme"
        self.caracteristique = {"Diminution importante de l’acuité visuelle", "Absence d'iris", "une gêne à la lumière"}
        self.nombres_touche = nombres_touche

#Anisométropie
class Anisométropie(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 8
        self.description = "Différence de réfraction entre les deux yeux. Les personnes atteintes d’anisométropie sont souvent myope d’un œil et hypermétrope de l’autre œil"
        self.carac = {"différence de réfraction entre les deux yeux", "différence de correction entre les deux yeux", "myopie sur un oeil et hypermetropie sur l'autre"}
        self.nombres_touche = nombres_touche

#Aphakie
class Aphakie(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 9
        self.description = "absence de cristallin suite à une intervention chirurgicale ou lié à une anomalie congénitale. Cette pathologie entraine une perte de la netteté (de loin ou de prêt) et une hypermétropie."
        self.caracteristique = {"Absence de cristallin", "perte de nettete (de loin ou de pres)", "hypermetropie"}
        self.nombres_touche = nombres_touche

#Asthénopie
class Asthénopie(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 10
        self.description = "Fatigue oculaire des muscles et des cils. Cette maladie des yeux entraine des douleurs oculaires, des maux de tête et des vertiges. On distingue principalement deux types d’asthénopie : l’asthénopie accomodative (qui concerne les myopes, les hypermétropes et les presbytes) et l’asthénopie musculaire (suite à un effort anormal visant à fixer une image de façon prolongée)."
        self.caracteristique = {"douleurs oculaires", "maux de tete", "vertige"}
        self.nombres_touche = nombres_touche

#Astigmatisme
class Astigmatisme (Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 11
        self.description = "une perturbation de la vision de près et de loin des lignes en raison d’une cornée légèrement déformée (cornée ovale au lieu d’arrondie)."
        self.caracteristique = {"Vision d'un trait à la place d'un point ", "cornee légerement deforme", "maux de tete", "picotement des yeux"}
        self.nombres_touche = nombres_touche

#Cécité
class Cecite(Maladie):
    def __init__(self,  descrption, caracteristique, nombres_touche):
        self.id = 12
        self.description = "Déficience visuelle totale (absence complète de vision) qui peut être liée à de multiples causes (affection congénitale, cancer, glaucome, cataracte, décollement de la rétine, rétinite pigmentaire, etc.). Une personne atteinte de cécité des deux yeux est dite aveugle"
        self.caracteristique = {"Déficience visuelle total"}
        self.nombres_touche = nombres_touche


#Colobome
class Colobome(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 13
        self.description = "Anomalie du développement du cristallin, de l’iris, de la choroïde ou de la rétine. Cette maladie génétique est décelée dès la naissance. L’acuité visuelle est variable en fonction de l’atteinte rétinienne"
        self.caracteristique = {"Anmalie du développement du cristallin, de l’iris, de la choroïde ou de la rétine", "Maladie genetique"}
        self.nombres_touche = nombres_touche

#Daltonisme
class Daltonisme(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 14
        self.description = "déficience d’un ou plusieurs cônes de la rétine oculaire. C’est une maladie génétique mais le daltonisme peut aussi survenir à la suite d’une lésion nerveuse, oculaire ou cérébrale. Cette déficience entraine une difficulté de perception des couleurs. Le plus fréquemment, un daltonien a des difficultés à faire la différence entre le vert et le rouge."
        self.caracteristique = {"difficulté de perception des couleurs (confusion entre le rouge et le vert en general)", "maladie genetique"}
        self.nombres_touche = nombres_touche

#Décollement de rétine
class Decollement_de_retine(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 15
        self.description = "Maladie rare de l’œil. C’est un décollement d’une partie de la surface de la rétine de son support. Non traitée, elle aboutit à une perte de la vue et donc à la cécité. Elle touche principalement les personnes de plus de 50 ans ayant une forte myopie ou du diabète. Le décollement de la rétine entraine une baisse brutale de la vue, une diminution du champ visuel, des mouches volantes ou une impression de voir des éclairs"
        self.caracteristique = {"baisse brutale de la vue", "diminution du champ visuel","impression de voir des mouches volantes ou des eclairs"}
        self.nombres_touche = nombres_touche

#DMLA
class DMLA (Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 16
        self.description = "Dégénérescence maculaire liée à l’âge. La DMLA est une dégénérescence de la macula (partie centrale de la rétine). Elle entraine donc une perte progressive de la vision centrale et donc une perte progressive de l’autonomie (arrêt de la conduite, de la lecture, des loisirs, etc.). On distinguera deux formes de DMLA ; La DMLA sèche (la plus fréquente) dont l’évolution est lente, mais inévitable. Et la DMLA humide dont l’évolution est très rapide (perte de la vision centrale en quelques semaines à quelques années). Dans certains cas, la DMLA peut entrainer la cécité. Cette maladie des yeux touche principalement les plus de 50 ans. c'est la premiere cause de malvoyance dans les pays developpes"
        self.caracteristique = {"perte progressive de la vision centrale", "premiere cause de malvoyance dans les pays developpes"}
        self.nombres_touche = nombres_touche

#Glaucome
class Glaucome (Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 17
        self.description = "maladie dégénérative de l’œil. Cette maladie entraine une dégénérescence du nerf optique et une perte progressive de la vision périphérique puis centrale. Elle est due à une pression oculaire trop importante dans l’œil. C’est une maladie grave car la perte de vision est irréversible et cette maladie entraine la cécité"
        self.caracteristique = {"dégénérescence du nerf optique", "perte progressive de la vision périphérique puis centrale", "perte de vision irreversible"}
        self.nombres_touche = nombres_touche

#Neuropathie optique de Leber
class Neuropathie_optique_de_Leber(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 18
        self.description = "maladie génétique touchant le nerf optique de l’oeil. La maladie de Leber entraine une perte de la netteté centrale et l’apparition d’un scotome (tâche dans le champ visuel). Cette maladie est détectée chez les jeunes entre 18 et 35 ans et la progression est très rapide (quelques jours à quelques semaines)."
        self.caracteristique = {"perte de la netteté centrale", "apparition de scotome", "progression tres rapide"}
        self.nombres_touche = nombres_touche


#Nystagmus
class Nystagmus(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 19
        self.description = "Déficience de la coordination des muscles de l’œil. Il entraine des mouvements involontaires (lents et rapides) de l’œil. Cette pathologie est fréquemment accompagnée d’un strabisme"
        self.caracteristique = {"mouvements involontaires (lents et rapides) de l’œil", "strabisme"}
        self.nombres_touche = nombres_touche

#Rétinite pigmentaire
class Retinite_pigmentaire(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 20
        self.description = "La rétinite pigmentaire est une maladie génétique de l’œil qui touche les photorécepteurs et l’épithélium pigmentaire. Cette maladie des yeux entraine une perte de la vision nocturne, un rétrécissement du champ de vision et souvent de la photophobie (sensibilité accrue à la lumière)."
        self.caracteristique = {"perte de la vision nocturne", "rétrécissement du champ de vision", "photophobie(sensibilité accrue à la lumière)"}
        self.nombres_touche = nombres_touche

#Rétinoblastome
class Retinoblastome(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 21
        self.description = "Le Rétinoblastome est une tumeur maligne de la rétine qui apparait chez les jeunes enfants âgés de moins de 5 ans. Ce cancer des yeux est d’origine génétique (mutation d’un chromosome). Cette maladie est héréditaire."
        self.caracteristique = {"cible souvent les enfants de moins 5ans", "origine génétique", "maladie hereditaire"}
        self.nombres_touche = nombres_touche

#Stargardt
class Stargardt(Maladie):
    def __init__(self, descrption, caracteristique, nombres_touche):
        self.id = 22
        self.description = "La maladie de Stargardt est une maladie génétique rare entrainant des lésions rétiniennes et une atrophie de la macula. La maladie de Stargardt entraine une baisse progressive et inévitable de la vue dès l’enfance (entre 5 et 16 ans). Toutefois les personnes touchées par cette maladie ne deviennent pas aveugles, même si leur acuité visuelle reste faible (1/10ème à 1/20ème)."
        self.caracteristique = {"maladie genetique rare", "baisse progressive et inévitable de la vue dès l’enfance ", "acuite visuelle faible (entre 1/10ème et 1/20ème)"}
        self.nombres_touche = nombres_touche


















