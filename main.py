import sys
import os
import argparse
from funcoes import *

def clear():
    os.system("\n\n\n")
    os.system("clear")

def menu(op, help=False):
  print("\n***********************************")
  try:
      if op == 1:
          mm1(help)
      elif op == 2:
          mms(help)
      elif op == 3:
          mm1k(help)
      elif op == 4:
          mmsk(help)
      elif op == 0:
          print("Saindo...")
          exit()
      else:
          print("Operacao Invalida... Exiting")
          exit()
  except KeyboardInterrupt:
       print("\n\nSaindo...")
       exit()


def showMenu(args):
    clear()
    print(" Escolha uma operacao:")
    print(" 1. MM1\n 2. MMS\n 3. MM1K\n 4. MMSK\n 0. Sair\n ")

    op = int(input("Op >> "))
    menu(op, help=args.ajuda)


parser = argparse.ArgumentParser()
parser.add_argument('--ajuda', action='store_true', dest='ajuda', help = 'Mostrar significado das variaveis')
args = parser.parse_args()
while True:
   showMenu(args)
   input("\nAperte ENTER para continuar...")
