#!/usr/bin/env python
# coding: utf-8

# In[2]:


nim_mhs = []
uts_mhs = []
uas_mhs = []
total_mhs = []
grade_mhs = []
keterangan_mhs = []
jumlah_data = int(input("Masukan Jumlah Data Mahasiswa: "))

for no in range(jumlah_data):
    print("Data Ke - ", str(i+1))
    NIM = input("Masukan NIM Mahasiswa \t\t : ")
    nim_mhs.append(NIM)
    
    UTS = int(input("Masukan Nilai UTS Mahasiswa \t : ")) 
    uts_mhs.append(UTS)
    
    UAS = int(input("Masukan Nilai UAS Mahasiswa \t : "))
    uas_mhs.append(UAS)
    
    TOTAL = (UTS + UAS)/2
    total_mhs.append(TOTAL)
    
    if 90 <= TOTAL <= 100:
        grade = "A"
        grade_mhs.append(grade)
    elif 80 <= TOTAL <= 89:
        grade = "B"
        grade_mhs.append(grade)
    elif 70 <= TOTAL <= 79:
        grade = "B+"
        grade_mhs.append(grade)
    elif 60 <= TOTAL <= 69:
        grade = "C+"
        grade_mhs.append(grade)
    elif 50 <= TOTAL <= 59:
        grade = "C"
        grade_mhs.append(grade)
    elif 40 <= TOTAL <= 49:
        grade = "D"
        grade_mhs.append(grade)
    elif 30 <= TOTAL <= 39:
        grade = "E"
        grade_mhs.append(grade)
    elif 0 <= TOTAL <= 29:
        grade = "F"
        grade_mhs.append(grade)
        
    if grade in "ABB+CC+":
        keterangan_mhs.append("Lulus")
    if grade in "DEF":
        keterangan_mhs.append("Tidak Lulus")
        
print("="*100)
print("NIM \t\t Nilai UTS \t Nilai UAS \t Total \t\t Grade \t Keterangan")
print("="*100)
for i in range(jumlah_data):
    print(nim_mhs[i], "\t", uts_mhs[i], "\t\t", uas_mhs[i], "\t\t", total_mhs[i], "\t\t", grade_mhs[i], "\t", keterangan_mhs[i])
    print("_"*100)
print("="*100)


# In[3]:


daftar_huruf = []

for no in range(10):
    huruf = input(f"ketikan huruf ke-{no+1}: ").lower()
    if len(huruf) == 1:
        daftar_huruf.append(huruf)
    else:
        print("Maaf input salah! Cukup 1 huruf setiap baris. Program ditutup")
        break
    no += 1

vokal = 0  
konsonan = 0
 
for i in range(len(daftar_huruf)):
    if daftar_huruf[i] in "aiueo":
        vokal += 1
    else:
        konsonan += 1
        
print(f"Jadi, huruf vokal ada {vokal} dan huruf konsonan ada {konsonan}.")


# In[ ]:




