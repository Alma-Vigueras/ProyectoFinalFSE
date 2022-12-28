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


        player.stop()
    player.stop()