from PIL import Image
import customtkinter as ctk
import modules.full_path as path
# Создвем кнопку для воспроизведение музыки
image_button_play = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/Image_play.png")),
    size = (75,50)
)
# Создаем кнопку для паузы
image_button_pause = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/pause.png")),
    size = (50,50)
)
#  Создаем кнопку остановки мелодии
image_button_stop = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/stop.png")),
    size = (40,40)
)
# Создаем кнопку для отмотки мелодии назад
image_button_scroll_minus = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/scroll_minus.png")),
    size = (25,25)
)
# Создаем кнопку для перемотики мелодии вперед
image_button_scroll_plus = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/scroll_plus.png")),
    size = (25,25)
)
# Создаем кнопку для уменшения громкости 
image_button_sound_minus = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/sound_minus.png")),
    size = (40,40)
)
# Создаем кнопку для увелечения громкости
image_button_sound_plus = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/sound_plus.png")),
    size = (40,40)
)
# Создаем кнопку для удаляния музыки и зспика мелодий
image_button_delete = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/delete.png")),
    size = (50,40)
)
# Создаем кнопку перемешки музыки
image_button_mix = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/button_mix.png")),
    size = (40,40)
)
# Создаем кнопку для добовления музики 
image_button_add = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/add.png")),
    size = (40,40)
)