'''
~ Constructor adalah method special yang otomatis dipanggil saat object dibuat
~ Dalam python, constructor adalah method __init__()
~ Constructor digunakan untuk initialize (setup awal) dengan data yang diperlukan
'''

# class
class Mahasiswa:
    nim = 0
    nama = ""
    
    # method
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        
# object 
mhs = Mahasiswa(1231, "Ahmad")

print(f"Nama: {mhs.nama}")
print(f"Nim: {mhs.nim}")
print()

'''
[Constructor dengan Validasi]
~ Salah satu keuntungan menggunakan constructor adalah, kita bisa menambahkan validasi saat object pertama kali dibuat secara otomatis
~ Contohnya: Misal kita bisa cek nilai parameter, jika tidak valid, kita bisa raise error
'''
class BankAccount:
    no = ""
    saldo = 0
    
    def __init__(self, no, saldo):
        if saldo < 0:
            raise ValueError("Saldo anda tidak mencukupi")
        
        self.no = no
        self.saldo = saldo
        
ahmad = BankAccount(123123, 1000)
# malik = BankAccount(123112, -1000)

print(f"Saldo Ahmad: Rp {ahmad.saldo}")
# print(malik.saldo)
print()

'''
[Method __str__() - String Representation]
~ Method __str__() menentukan bagaimana object ditampilkan sebagai string
'''
class Siswa:
    nis = 0
    nama = ""
    
    def __init__(self, nis, nama):
        self.nama = nama
        self.nis = nis
        
    def __str__(self):
        return f"Siswa dengan nis = {self.nis} dan nama = {self.nama}"
    
    '''
        [Method untuk Object Comparison]
        ~ Method __eq__() - Equality, bisa digunakan untuk membandingkan object dengan object lainnya
        ~ Saat kita menggunakan operator pembandingan ==, maka method ini yang akan dipanggil
    '''
    def __eq__(self, other):
        return self.nis == other.nis and self.nama == other.nama
        
# harus panggil setup manual
siswa = Siswa(834294, "Ahmad")
print(f"Info {siswa}")
print()

# Object Comparison
murid1 = Siswa(12345, "Ahmad")
murid2 = Siswa(12345, "Ahmad")
print(murid1 == murid2)

'''
[Method Comparison Lainnya]
~ Selain __eq__(self, other), kita juga bisa membuat operator  perbandingan yang lain
~ __lt__(self, other) untuk < (kurang dari)
~ __gt__(self, other) untuk > (lebih dari)
~ __le__(self, other) untuk <= (kurang dari sama dengan)
~ __ge__(self, other) untuk >= (lebih dari sama dengan)
~ __ne__(self, other) untuk != (tidak sama dengan)

'''

