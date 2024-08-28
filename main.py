from selectors import SelectSelector

Anrede = input("Bitte Anrede eingeben: ")
name = "Daniel"
wohnort = 'Hamburg'
Alter = 45
Geschlecht = input ('Bitte geben sie ihr Geschlecht ein: ')
if Geschlecht == 'Männlich':
    print ('Sehr geehrter Herr ' + Anrede)
elif Geschlecht == 'Weiblich':
    print ('Sehr geehrte Frau ' + Anrede)
else: print ('Sehr geehrtes ' + Anrede)


print("Hallo lieber " + Anrede)
print("Mein Name ist " + name)
print("Ich bin aus " + wohnort)
print("und bin " + str(Alter) + " Jahre alt")  # dfd
