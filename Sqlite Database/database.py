import sqlite3

con =sqlite3.connect("kütüphane.db")

cursor =con.cursor()
def tablo_olustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplık (isim TEXT,yazar TEXT,yayınevi TEXT,sayfa_sayısı INT)")
    con.commit()#tablodaki verileri güncellemek için

def veri_ekle():
    cursor.execute("Insert into kitaplık Values('istanbul hatırası','ahmet ümit','everest',561)")
    con.commit()

def veri_ekle2(isim,yazar,yayınevi,sayfa_sayısı):
    cursor.execute("Insert into kitaplık Values(?,?,?,?)",(isim,yazar,yayınevi,sayfa_sayısı))
    con.commit()

def verileri_al():
    cursor.execute("Select * From kitaplık")
    liste = cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al2():
    cursor.execute("Select isim,yazar From kitaplık")
    liste =cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_al3(yayınevi):
    cursor.execute("Select * From kitaplık where yayınevi = ? ",(yayınevi,))
    liste=cursor.fetchall()
    print("Kitaplık tablosunun bilgileri...")
    for i in liste:
        print(i)

def verileri_güncelle(eski_yayınevi,yeni_yayınevi):
    cursor.execute("Update kitaplık set yayınevi = ? where yayınevi = ?",(yeni_yayınevi,eski_yayınevi))
    con.commit()

def verileri_sil(yazar):
    cursor.execute("Delete From kitaplık where yazar = ?",(yazar,))
    con.commit()

verileri_sil("Ahmet Ümit")
verileri_al()
con.close()