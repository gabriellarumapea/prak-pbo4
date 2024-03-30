class Hewan:
    def __init__(self, nama, jenis_kelamin):
        self.nama = nama
        self.jenis_kelamin = jenis_kelamin

    def bersuara(self):
        pass

    def makan(self):
        pass

    def minum(self):
        print(f"{self.nama} sedang minum air")

class Kucing(Hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)

    def bersuara(self):
        print(f"Kucing {self.nama} bersuara: Meong!")

    def makan(self):
        print(f"Kucing {self.nama} sedang makan: tulang")

class Anjing(Hewan):
    def __init__(self, nama, jenis_kelamin):
        super().__init__(nama, jenis_kelamin)

    def bersuara(self):
        print(f"Anjing {self.nama} bersuara: Guk Guk!")

    def makan(self):
        print(f"Anjing {self.nama} sedang makan: tulang")

nama_hewan1 = input("Hewan1: ")
jenis_kelamin_hewan1 = input("JK: ")
nama_hewan2 = input("Hewan2: ")
jenis_kelamin_hewan2 = input("JK: ")

hewan1 = Kucing(nama_hewan1, jenis_kelamin_hewan1)
hewan2 = Anjing(nama_hewan2, jenis_kelamin_hewan2)

print(hewan1.nama) 
print(hewan2.nama) 

hewan1.bersuara()
hewan1.makan()
hewan2.bersuara()
hewan2.makan()
