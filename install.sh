#!/usr/bin/sh
# this working only for *nix 

mv packs.py packs
sudo cp packs /usr/bin/
mv packs packs.py
echo "Install completed!"