from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import TampilMahasiswa

def tampilkan_menu():
    print("\n=== MENU UTAMA ===")
    print("1. Tambah Mahasiswa")
    print("2. Hapus Mahasiswa")
    print("3. Cari Mahasiswa")
    print("4. Ubah Mahasiswa")
    print("5. Tampilkan Semua Mahasiswa")
    print("0. Keluar")

def main():
    data_mahasiswa = DataMahasiswa()
    
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_data_mahasiswa()
            mahasiswa = Mahasiswa(nim, nama, jurusan)
            data_mahasiswa.tambah_mahasiswa(mahasiswa)
            print("Mahasiswa berhasil ditambahkan.")
        
        elif pilihan == "2":
            nim = input("Masukkan NIM mahasiswa yang akan dihapus: ")
            if data_mahasiswa.hapus_mahasiswa(nim):
                print("Mahasiswa berhasil dihapus.")
            else:
                print("Mahasiswa tidak ditemukan.")
        
        elif pilihan == "3":
            nim = input("Masukkan NIM mahasiswa yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            TampilMahasiswa.tampilkan_detail(mahasiswa)
        
        elif pilihan == "4":
            nim = input("Masukkan NIM mahasiswa yang akan diubah: ")
            nama_baru = input("Masukkan nama baru: ")
            jurusan_baru = input("Masukkan jurusan baru: ")
            if data_mahasiswa.ubah_mahasiswa(nim, nama_baru, jurusan_baru):
                print("Data mahasiswa berhasil diubah.")
            else:
                print("Mahasiswa tidak ditemukan.")
        
        elif pilihan == "5":
            mahasiswa_list = data_mahasiswa.tampilkan_semua()
            TampilMahasiswa.tampilkan_semua(mahasiswa_list)
        
        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
