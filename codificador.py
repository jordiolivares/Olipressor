#!/bin/env python2
import Image
import codecs
import os
import sys
import bz2

im = Image.open(sys.argv[1]) # La imatge a comprimir donada en el terminal

#
# Escrivim els valors del tamany de la imatge
#

imcomprimida = str(im.size[0])+'\n'+str(im.size[1])+'\n' # Escrivim el tamany de la imatge

pixel = im.load()
tamanyx = im.size[0]-1
tamanyy = im.size[1]
pixelsbuits = 0
variable = 5  # Quant poden variar els pixels

imcomprimida += str(variable) + '\n'
# Comencem a llegir la imatge

for y in range(0,tamanyy): # Nem de linea en linea
    for x in range(0,tamanyx):
        if (x == 0): # Al ser el primer pixel, es grava com a referencia per despres
            pixeldoc = str(pixel[x,y]) # Converteix la tupla a un string 
            pixeldoc = pixeldoc.replace(",","") # Per treure les comes
            imcomprimida += pixeldoc
            important = x
            continue # Continue fa que passi dels seguents passos i que continui amb el for com si no hi hagues res mes 
        if (x == tamanyx-1): #  El -1 es necessari ja que range() dona un valor final de tamanyx-1 (498 en comptes de 499)
            pixeldoc = str(pixel[x,y])
            imcomprimida += ' '+str(pixelsbuits)+' ' # Escriu el nombre de pixels similars en el rang de la variable
            pixeldoc = pixeldoc.replace(",","")
            imcomprimida += pixeldoc + '\n'
            pixelsbuits = 0 # Reiniciem el comptador de pixels
            continue
#
# Si et veus amb cor d'intentar entendre aquest if, que es l'algoritme en si, et provocaras un trauma cerebral
#
        if (pixel[x,y][0] <= pixel[important,y][0]+variable) and (pixel[x,y][0] >= pixel[important,y][0]-variable) and\
(pixel[x,y][1] <= pixel[important,y][1]+variable) and (pixel[x,y][1] >= pixel[important,y][1]-variable) and\
(pixel[x,y][2] <= pixel[important,y][2]+variable) and (pixel[x,y][2] >= pixel[important,y][2]-variable):
            pixelsbuits += 1
            continue
        else:
            # Hem trobat un pixel que se surt del rang, L'HEM DE MARCAR DE REFERENCIA per als pixels subsequents
            pixeldoc = str(pixel[x,y])
            imcomprimida += ' ' + str(pixelsbuits) + ' ' # imprimim els pixels semblants a l'ultim
            pixelsbuits = 0 # reiniciem contador
            pixeldoc = pixeldoc.replace(",","")
            imcomprimida += pixeldoc
            important = x
            # i tornem a comencar
# Ara agafem les dades i les comprimim amb el algoritme bzip2
# per a fer una ULTRACOMPRESSIÓÓÓÓÓ!!!!
comprimida = bz2.BZ2File('processada.oli','w')
comprimida.write(imcomprimida)
comprimida.close()
