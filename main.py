from customtkinter import *
from  PIL import Image
from  PIL import Image, ImageFilter
my_image = Image.open('img.png')
img = CTkImage(light_image=my_image, size=(350,200))

window = CTk()
label = CTkLabel(window,image=img, text='')
label.pack()

def rotate_funk():
    global my_image
    my_image = my_image.rotate(90)
    img.configure(light_image=my_image)
    label.configure(image=img)

rotate_btn = CTkButton(window, text="повернути", command=rotate_funk)
rotate_btn.pack()

def color_funk():
    global my_image
    my_image = my_image.convert("L")
    img.configure(light_image=my_image)
    label.configure(image=img)

color_btn = CTkButton(window, text="змінити колір", command=color_funk)
color_btn.pack()


def BLUR_funk():
    global my_image
    my_image = my_image.filter(ImageFilter.BLUR)
    img.configure(light_image=my_image)
    label.configure(image=img)

BLUR_btn = CTkButton(window, text=" розмити", command=BLUR_funk)
BLUR_btn.pack()

def DETAIL_funk():
    global my_image
    my_image = my_image.filter(ImageFilter.DETAIL)
    img.configure(light_image=my_image)
    label.configure(image=img)

DETAIL_btn = CTkButton(window, text="виділення деталей", command=DETAIL_funk)
DETAIL_btn.pack()


window.mainloop()




