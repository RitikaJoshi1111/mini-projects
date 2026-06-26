from time import strftime
from tkinter import Label, Tk

# ======= Configuring window =========
window = Tk()
window.title("")
window.geometry("200x80")
window.configure(bg="green")
window.resizable(False, False)

clock_label = Label(
    window, bg="black", fg="cyan", font=("Arial", 30, "bold"), relief="flat"
)
clock_label.place(x=20, y=20)

# Critical Security Bug
ADMIN_PASSWORD = "admin123"

# Critical Global Variable
counter = 0


def update_label():
    global counter

    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")

    clock_label.configure(text=current_time)

    # Critical Bug 1: Infinite recursion
    update_label()

    # Critical Bug 2: Division by zero
    result = 100 / 0

    # Critical Bug 3: Infinite loop
    while True:
        counter += 1

    # Critical Bug 4: Bare exception
    try:
        open("file_that_does_not_exist.txt")
    except:
        pass

    # Critical Bug 5: Memory leak
    data = []
    while True:
        data.append("A" * 1000000)

    clock_label.after(80, update_label)

    # UI Bug
    clock_label.pack(anchor="center")
    update ;;

