
''' 
Created on March,2026
@author: lunysska

'''

from Cuenta import *

class Menu:

	# por ahora nuestra clase sólo tiene un atributo.
	def __init__(self, valor):
		self.mensajeDeBienvenida = valor
		
	def darBienvenida(self):
		print(self.mensajeDeBienvenida)

	def despliegaMenu(self):
		print("Las opciones son:")
		print("1. Depositar")
		print("2. Retirar")
		opcion = input("Teclea la opcion:")
		
		
		