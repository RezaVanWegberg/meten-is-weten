a = (int(input("Give A a number ")))
b = (int(input("Give B a number ")))

if a > b:
    Max = a
    Min = b
    print("A is de grootste waarde")
elif a < b:
    Min = a 
    Max = b 
    print("A is de kleinste waarde")
else:
    print("A en B zijn even groot")

print("Het minimum is: " + str(Min))
print("Het maximum is: " + str(Max))
