def determinante(matriz):
    restas = ((matriz[2][0] * matriz[1][1] * matriz[0][2]) + (matriz[2][1] * matriz[1][2] * matriz[0][0]) + (matriz[2][2] * matriz[1][0] * matriz[0][1]))
    sumas = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + (matriz[0][1] * matriz[1][2] * matriz[2][0]) + (matriz[0][2] * matriz[1][0] * matriz[2][1])
    return sumas - restas

def cramer(matriz, d):

    Det = determinante(matriz)


    matrizx = [
        [d[0], matriz[0][1], matriz[0][2]],
        [d[1], matriz[1][1], matriz[1][2]],
        [d[2], matriz[2][1], matriz[2][2]]
    ]

    matrizy = [
        [matriz[0][0], d[0], matriz[0][2]],
        [matriz[1][0], d[1], matriz[1][2]],
        [matriz[2][0], d[2], matriz[2][2]],
    ]

    matrizz = [
        [matriz[0][0], matriz[0][1], d[0]],
        [matriz[1][0], matriz[1][1], d[1]],
        [matriz[2][0], matriz[2][1], d[2]],
    ]

    Dx = determinante(matrizx)
    Dy = determinante(matrizy)
    Dz = determinante(matrizz)

    if Det == 0:
        return Det, Dx, Dy, Dz, None

    x = Dx / Det
    y = Dy / Det
    z = Dz / Det

    return Det, Dx, Dy, Dz, (x, y, z)