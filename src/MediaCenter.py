#!/usr/bin/env python3
#-
# ## ###############################################
#
# 
# MediaCenter.py
# File main
#
# Autor: 
# License: MIT
#
# ## ###############################################

import tkinter as tk
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import filedialog as fd
from tkinter import messagebox
import mediaLector as ml
import multiprocessing

def openFile():
	"""This function open files of type .bmp .png and .jpg"""
	file = fd.askopenfilename(initialdir = os.getcwd(), title = 'Seleccione archivo', defaultextension = '*.*', filetypes = (('png files','*.png'),('jpg files','*.jpg'),('bmp files','*.bmp')))
	
def openDireactory():
	"""This function open a directory media"""
	directory = fd.askdirectory()
	print('directory: ', directory)
	ml.playMedia(directory)
	
def eventUSB(directory, play):
	print('Abriendo multimedios...')
	if play:
		ml.playUSB(directory)
	
def checkUSBconnection(var):
	play = True
	while True:
		d={}
		for l in open('/proc/mounts'):
			if(l[0] == '/'):
				l = l.split()
				d[l[0]] = l[1]
			
		if('/dev/sdb1' in d):
			eventUSB(d['/dev/sdb1'], play)
			play = False
