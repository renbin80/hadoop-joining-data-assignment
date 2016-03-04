#!/usr/bin/env python

# ---------------------------------------------------------------
#This reducer code will input a line of text and 
#    output <word, total-count>
# ---------------------------------------------------------------
import sys

last_key = None
running_total = 0
found=0
count=0
for input_line in sys.stdin:

    input_line = input_line.strip()

    this_key, value = input_line.split("\t", 1)

#    print "Start: ", input_line, found, this_key, last_key, running_total

    try:
        val=int(value)
        running_total += val
    except ValueError:
        if value=="ABC":
            if last_key != this_key:
                found=1
                print( "{0}\t{1}".format(last_key, running_total))
                last_key=this_key
                running_total=0
                continue
            last_key=this_key
            found=1

            continue


    if (this_key!=last_key):
        if count > 0:
            running_total= running_total-val
            if found==1:
                print( "{0}\t{1}".format(last_key, running_total))
            running_total=val    

        found=0


    count+=1
    last_key=this_key

#    print "End: ", input_line, found, this_key, last_key, running_total
    

