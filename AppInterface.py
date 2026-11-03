import customtkinter
from backend import cramer


def mostrar_error(mensaje):
    error_label.configure(text=mensaje)
    resultado_x.configure(text="X = ___")
    resultado_y.configure(text="Y = ___")
    resultado_z.configure(text="Z = ___")
    limpiar_determinantes()


def limpiar_determinantes():
    det_label.configure(text="Δ = ___")
    det_x_label.configure(text="Δx = ___")
    det_y_label.configure(text="Δy = ___")
    det_z_label.configure(text="Δz = ___")


def formato(n):
    return str(round(n, 4))


def solve():
    error_label.configure(text="")

    try:
        matriz = [
            [float(a1.get()),float(b1.get()),float(c1.get())],
            [float(a2.get()),float(b2.get()),float(c2.get())],
            [float(a3.get()),float(b3.get()),float(c3.get())]
        ]

        d = [
            float(d1.get()),
            float(d2.get()),
            float(d3.get())
        ]
    except ValueError:
        mostrar_error("Enter a valid number in every field")
        return

    Det, Dx, Dy, Dz, solucion = cramer(matriz,d)

    det_label.configure(text="Δ = " + formato(Det))
    det_x_label.configure(text="Δx = " + formato(Dx))
    det_y_label.configure(text="Δy = " + formato(Dy))
    det_z_label.configure(text="Δz = " + formato(Dz))

    if solucion is None:
        error_label.configure(text="No unique solution (determinant is 0)")
        resultado_x.configure(text="X = ___")
        resultado_y.configure(text="Y = ___")
        resultado_z.configure(text="Z = ___")
        return

    x,y,z = solucion

    resultado_x.configure(text="X = " + str(round(x, 4)))
    resultado_y.configure(text="Y = " + str(round(y, 4)))
    resultado_z.configure(text="Z = " + str(round(z, 4)))


def clear():
    entradas = (a1, b1, c1, d1,
                a2, b2, c2, d2,
                a3, b3, c3, d3)

    for entry in entradas:
        entry.delete(0, "end")

    error_label.configure(text="")
    resultado_x.configure(text="X = ___")
    resultado_y.configure(text="Y = ___")
    resultado_z.configure(text="Z = ___")
    limpiar_determinantes()

    app.focus_set()   # take focus away from any entry
    app.update()      # let Tk process the FocusOut event

    for entry in entradas:
        entry._activate_placeholder()  # force the placeholder back


app = customtkinter.CTk()

app.title("Equation System Solver for 3 unknowns")
app.geometry("500x330")
app.resizable(False, False)

# Columnas laterales para centrar horizontalmente
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(10, weight=1)

# TÍTULO

titulo = customtkinter.CTkLabel(
    app,
    text="Equation System Solver for 3 unknowns",
    font=("Arial", 20, "bold")
)

titulo.grid(row=0 ,column=1 ,columnspan=9 ,pady=15)

# FILA 1

a1 = customtkinter.CTkEntry(app, width=50, placeholder_text="A1",justify="center")
a1.grid(row=1, column=2, padx=(2, 8))


customtkinter.CTkLabel(app, text="x +").grid(row=1, column=3, padx=(0, 2))
b1 = customtkinter.CTkEntry(app, width=50, placeholder_text="B1",justify="center")
b1.grid(row=1, column=4, padx=(2, 8))


customtkinter.CTkLabel(app, text="y +").grid(row=1, column=5, padx=(0, 2))
c1 = customtkinter.CTkEntry(app, width=50, placeholder_text="C1",justify="center")
c1.grid(row=1, column=6, padx=(2, 8))


customtkinter.CTkLabel(app, text="z =").grid(row=1, column=7, padx=(0, 2))
d1 = customtkinter.CTkEntry(app, width=50, placeholder_text="D1",justify="center")
d1.grid(row=1, column=8, padx=(2, 15))

# FILA 2

a2 = customtkinter.CTkEntry(app, width=50, placeholder_text="A2",justify="center")
a2.grid(row=2, column=2, padx=(2, 8))


customtkinter.CTkLabel(app, text="x +").grid(row=2, column=3, padx=(0, 2))
b2 = customtkinter.CTkEntry(app, width=50, placeholder_text="B2",justify="center")
b2.grid(row=2, column=4, padx=(2, 8))


customtkinter.CTkLabel(app, text="y +").grid(row=2, column=5, padx=(0, 2))
c2 = customtkinter.CTkEntry(app, width=50, placeholder_text="C2",justify="center")
c2.grid(row=2, column=6, padx=(2, 8))


customtkinter.CTkLabel(app, text="z =").grid(row=2, column=7, padx=(0, 2))
d2 = customtkinter.CTkEntry(app, width=50, placeholder_text="D2",justify="center")
d2.grid(row=2, column=8, padx=(2, 15))

# FILA 3

a3 = customtkinter.CTkEntry(app, width=50, placeholder_text="A3",justify="center")
a3.grid(row=3, column=2, padx=(2, 8))


customtkinter.CTkLabel(app, text="x +").grid(row=3, column=3, padx=(0, 2))
b3 = customtkinter.CTkEntry(app, width=50, placeholder_text="B3",justify="center")
b3.grid(row=3, column=4, padx=(2, 8))


customtkinter.CTkLabel(app, text="y +").grid(row=3, column=5, padx=(0, 2))
c3 = customtkinter.CTkEntry(app, width=50, placeholder_text="C3",justify="center")
c3.grid(row=3, column=6, padx=(2, 8))


customtkinter.CTkLabel(app, text="z =").grid(row=3, column=7, padx=(0, 2))
d3 = customtkinter.CTkEntry(app, width=50, placeholder_text="D3",justify="center")
d3.grid(row=3, column=8, padx=(2, 15))

# BOTONES

botones = customtkinter.CTkFrame(app, fg_color="transparent")
botones.grid(row=4, column=1, columnspan=9, pady=15)

button = customtkinter.CTkButton(
    botones,
    text="Solve",
    command=solve
)
button.grid(row=0, column=0, padx=5)

clear_button = customtkinter.CTkButton(
    botones,
    text="Clear",
    command=clear,
    fg_color="gray40",
    hover_color="gray30"
)
clear_button.grid(row=0, column=1, padx=5)

# MENSAJE DE ERROR

error_label = customtkinter.CTkLabel(
    app,
    text="",
    text_color="red"
)

error_label.grid(row=5, column=1, columnspan=9)

# RESULTADOS

resultado_x = customtkinter.CTkLabel(
    app,
    text="X = ___",
    font=("Arial", 16, "bold")
)

resultado_x.grid(row=1, column=9, padx=10)


resultado_y = customtkinter.CTkLabel(
    app,
    text="Y = ___",
    font=("Arial", 16, "bold")
)

resultado_y.grid(row=2, column=9, padx=10)


resultado_z = customtkinter.CTkLabel(
    app,
    text="Z = ___",
    font=("Arial", 16, "bold")
)

resultado_z.grid(row=3, column=9, padx=10)


# DETERMINANTES

determinantes = customtkinter.CTkFrame(app, fg_color="transparent")
determinantes.grid(row=6, column=1, columnspan=9, pady=(10, 0))

det_label = customtkinter.CTkLabel(determinantes, text="Δ = ___", font=("Arial", 14, "bold"))
det_label.grid(row=0, column=0, padx=12)

det_x_label = customtkinter.CTkLabel(determinantes, text="Δx = ___", font=("Arial", 14, "bold"))
det_x_label.grid(row=0, column=1, padx=12)

det_y_label = customtkinter.CTkLabel(determinantes, text="Δy = ___", font=("Arial", 14, "bold"))
det_y_label.grid(row=0, column=2, padx=12)

det_z_label = customtkinter.CTkLabel(determinantes, text="Δz = ___", font=("Arial", 14, "bold"))
det_z_label.grid(row=0, column=3, padx=12)


app.mainloop()