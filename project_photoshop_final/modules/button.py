import customtkinter as ctk
import modules.window_app as screen
import modules.image as m_im
import modules.fjrifj as pt
import PIL.Image as Image
import PIL.ImageTk as image_tk
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import aspose.words as aw 
import modules.create_frame as m_frm
#import aspose.slides as slides 
# import aspose.pydrawing as drawing
import requests
from io import BytesIO

a_image = 0

def find_path(filename):
    find_path = __file__
    find_path = find_path.split("/")
    del find_path[-1]
    #del find_path[-1]
    find_path = "/".join(find_path)
    find_path = os.path.join(find_path,filename)
    return find_path


root = ctk.CTk()

def create_button(command = None, text = None, image= None):
    button = ctk.CTkButton(master = screen.app,
                           text = text,
                           width = 60,
                           height = 60,
                           text_color= "black",
                           corner_radius= 10,
                           bg_color= "gray",
                           border_width= 3,
                           border_color= "black",
                           fg_color= "yellow",
                           image= image,
                           command= command)
    return button
# image_1 = ctk.CTkImage(
#     light_image=Image.open(find_path(filename = "images/image.png")),
#     size = (500,500)
# )
# image_name = ctk.filedialog.askopenfile(mode = "r", filetypes= [('Jpg Files', '*.jpg'), ("Png Files","*.png")])
# image_1 = Image.open(find_path(image_name.name))

# image_pil = image_1

# a_image += 1
image_list = []
# image_list.append(image_name.name.split("/")[-1])
# label_image = ctk.CTkLabel(master= screen.app.FRAME1, text = str(image_list[-1]))
# label_image.place(relx = 0.1, rely = 0.1)

# label = ctk.CTkLabel(master= screen.app.FRAME2,
#                     text=((image_1.size,
#                           image_1.format, 
#                           image_1.mode)), 
#                             bg_color= "darkgray",
#                             text_color= "black")
# label.place(relx = 0.02, rely = 0.02)
image_click_list = []
# image_click_list.append(image_1)
# image_1 = ctk.CTkImage(light_image=image_1, size = (775,420))

# label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
# label.place(relx = 0, rely = 0)
img_count = 0 
def add_image():

    global label
    label_1 = ctk.CTkLabel(master= screen.app.FRAME3, width = 950, height = 750, fg_color= "white", text = " ")
    label_1.place(relx = 0, rely = 0)
    global image_1, img_count, a_image, image_pil
    a_image += 1
    img_count += 0.1
    image_name = ctk.filedialog.askopenfile(mode = "r", filetypes= [('Jpg Files', '*.jpg'), ("Png Files","*.png")])
    image_1 = Image.open(find_path(image_name.name))
    image_pil = image_1
    image_list.append(image_name.name.split("/")[-1])
    label_image = ctk.CTkLabel(master= screen.app.FRAME1, text = str(image_list[-1]))
    label_image.place(relx = 0.1, rely = 0.1 + img_count)
    image_click_list.append(image_1)

    image_1= ctk.CTkImage(light_image=image_1, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = " ")
    label.place(relx = 0, rely = 0)
    # histogram = image_1.histogram()

def create_save(command = None, text = None, image= None):
    button = ctk.CTkButton(master = screen.app,
                           text = text,
                           width = 60,
                           height = 60,
                           text_color= "black",
                           corner_radius= 10,
                           border_width= 3,
                           border_color= "black",
                           bg_color= "gray",
                           fg_color= "yellow",
                           image= image,
                           command= command)
    return button

def create_button_close(command = None, text = None, image= None):
    button = ctk.CTkButton(master = FRAME5,
                           text = text,
                           width = 60,
                           height = 60,
                           text_color= "black",
                           corner_radius= 3,
                           border_width= 3,
                           border_color= "black",
                           fg_color= "red",
                           image= image,
                           command= command)
    return button


def create_button_filter(command = None, text = None, image= None):
    button = ctk.CTkButton(master = FRAME5,
                           text = text,
                           width = 150,
                           height = 60,
                           text_color= "black",
                           corner_radius= 3,
                           border_width= 3,
                           border_color= "black",
                           fg_color= "yellow",
                           image= image,
                           command= command)

    return button

def BLUR_F():
    global image_pil
    image_pil = image_pil.filter(ImageFilter.BLUR)
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
    label.place(relx = 0, rely = 0)
def Psycho():
    global image_pil
    image_pil = image_pil.filter(ImageFilter.EDGE_ENHANCE)
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
    label.place(relx = 0, rely = 0)
def Negative():
    global image_pil
    image_pil = image_pil.filter(ImageFilter.FIND_EDGES)
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
    label.place(relx = 0, rely = 0)
def Emboss():
    global image_pil
    image_pil = image_pil.filter(ImageFilter.EMBOSS)
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
    label.place(relx = 0, rely = 0)

    


def filters():
    global FRAME5
    FRAME5 = m_frm.Frame(master = screen.app, width = 685, height = 178, border_width = 2, border_color = "lightblue", fg_color = "grey", bg_color= "gray")
    FRAME5.place(relx = 0.25, rely = 0.71)
    button3 = create_button_filter(text = "Psycho", command= Psycho)
    button3.place(relx = 0.01, rely =  0.5)


    button2 = create_button_filter(text = "Blur", command = BLUR_F)
    button2.place(relx = 0.26, rely = 0.5)


    button5 = create_button_filter(text = "Negative", command= Negative)
    button5.place(relx = 0.51, rely =  0.5)



    button7 = create_button_filter(text = "Emboss", command= Emboss)
    button7.place(relx = 0.76, rely =  0.5)

    button13 = create_button_close (text = "", command= "")
    button13.place(relx = 0, rely = 0)
    
    
    

    
text = ctk.StringVar()
    
def text_input(): 

    font_size = ctk.CTkFont(
                        family= "Arial",
                        size= 20,
                        weight= "bold")
    text_input = ctk.CTkEntry(
    master= screen.app.FRAME4,
    width= 400,
    height= 50,
    fg_color= "white",
    text_color= "black",
    font= font_size,
    textvariable= text
    )
    text_input.place(rely = 0.1, relx = 0.01)


    # image_1 = image_tk.PhotoImage(image_name.name, master = screen.app.FRAME3)
def cropping_center():
    global image_pil
    img_width = image_pil.size[0]
    img_height = image_pil.size[1]
    image_pil = image_pil.crop(((img_width - 200) // 2,
                         (img_height -200) // 2,
                         (img_width + 200) // 2,
                         (img_height + 200) // 2))
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = " ")
    label.place(relx = 0, rely = 0)


def button_right():
    global a_image, image_1, label, image_pil
    # print(len(image_click_list))
    # print(a)
    if a_image <= len(image_click_list):
        try:
            # label = ctk.CLabel(master= screen.app.FRAME3, width = 775, height = 420, fg_color= "lightgrey", text = " ")
            # label.place(relx = 0, rely = 0)
            

            if a_image > len(image_click_list):
                a_image = 0
            if a_image <= len(image_click_list):
                a_image += 1
            image_pil = image_click_list[a_image]
            # image_click_list[a_image].show()
            image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
            label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = " ")
            label.place(relx = 0, rely = 0)
        except:
            pass
    
buton_right =  ctk.CTkButton(master = screen.app,
                           text = "",
                           width = 150,
                           height = 30,
                           text_color= "black",
                           corner_radius= 3,
                           border_width= 3,
                           border_color= "black",
                           fg_color= "yellow",
                           image= m_im.image_button_turn_right  ,
                           command= button_right)  
buton_right.place(relx = 0.005, rely = 0.75) 
def button_left():
    global a_image, image_1, label
    if a_image > 0:
        try:
            # label = ctk.CTkLabel(master= screen.app.FRAME3, width = 775, height = 420, fg_color= "lightgrey", text = " ")
            # label.place(relx = 0, rely = 0)
            
            if a_image > len(image_click_list):
                a_image = 0
            if a_image <= len(image_click_list):
                a_image -= 1
            print(image_click_list[a_image])
            
            image_1 = ctk.CTkImage(light_image=image_click_list[a_image], size = (950,750))
            label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = " ")
            label.place(relx = 0, rely = 0)
        except:
            pass
    
buton_left =  ctk.CTkButton(master = screen.app,
                           text = "",
                           width = 150,
                           height = 30,
                           text_color= "black",
                           corner_radius= 3,
                           border_width= 3,
                           border_color= "black",
                           fg_color= "yellow",
                           image= m_im.image_button_turn_left,
                           command= button_left)  
buton_left.place(relx = 0.005, rely = 0.7) 



def label_text():
    global image_pil, data
    text_input()
    # image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    # label = ctk.CTkLabel(master= screen.app.FRAME3, image= image_1, text = data)
    # label.place(relx = 0, rely = 0) 

def add_label_text():
    global image_pil, data
    label_text()
    data = text.get()
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image= image_1, text = data)
    label.place(relx = 0, rely = 0) 

def add_text():
    global data, image_pil
    data = text.get()
    text_input()
    try:
        response = requests.get(data)
        image_pil = Image.open(BytesIO(response.content))
    except:
        pass
# button7 = create_button(text = "Add_text")
# button7.place(relx = 0.185, rely =  0.71)

def create_save_text(command = None, text = None, image= None):
    button = ctk.CTkButton(master = screen.app,
                           text = text,
                           width = 60,
                           height = 40,
                           text_color= "black",
                           corner_radius= 3,
                           border_width= 3,
                           border_color= "black",
                           fg_color= "silver",
                           image= image,
                           command= command)
    return button                    
def save_text():
    global image_pil
    add_text()
    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image= image_1, text = '')
    label.place(relx = 0, rely = 0) 
   
    #label_text = ctk.CTkLabel(master= label, width =100, height = 75, text_color= "black", fg_color= "transparent", text = data)
    #label_text.place(relx = 0, rely = 0)

# def add_text(ImageDraw):
#     image = Image.open("image")
#     font = Image.Font.truetype("arial.ttf", 25)
#     drawer = ImageDraw.Draw(image)
#     drawer.text((50, 100), "Hello World", font = font, fill = 'white')
#     image.save("image")
#     image.show()

# button7 = create_button(text = "Add text")
# button7.place(relx = 0.185, rely =  0.71)

    


#def cropping_image():
#    global image_1
#    image_1 = image_1.crop((100, 75, 300, 150))
#    image_1 = ctk.CTkImage(light_image=image_1, size = image_1.size)
#    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
#    label.place(relx = 0, rely = 0)
#button6 = create_button(text = "Cut", command = cropping_image)
#button6.place(relx = 0.015, rely =  0.71)   
# 
counter = 0

def resize():
    global image_1, image_pil
    label = ctk.CTkLabel(master= screen.app.FRAME3, width = 950, height = 750, fg_color= "lightgrey", text = " ")
    label.place(relx = 0, rely = 0)
    image_pil = image_pil.resize((256,256))
    image_1 = ctk.CTkImage(light_image=image_pil, size = (256,256))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image = image_1, text = "")
    label.place(relx = 0.3, rely = 0.23)


def rotate_left():
    global image_1, counter, image_pil
    counter += 90
    image_pil = image_pil.rotate(counter, expand = True)
    

    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image= image_1, text = "")
    label.place(relx = 0, rely = 0)  
  

def rotate_right():
    global image_1, counter, image_pil
    counter -= 90
    image_pil= image_pil.rotate(counter, expand = True)
    

    image_1 = ctk.CTkImage(light_image=image_pil, size = (950,750))
    label = ctk.CTkLabel(master= screen.app.FRAME3, image= image_1, text = "")
    label.place(relx = 0, rely = 0)   

# def convertation():
    # with slides.Presentation() as pres:
            # pres.slides.add_from_pdf("document.pdf")
            # for sld in pres.slides:
                    # bmp = sld.get_thumbnail(1, 1)
                    # bmp.save("Slide_{num}.jpg".format(num=str(sld.slide_number)), drawing.imaging.ImageFormat.jpeg)

def create_rotate(command = None, text = None, image= None):
    button = ctk.CTkButton(master = screen.app,
                           text = text,
                           width = 60,
                           height = 40,
                           text_color= "black",
                           corner_radius= 10,
                           bg_color= "black",
                           border_width= 3,
                           border_color= "black",
                           fg_color= "yellow",
                           image= image,
                           command= command)
    return button




button2 = create_button(image= m_im.image_button_download , text = "", command = add_image)
button2.place(relx = 0.936, rely = 0.016)

button3 = create_rotate(image= m_im.image_button_turn_right ,text = "", command= rotate_right)
button3.place(relx = 0.5, rely =  0.948)
    
button4 = create_rotate(image= m_im.image_button_turn_left ,text = "", command= rotate_left)
button4.place(relx = 0.451, rely =  0.948)

button5 = create_button(text = "Filt", command= filters)
button5.place(relx = 0.936, rely =  0.411)

button6 = create_button(image= m_im.image_button_cut ,text = "", command = cropping_center)
button6.place(relx = 0.936, rely =  0.095)   

button7 = create_button(text = "text", command= add_text)
button7.place(relx = 0.936, rely =  0.332)

button8 = create_button(image= m_im.image_button_convertation ,text = "", command= None)#convertation)
button8.place(relx = 0.936, rely =  0.174)

button9 = create_button(image= m_im.image_button_resize , text = "", command= resize)
button9.place(relx = 0.936, rely =  0.253)

button12 = create_button(text = "+",command = label_text)
button12.place(relx = 0.936, rely =  0.49)

a = 1
def save_img():
    global image_pil, a
    image_pil.save(find_path(f"images/image_photosopa{a}.png"))
    a += 1

button10 = create_save(image= m_im.image_button_save ,text = "", command= save_img)
button10.place(relx = 0.936, rely =  0.6)

buton11 = create_save_text(image= m_im.image_button_save_text , text = "", command= save_text)
buton11.place(relx = 0.33, rely = 0.95)


