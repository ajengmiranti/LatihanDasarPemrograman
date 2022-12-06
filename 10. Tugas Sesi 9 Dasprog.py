print("Authorized By : Ajeng Miranti")

print('==== Program Menentukan Nilai Mahasiswa ====')
import array as myarr
lulus = ['A','B','C','B+','C+']

list_nilai =[9]
jumlah_mahasiswa = int(input("Berapa Banyak Jumlah mahasiswa : "))
data = int(input("data ke - "))
nim = input("Masukkan NIM : ")
matakuliah = input("Masukkan Mata Kuliah : ")
semester = input("Masukkan Semester : ")
nilai_UTS = float(input("Masukkan Nilai UTS : "))
nilai_UAS = float(input("Masukkan Nilai UAS : "))
print("=============================================================")
print("NIM            UTS     UAS     Total  Grade     Keterangan")
print("=============================================================")

total_nilai = ((nilai_UTS) + (nilai_UAS)) / (2)

if total_nilai >= 90:
  Grade = "A"
elif total_nilai >= 80:
  Grade = "B+"
elif total_nilai >= 70:
  Grade = "B"
elif total_nilai >= 60:
  Grade = "C+"
elif total_nilai >= 50:
  Grade = "C"
elif total_nilai >= 40:
  Grade = "D"
elif total_nilai >= 30:
  Grade = "E"
elif total_nilai < 29:
  Grade = "F"

if Grade in lulus:
    print(nim,end='\t')
    print(nilai_UTS,end='\t')
    print(nilai_UAS,end='\t')
    print(total_nilai,end='\t')
    print(Grade,end='\t')
    print('LULUS',end='\t')
    

else :
    print(nim,end='\t')
    print(nilai_UTS,end='\t')
    print(nilai_UAS,end='\t')
    print(total_nilai,end='\t')
    print(Grade,end='\t')
    print('TIDAK LULUS',end='\t')