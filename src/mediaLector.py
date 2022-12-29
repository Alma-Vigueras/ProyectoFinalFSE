#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################
#
# usb_lector.py
# Contains the tools to read a usb
#
# ## ###############################################

import vlc
import time
import glob
import webbrowser
import pyautogui
from tkinter import messagebox

def reproducirFotos(mymedia,tiempo):
    vlc_instance = vlc.Instance() #instancia reproductor de fotos#
    player = vlc_instance.media_list_player_new() #funcion para el formato en que se ven las fotos#
    Media = vlc_instance.media_list_new(mymedia)
    player.set_media_list(Media)

    for index, name in enumerate(mymedia):
       player.play_item_at_index(index)
	    time.sleep(tiempo) #tiempo de reproduccion
    player.stop()

def reproducirMusicaVideo(file):
    for f in file:
        vlc_instance = vlc.Instance()
		player = vlc_instance.media_player_new()
        media = vlc_instance.media_new(f)
        player.set_media(media)
        player.set_fullscreen(True)
        player-play()
        time.sleep(1.5)
        duration = player.get_length() / 1000
        time.sleep(duration)
        player.stop()
    player.stop()

def playUSB(directory):
    #Guarda los nombres tipo png
	varPhotoFiles = glob.glob(directory+"/Media/Fotos/*.jpg")#Asigna guardado en carpeta de fotos
    #Guarda los nombres tipo mp4
	varVideoFiles = glob.glob(directory+"/Media/Videos/*.mp4")#EN carpeta video
	#Guardan los nombres de los archivos tipo mp3 
	varMusicFiles = glob.glob(directory+"/Media/Musica/*.mp3")#EN carpeta musica

	print('varPhotoFiles: ',varPhotoFiles)
	print('varVideoFiles: ',varVideoFiles)
	print('varMusicFiles: ',varMusicFiles)
    
	if(len(varPhotoFiles)>0):