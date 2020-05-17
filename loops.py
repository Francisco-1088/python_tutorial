num = 1

for count in range(3):
while num > 0:
   num = int(input("Introduce un número: "))
   if num < 1:
      print ("¡Soy menos que 1!")
      print ("¡Adiós mundo cruel!")
   elif num == 1:
      print ("¡Soy igual a 1!")
   else:
      print ("El valor es: " + str(num))
      print ("El valor es: ", num)
