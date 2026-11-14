import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]

ortacha = sum(sarf) / len(sarf)

ortacha_royxat = []
for i in range(len(sarf)):
    ortacha_royxat.append(ortacha)

yuqori_kunlar = []
yuqori_sarf = []
for i in range(len(sarf)):
    if sarf[i] > ortacha:
        yuqori_kunlar.append(kunlar[i])
        yuqori_sarf.append(sarf[i])

print(f"O'rtacha sarf: {ortacha:.2f} kWh")
print(f"O'rtachadan yuqori kunlar: {', '.join(yuqori_kunlar)}")

plt.plot(kunlar, sarf, color="blue", marker="o", label="Kunlik sarf")
plt.plot(kunlar, ortacha_royxat, color="green", linestyle="--", label="O'rtacha sarf")
plt.plot(yuqori_kunlar, yuqori_sarf, "rs", label="O'rtachadan yuqori")

plt.title("Haftalik elektr sarfi")
plt.xlabel("Kunlar")
plt.ylabel("Sarf (kWh)")
plt.legend()
plt.grid(axis="y", linestyle="--")

plt.savefig("energiya_tahlili.png")
print("Grafik: energiya_tahlili.png")
plt.show()