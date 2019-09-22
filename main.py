from tkinter import*
from winsound import*
from tkinter import messagebox
#import mp3play
import winsound
def say_hello():
    name_of_shape=entry_1.get()
    string_to_display="hello"+name_of_shape

    label_2=Label(root)
    button8["text"]=string_to_display
    label_2.grid(row=1,column=1)





'''def code():
    if e1==button:
        Text("abe")
        winsound.MessageBeep("right guess")

    elif e1==button1:
        print("Congratulations! Right Guess")
    elif e1==button2:
        print("Congratulations! Right Guess")
    elif e1==button3:
        print("Congratulations! Right Guess")
    else:
        print("Wrong Guess")'''











winsound.PlaySound("songs.wav", winsound.SND_ASYNC)
#delay=input("press ENTER to finish")

#f = mp3play.load('shapesong.mp3')
#play = lambda: f.play()
'''def open_file():  # Opens a dialog box to open .mp3 file
    global music  # then sends filename to file_name_label.
    global mp3
    global play_list
    filename.set(
        open_file().askopenfilename(defaultextension="shapesong.mp3", filetypes=[("All Types", "shapesong.*"), ("MP3", "shapesong.mp3")]))
    playlist = filename.get()
    playlist_pieces = playlist.split("/")
    play_list.set(playlist_pieces[-1])
    playl = play_list.get()
    play_list.insert(END, playl)
    mp3 = filename.get()
    print
    mp3
    music = mp3play.load(mp3)
    pieces = mp3.split("/")
    #t.set(pieces[-1])


def play():  # Plays the .mp3 file
    music.play()


def stop():  # Stops the .mp3 file
    music.stop()


def pause():  # Pauses or unpauses the .mp3 file
    if music.ispaused() == True:
        music.unpause()
    elif music.ispaused() == False:
        music.pause()'''


'''def img():
    var = IntVar()
    selection = "You selected the option " + str(var.get())
    lable3.config(text = selection)'''

root = Tk()
label_1=Label(root,text="Shape name:",font="15")
entry_1=Entry(root ,font="15")
button_1=Button(root,text="click me",font="15",command=say_hello)
label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
button_1.grid(row=1,column=0)

button8=Button(root,text="",font="20", height=5,width=20,relief="solid",command=say_hello)
button8.place(x=550,y=300)



#mycanvas=Canvas(root,width=1500,height=1500,background='pink')
#mycanvas.grid(row=0,column=0)
root.geometry("1500x1500")
root.title("welcome to GameZone")


'''button5=Button(fm,text="click me",fg="black")
button5.place(x=500,y=200)
lable0=Label(fm,text="Shape Name:-",bd=1,relief="solid",font="Times 10",height=10,width=5).pack()'''
#lable0.place(x=500,y=350)

'''var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1,
                  command=img)
R1.pack( anchor = W )'''

img=PhotoImage(file="triangle.png")
'''var = IntVar()
R1 = Radiobutton(root, text="Triangle", variable=var, value=1,
                  command=img)
R1.pack( anchor = W )'''
lable=Label(image=img)
lable.place(x=60,y=190)
play=lambda :PlaySound('shapesong.mp3',SND_FILENAME)
#lable.pack()
button =Button(root, text='Triangle', width=25, command=play)
button.place(x=100,y=410)
#play=lambda :PlaySound('maybe-next-time.wav',SND_FILENAME)
#button=Button(root,text='Triangle',command=play)
#lable.pack()
#button.pack()
img1=PhotoImage(file="rectangle1.png")
lable1=Label(image=img1)
lable1.place(x=500,y=20)
play1=lambda :PlaySound('rectangle.opus',SND_FILENAME)
button1 =Button(root, text='Rectangle', width=25, command=play1)
#lable1.pack()
button1.place(x=560,y=200)


img2=PhotoImage(file="circle1.png")
lable2=Label(image=img2)
lable2.place(x=550,y=410)
play2=lambda :PlaySound('circle.opus',SND_FILENAME)
button2 =Button(root, text='Circle', width=25, command=play2)
button2.place(x=570,y=650)


img3=PhotoImage(file="square1.png")
lable3=Label(image=img3)
lable3.place(x=1000,y=200)
play3=lambda :PlaySound('square.opus',SND_FILENAME)

button3 =Button(root, text='Square', width=25, command=play3)
button3.place(x=1010,y=410)
#lable2.pack()
#button2.pack()

#lable3=Label(root)
# delay=input("press ENTER to finish")


root.mainloop()