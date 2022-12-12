from typing import List


#nomor1a
list = [456, 700, 200, 1000, 2000]
print("Nilai terbesar dari list adalah : ", max(list))

print("========================================")

#nomor1b
list = [456, 700, 200, 1000, 2000]
print("Nilai terkecil dari list adalah : ", min(list))

print("========================================")

#nomor1c
list = ["a", "b", "c", "d"]
list.append("e");
print("List terbaru : ", list)

print("========================================")

#nomor2a
tup = ("g","a", "n", "t", "e", "n", "g")
for x in ("g","a", "n", "t", "e", "n", "g"): print(x, end= '')
print(tup)

print("========================================")

#nomor2b
tup = (1, 2, 3, 5, 9, 10)
print("Nilai tuple terbesar : ", max(tup))

print("========================================")

#nomor2c
tup = (1, 2, 3, 5, 9, 10)
print("Nilai tuple terkecil : ", min(tup))

print("========================================")


#nomor3
dict = {"Name": "Ajeng Miranti", "Kelas": "TI22J", "Prodi": "Teknik Informatika"}
dict["Prodi"] = "TI";

print(dict)

print("========================================")