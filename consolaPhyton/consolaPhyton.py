

varString ="hello world"
varInt= 23
print (varString+" "+str(varInt))

milista=["pato","ganzo","perro"]
arreglo=[[1,2,"dato"],["condicion","texto",7]]

print (arreglo[0][2])
	

for oelement in arreglo:
	print(oelement)


class Cerveza:
	def __init__(self,nombre):
		self.nombre=nombre

	def anejo(self,tiempo):
		print("anejo un total de"+str(tiempo)+ "a")

miCerveza=Cerveza("monte carlo")
print(miCerveza.nombre)
miCerveza.anejo(50)


f=open("miarchivo.txt","a+")
f.write(" segundo texto escrito")
f.close()


f=open("miarchivo.txt","r")
contenido=f.read()
print(contenido)

import pyodbc

conn=pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
					'Server=DESKTOP-AMS7JKJ\MSSQLSERVER01;'
					'Database=consolePython;'
					'UID=connection;'
					'PWD=123456')

cursor=conn.cursor()
cursor.execute('select * from persona')

for row in cursor:
	print(row)

	