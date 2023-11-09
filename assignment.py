ExtraLarge = 10
Large = 6
OneTopping = 1
TwoTopping = 1.75
ThreeTopping = 2.5
FourTopping = 3.35
ifcondition = True
ifcondition2 = True
Tax = 0.13

while ifcondition:
    print("Choose your pizza size")
    PizzaSize = (input("large or extra large"))
    if PizzaSize ==  "large" or PizzaSize == "extra large" :
        ifcondition = False
       
if PizzaSize ==  "large":
    PizzaCost = Large
if PizzaSize == "extra large":
    PizzaCost = ExtraLarge

while ifcondition2:
    print("Choose your toppings")
    PizzaTop = (input("1, 2, 3 or 4"))
    if PizzaTop == "1" or "2" or "3" or "4":
        ifcondition2 = False

if PizzaTop == "1":
    PizzaCost = PizzaCost + OneTopping
if PizzaTop == "2":
    PizzaCost = PizzaCost + TwoTopping
if PizzaTop == "3":
    PizzaCost = PizzaCost + ThreeTopping
if PizzaTop == "4":
    PizzaCost = PizzaCost + FourTopping

Subtotal = PizzaCost
print(" Subtotal: $"+ str(PizzaCost))
Tax = Tax * Subtotal
print(" Tax: $" + str(round(Tax, 2)))
Total = Tax + Subtotal
print(" Total: $" + str(round(Total, 2)))
