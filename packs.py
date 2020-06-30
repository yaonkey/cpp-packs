#!/usr/bin/python3
import sys, getopt, os

#    ||          ||    =======     ========               
#    ||          ||    ||   //      \\         |      |  
#    ||          ||    =====          \\     --+--  --+--
#    ||          ||    ||   \\          \\     |      |  
#    ========    ||    =======     ========   
#
#    by yaonkey/lisovsky611            


IP = '127.0.0.1'
PORT = 23547
DEFAULT_DIR = {
    "win": "C:/users/cpp-packs/",
    "nix": "/usr/bin/cpp-packs/",
    "mac": "/user/cpp-packs/",
    "etc": "Unsupported platform"
}
HELP_TEXT = """
Usage: packs.py [options] file...
Options: 
-h            Get help.
-s <name>     Search pack by name.
-i <name>     Install pack to local project.
-r <name>     Remove pack from local project.
-d <dir>      Select dir for installing pack.
"""

def main(argv):
   packname = ''
   packdir = ''
   try:
      opts, args = getopt.getopt(argv, "hs:i:r:d:", ["help","search=","install=", "remove=", "dir="])
   except getopt.GetoptError:
      print ('packs.py --help to get help')
      sys.exit(2)

   for opt, arg in opts:
        if opt in ('-h', '--help'):
            print (HELP_TEXT)
            sys.exit()
        elif opt in ('-s', '--search'):
            packname = arg
        elif opt in ('-i', '--install'):
            packname = arg
            packdir = DEFAULT_DIR[checkPlatform()]
        elif opt in ('-r', '--remove'):
            packname = arg
        elif opt in ('-d', '--dir'):
            packdir = arg
        
   print (f'[*] Name: {packname}')
   print (f'[*] Dir: {packdir}')

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