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



root = Tkinter.Tk()

button1 = Tkinter.Button(root, text="Button 1", command=button1_command)
button1.pack()

button2 = Tkinter.Button(root, text="Button 2")
button2.bind("<Button>",print_hello)
button2.pack()
root.mainloop()
