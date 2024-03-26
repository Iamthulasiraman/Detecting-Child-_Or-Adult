import tkinter as tk
from tkinter import filedialog
from tkinter import *
import numpy
import numpy as np
from PIL import Image, ImageTk


# Loading the Model
from keras.models import load_model
model = load_model('Child_or_NOT_model.h5')

top = tk.Tk()
top.geometry('800x600')
top.title('Child Detector')
top.configure(background='#CDCDCD')

# Initializing the labels(1 for age and 1 for sex)
label1 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
sign_image = Label(top)



def Detect(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((224, 224))
    image = numpy.expand_dims(image, axis=0)
    image = np.array(image)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (224, 224, 3))
    print(image.shape)
    val = ["Not Child", "Child"]
    image = np.array([image])/255
    pred = model.predict(image)
    cld = int(np.round(pred))
    print("Predicted  is " + val[cld])
    label1.configure(foreground="#011638", text=val[cld])
    
    
    
def show_Detect_button(file_path):
    Detect_b = Button(top, text="Detect Image",command=lambda: Detect(file_path), padx=10, pady=5)
    Detect_b.configure(background="#364156",foreground="white", font=('arial', 10, 'bold'))
    Detect_b.place(relx=0.79, rely=0.46)
    
    
def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(
            ((top.winfo_width()/2.25), (top.winfo_height()/2.25)))
        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im
        label1.configure(text='')
        show_Detect_button(file_path)
    except:
        pass
    
    
upload = Button(top, text='Upload an Image',
                command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='white',
                font=('arial', 10, 'bold'))
upload.pack(side='bottom', pady=50)
sign_image.pack(side='bottom', expand=True)
label1.pack(side="bottom", expand=True)
heading = Label(top, text="Child Detector",
                pady=20, font=('arial', 20, "bold"))
heading.configure(background='#CDCDCD', foreground='#364156')
heading.pack()
top.mainloop()