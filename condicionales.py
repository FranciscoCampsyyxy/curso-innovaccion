# declaramos una variable
calificacion = input("introduce tu calificacion de la AZ-900: ")

calificacion = int(calificacion)

# preguntamos si la calificacion es menor a 700 
if calificacion < 700 :
    print("vees por no estudiar, estupide") # si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("mienteees, no puedes sacar mas de 1000, haz de ser onvre")
else : # si no se cumple el if anterior pasa a esta linea 
    print("felicidades, pasa por tu certificado") # se ejecuta si ninguno de los if se cumple


# verificador de mayoria de edad
edad = input("introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("bienvenido al mamitas")
elif edad > 100 :
    print("si vienes acompañado de tus abuelitos si te podemos fiar")
elif edad < 0 :
    print("ni que fueras viajero del tiempo")
else :
    print("no puedes llevarte esos cigarros ")