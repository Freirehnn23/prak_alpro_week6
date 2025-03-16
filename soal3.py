def hitung_ips(jumlah_matkul):
    total_bobot = 0
    total_sks = 0

    for i in range(1, jumlah_matkul + 1):
        print(f"\nMata kuliah ke-{i}:")
        nilai = input("Masukkan nilai (A/B/C/D): ").upper()
        
        if nilai == 'A':
            bobot = 4
        elif nilai == 'B':
            bobot = 3
        elif nilai == 'C':
            bobot = 2
        elif nilai == 'D':
            bobot = 1
        else:
            print("Nilai tidak valid. Harap masukkan A, B, C, atau D.")
            return None
        
        sks = 3  
        total_bobot += bobot * sks
        total_sks += sks

    ips = total_bobot / total_sks
    return ips

jumlah_matkul = int(input("Masukkan jumlah mata kuliah: "))

hasil_ips = hitung_ips(jumlah_matkul)

if hasil_ips is not None:
    print(f"\nIndeks Prestasi Semester (IPS) Anda adalah: {hasil_ips:.2f}")