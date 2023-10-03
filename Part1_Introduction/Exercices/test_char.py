

def testUpper( l ):
    for e in l :
        if e.upper() != e :
            return False

    return True




testUpper(['A', 'B', 'C' , 'D']) # True
