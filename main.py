import sys
import os
import argparse
from funcoes import *

def clear():
    os.system("\n\n\n")
    os.system("clear")

def menu(op, help, ler_p):
  print("\n***********************************")
  try:
      if op == 1:
          mm1(help, ler_p)
      elif op == 2:
          mms(help, ler_p)
      elif op == 3:
          mm1k(help, ler_p)
      elif op == 4:
          mmsk(help, ler_p)
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

    op = read("Op >> ", int)
    menu(op, args.ajuda, args.ler_p)


parser = argparse.ArgumentParser()
parser.add_argument('--ajuda', action='store_true', dest='ajuda', help = 'Mostrar significado das variaveis')
parser.add_argument('--p', action='store_true', dest='ler_p', help = 'Ler vários valores para p')
args = parser.parse_args()
while True:
   showMenu(args)
   input("\nAperte ENTER para continuar...")
