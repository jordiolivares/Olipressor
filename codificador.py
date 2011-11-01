#!/bin/env python2
import Image
import codecs
import os
import sys
import bz2

im = Image.open(sys.argv[1]) # The image file to compress

#
# We write the size of the image for later
#

imcomprimida = str(im.size[0])+'\n'+str(im.size[1])+'\n'

pixel = im.load()
tamanyx = im.size[0]-1 # Why -1 ? Can't remember why.. let's remove it and try without...
# Seems to work, let's see the decompressed image...  Oh god oh god oh god what have I done
tamanyy = im.size[1]
pixelsbuits = 0 # Counter of pixels that look-alike
variable = 5  # Range of the look-alike pixels

imcomprimida += str(variable) + '\n'
# Now we start reading the image

for y in range(0,tamanyy): # Let's go line by line
    for x in range(0,tamanyx):
        if (x == 0): # As it's the first pixel, we mark it as reference and go to the next one
            pixeldoc = str(pixel[x,y]) # Transforms the Tuple to a String 
            pixeldoc = pixeldoc.replace(",","") # Remove the commas (Makes the compressed size exponentially smaller
            imcomprimida += pixeldoc
            important = x
            continue 
        if (x == tamanyx-1): # range(1,x) gives a final value of x-1, so we go around it
            pixeldoc = str(pixel[x,y])
            imcomprimida += ' '+str(pixelsbuits)+' ' # We write the number of look-alike pixels
            pixeldoc = pixeldoc.replace(",","")
            imcomprimida += pixeldoc + '\n'
            pixelsbuits = 0 # Restart the counter
            continue
#
# The algorithm that checks if a pixel looks-alike the first one in the range defined in "variable"
#
        if (pixel[x,y][0] <= pixel[important,y][0]+variable) and (pixel[x,y][0] >= pixel[important,y][0]-variable) and\
(pixel[x,y][1] <= pixel[important,y][1]+variable) and (pixel[x,y][1] >= pixel[important,y][1]-variable) and\
(pixel[x,y][2] <= pixel[important,y][2]+variable) and (pixel[x,y][2] >= pixel[important,y][2]-variable):
            pixelsbuits += 1
            continue
        else:
            # Seems we got a pixel different than the others, we mark it as the new reference
            pixeldoc = str(pixel[x,y])
            imcomprimida += ' ' + str(pixelsbuits) + ' ' # Print look-alike pixels
            pixelsbuits = 0 # Restart counter
            pixeldoc = pixeldoc.replace(",","")
            imcomprimida += pixeldoc
            important = x
            # and here we go again
# Now we grab all those Strings and compress them with bzip2
# so we get an ULTRACOMPREEEEESSSSSEEEEEDDD IMAAAAAAAAGE!!!!
comprimida = bz2.BZ2File('processada.oli','w') # Name of compressed image is 'processada.oli' by default
comprimida.write(imcomprimida)
comprimida.close()
