print("Taschi ")
zahl1 = int(input("Bitte die 1 zahl eingeben: "))
zahl2 = int(input("Bitte die 2 zahl eingeben: "))
operation = input("+, -, * oder / :")

if(operation == "+"):
  summe = zahl1 + zahl2
  print("Summe", summe)
  
if(operation == "-"):
  dif = zahl1 - zahl2
  print("Differenz", dif)

if(operation == "*"):
  Pro = zahl1 * zahl2
  print("Produkt", Pro)
  
if(operation == "/"):
  if(zahl2 == 0):
    print("Danke du wolltest durch 0 dividiert")
  if(zahl2 != 0):
    qou = zahl1 / zahl2
    print("Qutient", qou)
   