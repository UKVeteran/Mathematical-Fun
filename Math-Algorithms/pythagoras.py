"""
input two of the three side in right angled triangle and return the third. use "?" to indicate the unknown side. 
"""

def pythagoras(opposite,adjacent,hypotenuse):
    try:
        if opposite == str("?"):
            return ("Opposite = " + str(((hypotenuse**2) - (adjacent**2))**0.5))
        elif adjacent == str("?"):
            return ("Adjacent = " + str(((hypotenuse**2) - (opposite**2))**0.5))
        elif hypotenuse == str("?"):
            return ("Hypotenuse = " + str(((opposite**2) + (adjacent**2))**0.5))
        else:
            return "You already know the answer!"
    except:
        print ("Error, check your input. You must know 2 of the 3 variables.")
        
print(pythagoras(3,4,"?"))