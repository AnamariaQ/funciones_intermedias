#1 Actualizar valores en diccionarios y listas
#Cambia el valor 10 en x a 15. Una vez que hayas terminado
#  x ahora debería ser [ [5,2,3], [15,8,9] ].
#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
#En el directorio_deportes, cambia "Messi" por "Andrés".
#Cambia el valor 20 en z a 30

x = [ [5,2,3], [10,8,9] ]
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15 #la lista en la posicion del indice 1 que seria la 2da lista y en indice 0 cambiamos a 10
print(x) #imprime el nuevo valor de x [[5, 2, 3], [15, 8, 9]]
estudiantes[0]['last_name']='Bryant'
print(estudiantes)#imprimira la lista con el nombre de alumno 'Bryant'
directorio_deportes['fútbol'][0]='Andrés'
print(directorio_deportes)#imprime el diccionario con con Andres en la lista dentro del diccionario
z[0]['y']=30 #con el indice 0 y la clave 'y' se cambia el valor a 30
print(z) #imprimira con el nuevo valor de la clave 'y'


#2 Iterar a través de una lista de diccionarios
#Crea una función iterateDictionary(some_list)
#para que, dada una lista de diccionarios
#la función recorra cada diccionarios de la lista
#e imprima cada llave y el valor asociado.

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'}, #0
        {'first_name' : 'John', 'last_name' : 'Rosales'}, #1
        {'first_name' : 'Mark', 'last_name' : 'Guillen'}, #2
        {'first_name' : 'KB', 'last_name' : 'Tonel'} #3
    ]

def iterateDictionary(some_list,parametro2):
    for diccionario in some_list: # acceso a cada elemento de la lista (en este caso a cada diccionario)
        texto=[]
        #print(type(texto))
        for llave in diccionario: # acceso a cada clave y valor de cada diccionario
            #print(llave+'-'+element[llave])
            texto.append(llave+'-'+diccionario[llave])
        print('; '.join(texto))
iterateDictionary(estudiantes,'last_name')

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
'''first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel'''

#3 Obtener valores de una lista de diccionarios
#Crea una función iterateDictionary2(key_name, some_list)
#que, dada una lista de diccionarios y un nombre de clave
# la función imprima el valor almacenado en esa clave para cada diccionario.
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
'''Michael
John
Mark
KB'''
#Y iterateDictionary2('last_name', estudiantes) debería generar:
'''Jordan
Rosales
Guillen
Tonel'''

def iterateDictionary2(some_list,parametro2): #iteratyDictionary(estudiantes)
    for diccionario in some_list:
        print(diccionario[parametro2])

#4   Iterar a través de un diccionarios con valores de lista

def printInfo(some_dict):
    #print(some_dict)
    for d in some_dict:
        print(d)
        print(str(len(some_dict[d]))+" "+d)
        for a in some_dict[d]:
            print(a)
    
    
dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)