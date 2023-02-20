import os
import time
import datetime
from tabulate import tabulate

data = {}
#FUNCTION**
def tambah_data(nim,nama,kelas,prodi,lahir):
    """TAMBAH DATA"""
    if (nim in data):
        print("DATA GAGAL DITAMBAHKAN, NIM SUDAH ADA !")
        return False
    else:
        data[nim] = nim,nama,kelas,prodi,lahir
        print("\n\nDATA BERHASIL DITAMBAHKAN!")
    time.sleep(1.2)


def cari(nim):
    cari_data = {}
    for key,value in data.items():
        if (nim in key):
            cari_data[nim] = value
    print(tabulate(cari_data.values(),headers=["Nim","Nama","Kelas","Prodi","Tanggal Lahir"],tablefmt="double_grid",colalign=("left","left","center","left","center")))


def update_data(nim):
    """FUNGSI UPDATE"""
    if (nim in data):
        print("\nDATA YANG AKAN DIUPDATE")
        cari(nim)
    elif (nim =="keluar" or nim == "exit" or nim == "batal"):
        main()
    else :
        print("\n\nDATA TIDAK DITEMUKAN. SILAHKAN COBA LAGI !")
        time.sleep(1.2)
        update_mahasiswa()
    print("\nSILAHKAN MASUKKAN DATA BARU! ")

    while True:
        nama = input("Masukkan Nama\t\t: ").upper()
        if (nama == "KELUAR" or nama == "EXIT" or nama == "BATAL"):
            main()
        elif (nama == ""):
            print("Nama tidak boleh kosong !")
            continue
        else:
            pass
        break

    while True:
        kelas = input("Masukkan Kelas\t\t: ").upper()
        if (kelas == "KELUAR" or kelas == "EXIT" or kelas == "BATAL"):
            main()
        elif (kelas == ""):
            print("Kelas tidak boleh kosong !")
            continue
        else:
            pass
        break

    while True:
        prodi = input("Masukkan Prodi\t\t: ").upper()
        if (prodi == "KELUAR" or prodi == "EXIT" or prodi == "BATAL"):
            main()
        elif (prodi == ""):
            print("Prodi tidak boleh kosong !")
            continue
        else:
            pass
        break

    print("\nTanggal Lahir")

    while True:
        try:
            tahun = int(input("Masukkan Tahun(4 digit)\t: "))
            bulan = int(input("Masukkan Bulan(1-12)\t: "))
            tanggal= int(input("Masukkan Tanggal(1-31)\t: "))
            lahir = datetime.datetime(tahun,bulan,tanggal).strftime("%x")
            break
        except ValueError:
            print("Tahun,bulan, atau tanggal yang anda masukkan tidak valid. Silahkan coba lagi !")
            time.sleep(1.2)

    while True:
        update = input("Apakah anda yakin ingin mengubah data? [y/n]: ").lower()
        if (update == "y"):
            update_masbro(nim,nama,kelas,prodi,lahir)
            while True:
                keluar = input("Keluar[y]: ").lower()
                if (keluar == "y"):
                    main()
                else:
                    continue
        elif (update == "n"):
            print("\nDATA TIDAK JADI DIUPDATE !")
            time.sleep(1.2)

            while True:
                keluar = input("\nKeluar ?[y/update]: ").lower()
                if (keluar == "y"):
                    main()
                elif (keluar == "update"):
                    update_masbro(nim,nama,kelas,prodi,lahir)

                    while True:
                        apakah_keluar = input("Keluar ?[y]").lower()
                        if (apakah_keluar == "y"):
                            main()
                        else:
                            print("Hanya ada opsi [y] !")
                            continue

                else:
                    print("Pilihan tidak tersedia. Silahkan pilih kembali !")
                    break

        else:
            print("Pilihan tidak tersedia !")
            time.sleep(1.2)
            continue


def update_masbro(nim,nama,kelas,prodi,lahir):
    data.update({nim:[nim,nama,kelas,prodi,lahir]})
    print("\n\nDATA BERHASIL DI UPDATE !\n")
    time.sleep(1.2)
    cari(nim)


def hapus_data(nim):
    """HAPUS MAHASISWA"""
    if (nim in data):
        print("\n\nDATA YANG AKAN DIHAPUS")
        cari(nim)
    elif (nim =="keluar" or nim == "exit" or nim == "batal"):
        main()
    else :
        print("\n\nDATA TIDAK DITEMUKAN. SILAHKAN COBA LAGI !")
        time.sleep(1.2)
        hapus_mahasiswa()

    while True:
        delete = input("Apakah anda yakin ingin menghapus data ?[y/n]: ").lower()
        if (delete == "y"):
            del data[nim]
            print("DATA BERHASIL DIHAPUS !")
            time.sleep(1.2)
            main()
        elif (delete == "n"):
            print("DATA TIDAK JADI DIHAPUS !")
            time.sleep(1.2)
            main()
        else :
            print("Pilihan tidak tersedia !")
            time.sleep(1.2)
            continue


def total_mahasiswa():
    siswa = len(data)
    return siswa+1


def tambah_mahasiswa():
    """TAMBAH MAHASISWA"""
    while True:
        os.system("clear")
        print(f"""{'*'*30}\n*{'TAMBAH MAHASISWA':^28}*\n{'*'*30}\n\nKeluar/Exit untuk batal !\n\nMahasiswa {total_mahasiswa()}\n\nData Diri""")
        
        while True:
            nama = input("Masukkan Nama\t\t: ").upper()
            if (nama == "KELUAR" or nama == "EXIT" or nama == "BATAL"):
                main()
            elif (nama == ""):
                print("Nama tidak boleh kosong !")
                continue
            else:
                pass

            break

        while True:
            try:
                nim = int(input("Masukkan NIM\t\t: "))
                break
            except ValueError:
                print("Masukkan Nim dengan angka!")

        while True:
            kelas = input("Masukkan Kelas\t\t: ").upper()
            if (kelas == "KELUAR" or kelas == "EXIT" or kelas == "BATAL"):
                main()
            elif (kelas == ""):
                print("Kelas tidak boleh kosong !")
                continue
            else:
                pass

            break

        while True:
            prodi = input("Masukkan Prodi\t\t: ").upper()
            if (prodi == "KELUAR" or prodi == "EXIT" or prodi == "BATAL"):
                main()
            elif (prodi == ""):
                print("Prodi tidak boleh kosong !")
                continue
            else:
                pass

            break

        print("\nTanggal Lahir")

        while True:
            try:
                tahun = int(input("Masukkan Tahun(4 digit)\t: "))
                bulan = int(input("Masukkan Bulan(1-12)\t: "))
                tanggal= int(input("Masukkan Tanggal(1-31)\t: "))
                lahir = datetime.datetime(tahun,bulan,tanggal).strftime("%x")
                break
            except ValueError:
                print("Tahun,bulan, atau tanggal yang anda masukkan tidak valid. Silahkan coba lagi !")
                time.sleep(1.2)

        tambah_data(str(nim),nama,kelas,prodi,lahir)

        while True:
            pilihan = input("\nIngin menambahkan data lagi?[y/n]: ").lower()
            if (pilihan == "y"):
                break
            elif (pilihan == "n"):
                return main()
            else:
                print("Maaf pilihan tidak tersedia. Silahkan pilih kembali !")
                continue


def lihat_mahasiswa():
    """LIHAT MAHASISWA"""
    os.system("clear")
    print(f"""{'*'*30}\n*{'LIHAT DATA':^28}*\n{'*'*30}""")
    if (len(data) <1):
        print("DATA KOSONG, SILAHKAN TAMBAH DATA TERLEBIH DAHULU !")
    else:
        print(tabulate(data.values(),headers=["Nim","Nama","Kelas","Prodi","Tanggal Lahir"],tablefmt="double_grid",colalign=("left","left","center","left","center")))
   
    keluar = input("Keluar[y]: ").lower()
    if (keluar == "y"):
        main()
    else:
        os.system("clear")
        lihat_mahasiswa()


def hapus_mahasiswa():
    """HAPUS MAHASISWA"""
    os.system("clear")
    print(f"""{'*'*30}\n*{'HAPUS DATA':^28}*\n{'*'*30}\n""")
    hapus_data(input(f"{'Masukkan Nim yang ingin anda Hapus datanya.'.upper()} (Keluar/Exit untuk keluar): ").lower())


def update_mahasiswa():
    """UPDATE MAHASISWA"""
    os.system("clear")
    print(f"""{'*'*30}\n*{'UPDATE MAHASISWA':^28}*\n{'*'*30}\n""")
    update_data(input(f"{'Masukkan Nim yang ingin anda Update datanya.'.upper()} (Keluar/Exit untuk keluar): ").lower())

#Running
def main():  
    while True:
        try:
            os.system("clear")
            print(f"""{'*'*30}\n*{'APLIKASI':^28}*\n*{'CRUD SEDERHANA':^28}*\n*{'*'*28}*
* MENU:{'*':>23}
* 1.Tambah Mahasiswa{'*':>10}
* 2.Lihat Mahasiswa{'*':>11}
* 3.Update Mahasiswa{'*':>10}
* 4.Delete Mahasiswa{'*':>10}
* 5.Exit Program{'*':>14}\n{'*'*30}""")
            menu = int(input("Masukkan Pilihan Anda [1/2/3/4/5]: "))
            if (menu == 1):
                tambah_mahasiswa()
            if (menu == 2):
                lihat_mahasiswa()
            if (menu == 3):
                update_mahasiswa()
            if (menu == 4):
                hapus_mahasiswa()
            if (menu == 5):
                print("\n\nterima kasih sudah menggunakan program saya :)".upper())
                exit()
            else:
                print("Pilihan tidak tersedia. Silahkan pilih kembali !")
                time.sleep(1.2)
            pass
        except ValueError:
            print("Mohon gunakan angka!")
            time.sleep(1.2)

print(main())