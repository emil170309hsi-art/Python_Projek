# Latihan 1: Sintaks Tuple
hari = ("Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu")
angka_ganjil = (7,)

print(hari, type(hari))
print(angka_ganjil, type(angka_ganjil))

# Latihan 2: Immutability
koordinat_awal = (10, 20)
koordinat_baru = (koordinat_awal[0], 25)

print("Koordinat awal:", koordinat_awal)
print("Koordinat baru:", koordinat_baru)

# Latihan 3: Tuple Assignment
warna = (255, 165, 0)
red, green, blue = warna

print("Red:", red)
print("Green:", green)
print("Blue:", blue)

# Latihan 4: Dictionary dengan Tuple Key
papan_catur = {}

papan_catur[(1, 'a')] = "Benteng Putih"
papan_catur[(1, 'e')] = "Raja Putih"
papan_catur[(8, 'h')] = "Benteng Hitam"
papan_catur[(8, 'd')] = "Menteri Hitam"

print("Bidak di (1, 'a'):", papan_catur[(1, 'a')])