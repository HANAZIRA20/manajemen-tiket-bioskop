# menu_main.py

from tambah import tambah
from hapus import hapus
from update import update
from lihat import lihat

def menu():
    while True:
        print("\n===== MANAJEMEN TIKET BIOSKOP =====")
        print("1. Tambah")
        print("2. Hapus")
        print("3. Update harga")
        print("4. Lihat daftar")
        print("0. Keluar")

        pilih = input("Pilih menu (0-4): ")
        if pilih == "1":
            tambah()
        elif pilih == "2":
            hapus()
        elif pilih == "3":
            update()
        elif pilih == "4":
            lihat()
        elif pilih == "0":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()