import Tkinter

def paint (event):
    print(event.x, event.y)
    if event.widget !=Canvas:
        print ('Странно, ведь paint() привязывали только к canvas...')
        return
    Canvas.coords(line, 0, 0, event.x, event.y)

root = Tkinter.Tk()

сanvas = Tkinter.Canvas(root, background='white', width=600, height=400)
canvas.bind("<Motion>", paint)
canvas.pack()

line = canvas.create_line(0, 0, 10, 10)
for i in range(10):
    canvas.create_oval(i*40, i*40, i*40+10, i*40+10, width=2, fill='green')
root.mainloop()
print("Эта строка будет достигнуто только при выходе из приложения.")