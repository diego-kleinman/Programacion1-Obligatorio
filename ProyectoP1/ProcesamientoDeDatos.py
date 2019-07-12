import os  ##Importo modulo para poder abrir directamente la carpeta de archivos para pasar por el programa
import time ##Importo time para ponerle un time.sleep para que se vea el print por unos segundos en el cmd
from os import remove ##Importo módulo para borrar archivos al final del programa

##Pongo rutas dinámicas para que el programa trabaje en cualquier ubicación de cualquier computadora
path = os.path.dirname(os.path.abspath(__file__))
path2 = str(path)
listadirect = path2.split("\\")
auxilio = len(listadirect)
stringauxiliar = ""
for i in range(auxilio -1):
    stringauxiliar = str(stringauxiliar) + str(listadirect[i]) + "\\"
string1 = stringauxiliar    
stringauxiliar = string1 + "ArchivosDePrueba\\"
stringauxiliar2 = string1 + "ArchivosDepurados\\"
lista_de_archivos = os.listdir(stringauxiliar)

#Hago la depuración

def depuracion() :
    lista_depurados = []
    for i in lista_de_archivos :
        f = open(stringauxiliar + i )
        ## Leo la primer linea
        lista1 = (f.readline()).strip().split(",")
        ## Hago un contador total del tiempo en horas que ha pasado desde una fecha 0/0/0 hipotética , asumiendo que los meses tienen todos 31 dias
        Contador1 = int(lista1[3])*8928 + int(lista1[2])*744 + int(lista1[1])*24 + int(lista1[4]) + int(lista1[5])/60
        ## Leo la última línea 
        lista2 = (f.readlines()[-1]).strip().split(",")
        ## Vuelvo a hacer un contador 
        Contador2 = int(lista2[3])*8928 + int(lista2[2])*744 + int(lista2[1])*24 + int(lista2[4]) + int(lista2[5])/60
        ## Calculo la diferencia para comprobar que el archivo tuvo al menos 12hs de toma de datos
        Diferencia_horas = abs(Contador1 - Contador2)
        f.close()
        if Diferencia_horas < 12 :
            print("Archivo: " + i + " depurado ya que no cumple con las 12hs de diferencia entre toma de datos")
        else :
            lista_control = []
            f = open(str(stringauxiliar) + i )
            for linea in f :
                lista3 = linea.strip().split(",")
                if float(lista3[6]) < -10 or float(lista3[6]) > 50 :
                    lista_control.append(float(lista3[6]))
            f.close()
            if lista_control == [] :
                lista_depurados.append(i)
                f = open(str(stringauxiliar) + i )
                f2 = open(stringauxiliar2 + i ,"w")
                for linea in f :
                    f2.write(linea)
                f2.close()
            f.close()
            if lista_control != [] :
                print("Archivo: " + i + " depurado ya que posee "  + str(lista_control) + " como datos anómalos")
    return lista_depurados

def procesar_archivos(lista_nombres_archivo) :
    if len(lista_nombres_archivo) >= 5 : ##Me fijo si tengo al menos 5 archivos en la carpeta de depurados
        ##Creo una lista con las ubicaciones de cada archivo ordenadas por orden de apertura
        lista_ubicaciones = []
        for i in lista_nombres_archivo :
            f = open(stringauxiliar2 + i )
            linea = f.readline()
            lista3 = linea.strip().split(",")
            lista_ubicaciones.append(lista3[0])
            f.close()

        Promedios_Temp = []
        Promedios_Luz = []
        for i in lista_nombres_archivo :
            f = open(stringauxiliar2 + i )
            lista_Temp = []
            lista_Luz = []
            for linea in f :
                lista2 = linea.strip().split(",")
                lista_Temp.append(float(lista2[6]))
                lista_Luz.append(float(lista2[7]))
            ##Saco promedios de luz y temp dentro de cada archivo
            Suma_temp = 0
            Suma_luz = 0
            for e in lista_Temp :
                Suma_temp = Suma_temp + e
            for a in lista_Luz :
                Suma_luz = Suma_luz + a
            p_temp = Suma_temp / len(lista_Temp)
            p_luz = Suma_luz / len(lista_Luz)
            ##Agrego los promedios de cada archivo a la lista total de promedios
            Promedios_Temp.append(float(p_temp))
            Promedios_Luz.append(float(p_luz))
            f.close()      

        ##Hago una lista vacía para que contenga con los 5 promedios más grandes y más chicos
        Mayores_temp = []
        Mayores_luz = []
        Menores_temp = []
        Menores_luz = []

        ##Creo duplicados de las listas de promedios ya que quiero tener su orden original para referirme a las ubicaciones de cada archivo
        Promedios_Luz2 = []
        Promedios_Temp2 = []
        for a in Promedios_Luz :
            Promedios_Luz2.append(a)
        Promedios_Temp2 = []
        for a in Promedios_Temp :
            Promedios_Temp2.append(a)

        ##Ordeno las listas de promedios originales para tomar los mayores y menores datos, la luz la tomo al reves, cuanto mas grande el valor es menos luz
        Promedios_Luz.sort()
        Promedios_Temp.sort()
        Mayores_luz = Promedios_Luz[:5]
        Menores_temp = Promedios_Temp[:5]
        Promedios_Luz.reverse()
        Promedios_Temp.reverse()
        Menores_luz = Promedios_Luz [:5]
        Mayores_temp = Promedios_Temp [:5]

        ## Referencio los datos en su orden dado a la lista de promedios clonada, para posteriormente referenciarlos a la ubicación correspondiente de la lista de ubicaciónes

        ubicaciones_mayor_luz = []
        ubicaciones_menor_luz = []
        ubicaciones_mayor_temp = []
        ubicaciones_menor_temp = []
        for i in range(5) : ## Quiero generar listas con 5 ubicaciónes cada una
            ubicaciones_mayor_luz.append(lista_ubicaciones[Promedios_Luz2.index(Mayores_luz[i])])
            ubicaciones_menor_luz.append(lista_ubicaciones[Promedios_Luz2.index(Menores_luz[i])])
            ubicaciones_mayor_temp.append(lista_ubicaciones[Promedios_Temp2.index(Mayores_temp[i])])
            ubicaciones_menor_temp.append(lista_ubicaciones[Promedios_Temp2.index(Menores_temp[i])])
        return "Los 5 lugares con promedio más alto de luminosidad son : " + str(ubicaciones_mayor_luz) + "\n" + "Los 5 lugares con promedio más bajo de luminosidad son : " + str(ubicaciones_menor_luz) + "\n" + "Los 5 lugares con promedio más alto de temperatura son : " + str(ubicaciones_mayor_temp) + "\n" + "Los 5 lugares con promedio más bajo de temperatura son : " + str(ubicaciones_menor_temp)
    else :
        return "No hay suficientes archivos para sacar las 5 mejores ubicaciónes, aumente el numero de archivos o cambie los inválidos por válidos"

b = depuracion() ##Ejecuto la depuración sobre la carpeta "ArchivoDePrueba"
print(procesar_archivos(b)) ##Ejecuto el procesamiento de datos sobre la lista de nombres de archivos depurados dentro de la carpeta "ArchivosDepurados" e imprimo el resultado del mismo en pantalla

## Remuevo archivos de la carpeta de ArchivosDepurados para que en caso de que un archivo pase la depuración pero luego se modifique manualmente y no la pase, no esté ya
## en la carpeta de depurados, ya que si ese fuera el caso, el archivo igualmente se procesaría en su versión "vieja".
for e in b:
        remove(stringauxiliar2 + str(e) )

time.sleep(10) #El time.sleep es para que se muestre el resultado por 10s en el cmd, sino se cierra automaticamente cuando termina de ejecutar y no da tiempo a leer




