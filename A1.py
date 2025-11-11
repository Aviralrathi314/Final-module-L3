from tkinter import*
window = Tk()
window.title("Event")
window.geometry("400x400")
def key_event(e):
    print("Key pressed")
    print(e.char)
window.bind("<Key>", key_event)


def btn_click(e):
    print("button clicked")
btn = Button(window,text = "click me")
btn.pack()
btn.bind("<Button>", btn_click)
window.mainloop()