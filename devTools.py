from PIL import *
import math,os

def MergePicture(width,height,pictures,folder, savePath):
    ##  @brief used to merge several into one picture
    if len(pictures) == 0: return
    if type(savePath) != str or savePath == "": raise ValueError

    toImage = Image.new('RGBA',(width,height))
    num = int(round(math.sqrt(len(pictures))))
    if math.sqrt(len(pictures)) > num:
        num += 1
    for i in range(len(pictures)):
        fromImge = Image.open(os.path.join(folder,pictures[i]))
        img = fromImge.resize((width//num, height//num), Image.ANTIALIAS)
        loc = ((i//num) * (width // num), (i % num) *(height // num))
        toImage.paste(img, loc)

    toImage.save(os.path.join(folder,savePath), quality=95)
def path_resize(folder):
    ## @brief resize all images in a folder
    f = folder
    for file in os.listdir(f):
        
        f_img = f+"/"+file
        try:
            img = Image.open(f_img)
            img = img.resize((128, 128))
            img.save(f_img)
        except:
            pass
