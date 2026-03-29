# Trying to use not only whatever I've learned in week 1 but also of week 0.
# Let's try something less calculation but tied to numbers and sometimes fales or trues.
# I didn't want to copy the guy on the video, so I did this:
def main():
    a = input("Patent: ").strip().title()
    b = input("Name: ").strip().title()
    c = int(input("Rad digit: "))
    d = int(input("Sector Code: "))
    print(f"Patent: {a} | Individual: {b} | Radiation: {c}Rad | Sector:{d}, {cabin(d)} | Access", parole(a, c))

def cabin(sector):
    if sector % 2 == 0:
        return "Cabin A"
    else:
        return "Cabin B"

def parole(patent, radiation):
    match patent:
        case "Marshall" | "Cadet" | "Big Boss":
            patent = 1
    if patent != 1 or radiation > 50:
        return "DENIED." 
    if patent == 1 and radiation <= 50:
        return "GRANTED."


main()

# THis thing is HIGHLY crashable but it works somehow.
    

