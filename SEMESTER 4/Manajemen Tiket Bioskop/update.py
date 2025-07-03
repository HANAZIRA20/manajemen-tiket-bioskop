# update.py
from daftar import daftar_film

def update():
    print("\n=== UBAH DATA FILM ===")
    # Menampilkan daftar film yang ada
    for f in daftar_film:
        print(f'{f["id"]}. {f["judul"]} ({f["genre"]}) - Rp{f["harga"]:,}'.replace(",", "."))
    
    try:
        # Meminta ID film yang akan diubah
        id_edit = int(input("\nMasukkan ID film yang ingin diubah: "))
        
        # Mencari film berdasarkan ID
        for film in daftar_film:
            if film["id"] == id_edit:
                # Meminta input untuk nama baru
                judul_baru = input(f"Judul baru (saat ini: {film['judul']}): ")
                
                # Meminta input untuk harga baru
                harga_baru_str = input(f"Harga baru (saat ini: Rp{film['harga']:,}): ".replace(",", "."))
                harga_baru = int(harga_baru_str.replace(".", ""))
                
                # Memperbarui nama dan harga film
                film["judul"] = judul_baru
                film["harga"] = harga_baru
                
                print("\n✅ Data film berhasil diubah.")
                return # Keluar dari fungsi setelah update berhasil

        # Pesan ini akan tampil jika loop selesai tanpa menemukan ID
        print("ID film tidak ditemukan.")

    except ValueError:
        # Menangani error jika input bukan angka
        print("Input salah. Pastikan ID dan harga berupa angka.")
    except Exception as e:
        # Menangani error tak terduga lainnya
        print(f"Terjadi kesalahan: {e}")
