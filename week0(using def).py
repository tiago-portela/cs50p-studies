# Using def.
# Didn't make use of def properly in the last code in week0, therefore I'm doing this.
l = int(input("Your value of variation: "))
p = float(round(2 * (10 + 10 + 223 + 90 / 4) / l, 2))


def x(): #tax
    return float(round(1000 + (90 * 90 * p), 2))

m = float(input("Hey, now add your id digit: "))
print(f"The total is {float(m * x())}")

# The justification for this code: my lack of defs in my first week0, which would not make sense if I wanted to show what I've learned.
# Well, this is just a simple math calculation.
