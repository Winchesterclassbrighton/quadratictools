import math as mt


def factor(a, b, c):
    q = mt.pow(b, 2.0)-4*a*c
    if q > 0:
        r1 = (-b+mt.sqrt(q))/(2*a)
        r2 = (-b-mt.sqrt(q))/(2*a)
        if r1 < 0 :
            if r2 < 0:
                result = str(a) + " ( x + " + str(r1) + " ) ( x + " + str(r2) + " )"
            else:
                result = str(a) + " ( x + " + str(r1) + " ) ( x - " + str(r2) + " )" 
        elif r2 < 0:
            result = str(a) + " ( x - " + str(r1) + " ) ( x + " + str(r2) + " )" 
        else:
            result = str(a) + " ( x - " + str(r1) + " ) ( x - " + str(r2) + " )"
        return result
    else:
        return "EXCEPTION: unfactorable due to imaginary roots"


print(factor(1, 5, 6))
