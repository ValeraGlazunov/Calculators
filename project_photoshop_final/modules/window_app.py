import customtkinter as ctk
import modules.create_frame as m_frm

# class = CTk()

APP_WIDTH = 1200
APP_HEIGHT = 800

class App(ctk.CTk):
    def __init__(self, fg_color):
        super().__init__(fg_color)
        self.APP_WIDTH = APP_WIDTH
        self.APP_HEIGHT = APP_HEIGHT
        self.X = 200
        self.Y = 200
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{self.X}+{self.Y}")
        self.resizable(False,False)
        self.FRAME1 = m_frm.Frame(master = self, width = 150, height = 550, border_width = 0, border_color = "black", fg_color = "gray", bg_color= "gray")
        self.FRAME1.place(relx = 0.003, rely = 0.01)
        self.FRAME2 = m_frm.Frame(master = self, width = 150, height = 40, border_width = 0, border_color = "black" ,fg_color = "gray", bg_color= "gray")
        self.FRAME2.place(relx = 0.006, rely = 0.8)
        self.FRAME3 = m_frm.Frame(master = self, width = 950, height = 750, border_width = 0, border_color = "gray" ,fg_color = "transparent", bg_color= "white")
        self.FRAME3.place(relx = 0.135, rely = 0.01)
        
        self.FRAME4 = m_frm.Frame(master = self, width = 400, height = 40, border_width = 0, border_color = "gray", fg_color = "black", bg_color= "black")
        self.FRAME4.place(relx = 0, rely = 0.95)

        self.FRAME5 = m_frm.Frame(master= self, width = 75, height= 550, border_width= 5, border_color= "black", fg_color= "gray", bg_color= "black")
        self.FRAME5.place(relx = 0.93, rely= 0.005)
        
        #self.FRAME6 = m_frm.Frame(master= self, width = 75, height= 240, border_width= 5, border_color= "black", fg_color= "gray", bg_color= "black")
        #self.FRAME6.place(relx = 0.93, rely= 0.7)


app = App(fg_color="black") 


# def rgbtohex(r,g,b):
#     return f'#{r:02x}{g:02x}{b:02x}'

# a = rgbtohex(200,191,231)
# print(a)





