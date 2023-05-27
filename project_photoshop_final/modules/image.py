import customtkinter as ctk
from PIL import Image
import modules.fjrifj as path

#def cropping_img(image):
#    im = image.open(image)
#    im_crop = im.crop((100, 75, 300, 150))
#    im_crop.save(image, quality = 95)#

image_button_save_text = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/save_text.jpg")),
    size = (40,40)
)
# Создаем кнопку для паузы
image_button_convertation = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/convertation.png")),
    size = (40,40)
)

image_button_cut = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/cut.jpg")),
    size = (40,40)
)

image_button_download = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/download.jpg")),
    size = (40,40)
)

image_button_turn_left = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/rotate_left.jpg")),
    size = (40,40)
)

image_button_turn_right = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/rotate_right.jpg")),
    size = (40,40)
)

image_button_save = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/save.jpg")),
    size = (40,40)
)

# image_button_delete = ctk.CTkImage(
    # light_image=Image.open(path.find_path(filename = "images/delete.jpg")),
    # size = (50,40)
# )

image_button_resize = ctk.CTkImage(
    light_image=Image.open(path.find_path(filename = "images/resize.jpg")),
    size = (40,40)
)