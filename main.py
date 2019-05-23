import sys
import os
from funcoes import *

def menu(op):
   os.system("\n\n\n")
   os.system("clear")
   if op == "mm1":
      mm1()
   elif op == "mms":
      mms()
   elif op == "mm1k":
      mm1k()
   elif op == "mmsk":
      mmsk()
   else:
      print("Operacao Invalida... Exiting")
      exit()


op = sys.argv[1] #captura o argumento enviado no terminal
menu(op)
