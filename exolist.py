##################
# exercice tableau
##################

##################
# import
##################


##################
#classes
##################
class exercice:
    def __init__(self): #initalise les tableaux noms et note
        self.nom = ["Jean", "Moussa", "Didier", "Kevin", "Marine", "Julien","Yasmina", "Mickael", "Abdel", "Céline", "Audrey", "Binta"]
        self.note = [8,9.5,14,7.5,17,14,5,17.5,13,7.5,12.5,7.5]
    def moyenne(self): #calcule la moyenne à partir de la somme et et de la taille du tableau
        return sum(self.note)/len(self.note)
    def findall(self, nom, array): #fonction pour trouver tout les valeurs indiqués dans le tableau indiquée
        finding = [] #tableaux des resultats
        for x in range(len(array)): # boucle for pour parcourir le tableau
            if array[x] == nom: # si l'itération == valeur indiqué
                finding.append([x, nom]) #ajoute le nom dans le tableau de resultat
        return finding # retourn le tableau de resultat
    def find(self,name):
        try: #essaye:
            finding = self.nom.index(name) # de trouver l'index de la valeur
            return True, finding, self.note[finding], self.findall(self.note[finding], self.note) # retourne, l'index du nom, la note du nom, récupère toute les notes identique à celle associé au nom
        except ValueError: # si l'exeption ValueError est relevé
            return False #retourne rien
    def maxmin(self, array): 
        return max(array), min(array) # fonction retournant le maximum et le minimum du tableau
    def classement(self, array, nom):
        array.sort(reverse=True) # trie le tableau
        return array.index(nom)+1 #retoune la position du nom



exo = exercice() #instencie la classe exercice
print(exo.find('Didier'))
print(exo.maxmin(exo.note))
print(exo.classement(exo.note, 17.5))
