# lihat.py
from daftar import daftar_film

def lihat():
    print("\n=== DAFTAR FILM ===")
    if not daftar_film:
        print("Belum ada film.")
    for f in daftar_film:
        print(f'{f["id"]}. {f["judul"]} ({f["genre"]}) - Rp{f["harga"]:,}'.replace(",", "."))