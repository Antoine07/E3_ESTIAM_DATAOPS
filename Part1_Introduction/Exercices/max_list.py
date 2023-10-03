
def maxList(l):
    lenList = len(l)
    if lenList > 0 :
        elMax = l[0]
        i = 0 # pour l'indice 

        for e in range(1, lenList ):
            if l[e] > elMax:
                elMax = l[e]
                i = e

        return {"max" : elMax, "indice" : i }
    else:
        return None 


print( maxList([19, 1, 100, 234, 89, 0, -1]) )