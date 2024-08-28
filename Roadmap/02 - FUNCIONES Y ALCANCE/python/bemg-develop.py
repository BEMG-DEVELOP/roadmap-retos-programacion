#Funciones y alcances
#Una función se define mediante la palabra reservada def, seguida del nombre de la función, paréntesis y dos puntos
import asyncio


def usuario(nombreCompleto):
  print("Hola", nombreCompleto)


#usuario('Brian E. Mtz. Gr.')


def operaciones(a, operador, b):
  match operador:
    case '+':
      print('La suma es :', a + b)
    case '-':
      print('La resta es :', a - b)
    case '*':
      print('La multiplicación es :', a * b)


#operaciones(4,'+',12)

i = 5


def f(arg=i):
  print(arg)


i = 6
#f()


def incremento(n):
  return lambda x: x + n


g = incremento(42)


#print(g(1))
async def tarea1():
  print("Tarea 1 Iniciada")
  await asyncio.sleep(3)
  usuario('Brian E. Mtz. Gr.')
  await asyncio.sleep(3)
  print("Tarea 1 Finalizada")


async def tarea2():
  print("Tarea 2 iniciada")
  await asyncio.sleep(1)
  operaciones(4, '*', 5)
  await asyncio.sleep(1)
  print("Tarea 2 finalizada")


async def main():
  await asyncio.gather(tarea1(), tarea2())


asyncio.run(main())
