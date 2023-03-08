#for i in [0,1,2,3] : 
 #   print("i a pour valeur", i) 

#a = int(input("saisir une nombre : "))
#for i in range(1, 11) :
#    print(a, " *", i, "=", (a*i) )

# ######################
# def test(none,ntwo):
#     s = 0
#     s2 = 0
#     for i in range(1,none):
#         if none%i == 0:
#             s=s+i
#     for i in range(1,ntwo):
#         if ntwo%i == 0:
#             s2=s2+i
#     if s==ntwo and s2==none : 
#         return True
#     else :
#         return False
#     print(test(none,ntwo))
# def fromzerotomile():
#     list =[]
#     for i in range (1,1300):
#         for j in range(i+1,1300):
#             if i != j and test(i,j):
#                 mytuple= (i,j)
#                 list.append(mytuple)
#     return list
# print(fromzerotomile())
# #################
# a = input("entrer un nombre :")
# s=0
# for i in a:
#   s=s+1
# print (s)
# a= list(input("enter un nombre: "))
# for i in range(0,a):
#     print(list[a-i], " ,")
# #############
# s=0
# for i in range(-10,100):
#     if(i==0):
#         continue
#     else:
#        s=s+1/i
# print(s)    
# ####################
# n= int(input("ecrire un nombre : "))
# list=[]
# while(n != 0):
#     modulo = n%10
#     list.append(modulo)
#     n=n//10
# print("le premier chiffre est", list[-1], "le dernier est", list[0])
# ###########################
import array
# for i in range(1,11):
#    b=a+a*0.1
   
# print("le nombre devient: ", b)
# -------------------------------------------------

# def revers():
#    tab = array(['a','b','c','d','e'])
#    for i in tab:
#       print(tab[i-1])
#       i=i+1

# print(revers())

# def voyell(l):
#    nbvoye=0
#    for i in range(0,len(l)):
#       if (l[i] in ['a','e','i','u','y','A','E']):
#          nbvoye = nbvoye+1
#    print(nbvoye)

# voyell("Salma El Allali")

#----------------------------

# def fact(a):
#    if a == 0 or a == 1 :
#       return 1
#    else :
#       return a*fact(a-1)
   
# print(fact(3))
#---------------------------------------------------



# class personne:
#    def __init__(self, name, age):
#       self.name= name
#       self.name= age
#    def afficher(self):
#        print("bonjour je suis " +self.name+ "et j'ai "+ self.age + " ans")

# personne1 = personne("salma","20")
# personne1.afficher()

# class voiture:
#    def __init__(self , marque):
#       self.marque= marque
#    def annee_modele(model):
#       return "2022"
#    def afficher(self):
#       print("la marque de cette voiture est :" +self.marque+ " model "+self.annee_modele())
# mvoiture= voiture("audi")
# mvoiture.afficher()

# class comptebancaire:
#    def __init__(self,idnumber,nomprenom, solde) :
#       self.numerocompte= idnumber
#       self.nom=nomprenom
#       self.solde=solde
#    def versement(self, number):
#       if(self.solde < number):
#          print("on peut pas effectuer virement")

#    def retrait(self, number1):
#       if(int(self.solde) < number1):
#          print("on peut pas effectuer le retrait")
#       else :
#          print("retrait effectue")
#          self.solde=int(self.solde)-int(number1)

#    def afficher(self):
#       print(" votre numero d compte est "+self.numerocompte+ " votre nom est: "+self.nom+ " votre solde est: "+int(self.solde))
# compte = comptebancaire("123","salma","1000")
# compte.afficher()
# compte.retrait(600)
#abstraction-------------------------------------
# from abc import ABC, abstractclassmethod
# class bank(ABC):
#    @abstractclassmethod
#    def balance_check(self):
#       pass
#    @abstractclassmethod
#    def interest(self):
#       pass
# class sbi(bank):
#    def balance_check(self):
#       print("balance is 100 rupees")
#    def interest(self):
#       print("sbi interest is 5 rupees")
# s=sbi()
# s.balance_check()
# s.interest()

#----fichier-------------------------------------------

# file = open("C:\Users\hp\Desktop\new.txt","w")
# file.write("j'ai supprime tout")
# file.close()
# file = open(r"C:\Users\hp\Desktop\new.txt","r")
# print(file.read())


# import os
# os.remove(r"C:\Users\hp\Desktop\new.txt")

# import os
# if os.path.exists(r"C:\Users\hp\Desktop\new.txt"):
#    print("fichier trouvale")
# else:
#    print("fichier introuvable")

#-------exercice------------
def saisir():
   new = "0"
   fichier = open("concour.txt","a")
   decision = {"a": "admise", "r": "refusee","aj": "ajournee"}
   while new == "0":
      cin = input("saisir le CIN ")
      nom = input("saisir le nom ")
      age= input("saisir le age ")
      dec = input("saisir decision ")
      ligne= cin+";"+nom+";"+age+";"+decision[dec]+"\n"
      fichier.write(ligne)
      new = input("saisir un nouveau candidat 0 ou n ")
   fichier.close()

def admis():
   fichier = open("concour.txt")
   dest = open("admis.txt","a")
   for ligne in fichier:
      L= ligne.split(";")
      if L[3].strip()== "admise":
         dest.write(ligne)
   fichier.close()
   dest.close()

admis()

def attente():
   fichier= open("admis.txt")
   dest = open("attente.txt","a")
   for ligne in fichier:
      L=ligne.split(";")
      if int(L[2]) >= 30:
         enreg = L[0]+ ";" +L[1]+ ";" + L[3] + "\n"
         dest.write(enreg)
   fichier.close()
   dest.close()





















