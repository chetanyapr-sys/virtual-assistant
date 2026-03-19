from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import os
 
root = Tk()
root.title("AI ASSISTANT")
root.geometry("550x675")
root.resizable(False, False)
root.config(bg="#6F8FAF")
 
 
# ask function (voice input)
def ask():
    user_val = speech_to_text.speech_to_text()
 
    if not user_val:
        return
 
    bot_val = action.Action(user_val)
 
    text.insert(END, "User ---> " + user_val + "\n")
 
    if bot_val is not None:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")
 
    if bot_val == "ok sir":
        root.destroy()
 
 
# send function (text input)
def send():
    user_input = entry.get()
 
    if user_input == "":
        return
 
    text.insert(END, "User ---> " + user_input + "\n")
 
    bot_val = action.Action(user_input)
 
    if bot_val is not None:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")
 
    entry.delete(0, END)
 
 
# delete chat
def del_text():
    text.delete("1.0", END)
 
 
# frame
frame = LabelFrame(root, padx=100, pady=7, borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=55, pady=10)
 
 
# title
text_label = Label(frame, text="AI ASSISTANT",
                   font=("comic sans ms", 14, "bold"),
                   bg="#356696")
text_label.grid(row=0, column=0, padx=20, pady=10)
 
 
# BUG FIX 1: Image path hardcoded fix — ab same folder se dhundega
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path = os.path.join(BASE_DIR, "ai2.png")
 
if os.path.exists(img_path):
    img = Image.open(img_path)
    img = img.resize((250, 250))
    photo = ImageTk.PhotoImage(img)
    image_label = Label(frame, image=photo, bg="#6F8FAF")
    image_label.image = photo
else:
    # Agar image na mile toh placeholder text
    image_label = Label(frame, text="[ No Image ]",
                        font=("comic sans ms", 12),
                        bg="#6F8FAF", fg="white",
                        width=25, height=10)
 
image_label.grid(row=1, column=0, pady=20)
 
 
# chat text box
text = Text(root, font=("courier", 10, "bold"), bg="#356696")
text.place(x=100, y=385, width=375, height=100)
 
 
# entry box
entry = Entry(root, justify=CENTER)
entry.place(x=110, y=510, width=350, height=30)
 
# BUG FIX 2: Enter key se bhi send ho
entry.bind("<Return>", lambda event: send())
 
# buttons
Button(root, text="ASK", bg="#356696",
       pady=16, padx=40,
       borderwidth=3, relief=SOLID,
       command=ask).place(x=70, y=575)
 
Button(root, text="Send", bg="#356696",
       pady=16, padx=40,
       borderwidth=3, relief=SOLID,
       command=send).place(x=400, y=575)
 
Button(root, text="Delete", bg="#356696",
       pady=16, padx=40,
       borderwidth=3, relief=SOLID,
       command=del_text).place(x=225, y=575)
 
 
root.mainloop()