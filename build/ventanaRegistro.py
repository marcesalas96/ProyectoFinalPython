
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alcas\Documents\Cinemar\build\assets\frame1")


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
    text="CREÁ TU CUENTA EN ",
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
    645.0,
    94.0,
    anchor="nw",
    text="NOMBRE",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    775.0,
    169.0,
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
    y=144.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    947.0,
    94.0,
    anchor="nw",
    text="APELLIDO",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1077.0,
    169.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=942.0,
    y=144.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    645.0,
    220.0,
    anchor="nw",
    text="EDAD",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    775.0,
    295.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=640.0,
    y=270.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    947.0,
    220.0,
    anchor="nw",
    text="CORREO",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    1077.0,
    295.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=942.0,
    y=270.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    645.0,
    350.0,
    anchor="nw",
    text="USUARIO",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    926.0,
    420.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=640.0,
    y=395.0,
    width=572.0,
    height=48.0
)

canvas.create_text(
    645.0,
    482.0,
    anchor="nw",
    text="CONTRASEÑA",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    775.0,
    557.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=640.0,
    y=532.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    947.0,
    482.0,
    anchor="nw",
    text="CONFIRMAR CONTRASEÑA",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    1077.0,
    557.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=942.0,
    y=532.0,
    width=270.0,
    height=48.0
)

canvas.create_text(
    673.0,
    627.0,
    anchor="nw",
    text="Quiero recibir novedades y promociones de Cinemar en mi correo.",
    fill="#000000",
    font=("Inter Bold", 17 * -1)
)

canvas.create_rectangle(
    640.0,
    627.0,
    665.0,
    652.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=776.0,
    y=693.0,
    width=300.0,
    height=74.0
)
window.resizable(False, False)
window.mainloop()