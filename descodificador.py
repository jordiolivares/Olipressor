import Image
import linecache
import random
import bz2
import os
import sys
imatge = bz2.BZ2File(sys.argv[1],'U') # Compressed image
#
#
#
# We read the three first lines and get the variable used in the compression
# phase PLUS the size of the image (VITAL)
#
#
#
tamanyx = imatge.readline()
tamanyx = tamanyx.strip('\n')
tamanyx = int(tamanyx)
tamanyy = imatge.readline()
tamanyy = tamanyy.strip('\n')
tamanyy = int(tamanyy)
tamany = (tamanyx,tamanyy) # Group the sizes into a Tuple
variable = imatge.readline()
variable = variable.strip('\n')
variable = int(variable)

# Create image

final = Image.new("RGB",tamany)
aprocessar = []

# 
# 
# First attempt at a parser, please don't kill me
# 
# 
for linea in range(4,(tamanyy+3)): # Add 3 so that the last lines aren't omitted
    fila = imatge.readline()
    fila = fila.replace(" ",",") # We replace the Spaces with commas for the eval() function
    fila = fila.strip('\n')
    fila = eval(fila) # String to Tuple
    rgb = fila[0]
    aprocessar.append(rgb)
    for i in range(0,len(fila)):
        if (i%2 != 0): # We find the look-alike-pixels counter which are all the odd numbers
            rgb = fila[(i-1)]
            pixels = fila[i]
            aprocessar.append(rgb)
            for x in range(pixels,0,(-1)):
                # We pull the pixels that look-alike out from the blue
                # The pixel creator doesn't like negative numbers
                R = abs(random.randint((rgb[0]-variable),(rgb[0]+variable)))
                G = abs(random.randint((rgb[1]-variable),(rgb[1]+variable)))
                B = abs(random.randint((rgb[2]-variable),(rgb[2]+variable)))
                aleatori = (R,G,B)
                aprocessar.append(aleatori)
        if (i == (len(fila)-1)):
            rgb = fila[(len(fila)-1)]
            aprocessar.append(rgb)
# Decompressed image defaults to PNG format
final.putdata(aprocessar)
final.save("descomprimida.png", "PNG")
