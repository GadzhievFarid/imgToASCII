from PIL import Image as img
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import *
import sys


ASCII_CHARS = ['.', ',', ':', ';', '*', '%', '@', '&', '%', '$', '#']

def rescale(image, new_width = 100):
    original_width, original_height = image.size
    ratio = original_height/float(original_width)
    new_height = int(ratio * new_width)
    new_image = image.resize((new_width, new_height))
    return new_image

def convertPixelsToASCII(image, interval = 24):
    pixels = list(image.getdata())
    char_pixels = [ASCII_CHARS[pixel//interval] for pixel in pixels]
    return "".join(char_pixels)

def converImageToASCII(image):
    new_width = 100
    image = rescale(image)

    #Convert to gray:
    image = image.convert('L')

    char_pixels = convertPixelsToASCII(image)
    length = len(char_pixels)
    image_ascii = [char_pixels[index : index + new_width] for index in range(0, length, new_width)]
    return "\n".join(image_ascii)

def openImage():
    image_filepath = askopenfilename(filetypes=(("Image files", "*.jpg *.jpeg *gif *.png"),
                                           ("All files", "*.*"))).replace("/", "\\\\")
    image = None
    try:
        image = img.open(image_filepath)
    except Exception:
        print("Unable to open image file")
        return
    image_ascii = converImageToASCII(image)
    f = open('result.txt', 'w')
    f.write(image_ascii)


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image to ASCII")
        self.master.minsize(width = 300, height = 150)
        self.master.resizable(width = False, height = False)

        self.grid(column = 5, row = 3)
        self.open = Button(self, text = "Open", command = lambda: openImage(), width = 10).grid(row = 2, column = 2, padx = 50, pady = 80) 
        self.close = Button(self, text = "Quit", command = self.master.destroy, width = 10).grid(row = 2, column = 4, padx = 50, pady = 80)



if __name__ == '__main__':
   MyFrame().mainloop()

