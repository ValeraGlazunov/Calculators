import customtkinter as ctk
import modules.screen as screen
import modules.image as image
import pybass3
import modules.button_function as functions
import modules.full_path as path

#song = pybass3.Song(path.find_path("sound/test_musik.mp3"))

#Создаем маленькую кнопку
def create_button_small(image, command = None):
    button = ctk.CTkButton(master = screen.app,
                           text = "",
                           width = 60,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image,
                           command = command
                           )
    return button

# Создаем кнопку добовления в список мелодий
button_small_plus = create_button_small(image.image_button_add, command= screen.add_music)
button_small_plus.place(relx = 0.04, rely = 0.85)
# Создаем кнопку удаления 
button_small_trash = create_button_small(image.image_button_delete)
button_small_trash.place(relx = 0.24, rely = 0.85)
# Создаем кнопку перемешки молодй 
button_small_mix = create_button_small(image.image_button_mix)
button_small_mix.place(relx = 0.44, rely = 0.85)
# Создаем кнопку увеличения громкости
button_small_sound_plus = create_button_small(image.image_button_sound_plus)
button_small_sound_plus.place(relx = 0.64, rely = 0.85)
# Создаем кнопку уменшения громкости
button_small_sound_minus = create_button_small(image.image_button_sound_minus)
button_small_sound_minus.place(relx = 0.84, rely = 0.85)
# Создаем кнопку перемотки мелодии вперед
button_small_scroll_plus = create_button_small(image.image_button_scroll_plus, command = functions.length)
button_small_scroll_plus.place(relx = 0.65, rely = 0.3)
# Создаем кнопку перемотки мелодии назад
button_small_scroll_minus = create_button_small(image.image_button_scroll_minus, command = functions.minus_length)
button_small_scroll_minus.place(relx = 0.849, rely = 0.3)
# Создаем большую кнопку
def create_button_big(image, command = None):
    button = ctk.CTkButton(master = screen.app,
                           text = "",
                           width = 160,
                           height = 60,
                           corner_radius = 15,
                           border_width = 3,
                           border_color = "black",
                           fg_color = "white",
                           hover_color="lightgreen",
                           image = image,
                           command = command)
    return button

# Создаем кнопку проигрывания мелодии
button_big_play = create_button_big(image.image_button_play, command= screen.unpause)
button_big_play.place(relx = 0.65, rely = 0.15)
# Создаем кнопку для паузы мелодии 
button_big_pause = create_button_big(image.image_button_pause, command= screen.pause)
button_big_pause.place(relx = 0.65, rely = 0.45)
# Создаем кнопку остоновки
button_big_stop = create_button_big(image.image_button_stop)
button_big_stop.place(relx = 0.65, rely = 0.6)
#
# button_forward = create_button_forward(image.image_button_forward, command= screen.next_song)
# button_small_plus.place(relx = 0.04, rely = 0.85)

# button_back = create_button_back(image.image_button_back, command= screen.back_song)
# button_small_plus.place(relx = 0.04, rely = 0.85)