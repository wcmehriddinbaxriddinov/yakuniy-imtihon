import json

try:
    with open("inventar.json", "r") as file:
        kitoblar = json.load(file)

    natija = []
    for kitob in kitoblar:
        mavjud = kitob["jami"] - kitob["band"]
        natija.append({"nom": kitob["nom"], "mavjud": mavjud})
        print(f"{kitob['nom']}: {mavjud} ta mavjud")

    with open("mavjud_kitoblar.json", "w") as file:
        json.dump(natija, file, indent=4)

    print(f"{len(natija)} ta yozuv saqlandi.")

except FileNotFoundError:
    print("Xato: inventar.json fayli topilmadi")
except json.JSONDecodeError:
    print("Xato: fayl tarkibi noto'g'ri JSON formatida")
except KeyError as xato:
    print(f"Xato: yozuvda {xato} kaliti yo'q")