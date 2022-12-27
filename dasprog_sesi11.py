print("="*30 )
print('PROGRAM MENGHITUNG LUAS')
print('='*30)
print('1).luas segitiga\n2).luas persegi panjang \n3).keliling persegi panjang ')


def luas_segitiga ():
    print('='*30,'PROGRAM LUAS SEGITIGA','='*30)
    alas = float(input('masukan nilai alas\t = '))
    tinggi = float(input('masukann nilai tinggi \t= '))
    luas = 1/2 * alas * tinggi
    print('luas segitiga adalah = ',luas )

def luas_persegi_panjang():
    print('='*30,'PROGRAM PERSEGI PANJANG','='*30)
    panjang = int(input('masuknan nilai panjang\t = '))
    lebar = int(input('masukan nilai lebar \t= '))
    l = panjang * lebar 
    print('luas persegi panjang adaah = ',l)

def keliling_persegi_panjang():
    print('='*30,'KELILING PERSEGI PANJANG','='*30)
    panjang = int(input('masukan nilai panjang \t = '))
    lebar = int(input('masukan nilai lebar\t = '))
    keliling = panjang + lebar + panjang + lebar
    print('keliling persegi panjang adalah \t= ',keliling)
    
while True:
  
    user = input('masukan angka untuk masuk program  = ')
   
    if (user == '1'):
        luas_segitiga()
    elif(user == '2'):
        luas_persegi_panjang()
    elif(user == '3'):
        keliling_persegi_panjang()
    elif(user == 'Y'):
        user
    elif(user == 'N'):
        print('program selesai ')
        break
    else:
        print('masukan kode yang benar')