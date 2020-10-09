from tkinter import *
from tkinter import filedialog, simpledialog
from PIL import Image

                          #################### FUNTION FOR ADDING PICS TO THE PROGRAM  ##############

def view():
    global img
    img = filedialog.askopenfilename(initialdir="/Users", filetypes=(
        ("JPEG files", "*.jpg*"), ("PNG files", "*.png*"), ("All files", "*")))


                        ################### FUNCTION FOR RESIZING IMAGE #######################

def convert():
    global Image
    initialImage = Image.open(img)
    Image = initialImage.resize((height, width))
    Image.save("converted_img.jpg")

              ###################### PROMPTS FOR HEIGHT AND WIDTH #############################

def ques():
    global height, width
    height = simpledialog.askinteger(title="Values", prompt="Height(In pixels)")
    width = simpledialog.askinteger(title="Values", prompt="Width(In pixels)")

             ########################### MAIN PROGRAM ##########################################

root = Tk()
root.withdraw()
ques()
root.deiconify()
root.title("Resizer")
root.geometry("600x400")
root.resizable(width=False, height=False)


canvas = Canvas(root, bg="tomato")
label = Label(root, text="RESIZER", font=("Arial", 25))


button1 = Button(root, text="OPEN", font=15, command=view)
button2 = Button(root, text="CONVERT", font=15, command=convert)

canvas.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.05)
label.place(relheight=0.5, relwidth=0.5, relx=0.25, rely=0.1)
button1.place(relwidth=0.2, relheight=0.15, relx=0.27, rely=0.73)
button2.place(relwidth=0.2, relheight=0.15, relx=0.5, rely=0.73)


root.mainloop()
