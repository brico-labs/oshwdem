#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

try:
    import scribus
except ImportError,err:
    print "This Python script is written for the Scribus scripting interface."
    print "It can only be run from within Scribus."
    sys.exit(1)

#########################
# YOUR IMPORTS GO HERE  #
#########################

def main(argv):
    """Convert all colors to CMYK colors."""
    #########################
    #  YOUR CODE GOES HERE  #
    #########################
    if scribus.haveDoc():
        clrs = scribus.getColorNames()
        for clr in clrs:
		cmyk = scribus.getColor(clr)
		c = cmyk[0]
		cd = c*100/255
		ca = "c"+str(cd)
		m = cmyk[1]
		md = m*100/255
		ma = "m"+str(md)
		y = cmyk[2]
		yd = y*100/255
		ya = "y"+str(yd)
		k = cmyk[3]
		kd = k*100/255
		ka = "k"+str(kd)
		scribus.defineColor(clr,c,m,y,k)

def main_wrapper(argv):
    """The main_wrapper() function."""
    try:
        scribus.statusMessage("Running script...")
        scribus.progressReset()
        main(argv)
    finally:
        if scribus.haveDoc():
            scribus.setRedraw(True)
        scribus.statusMessage("")
        scribus.progressReset()

if __name__ == '__main__':
    main_wrapper(sys.argv)

