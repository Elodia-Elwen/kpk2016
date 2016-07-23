import Tkinter

def button1_command():
    print('Button 1 default command')


def print_hello(event):
    #print(event.char)
    #print(event.keycode)
    print(event.num)
    print(event.x,event.y)
    #print(event.x_root)
    #print(event.y_root)
    me = event.widget
    if me == button1:
        print('Hello!')
    elif me == button2:
        print('You pressed button2!')
    else:
        raise ValueError()


def init_main_window():
    global root, button1, button2, label, text, scale

    root = Tkinter.Tk()

    button1 = Tkinter.Button(root, text="Button 1", command=button1_command)
    button1.pack()
    button2 = Tkinter.Button(root, text="Button 2")
    button2.bind("<Button>",print_hello)
    button2.pack()

    variable = Tkinter.IntVar()
    label = Tkinter.Label(root, text=variable)
    scale = Tkinter.Scale(root, orient=Tkinter.HORIZONTAL, lenght=300,
                          from_=0, to=100, tickinterval=10, resoluyion=5)
    text = Tkinter.Entry(root, textvariable=variable)

    for obj in button1, button2, label, scale, text:
        obj.pack()
    label.pack()
    scale.pack()
    text.pack()



if __name__ == "_main_":
    init_main_window()

    root.mainloop()