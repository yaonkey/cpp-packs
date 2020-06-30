#!/usr/bin/python3
import sys, getopt, os

#    ||          ||    =======     ========               
#    ||          ||    ||   //      \\         |      |  
#    ||          ||    =====          \\     --+--  --+--
#    ||          ||    ||   \\          \\     |      |  
#    ========    ||    =======     ========   
#
#    by yaonkey/lisovsky611            


WELCOME_TEXT = '''
    ||          ||    =======     ========               
    ||          ||    ||   //      \\\         |      |  
    ||          ||    =====          \\\     --+--  --+--
    ||          ||    ||   \\\          \\\     |      |  
    ========    ||    =======     ========               
'''
print(WELCOME_TEXT)

IP = '127.0.0.1'
PORT = 23547
DEFAULT_DIR = {
    "win": "C:/users/cpp-packs/",
    "nix": "/usr/bin/cpp-packs/",
    "mac": "/user/cpp-packs/",
    "etc": "Unsupported platform"
}

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--input"):
         inputfile = arg
      elif opt in ("-o", "--output"):
         outputfile = arg
   print (f'Input file is {inputfile}')
   print (f'Output file is {outputfile}')

def checkPlatform():
    """ Check current platform. return str """
    if os.name == 'posix':
        return "nix"
    elif os.name == 'win':
        return "win"
    elif os.name == 'darwin':
        return "mac"
    else:
        return "etc"

def searchPack(name: str):
    """ Search packs by name. return bool """
    pass

def isLocalExists(name: str):
    """ Check exists in local dir. return bool """
    pass

def downloadPack(name: str):
    """ If pack is exists => download pack. return bool """
    pass

def installPack(name: str, location: str):
    """ If pack is exists on service => install to location.
     return int """
    pass

def unistallPack(name: str, isGlobal: bool=True):
    """ Local or global deleting packs. return int """
    pass

def uploadPack(name: str):
    """ Upload ur packs to service.
    Enter login and password to do this. 
    return int """
    pass


if __name__ == "__main__":
   main(sys.argv[1:])