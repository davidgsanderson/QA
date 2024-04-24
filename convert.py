unit = input("What unit would you like to input weight?")
weight = float(input("Please enter your weight to convert"))

if unit.lower() == "kgs" :
    result = weight * 2.205
elif unit.lower() == "lbs":
    result = weight/2.205
else :
    print("Incorrect unit")

print(result)
    

