import sys
import os
from funcoes import *

def clear():
    os.system("\n\n\n")
    os.system("clear")

def menu(op):
  print("\n***********************************")
  try:
      if op == 1:
          mm1()
      elif op == 2:
          mms()
      elif op == 3:
          mm1k()
      elif op == 4:
          mmsk()
      elif op == 0:
          print("Saindo...")
          exit()
      else:
          print("Operacao Invalida... Exiting")
          exit()
  except KeyboardInterrupt:
       print("\n\nSaindo...")
       exit()


def showMenu():
    clear()
    print(" Escolha uma operacao:")
    print(" 1. MM1\n 2. MMS\n 3. MM1k\n 4. MMSK\n 0. Sair\n ")

    op = int(input("Op >> "))
    menu(op)

while True:
   showMenu()
   input("\nAperte ENTER para continuar...")
