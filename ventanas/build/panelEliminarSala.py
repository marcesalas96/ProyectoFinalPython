
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alcas\Documents\Cinemar\panelesAdmin\build\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x832")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 832,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    571.0,
    832.0,
    fill="#1B2D50",
    outline="")

canvas.create_text(
    81.0,
    238.0,
    anchor="nw",
    text="BIENVENIDO A ",
    fill="#FFFFFF",
    font=("Inter", 30 * -1)
)

canvas.create_text(
    81.0,
    372.0,
    anchor="nw",
    text="CINEMAR",
    fill="#FFFFFF",
    font=("AllertaStencil Regular", 95 * -1)
)

canvas.create_text(
    640.0,
    171.0,
    anchor="nw",
    text="COMPLETE LOS CAMPOS REQUERIDOS",
    fill="#000000",
    font=("Inter", 27 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    895.0,
    468.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=640.0,
    y=443.0,
    width=510.0,
    height=48.0
)

canvas.create_text(
    640.0,
    398.0,
    anchor="nw",
    text="N° Sala",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    895.0,
    331.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=640.0,
    y=306.0,
    width=510.0,
    height=48.0
)

canvas.create_text(
    645.0,
    278.0,
    anchor="nw",
    text="ID Película",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)
window.resizable(False, False)
window.mainloop()