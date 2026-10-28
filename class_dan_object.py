# class
class Mahasiswa:
    nim = 0
    nama = ""
    
    # method
    def perkenalan(self):
        print(f"Hallo nama saya {self.nama}")
        
    def hello(self, nama):
        print(f"Hallo {nama}, nama saya {self.nama}")
        
# object 
mahasiswa1 = Mahasiswa()
mahasiswa1.nama = "Ahmad Maulana"
mahasiswa1.perkenalan()

mahasiswa2 = Mahasiswa()
mahasiswa2.nama = "Ahmad Maliki"
mahasiswa2.hello("Ahmad Maulana")