import csv

jami = {}

try:
    with open("qatnov.csv", "r", encoding="utf-8") as file:
        oqish = csv.DictReader(file)
        for qator in oqish:
            yonalish = qator["yonalish"]
            yolovchi = int(qator["yolovchi"])
            if yonalish in jami:
                jami[yonalish] += yolovchi
            else:
                jami[yonalish] = yolovchi

    for yonalish in jami:
        print(f"{yonalish}-yo‘nalish: {jami[yonalish]} nafar")

except FileNotFoundError:
    print("Xato: qatnov.csv fayli topilmadi")
except KeyError as xato:
    print(f"Xato: faylda {xato} ustuni yo'q")
except ValueError:
    print("Xato: yo'lovchilar soni son emas")