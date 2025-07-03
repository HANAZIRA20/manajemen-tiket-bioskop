# tambah.py
from daftar import daftar_film

def tambah():
    judul = input("Judul: ")
    genre = input("Genre: ")
    try:
        harga = int(input("Harga (contoh: 45000): ").replace(".", ""))
        id_baru = max((f["id"] for f in daftar_film), default=0) + 1
        daftar_film.append({"id": id_baru, "judul": judul, "genre": genre, "harga": harga})
        print("Film ditambah.")
    except:
        print("Harga harus berupa angka.")