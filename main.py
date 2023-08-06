import hashlib

input_teks = input("Masukkan teks yang ingin di-hash: ")
if not input_teks:
    print("Input teks kosong. Tidak ada hash yang dihasilkan.")
else:
    algoritma_hash = ["md5", "sha1", "sha256", "sha512"]   
    for algoritma in algoritma_hash:        
        if algoritma == "md5":
            objek_hash = hashlib.md5()
        elif algoritma == "sha1":
            objek_hash = hashlib.sha1()
        elif algoritma == "sha256":
            objek_hash = hashlib.sha256()
        elif algoritma == "sha512":
            objek_hash = hashlib.sha512()        
        else:
            raise ValueError("Algoritma hash tidak valid")
        objek_hash.update(input_teks.encode())
        hasil_hash = objek_hash.hexdigest()
        print(f"[*] Hasil hash {algoritma.upper()}: {hasil_hash}")
