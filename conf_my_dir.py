#Ce porgramme permettra de gerer la configuration par defaut de my_dir
#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importation des bibliotheques

import shutil
import os

# Copie de la fichier source .


path="/usr/bin/"
path2="/etc/init.d/"

print('Copie de la fichier source vers /usr/bin')
shutil.copy('my_dir.py',path)

print('Creation fichier dans /etc/init.d/')
shutil.copy('my_dir',path2)

print ('Rendre executable le programme source')
os.system('chmod +x /etc/init.d/my_dir')

print(' Configuration de la commande qui gere les demons')

os.system('update-rc.d my_dir defaults')

print("COnfiguration terminé")