import customtkinter
import os
from backend import cramer

VERDE_FONDO = "#14532d"
VERDE_TEXTO = "#4ade80"


def fmt(n):
    """Entero si es entero; si no, redondeado a 4 decimales."""
    n = round(n, 4)
    if n == int(n):
        return str(int(n))
    return str(n)


def ecuacion(fila, d):
    a, b, c = fila
    return f"{fmt(a)}x + {fmt(b)}y + {fmt(c)}z = {fmt(d)}"


def limpiar_panel():
    for lbl in eq_labels:
        lbl.configure(text="")
    for lbl in det_valores:
        lbl.configure(text="___")
    for lbl in sol_labels:
        lbl.configure(text="", fg_color="transparent")


def mostrar_error(mensaje):
    error_label.configure(text=mensaje)
    resultado_x.configure(text="X = ___")
    resultado_y.configure(text="Y = ___")
    resultado_z.configure(text="Z = ___")
    limpiar_panel()


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

    # Sistema ingresado
    for lbl, fila, valor in zip(eq_labels, matriz, d):
        lbl.configure(text=ecuacion(fila, valor))

    # Determinantes
    for lbl, valor in zip(det_valores, (Det, Dx, Dy, Dz)):
        lbl.configure(text=fmt(valor))

    if solucion is None:
        error_label.configure(text="No unique solution (determinant is 0)")
        resultado_x.configure(text="X = ___")
        resultado_y.configure(text="Y = ___")
        resultado_z.configure(text="Z = ___")
        for lbl in sol_labels:
            lbl.configure(text="", fg_color="transparent")
        return

    x,y,z = solucion

    resultado_x.configure(text="X = " + fmt(x))
    resultado_y.configure(text="Y = " + fmt(y))
    resultado_z.configure(text="Z = " + fmt(z))

    # Solución paso a paso
    for lbl, nombre, num, valor in zip(sol_labels, "xyz", (Dx, Dy, Dz), solucion):
        lbl.configure(
            text=f"  {nombre} = {fmt(num)} / {fmt(Det)} = {fmt(valor)}",
            fg_color=VERDE_FONDO
        )


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
    limpiar_panel()

    app.focus_set()   # take focus away from any entry
    app.update()      # let Tk process the FocusOut event

    for entry in entradas:
        entry._activate_placeholder()  # force the placeholder back


app = customtkinter.CTk()

app.title("Equation System Solver for 3 unknowns")
ruta_icono = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")
app.after(200, lambda: app.iconbitmap(ruta_icono))
app.geometry("500x650")
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


# PANEL DE RESULTADOS

panel = customtkinter.CTkFrame(app, fg_color="transparent")
panel.grid(row=6, column=1, columnspan=9, sticky="we", padx=20, pady=(10, 15))
panel.grid_columnconfigure((0, 1, 2, 3), weight=1)

# Sistema ingresado
customtkinter.CTkLabel(
    panel, text="Entered System", font=("Arial", 16, "bold")
).grid(row=0, column=0, columnspan=4, sticky="w", pady=(0, 4))

eq_labels = []
for i in range(3):
    lbl = customtkinter.CTkLabel(panel, text="", font=("Arial", 12), anchor="w")
    lbl.grid(row=1 + i, column=0, columnspan=4, sticky="w")
    eq_labels.append(lbl)

# Determinantes
customtkinter.CTkLabel(
    panel, text="Determinants", font=("Arial", 16, "bold")
).grid(row=4, column=0, columnspan=4, sticky="w", pady=(10, 4))

det_valores = []
for col, nombre in enumerate(("Δ", "Δx", "Δy", "Δz")):
    customtkinter.CTkLabel(
        panel, text=nombre, font=("Arial", 11), anchor="w"
    ).grid(row=5, column=col, sticky="w")
    valor_label = customtkinter.CTkLabel(
        panel, text="___", font=("Arial", 22), anchor="w"
    )
    valor_label.grid(row=6, column=col, sticky="w")
    det_valores.append(valor_label)

# Solución
customtkinter.CTkLabel(
    panel, text="Solution", font=("Arial", 16, "bold")
).grid(row=7, column=0, columnspan=4, sticky="w", pady=(10, 4))

sol_labels = []
for i in range(3):
    lbl = customtkinter.CTkLabel(
        panel,
        text="",
        font=("Arial", 12),
        anchor="w",
        text_color=VERDE_TEXTO,
        fg_color="transparent",
        corner_radius=6,
        height=30
    )
    lbl.grid(row=8 + i, column=0, columnspan=4, sticky="we", pady=2)
    sol_labels.append(lbl)


app.mainloop()