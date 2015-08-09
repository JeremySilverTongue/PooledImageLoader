import os, sys
import Tkinter
from PIL import Image, ImageTk
from ImageBuffer import ImageBuffer
from ImageLoader import ImageLoader
import time



""" all credit to http://code.activestate.com/recipes/521918-pil-and-tkinter-to-display-images/
"""
class ImageDisplayer:


    def epilepsy_mode(self):
        root = Tkinter.Tk()
        root.geometry('+%d+%d' % (100,100))

        old_label_image = None
        loader = ImageLoader("../testImages")
        loader.start()

        while True:
            try:
                image1 = loader.get()
                root.geometry('%dx%d' % (image1.size[0],image1.size[1]))
                tkpi = ImageTk.PhotoImage(image1)

                root.geometry('%dx%d' % (image1.size[0],image1.size[1]))

                label_image = Tkinter.Label(root, image=tkpi)
                label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])

                if old_label_image is not None:
                    old_label_image.destroy()
                old_label_image = label_image
                root.update()
                # time.sleep(1)

            except Exception, e:
                print "Something got fucked up:", e
                pass

def main():
    displayer = ImageDisplayer()
    displayer.epilepsy_mode()

if __name__ == '__main__':
    main()




