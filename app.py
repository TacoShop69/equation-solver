import streamlit as st
from PIL import Image
from backend import cramer

st.set_page_config(page_title="Equation System Solver", page_icon=Image.open("icon.ico"))
st.title("Equation System Solver for 3 unknowns")
st.caption("Each row is:  A·x + B·y + C·z = D")

CAMPOS = [f"{col}{fila}" for fila in (1, 2, 3) for col in "ABCD"]

st.session_state.setdefault("error", "")
st.session_state.setdefault("resultado", None)


def fmt(n):
    """Entero si es entero; si no, redondeado a 4 decimales."""
    n = round(n, 4)
    if n == int(n):
        return str(int(n))
    return str(n)


def ecuacion(fila, d):
    a, b, c = fila
    return f"{fmt(a)}x + {fmt(b)}y + {fmt(c)}z = {fmt(d)}"


def solve():
    st.session_state["error"] = ""
    st.session_state["resultado"] = None

    try:
        valores = {
            k: float(st.session_state[k].replace(",", "."))
            for k in CAMPOS
        }
    except ValueError:
        st.session_state["error"] = "Enter a valid number in every field"
        return

    matriz = [[valores[f"{c}{i}"] for c in "ABC"] for i in (1, 2, 3)]
    d = [valores[f"D{i}"] for i in (1, 2, 3)]

    Det, Dx, Dy, Dz, solucion = cramer(matriz, d)

    st.session_state["resultado"] = {
        "Det": Det, "Dx": Dx, "Dy": Dy, "Dz": Dz, "solucion": solucion,
        "matriz": matriz, "d": d
    }

    if solucion is None:
        st.session_state["error"] = "No unique solution (determinant is 0)"


def clear():
    for k in CAMPOS:
        st.session_state[k] = ""
    st.session_state["error"] = ""
    st.session_state["resultado"] = None


# Input grid (3 rows x 4 columns)
for fila in (1, 2, 3):
    columnas = st.columns(4)
    for columna, letra in zip(columnas, "ABCD"):
        columna.text_input(
            f"{letra}{fila}",
            key=f"{letra}{fila}",
            placeholder=f"{letra}{fila}",
            label_visibility="collapsed",
        )

# Buttons
b1, b2, _ = st.columns([1, 1, 3])
b1.button("Solve", on_click=solve, type="primary")
b2.button("Clear", on_click=clear)

# Messages and results
if st.session_state["error"]:
    st.error(st.session_state["error"])

res = st.session_state["resultado"]
if res is not None:
    st.subheader("Entered System")
    for fila, valor in zip(res["matriz"], res["d"]):
        st.write(ecuacion(fila, valor))

    st.subheader("Determinants")
    columnas = st.columns(4)
    nombres = ("Δ", "Δx", "Δy", "Δz")
    valores = (res["Det"], res["Dx"], res["Dy"], res["Dz"])
    for columna, nombre, valor in zip(columnas, nombres, valores):
        columna.markdown(
            f"<small>{nombre}</small><br><span style='font-size:2rem'>{fmt(valor)}</span>",
            unsafe_allow_html=True,
        )
    if res["solucion"] is not None:
        st.subheader("Solution")
        for nombre, numerador, valor in zip(
            "xyz", (res["Dx"], res["Dy"], res["Dz"]), res["solucion"]
        ):
            st.success(f"{nombre} = {fmt(numerador)} / {fmt(res['Det'])} = {fmt(valor)}")