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
    player =  #funcion para el formato en que se ven las fotos#
    Media = 
    player.set_media_list(Media)

    for index, name in enumerate(mymedia):
       
    player.stop()