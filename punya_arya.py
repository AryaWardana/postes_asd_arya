#nama : Arya wahyu wardana
#nim  : 2209116075
#kelas: Sistem Informasi
from prettytable import PrettyTable


class soundclound:
    def __init__(self, Nama_lagu, Nama_penyanyi, Durasi):
        self.Nama_lagu = Nama_lagu
        self.Nama_penyanyi = Nama_penyanyi
        self.Durasi = Durasi
        self.next = None


class SoundcloundLinkedList:
    def __init__(self):
        self.head = None

    def tambah_Lagu(self, Nama_lagu, Nama_penyanyi, Durasi):
        new_soundclound = soundclound(Nama_lagu, Nama_penyanyi, Durasi)

        if not self.head:
            self.head = new_soundclound
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_soundclound


    def tampilkan_Daftar_lagu(self):
        if not self.head:
            print("Tidak ada nama lagu yang terdaftar.")
        else:
            current = self.head
            table = PrettyTable(["Nama lagu", "Nama penyanyi", "Durasi"])
            while current:
                table.add_row([current.Nama_lagu, current.Nama_penyanyi, current.Durasi])
                current = current.next
            print(table)

    def cari_Daftar_lagu(self, Nama_lagu):
        current = self.head
        while current is not None:
            if current.Nama_lagu == Nama_lagu:
                return current
            current = current.next
        return None


    def hapus_daftar_lagu(self, Nama_lagu):
        current = self.head
        if current and current.Nama_lagu == Nama_lagu:
            self.head = current.next
            current = None
            print("Nama lagu berhasil dihapus")
            return
        prev = None
        while current and current.Nama_lagu != Nama_lagu:
            prev = current
            current = current.next
        if current is None:
            print("Daftar lagu dengan nama tersebut tidak ditemukan.")
            return
        prev.next = current.next
        current = None
        print("Nama lagu berhasil dihapus!")



def Menu():
    print("""
    |========================================|
    |---------------SOUNDCLOUND--------------|
    |========================================|
    |1. Tambah lagu                          |
    |2. Tampilkan daftar lagu                |
    |3. Cari daftar lagu                     |
    |4. Hapus daftar lagu                    |
    |5. Keluar                               |
    |========================================|""")


Menu()
listt = SoundcloundLinkedList()

while True:
    output = input("Masukan pilihan anda: ")

    if output == "1":
        Nama_lagu = input("Masukan nama lagu          : ")
        Nama_penyanyi = input("Masukan nama penyanyi      : ")
        Durasi = input("Masukan durasi  : ")
        listt.tambah_Lagu(Nama_lagu, Nama_penyanyi, Durasi)
        print("Daftar lagu berhasil ditambahkan!")
    
    elif output == "2":
        listt.tampilkan_Daftar_lagu()

    elif output == "3":
        Nama_lagu = input("Masukan nama lagu yang ingin dicari: ")
        soundclound = listt.cari_Daftar_lagu(Nama_lagu)
        if soundclound:
            print(f"daftar lagu dengan nama {Nama_lagu} ditemukan")
            print(f"Nama lagu: {soundclound.Nama_lagu}")
            print(f"Nama penyanyi : {soundclound.Nama_penyanyi}")
            print(f"Durasi : {soundclound.Durasi}")
        else:
            print(f"daftar lagu dengan nama {Nama_lagu} tidak ditemukan.")



    elif output == "4":
        listt.tampilkan_Daftar_lagu()
        Nama_lagu = input("Masukan Nama lagu  yang ingin dihapus: ")
        soundclound = listt.cari_Daftar_lagu(Nama_lagu)
        if soundclound:
            listt.hapus_daftar_lagu(Nama_lagu)
        else:
            print(f"daftar lagu dengan Nama {Nama_lagu} tidak ditemukan.")

    elif output == "5":
        exit()




