import Image
import linecache
import random
import bz2
import os
import sys
imatge = bz2.BZ2File(sys.argv[1],'U') # la imatge en si comprimida
#
#
#
# Extraiem les variables tamanyx, tamanyy i la variable
# i les convertim a int per a poder utilitzar-les
#
#
#
tamanyx = imatge.readline()
tamanyx = tamanyx.strip('\n')
tamanyx = int(tamanyx)
tamanyy = imatge.readline()
tamanyy = tamanyy.strip('\n')
tamanyy = int(tamanyy)
tamany = (tamanyx,tamanyy) # Les convertim a una tupla per a ser utils
variable = imatge.readline()
variable = variable.strip('\n')
variable = int(variable)

# Creem la imatge

final = Image.new("RGB",tamany)
aprocessar = []

# 
# 
# Comenca la tortura de la lectura de linees
# 
# 
for linea in range(4,(tamanyy+3)): # Sumem 3 per a no oblidar-nos les 4 ultimes linees
    fila = imatge.readline()
    fila = fila.replace(" ",",") # Per a la funcio eval() substituim els espais per comes
    fila = fila.strip('\n')
    fila = eval(fila) # Convertim el string en una tupla
    rgb = fila[0]
    aprocessar.append(rgb)
    for i in range(0,len(fila)):
        if (i%2 != 0): # Trobem el contador de pixels
            rgb = fila[(i-1)]
            pixels = fila[i]
            aprocessar.append(rgb)
            for x in range(pixels,0,(-1)):
                # Crearem ara els pixels que falten
                # Fem que sigui un nombre absolut per a evitar problemes amb els negatius
                R = abs(random.randint((rgb[0]-variable),(rgb[0]+variable)))
                G = abs(random.randint((rgb[1]-variable),(rgb[1]+variable)))
                B = abs(random.randint((rgb[2]-variable),(rgb[2]+variable)))
                aleatori = (R,G,B)
                aprocessar.append(aleatori)
        if (i == (len(fila)-1)):
            rgb = fila[(len(fila)-1)]
            aprocessar.append(rgb)
# Guardem la imatge en format PNG (Tranquils, es pot canviar)
final.putdata(aprocessar)
final.save("descomprimida.png", "PNG")
