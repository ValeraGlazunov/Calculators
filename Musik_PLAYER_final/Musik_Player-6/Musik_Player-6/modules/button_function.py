# from argparse import ArgumentParser
import modules.full_path as path
import customtkinter as ctk
import pygame
import modules.add_buttons as bt
import modules.create_frame as fr
# from pybass3 import Song
# import time


def length():
	# print(1111)
	length = pygame.mixer.music.get_pos()
	print(length)
	# pygame.mixer.music.rewind()
	pygame.mixer.music.set_pos(length//1000 * 5)

def minus_length():
	length = pygame.mixer.music.get_pos()
	pygame.mixer.music.get_pos(length//1000 // 2)
	

# def next_song():
	# status_bar.config(text='')
	# my_slider.config(value=0)
# 



# master_frame = fr.Frame(ctk.CTkFrame)
# master_frame.pack(pady=20)

# controls_frame = fr.Frame(master_frame)
# controls_frame.grid(row=1, column=0)
 
# def volume(x):
#     pygame.mixer.music.set_volume(volume_slider.get())
 
 
 
 
# volume_frame = fr.LabelFrame(master_frame, text="Volume")
# volume_frame.grid(row=0, column=1)
# volume_slider = ctk.Scale(master_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume_slider, length=125  )
# volume_slider.grid(row=0, column=1)
