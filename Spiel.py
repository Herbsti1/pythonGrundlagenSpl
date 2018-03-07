import random
zufallszahl = random.randint(1,101)

print("Zahlraten - errrate meine Zahl zwischen 1 und 100")
versuch = 0
gewonnen = False


while gewonnen == False:
  zahl = int(input("Welche Zahl"))
  versuch = versuch + 1
  if (zahl == zufallszahl):
    print("Gratuliere! du hast die Zahl erraten.")
    gewonnen = True
  elif (zahl < zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist größer.")
  elif (zahl > zufallszahl):
    print("Leider nein! Die gesuchte Zahl ist kleiner.")
    
print("anzahlö der Versuche", versuch)