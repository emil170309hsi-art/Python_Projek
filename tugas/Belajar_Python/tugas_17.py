# Tugas Latihan 1
biodata = {
    "nama": "Muhammad Emil Fikar",
    "umur": 17,
    "hobi": ["ngoding", "membaca", "berenang"],
    "sudah_menikah": False,
}

print(biodata)
print(biodata["nama"])
print(biodata["hobi"][0])

# Tugas Latihan 2
biodata["kota"] = "Bogor"
biodata["umur"] = biodata["umur"] + 1
print(biodata)

# Tugas Latihan 3
# biodata["pekerjaan"]
print(biodata.get("pekerjaan"))
print(biodata.get("pekerjaan", "Pelajar"))

# Tugas Latihan 4
kalimat = input("Masukkan sebuah kalimat: ")
daftar_kata = kalimat.lower().split()

histogram = {}
for kata in daftar_kata:
    histogram[kata] = histogram.get(kata, 0) + 1

print(histogram)