import streamlit as st
from backend import cramer

st.set_page_config(page_title="Equation System Solver")
st.title("Equation System Solver for 3 unknowns")

CAMPOS = [f"{col}{fila}" for fila in (1, 2, 3) for col in "ABCD"]

st.session_state.setdefault("error", "")
st.session_state.setdefault("resultado", None)


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

    resultado = cramer(matriz, d)

    if resultado is None:
        st.session_state["error"] = "No unique solution (determinant is 0)"
    else:
        st.session_state["resultado"] = resultado


def clear():
    for k in CAMPOS:
        st.session_state[k] = ""
    st.session_state["error"] = ""
    st.session_state["resultado"] = None


# Input grid: box, label, box, label, box, label, box
ANCHOS = [3, 1, 3, 1, 3, 1, 3]
ETIQUETAS = ("x +", "y +", "z =")

for fila in (1, 2, 3):
    cols = st.columns(ANCHOS, vertical_alignment="center")

    for pos, letra in zip((0, 2, 4, 6), "ABCD"):
        cols[pos].text_input(
            f"{letra}{fila}",
            key=f"{letra}{fila}",
            placeholder=f"{letra}{fila}",
            label_visibility="collapsed",
        )

    for pos, texto in zip((1, 3, 5), ETIQUETAS):
        cols[pos].markdown(
            f"<div style='text-align:center'>{texto}</div>",
            unsafe_allow_html=True,
        )

# Buttons
b1, b2, _ = st.columns([1, 1, 3])
b1.button("Solve", on_click=solve, type="primary")
b2.button("Clear", on_click=clear)

# Messages and results
if st.session_state["error"]:
    st.error(st.session_state["error"])
elif st.session_state["resultado"] is not None:
    x, y, z = st.session_state["resultado"]
    st.success(f"X = {round(x, 4)}   |   Y = {round(y, 4)}   |   Z = {round(z, 4)}")