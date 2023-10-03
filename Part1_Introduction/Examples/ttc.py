"""
Créez une fonction qui calcule le prix TTC d'un produit 
"""

def ttc(tva, priceHT):

    # return tva * priceHT + priceHT
    return priceHT * ( 1 + tva )

print( ttc( priceHT = 100, tva = 0.2 ) )


