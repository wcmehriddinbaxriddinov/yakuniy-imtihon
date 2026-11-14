kodlar = [" UZ-2026-AB1234 ", "UZ-26-AB1234", "UZ-2026-aB1234"]
raqamlar = "0123456789"
harflar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def tekshir(kod):
    if len(kod) != 14:
        return False
    if kod[:3] != "UZ-":
        return False
    for i in kod[3:7]:
        if i not in raqamlar:
            return False
    if kod[7] != "-":
        return False
    for i in kod[8:10]:
        if i not in harflar:
            return False
    for i in kod[10:]:
        if i not in raqamlar:
            return False
    return True
for kod in kodlar:
    kod = kod.strip()
    if tekshir(kod):
        print(f"{kod}: yaroqli | yil: {kod[3:7]} | seriya: {kod[8:]}")
    else:
        print(f"{kod}: yaroqsiz")