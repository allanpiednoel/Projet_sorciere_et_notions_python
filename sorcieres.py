import sys
import math
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


liste_clients = []
liste_sorts = []
index=-1



class Client:
    def __init__(self,id, prix, ingr0, ingr1, ingr2, ingr3,numberIngr=0):
        self.id = id
        self.prix = prix
        self.ingr0 = ingr0
        self.ingr1 = ingr1
        self.ingr2 = ingr2
        self.ingr3 = ingr3
        self.prix = prix
        self.numberIngr = abs(self.ingr0)+abs(self.ingr1)+abs(self.ingr2)+abs(self.ingr3)

    def __repr__(self):
        return f"{self.id},{self.prix}, {self.ingr0}, {self.ingr1}, {self.ingr2}, {self.ingr3}"
    
    def jettePotion(self,*args):
            print ("BREW ",self.id)

    
class Sorts:
    def __init__(self, id, castable, ingr0=0, ingr1=0, ingr2=0, ingr3=0):
        self.id = id
        self.ingr1 = ingr0
        self.ingr2 = ingr1
        self.ingr3 = ingr2
        self.ingr4 = ingr3
        self.castable = castable

    def __repr__(self):
        return f"\n{self.id},{self.castable}, {self.ingr1}, {self.ingr2}, {self.ingr3}, {self.ingr4}\n"
    
    def jetteSort(self, *args):
     
        if self.castable:
            print("CAST ", self.id)   
        elif self.castable==False:
            print("REST")

        
class Sorciere:
    def __init__(self, inv_0_, inv_1_, inv_2_, inv_3_, score, liste_sorts, liste_clients):
        self.inv_0_ = inv_0
        self.inv_1_ = inv_1
        self.inv_2_ = inv_2
        self.inv_3_ = inv_3
        self.score = score
        self.liste_sorts = liste_sorts
        self.liste_clients = liste_clients


    def __repr__(self):
        return f"{self.inv_0_}:{self.inv_1_}: {self.inv_2_}: {self.inv_3_}: {self.score}: {self.liste_sorts}\n"
        

    def getEau_unit(self):
        self.liste_sorts[0].jetteSort()

    def getFeuille_unit(self):
     
        self.liste_sorts[1].jetteSort()
        

    def getTache_unit(self):
       
        self.liste_sorts[2].jetteSort()

    def getTacos_unit(self):
     
        self.liste_sorts[3].jetteSort()

    def getIngredientsPotion(self, id_a_calculer):
        delta = []
        validation =0
        
        sorts_a_faire = {}
#on doit calculer l'ordre des sorts pour réaliser la commande
#-recupérer les ingrédients de la commande
        for client in liste_clients:
            if client.id==id_a_calculer:
                delta=[client.ingr0,client.ingr1,client.ingr2,client.ingr3]
                #connaitre la différence entre l'inventaire et la commande visée (si c nég -> il en manque; si c pos -> on en a en rab)
              
                a =self.inv_0_+client.ingr0
                b =self.inv_1_+client.ingr1
                c =self.inv_2_+client.ingr2
                d =self.inv_3_+client.ingr3

                #j'ai choisi sous forme de dictionnaire uniquement pour ma compréhension
                sorts_a_faire={1:a,2:b,3:c,4:d}                   
                break


        #variable servant à savoir si on a tout les ingrédients nécéssaire à la commande visée
        for i in range(1,5):
            if sorts_a_faire[i]>=0:
                validation += 1
              
        if validation==4:
            for client in liste_clients:
                if client.id==id_a_calculer:
                    client.jettePotion()
            #print("BREW", id_a_calculer)           
            return

        #Pour ne pas me perdre, j'ai changé les noms des ingrédients:
        #   -Ingredient0 -> Eau
        #   -Ingrédient1 -> Feuille
        #   -Igredient2 -> Tache
        #   -Ingredien3 -> Tacos


        #garder un seuil minimal d'Eau
        if sorts_a_faire[1]<1:
            self.getEau_unit()
            return

        #on commence par les ingrédients les plus longs a avoir pour faire le moins de mouvements possible
        #toujours interrompre les boucles avec return pour eviter de surcharger la sortie standart (un seul print a la fois)
        #peut etre peut-on optimiser ce bout de code?
        debug(sorts_a_faire)
        if sorts_a_faire[4] < 0:
                
            for i in range(1,4):

                if self.liste_sorts[i].castable:
                    self.liste_sorts[i].jetteSort()
                    return

                else: pass

        elif sorts_a_faire[3] < 0:

                
            for i in range(1,3):
                if self.liste_sorts[i].castable:
                    self.liste_sorts[i].jetteSort()
                    return 
                else: pass  
            
        elif sorts_a_faire[2] < 0:
                
            for i in range(1,2):
                if self.liste_sorts[i].castable:
                    self.liste_sorts[i].jetteSort()
                    return
                else: pass

        elif sorts_a_faire[1] < 0:           
            if self.liste_sorts[0].castable:
                self.liste_sorts[0].jetteSort()
                return
            else: pass


        #si on ne peut rien faire, rest restaure tous les sorts
        debug("aaaaa")
        print("REST")



        return
         

DEBUG = True
def debug(*args, force=False, **kwargs):
    if DEBUG or force:
        print(*args, **kwargs, file=sys.stderr, flush=True)


# game loop
mem_score = []
mem_s = 1
while True:
    

    liste_clients = []
    liste_sorts = []
    index+=1
    if index >3:index=0
    best_price =0
    best_id=0
    action_count = int(input())  # the number of spells and recipes in play
    for i in range(action_count):
        inputs = input().split()
        action_id = int(inputs[0])  # the unique ID of this spell or recipe
        action_type = inputs[1]  # in the first league: BREW; later: CAST, OPPONENT_CAST, LEARN, BREW
        delta_0 = int(inputs[2])  # tier-0 ingredient change
        delta_1 = int(inputs[3])  # tier-1 ingredient change
        delta_2 = int(inputs[4])  # tier-2 ingredient change
        delta_3 = int(inputs[5])  # tier-3 ingredient change
        price = int(inputs[6])  # the price in rupees if this is a potion
        tome_index = int(inputs[7])  # in the first two leagues: always 0; later: the index in the tome if this is a tome spell, equal to the read-ahead tax; For brews, this is the value of the current urgency bonus
        tax_count = int(inputs[8])  # in the first two leagues: always 0; later: the amount of taxed tier-0 ingredients you gain from learning this spell; For brews, this is how many times you can still gain an urgency bonus
        castable = inputs[9] != "0"  # in the first league: always 0; later: 1 if this is a castable player spell
        repeatable = inputs[10] != "0"  # for the first two leagues: always 0; later: 1 if this is a repeatable player spell
        

        #differencier les clients et les sorts
        if(price!=0):
            
            liste_clients.append((Client(action_id, price, delta_0,delta_1,delta_2,delta_3)))

        elif action_id > 77:

            liste_sorts.append((Sorts(action_id, castable, delta_0,delta_1,delta_2,delta_3)))

        del liste_sorts[4:]

            
        if best_price<price:

            best_price=price
            best_id=action_id



    ma_sorciere=[]
    debug(best_id)
    for i in range(2):
        # inv_0: tier-0 ingredients in inventory
        # score: amount of rupees
        inv_0, inv_1, inv_2, inv_3, score = [int(j) for j in input().split()]
        ma_sorciere.append(Sorciere(inv_0, inv_1, inv_2, inv_3, score, liste_sorts, liste_clients))
    debug(ma_sorciere[0])


    #effectuer un REST après avoir jeté une potion pour revenir a 0

    if len(mem_score)>=3 and mem_s == 1:

        if mem_score[1]!=mem_score[2]:

            del mem_score[2]
            mem_s = 0
            print("REST")
            pass

            #lancer la fonction de stratégie
    ma_sorciere[0].getIngredientsPotion(id_a_calculer=best_id)

    #mémoire de score

    mem_score.append(ma_sorciere[0].score)

    if len(mem_score)>3:

        del mem_score [2]
    


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # in the first league: BREW <id> | WAIT; later: BREW <id> | CAST <id> [<times>] | LEARN <id> | REST | WAIT
