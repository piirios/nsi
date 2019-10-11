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
    def __init__(self):
        self.nom = ["Jean", "Moussa", "Didier", "Kevin", "Marine", "Julien","Yasmina", "Mickael", "Abdel", "Céline", "Audrey", "Binta"]
        self.note = [8,9.5,14,7.5,17,14,5,17.5,13,7.5,12.5,7.5]
    def moyenne(self):
        return sum(self.note)/len(self.note)
    def findall(self, nom, array):
        finding = []
        for x in range(len(array)):
            if array[x] == nom:
                finding.append([x, nom])
        return finding
    def find(self,name):
        try:
            finding = self.nom.index(name)
            return True, finding, self.note[finding], self.findall(self.note[finding], self.note)
        except ValueError:
            return False
    def maxmin(self, array):
        return max(array), min(array)
    def classement(self, array, nom):
        array.sort(reverse=True)
        return array.index(nom)+1



exo = exercice()
print(exo.find('Didier'))
print(exo.maxmin(exo.note))
print(exo.classement(exo.note, 17.5))
