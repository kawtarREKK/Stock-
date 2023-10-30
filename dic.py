dic_prix={"samar":20,"beurre_jawda":90,"the":25,"poire":20}
stock=[["samar",100],["the",200],["beurre_jewda",150],["poire",250]]
article=input("qulle article tu veux ?")
quantité=float(input("donnez la quantité:"))
prix_total=0
x="oui"
existe=False
for i in range(4):
    if article==stock[i][0] and quantité<=stock[i][1]:
        prix =quantité*dic_prix[article]
        prix_total+=prix
        stock[i][1]-=quantité
        existe=True
    elif article== stock[i][0] and quantité>stock[i][1] : 
        print (" la quantité que tu veux est supérieur a la quantité de stock\n la quantité de stock est:",stock[i][1])
        réponse=(input("Voulez_vous cette quantité disponible en stock?"))
        if réponse=="oui":
            prix=stock[i][1]*dic_prix[article]
            prix_total+=prix
            existe=True
    
if existe!=True:
    print(" désolé cette article né pas déssponible ")

while x=="oui" :
    x=input("est_ce que tu veux autre article?")
    
    if x== "oui"  :
        article =input("qulle article tu veux ?")
        quantité =float(input("donnez la quantité:"))
        existe=False
        for i in range(4):
            if article==stock[i][0] and quantité <=stock[i][1]:
                prix =quantité*dic_prix[article]
                prix_total+=prix 
                stock[i][1]-=quantité
                existe=True
            elif article==stock[i][0] and quantité>stock[i][1] and stock[i][1]>0:
                print (" la quantité que tu veux est supérieur a la quantité de stock\n la quantité de stock est:",stock[i][1])
                réponse=(input("Voulez_vous cette quantité disponible en stock?"))
                if réponse=="oui":
                    prix=stock[i][1]*dic_prix[article]
                    prix_total+=prix
                    existe=True
            elif article== stock[i][0] and quantité>stock[i][1] and stock[i][1]==0: 
                    print(f"cette article est épuisée en stock")
                    existe=True
        if existe!=True:
            print(" désolé cette article né pas déssponible ")
    else:
        x="Non"
print("le prix total est " ,prix_total)                



    
        

