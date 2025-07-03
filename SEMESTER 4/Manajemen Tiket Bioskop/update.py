# update.py
from daftar import daftar_film

def update():
    print("\n=== DAFTAR FILM ===")
    for f in daftar_film:
        print(f'{f["id"]}. {f["judul"]} ({f["genre"]}) - Rp{f["harga"]:,}'.replace(",", "."))
    try:
        id_edit = int(input("ID film yang ingin diubah harganya: "))
        for film in daftar_film:
            if film["id"] == id_edit:
                harga_baru = int(input(f"Harga baru (harga saat ini Rp{film['harga']:,}): ").replace(".", ""))
                film["harga"] = harga_baru
                print("Harga diubah.")
                return
        print("ID tidak ditemukan.")
    except:
        print("Input salah.")