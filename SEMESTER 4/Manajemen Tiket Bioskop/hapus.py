# hapus.py
from daftar import daftar_film

def hapus():
    print("\n=== DAFTAR FILM ===")
    for f in daftar_film:
        print(f'{f["id"]}. {f["judul"]} ({f["genre"]}) - Rp{f["harga"]:,}'.replace(",", "."))
    try:
        id_hapus = int(input("ID yang ingin dihapus: "))
        for f in daftar_film:
            if f["id"] == id_hapus:
                daftar_film.remove(f)
                print("Film dihapus.")
                return
        print("ID tidak ditemukan.")
    except:
        print("Input tidak valid.")