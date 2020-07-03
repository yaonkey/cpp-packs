#!/usr/bin/python3
import sys, getopt, os, pathlib, json

#    ||=====     //====\\    =======   ||   //   ========               
#    ||   //     ||    ||   ||         || //      \\         
#    ||_//       ||====||   ||         ||==         \\     
#    ||          ||    ||   ||         || \\          \\   
#    ||          ||    ||   =======    ||   \\   ========   
#
#    by yaonkey/lisovsky611            

IP, PORT = '', ''
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
-u <name>     Upload your pack to packs list.
-g            Global pack install.
"""

def main(argv):
    config = loadConfig()
    global IP
    global PORT
    IP = config['repo-ip']
    PORT = config['repo-port']
    packname = ''
    packdir = 'current'
    try:
        opts, args = getopt.getopt(argv, "hs:i:r:d:u:g", ["help","search=","install=", "remove=", "dir=", "upload=", "global"])
    except getopt.GetoptError:
        print ('Use packs.py --help to get help')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print (HELP_TEXT)
            sys.exit()
        elif opt in ('-s', '--search'):
            packname = arg
        elif opt in ('-i', '--install'):
            packname = arg
            packdir = os.getcwd()
        elif opt in ('-r', '--remove'):
            packname = arg
            packdir = os.getcwd()
        elif opt in ('-d', '--dir'):
            packdir = arg
        elif opt in ('-g', '--global'):
            packdir = config['global-path']
        elif opt in ('-u', '--upload'):
            packname = arg
            uploadPack(packname)
        else:
            print ('Use packs.py --help to get help')

    # this lines for debugging
    print (f'[*] Name: {packname}')
    print (f'[*] Dir: {packdir}')
    print (f'[*] Repo: {config["repo-ip"]}:{config["repo-port"]}')

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

def loadConfig():
    """ Working with configuration file. return dict """
    if os.path.exists("config.json"):
        with open("config.json", "r") as config_file:
            data = json.load(config_file)
    else:
        data = {
            "name": "packs-config",
            "repo-ip": "location.com",
            "repo-port": 43523,
            "global-path": f"{DEFAULT_DIR[checkPlatform()]}"
        }
        with open("config.json", "w") as config_file:
            json.dump(data, config_file)
    return data

def searchPack(name: str):
    """ Search packs by name. return bool """
    pass

def isLocalExists(name: str):
    """ Check exists in local dir. return bool """
    return True if os.path.exists(name) else False
    

def downloadPack(name: str):
    """ If pack is exists => download pack. return bool """
    if not isLocalExists:
        pass  # download
    else:
        return False

def installPack(name: str, location: str):
    """ If pack is exists on service => install to location.
     return int """
    if downloadPack(name):
        pass  # install
    else:
        return 0

def uninstallPack(name: str, isGlobal: bool=False):
    """ Local or global removing packs. return int """
    if isLocalExists(name):
        pass  # remove
    else:
        return 0

def uploadPack(name: str):
    """ Upload ur packs to service.
    Enter login and password to do this. 
    return int """
    pass


if __name__ == "__main__":
   main(sys.argv[1:])