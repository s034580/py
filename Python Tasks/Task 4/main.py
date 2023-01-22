# Turimas sąrašas, pvz.:

# canvas = [
#   "abc",
#   "ded"
# ]

# Sukurkite funkciją "addFrame", kuri pridėtų rėmelį ir grąžintų pamodifikuotą sąrašą:

# canvas_with_frame = [
#   "*****"
#   "*abc*",
#   "*ded*",
#   "*****"
# ]

# Pastaba: sąrašas gali ir neturėti nei vieno elemento arba turėtų tusčių elementų. pvz.
# canvas = [] arba canvas = [""]

# Jeigu sąrašas yra tusčias arba visi elementą tušti išmeskite klaidą - "Error: empty canvas provided".
# Beje, sąraše esantis tekstas, gali būti ir skirtingo ilgio. Todėl rėmelis turėtų būti brėžiamas pagal ilgiausią saraše esantį elementą.


def addFrame(canvas):
    if not canvas or all(not row for row in canvas):
        raise ValueError("Error: empty canvas provided")
    max_length = max(len(row) for row in canvas)
    frame = "*" * (max_length + 2)
    canvas = [frame] + ["*" + row + "*" for row in canvas] + [frame]
    return "\n".join(canvas)

canvas = ["abc", "ded"]
canvas_with_frame = addFrame(canvas)
print(canvas_with_frame)
