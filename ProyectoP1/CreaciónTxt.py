import serial
import time
import datetime
import os

path = os.path.dirname(os.path.abspath(__file__))
path2 = str(path)
listadirect = path2.split("\\")
auxilio = len(listadirect)
stringauxiliar = ""
for i in range(auxilio -1):
    stringauxiliar = str(stringauxiliar) + str(listadirect[i]) + "\\"
string1 = stringauxiliar    
stringauxiliar = string1 + "ArchivosDePrueba\\"

def crear_txt() :
    ubicacion = input("Ingrese ubicacion de la medicion ")
    Nombre = input("Ingrese nombre del archivo ")
    puerto = input("ingrese puerto en mayusculas, ej: COM4 ")
    output_file = open(str(stringauxiliar) + Nombre + ".txt","w")
    ser = serial.Serial(puerto, baudrate= 9600, timeout = 1.0) 
    try :  ##Relaccionado al except de más adelante
        while True :
            line = ser.readline()
            line = line.decode("utf-8") #ser.readline te da un binario, esto lo convierte a string
            if line != "" :
                impresion = str(ubicacion) + "," + str(time.strftime("%d")) + "," + str(time.strftime("%m")) + "," + str(time.strftime("%Y")) + "," + str(time.strftime("%H")) + "," + str(time.strftime("%M")) + "," + line + "\n"
                impresion = impresion.strip("\n")
                print(impresion) ##Para ver en la terminal python lo que estoy imprimiendo en el txt
                output_file.write(impresion+"\n") 
        output_file.close()
    except KeyboardInterrupt :  ## Lo pongo para que cuando el usuario presione "crtl c" para finalizar la toma de datos en lugar de mostrar un error en el programa diga "Finalizando toma de datos"
        print("Finalizando toma de datos")
        time.sleep(10)



crear_txt()  ##Ésta la ejecuto una sola vez por 12 hs tomando datos cada 5 min con el delay de 300000 de arduino

