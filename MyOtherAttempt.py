# Without consistence, I stopped learning about programming so soon, yet here I return.
# This file is an attempt to remember eveything I've learned and build from zero something, anything.
# I'll use every syntax I know and improve this code from time to time.
def main():
    kg = float(input("IMC palate, insert your weight in the scale kg or g. "))
    m = float(input("Now insert your height in any the scale m or cm. "))
    if kg < 0:
        print("Invalid.")
    if m < 0:
        print("Invalid")
    if kg > 635:
        convert(kg)
    if m > 3:
        convertm(m)
    print(f"You are {imc(kg, m)}")
    
def convert(kg):
    return float(kg / 1000)

def convertm(m):
    return float(m / 100)

def imc(kg, m):
    x = kg / (m ** 2)
    if x < 18.5:
        return f"Dead and {x}"
    elif 18.5 < x < 24.9:
        return f"Normal and {x}"
    elif x > 24.9:
        return f"Careful and {x}"
    
if __name__ == main():
    main()

# I'll update this from time to time.
