#!/usr/bin/python
# -*- coding: utf-8 -*-
import glob
import os
import shutil
import time
import grp
import pwd


def movefile(file,extension):
	path="/home/cbag/Téléchargements/"+extension

	if not os.path.isdir(path):
		os.mkdir(path)

	(filepath,filename)=os.path.split(file)
	cpath=os.path.join(path,filename)
	shutil.move(file,path)
	os.chown(path,1000,1000)
	os.chown(cpath,1000,1000)
	print ("Copie ",file,": Ok")


def listerfile():
	path="/home/cbag/Téléchargements/"
	all_files=os.path.join(path,'*.*')
	for i in glob.glob(all_files):
		(filepath,filename)=os.path.split(i)
		extension=(os.path.splitext(filename)[-1])[1:]
		full_dir=os.path.join(path,filename)
		movefile(full_dir,extension)
		
		

if __name__=='__main__':
	while True:
		listerfile()
		time.sleep(10)