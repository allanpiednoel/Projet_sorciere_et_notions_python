
class Telephone:

    #attributs de classe

    smartphone = False 
    materiaux= "plastique, metal"
    
    def __init__(self, nom, annee_fabrication, Nb_proprios=0):

         #attributs d'instance

        self.nom = nom                                 
        self.annee_fabrication = annee_fabrication
        self.Nb_proprios = Nb_proprios

        if (self.annee_fabrication>2000):
            self.smartphone = True

      #permet de faciliter le print      
    
    def __str__(self):        
        if(self.smartphone):
            result = f"ce smartphone est un {self.nom}, et est sorti en {self.annee_fabrication}, a eu {self.Nb_proprios} proprietaires.\n"
        else:
            result = f"ce vieux telephone est un {self.nom}, et est sorti en {self.annee_fabrication},  a eu {self.Nb_proprios} proprietaires.\n"
        return result

    #methode d'instance

    def leBonCoin (self):
        self.Nb_proprios += 1

    #methode de classe

    @classmethod
    def RueeVersLor(cls):
        cls.materiaux = "100% pur or"

#heritage

class Telephone_clapet(Telephone):

    touches = True

    def __init__(self,nom, annee_fabrication, prise_ecouteurs, Nb_proprios=10):
        super().__init__(nom, annee_fabrication)
        self.prise_ecouteurs =  prise_ecouteurs
        self.Nb_proprios = Nb_proprios

    def __str__(self):
        return f"ce vieux telephone est un {self.nom}, et est sorti en {self.annee_fabrication}, a eu {self.Nb_proprios} proprietaires. prises ecouteurs ? {self.prise_ecouteurs}\n"

#instanciation de classes

telephone1 = Telephone("OnePlus", annee_fabrication = 2018)
telephone2 = Telephone("nokia 3310", annee_fabrication = 2000)
telephone3 = Telephone("Iphone", annee_fabrication = 2020)

telephone4 = Telephone_clapet ("Logicom", annee_fabrication = 1980,prise_ecouteurs=True)

#on peut accéder aux différentes variables d'instances, ou a tout a la fois

print (telephone1.nom)
print (telephone1.annee_fabrication)
print (telephone2)
print (telephone3)

telephone3.leBonCoin()
telephone3.leBonCoin()

print (telephone3)
print (telephone2)

Telephone.RueeVersLor()

print (f"le {telephone1.nom} est en {telephone1.materiaux}")
print (f"le {telephone2.nom} est en {telephone2.materiaux}")

print(telephone4)

print (f"le {telephone4.nom} est en {telephone4.materiaux}")