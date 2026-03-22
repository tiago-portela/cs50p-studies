#What i've learned with CS50P today
#Variables, functions and types of data, and the split(one shall never forget how to split...I suppose.)
p = print
z = input("Howdy! What's your name? ").strip().title()
a, b = z.split(" ")
x = int(input("And your age? "))
p(f"Hey, {a}! You still have {980 - x} years before 980!")
#But obviously I want something crazier, so why not a calculator that calculates wrong
e = float(input("This is a calculator of multiplication that works with only two numbers. Go on, insert the first: "))
w = float(input("Now the second: "))
print(f"Here the result! {round((e / w) + 2+2)}")
print("Yeah, it is wrong. Cry about it.")
#I am feeling that I depend too much on the input to do anything and I could probably try something else in the calculator trope, but I don't know how yet.
