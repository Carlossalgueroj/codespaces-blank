import random 
import time
p = 0 #Preguntas hechas 
u = 0#Puntuación optenida después de las preguntas 
#Eleccion del Nivel a jugar
print('Bienvenido al juego de cultura general\nAntes de jugar le recomendamos que lea el manual: https://docs.google.com/document/d/1X8_IhuTsucViDj1xlnEka4UU4GigPJEyDZgQvn9kM-g/edit?usp=sharing\nEspero que disfrute del juego ')
Nivel = input('Nivel Facil(F),Dificil(D) o Imposible(I): ')  
#Todas las preguntas del juego están almacenadas en este diccionario 
Joc = {
  'F':  {'¿Cómo se llama la lengua oficial en china? ':'mandarin',
   '¿Cuál es el río más caudaloso del mundo? ':'amazonas',
   '¿Qué mes tiene menos de 30 días? ': 'febrero',
   '¿Qué planeta es el más cercano al Sol? ':'mercurio',
    '¿Cuál es la montaña más alta en la actualidad? ': 'everest',
    'En qué país se encuentra la Torre Eiffel ':'francia',
    '¿Cuál es el país con mayor población del mundo? ': 'china',
    '¿Cuántas sílabas tiene la palabra abecedario? ': 'cinco',
    '¿Cómo se llama la otra especie de seres humanos que convivieron con los Homo sapiens en Europa? ':'neandertales',
    '¿Cómo se llama la parte de la oración en la que se habla de aquello que hace el sujeto? ':'predicado',
    '¿Cuál es el pico más alto de España? ':'teide',
    '¿En qué país se encuentra la Torre de Pisa? ':'italia',
    '¿Cuál es el río más caudaloso de España? ':'ebro',
    '¿Cuál es la capital de Alemania? ':'berlin',
    '¿Quién ganó el mundial de fútbol de 2010? ':'españa',
    '¿En qué ciudad española podremos encontrar La Giralda? ':'sevilla',
    '¿En qué ciudad española se encuentra la Sagrada Familia? ':'barcelona',
    '¿Qué juego está formado por peones, alfiles, reyes y reinas? ':'ajedrez',
   '¿Como se escribe 19 en números romanos?':'xix',
   '¿Qué tipo de palabra es “para”? ':'preposicion'},
  'D': {'¿Cuál es la flor nacional de Japón? ': 'cerezo',
  '¿Qué órgano del cuerpo humano consume más energía? ': 'cerebro', 
  '¿Qué país tiene más islas en el mundo? ': 'suecia', 
  '¿De qué ciudad provienen los Beatles? ': 'liverpool',
    'En la mitología griega, ¿quién era el mensajero de los dioses? ': 'hermes',
    'Uno de los cinco sabores que podemos percibir junto al dulce, el salado, el ácido o agrio, y el amargo és el ':'umami',
    '¿De qué planeta es Spock, el personaje de Star Trek? ': 'vulcano',
    '¿A qué neurotransmisor lo conocemos como “la hormona de la felicidad”? ': 'serotonina',
    '¿Cuál es la capital de Islandia? ':'reikiavik',
    '¿Quién enunció la metáfora filosófica del mito de la caverna? ':'platon',
    '¿Cómo se llamaba la esposa de Ulises, el personaje de la Odisea creado por Homero? ':'penelope',
   '¿En qué país se originó el cóctel “mojito”? ':'cuba',
    '¿En qué país se encuentra el desierto de Atacama? ':'chile',
    '¿En qué país se encuentra ubicada la Casa Rosada? ':'argentina',
  '¿En qué lugar del cuerpo se produce la insulina? ':'pancreas',
  '¿En qué país se encuentra el K2, la segunda montaña más alta del mundo? ':'pakistan',
 '¿Qué representaba el dios Thot en el antiguo Egipto? ':'sabiduria',
  '¿Cuál es el animal terrestre más rápido del mundo? ':'guepardo',
  '¿Cuál es el único mamífero capaz de volar? ':'murcielago',
  'Si tienes acrofobia, tienes miedo a las... ':'alturas',
     '¿Cómo se escribe 1760 en numeros romanos?':'mdcclx'},
  'I': {'¿Comó se llama la madre de Putin? ': 'maria',
    'Apellido del ganador de los 100 metros masculino de las olimpiadas Barcelona 1992: ': 'christie',
  '¿Cuál es la capital de namibia? ': 'windhoek',
    '¿Comó se llamaba el inventor de la fregona?': 'manuel',
   '¿Cómo se llama el creador de la guitarra moderna?':'antonio',
   'Topónimo más largo del Reino Unido y el tercero más largo del mundo' : 'llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch',
   'Según el Libro Guinness de los Récords, ¿Cuál és el rio más corto de La Tierra?':'roe',
   '¿Cuantas horas se tarda en llegar a Rusia desde España, en avion?':'diez',
   '¿Cual es la capital de Dinétah?':'tseghahoodzani',
   'Gentilicio de las personas que viven en La isla del Man':'manes',
   'Capital de Barotseland':'mongu',
   '¿Cuál es la palabra más larga del español?':'electroencefalografista',
   '¿Cuál es el satélite natural más grande del Sistema Solar?':'ganimedes',
'¿Qué es tan frágil que al decir su nombre se rompe? ':'silencio',
'¿Cuál es el día más largo de la semana? ':'miercoles',
'¿Cuál es la cosa que mientras más grande es, se visualiza menos? ':'oscuridad',
'¿En qué mes celebran los rusos la Revolución de Octubre? ':'noviembre',
'¿En qué país se fabrican los sombreros de Panamá? ':'ecuador',
'¿En que lugar aparece el día jueves antes que el miércoles? ':'diccionario',
'¿Cuál es el animal que siempre anda con las patas en la cabeza?':'piojo'}
} 
while Nivel not in Joc:
  Nivel = input('F para Facil, D para Dificil, I para Imposible: ')
#Este while define cuantas preguntas va ha haber en todo el juego
while p != 10:
  p=p+1
  x = random.randint(0,len(Joc[Nivel])-1)
  #Dependiendo el nivel elegido se tienen más o menos intentos 
  if Nivel=='F':
    i = 1
  elif Nivel == 'D':
    i = 2
  else:
    i = 3

  lista = list(Joc[Nivel])#Preguntas
  Respuesta = Joc[Nivel][lista[x]]
  y = input('\n{}- {}\n\t'.format(p,lista[x])).capitalize()#El usuario introducira su respuesta 
  
  time.sleep(2)#Estos 2 segundos provocara tension al usuario, al no saber si tiene la respuesta correcta o incorrecta 

  while i != 4 and y != Respuesta.capitalize():#En el momento en que la respuesta sea incorrecta se ara lo siguiente:
    print('Te quedan',4-i,'intentos')
    u = u - i #Restar un poco de puntuacion 
    a= ''#Variable que usaremos para guardar la pista 
    o = 0#Variable que cuenta las letras de la palabra
    y = y+' '*len(Respuesta)#le añadimos espacios para evitar problemas 
    Pista = (input('ELige: pista wordle(1) o posicion letra(2): '))#elige el tipo de pista 
    while Pista !='1' and Pista != '2':#Correguir errores
      Pista= input('Las opciones son 1 o 2 no {}: '.format(Pista))
    letra = ''
    if Pista == '2':
      letra = input('Escoge una letra: ')#letra que se va a mostrar en la palabra
      while len(letra)>1 or letra.islower()== False:#Control de error
        letra =   input('Escoge una letra (a,z)(Minuscula) (solo una): ')
    while o < len(Respuesta):#Creacion de pista
      if (y[o]!=Respuesta.capitalize()[o] and Pista =='1') or (letra!=Respuesta[o] and Pista == '2'):
        a = a +y[o].replace(y[o],'_')
      else:
        a = a + Respuesta.capitalize()[o]
      o = o + 1
    if Pista == '2' and letra not in Respuesta:
      print(letra,'no esta en la palabra')
      
    print('Pista: \t',a,'\nVuelve a intentarlo')# se muestran la pista 
    y=input('\t').capitalize()
    i=i+1
   
  if y == Respuesta.capitalize():
    print('Correcto')
    u = u+10#En el caso de que la respuesta sea correcta de sumaran 10 puntos a la puntuación

  else:
    print('Incorrecto','Respuesta correcta: ', Respuesta)# en el caso de que el usuario no haya sabido la respuesta se le mostrara la correcta
  Joc[Nivel].pop(lista[x])#se elimina la pregunta del diccionario para que no se vuelva a repetir la misma
if u<0:#En el caso de que hayas tenido las 10 preguntas incorrecta, tu puntuacion sera negativa ya que se le resta puntuacion en cada intento, así que para impedirlo si tu puntacion es negativa sera 0
  u = 0
print('Tu puntuación es',u)