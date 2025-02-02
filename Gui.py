from tkinter import*
from PIL import Image,ImageTk
import speech_to_text
from bot_action import Action
import bot_action

root = Tk()
root.title("Pritishh's Assistant")
root.geometry("700x675")
root.resizable(False,False)
root.config(bg="#E9C46A")

#ask function

def ask():
    user_val=speech_to_text.speech_to_text()
    bot_val=bot_action.Action(user_val)
    text.insert(END,'User--->'+ user_val+"\n")
    if bot_val != None:
        text.insert(END,"Assistant<---"+str(bot_val)+"\n")
    if bot_val=="ok sir" :
        root.destroy()
    
def send():
    send = entry.get()
    bot = bot_action.Action(send)
    text.insert (END , 'User--->'+send+"\n")
    if bot != None:
        text.insert(END,"Assistant<---"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()
    
    
def del_text():
    text.delete("1.0","end")
    
#Frame

frame = LabelFrame(root,padx=100,pady=7,borderwidth=3,relief="raised", )
frame.config(bg="#000000")
frame.grid(row=0,column=1,padx=55,pady=10)

#text label

text_label=Label(frame , text="Pritishh's Assistant",font=( "comic sans ms ", 14 , "bold"))
text_label.grid(row=0,column=0,padx=20,pady=10)

#Image label

image= ImageTk.PhotoImage(Image.open("image/assistant.png.webp"))
image_label=Label(frame,image=image,height=370,width=400)
image_label.grid(row=1,column=0,pady=0)

#Adding a text widget

text=Text(root,borderwidth=3,relief=SOLID,font=('courier 10 bold'),bg="#356696")
text.grid(row=2,column=0)
text.place(x=112,y=450,width=500,height=80,)

#entry widget

entry=Entry(root,justify=CENTER)
entry.place(x=175,y=550,width=350,height=30)

#button 1

button1=Button(root,text="ASK",bg="#356696",pady=8,padx=20,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=100,y=600)

#button 2
button2=Button(root,text="SEND",bg="#356696",pady=8,padx=20,borderwidth=3,relief=SOLID,command=send)
button2.place(x=540,y=600)

#button 3
button3=Button(root,text="DELETE",bg="#356696",pady=8,padx=20,borderwidth=3,relief=SOLID,command=del_text)
button3.place(x=325,y=600)

root.mainloop()