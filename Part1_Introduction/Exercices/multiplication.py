"""

1. Créez une boucle pour afficher la table de multiplication de 7 par exemple
2. Créez une fonction qui permet de calculer l'ensemble de toutes les tables de multiplication

""" 

# la table 7
for n in range(1, 11):
    print( n * 7)

# Une fonction qui permet d'avoir toutes les tables 
def mutl(n):
    # une liste 
    res = []
    for n in range(1, 11):
        # print( n * 7)
        # on a poussé les éléments dans la liste 
        res.append(n * 7)
    
    # sortir le résultat de la fonction 
    return res 


print( mutl(11) )
