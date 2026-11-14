log = " hall-a, HALL-B, hall-a, , hall-c, HALL-B, hall-a "

matn = []
for soz in log.split(","):
    soz = soz.strip()
    if soz != "":
        matn.append(soz.upper())

noyob = set(matn)

print(
    f"Tozalangan: {', '.join(matn)}\n" \
    f"Noyob bo'limlar: {len(noyob)}"
)