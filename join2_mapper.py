#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This mapper code will input a <date word, value> input file, and move date into 
#  the value field for output
#  
#  Note, this program is written in a simple style and does not full advantage of Python 
#     data structures,but I believe it is more readable
#
#  Note, there is NO error checking of the input, it is assumed to be correct
#     meaning no extra spaces, missing inputs or counts,etc..
#
# See #  see https://docs.python.org/2/tutorial/index.html for details  and python  tutorials
#
# --------------------------------------------------------------------------

#Ex:
#Hot_Show,ABC
#Hot_Show,234

ABC_showlist = list() 

for line in sys.stdin:
    line       = line.strip()   #strip out carriage return
    line_items  = line.split(",")   #split line, into key and value, returns a list
    #key_in     = line_items[0].split(" ")   #key is first item in list
    key_in     = line_items[0]  #key is first item in list
    value_in   = line_items[1]   #value is 2nd item 

    #print key_in
    #if len(key_in)>=2:           #if this entry has <date word> in key
    #    date = key_in[0]      #now get date from key field
    #    word = key_in[1]
    #    value_out = date+" "+value_in     #concatenate date, blank, and value_in
    #    print( '%s\t%s' % (word, value_out) )  #print a string, tab, and string
    #else:   #key is only <word> so just pass it through

    if (value_in == "ABC" or value_in.isdigit()==True):
        #print(len(ABC_showlist))
        print( '%s\t%s' % (key_in, value_in) )  #print a string tab and string
            #else: print ("Not!")
#print (ABC_showlist)


#Note that Hadoop expects a tab to separate key value
#but this program assumes the input file has a ',' separating key value
