class TampilMahasiswa:
    @staticmethod
    def tampilkan_semua(mahasiswa_list):
        if len(mahasiswa_list) == 0:
            print("Tidak ada data mahasiswa.")
        else:
            for mahasiswa in mahasiswa_list:
                print(mahasiswa)

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(mahasiswa)
        else: 
            print("Mahasiswa tidak ditemukan.")
            
             