import requests

ruxsat_etilgan = ["mp3", "mp4", "pdf", "png", "jpg", "jpeg", "webp"]

url = input("Fayl havolasini kiriting: ")

fayl_nomi = url.split("?")[0].split("/")[-1]
kengaytma = fayl_nomi.split(".")[-1].lower()

if kengaytma not in ruxsat_etilgan:
    print(
        f"Xatolik: Bu fayl formati qo'llab-quvvatlanmaydi!\n" \
        f"Ruxsat etilgan formatlar: {', '.join(ruxsat_etilgan)}"
    )
else:
    print(f"Fayl turi: {kengaytma.upper()}")
    print("Yuklab olinmoqda...")

    data = requests.get(url)

    if data.status_code == 200:
        with open(f"downloads/{fayl_nomi}", "wb") as file:
            file.write(data.content)
        print(
            f"Fayl muvaffaqiyatli yuklandi!\n" \
            f"Saqlangan fayl: downloads/{fayl_nomi}"
        )
    else:
        print(
            f"Faylni yuklab bo'lmadi!\n" \
            f"URL manzilni tekshiring yoki fayl mavjud emas."
        )