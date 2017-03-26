import sys
import os
import datetime

def banner ( ) :
 print '''
 ================================================\n
 ||       ||    ||=======>    =       =
 ||       ||    ||             =     =
 ||       ||    ||              =   =
 ||       ||    ||               = =
 ||=======||    ||=======>        =
 ||       ||    ||              =  =
 ||       ||    ||             =    =
 ||       ||    ||            =      =
 ||       ||    ||=======>   =        =\n
 ===============================================\n
'''
 print '''
###################################################
##   HEX - A Digit To Hexadecimal File Converter ##
##########       Author - Antu Roy       ##########
#################  Version 1.0   ##################
###################################################
'''

class decoderx:
 def __init__ ( self ,inp , outp ) :
  self . inp = inp
  self . outp = outp
 def decod (self) :
  read = open ( self.inp , "r" )
  read1 = read . read ( )
  decode = read1.encode("hex")
  read.close()
  kout = self.outp
  fk=open(kout,"w")
  dec = "0x"+decode
  fk.write(dec)
  fk.close()
def main ( ) :
 banner ( )
 print " [ + ] Program started... \n"
 print " [ + ] Input File Path \n"
 ina = raw_input ( " ==> \n ")
 print " [ + ] Path to Outfile \n "
 outb = raw_input ( " ==> \n ")
 print "-"*33
 try :
  print " Reading File...\n"
  print " Encoding Started ... \n"
  print " Please wait...\n Large File May Take Some Time.\n"
  a=decoderx ( ina , outb )
  a.decod()
  print " File Found ...\n"
  print " Encoded...\n"
  print " Saving File...\n"
  print " File Saved.\n"
  ln = " HEX at %s writing successful " % (datetime.datetime.now())
  print ln
 except :
  print " Failed...\n "
  ln = " Failed to convet file in hex at %s " %(datetime.datetime.now())
  print ln
 print " Closing Program... \n "
 sys.exit(-1)
if __name__ == "__main__" :
 main()
