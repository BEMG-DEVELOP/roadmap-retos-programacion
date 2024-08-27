#Operadores  y estructuras de control
suma = 5 + 4
resta = 5 - 4
division = 5 / 4
multiplicacion = 5 * 4
grupo = 12 + (10 * 2)
#Variables para hacer operaciones matematicas
a = 30
b = 20
c = 40
#Aqui vamos a usar operadores con  variables, estas claro pueden cambiar el valor.
x = (a + c) / b
y = (a % b) * c

division1 = c / b  #clasica division
division2 = c // b #La división de piso descarta la parte fraccionaria
division3 = c % b #El operador % devuelve el resto de la división

elevado = 2 ** 2
elevedoc = c ** 2

print(("Suma", suma, "Resta", resta, "Division", division, "Multiplicacion",multiplicacion),
      (x, y),
      "divisiones",("d1", division1, "d2", division2, "d3", division3),
      elevado)

#Estructuras de control
word = ['perro','gato','pajaro','leon','tigre']

#Estructura for
for w in word:
  print(w, len(w)) #Va hacer una lista del las palabras y su longitud  
for i in range(5):
  print(i) #Va a imprimr del 0 al 4 por el rango de 5 inicia en 0

print("Rango de valores de 3 en 3 ",list(range(0,10,3))) #Va a imprimir del 0 al 10 de 3 en 3
#Estructuras if
#g = int(input("Digite el número para las operaciones: "))
if x > c:
  print("Su cantidad es mayor que:" + str(c))
elif x < c:
    print("Su cantidad es menor que:" + str(c))
elif x == c:
    print("Su cantidad es igual que:" + str(c))
#Sentencias break, continue y else
#Break
for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
          print(n, 'Iguales', x, '*', n//x)
          break
  else:
        # loop fell through without finding a factor
        print(n, 'es un número primo')
#Continue
for num in range(2, 10):
  if num % 2 == 0:
    print("Encontraste un número par", num)
    continue
  print("Has encontrado un número impar", num)
#Match esta instruccion compara su valor con sucesivos patrones dados como uno  o más bloques, es similar a un switch.

def error(status):
  match status:
    case 400:
      return "Error de solicitud"
    case 404:
      return "Error de pagina no encontrada"
    case 500:
      return "Error en el servidor"
    case 201|202:
      return "Erro de envio"
    case _:
      return "Error desconocido"
      
status_codes = [400, 404, 500, 201, 202, 418]

for code in status_codes:
    print(f"Status {code}: {error(code)}")
