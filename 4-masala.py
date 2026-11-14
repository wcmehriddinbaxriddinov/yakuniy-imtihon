xizmatlar = {"diagnostika": 50000, "tozalash": 80000,
             "sozlash": 40000, "almashtirish": 120000}

def hisobla(*args, **kwargs):
    mijoz = kwargs.get("mijoz", "Noma'lum")
    foiz = kwargs.get("chegirma", 0)
    jami = 0
    for nom in args:
        if nom in xizmatlar:
            jami += xizmatlar[nom]
        else:
            print(f"Ogohlantirish: {nom} xizmati topilmadi")
    chegirma = jami * foiz // 100
    tolov = jami - chegirma
    print(
        f"Mijoz: {mijoz}\n" \
        f"Xizmatlar jami: {jami} so'm\n" \
        f"Chegirma: {chegirma} so'm\n" \
        f"To'lov: {tolov} so'm"
    )

hisobla("diagnostika", "tozalash", "sozlash", mijoz="Nodira", chegirma=10)