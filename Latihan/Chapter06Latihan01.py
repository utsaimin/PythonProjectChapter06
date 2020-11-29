def isPythagoras(a, b, c):
    if((a*a) == (c*c) - (b*b) or (b*b) == (c*c) - (a*a) or (c*c) == (a*a) + (b*b)):
        print(True)

    else :
        print(False)

#a
isPythagoras(3, 4, 5)
#b
isPythagoras(5, 9, 12)
#c
isPythagoras(8, 6, 10)
#d
isPythagoras(7, 8, 11)

