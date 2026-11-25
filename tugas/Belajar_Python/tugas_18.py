# Tugas Latihan 1
harga_buah = {
    "apel": 5000,
    "jeruk": 8500,
    "mangga": 7800,
    "pisang": 3000,
}

total_harga = 0
for buah, harga in harga_buah.items():
    print(f"Harga 1 kg {buah} adalah Rp {harga}")
    total_harga += harga

print(f"Total harga semua buah: Rp {total_harga}")

# Tugas Latihan 2
kontak = {}
kontak["Ibu"] = "081234567890"
kontak["Ayah"] = "081298765432"
kontak["Teman"] = "081355556666"
kontak["Ibu"] = "081211112222"
kontak.pop("Teman")
print(kontak)

# Tugas Latihan 3
produk = {
    "PROD001": {
        "nama": "Keyboard Mechanical",
        "harga": 450000,
        "stok": 12,
    },
    "PROD002": {
        "nama": "Mouse Wireless",
        "harga": 175000,
        "stok": 25,
    },
}

print(produk["PROD002"]["nama"])
print(produk["PROD002"]["harga"])

# Tugas Latihan 4
frekuensi_hari = {}
with open("mbox-short.txt", "r", encoding="utf-8") as file:
    for baris in file:
        if baris.startswith("From "):
            kata = baris.split()
            if len(kata) >= 3:
                hari = kata[2]
                frekuensi_hari[hari] = frekuensi_hari.get(hari, 0) + 1

print(frekuensi_hari)