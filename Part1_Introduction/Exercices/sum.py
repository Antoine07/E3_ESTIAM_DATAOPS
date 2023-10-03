"""

Faites une fonction qui fait la somme de N entier(s) consécutif(s)

sumInt( 10 )

1 + 2 + ... + 10 

"""

def sumInt( n ):
    s = 0
    for i in range(0, n + 1):
        s += i

    return s 

print( sumInt( 100 ) )
