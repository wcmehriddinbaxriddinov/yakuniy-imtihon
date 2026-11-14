haroratlar = [-20, -19, -17, -16, -18, -21, -15, -14, -20]

xavf = 0
yigindi = 0

for harorat in haroratlar:
    yigindi += harorat
    if harorat > -18:
        xavf += 1

ortacha = yigindi / len(haroratlar)

print(
    f"Xavfli haroratlar: {xavf} ta\n" \
    f"O'rtacha haroratlar: {ortacha:.2f} C"
)