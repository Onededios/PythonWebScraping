#!/bin/bash
/bin/python3 seleniumscraping.py | grep -B11 -e "0\.[0-9][0-9]" -e "Did Not Attempt"  | grep -oP '<a[^<]*href="\K[^"]+' | awk -F '/' '{print "Nombre: " $7;print "Enlace: " $0; print "-----------------------------------------------------------------------------------------------------"}' | less
