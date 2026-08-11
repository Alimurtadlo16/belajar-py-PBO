class SaldoMinimalEror(Exception):
    def __init__(self, pesan="Penarikan gagal!!! Batas minimal saldo tersisa adalah Rp50.000"):
        self.pesan = pesan
        super().__init__(self.pesan)

class PenarikanNegatifEror(Exception):
    def __init__(self, pesan="Penarikan gagal!!! Jumlah penarikan harus lebih dari Rp0"):
        self.pesan = pesan
        super().__init__(self.pesan)

class SetoranNegatifEror(Exception):
    def __init__(self, pesan="Setoran gagal!!! Jumlah setoran harus lebih dari Rp0"):
        self.pesan = pesan
        super().__init__(self.pesan)

class AkunTerblokirEror(Exception):
    def __init__(self, pesan="AKUN ANDA TERBLOKIR! Anda telah salah memasukkan PIN sebanyak 3 kali."):
        self.pesan = pesan
        super().__init__(self.pesan)

class RekeningBank:
    def __init__(self, pemilik, saldoAwal, pinAwal="123456"):
        self.pemilik = pemilik
        self.saldo = saldoAwal
        self.pin = pinAwal
        self.saldoMinimal = 50000

    def verifikasiPIN(self):
        kesempatan = 3
        while kesempatan > 0:
            input_pin = input(f"Masukkan PIN ATM Anda {kesempatan}): ")
            if input_pin == self.pin:
                print("✓ PIN Benar! Akses diberikan.")
                return True
            else:
                kesempatan -= 1
                print("✗ PIN Salah! Silakan coba lagi. atau hubungi call center jika lupa pin anda")
        raise AkunTerblokirEror()

    def cekSaldo(self):
        print(f"\n=== INFORMASI REKENING ===")
        print(f"Pemilik Akun : {self.pemilik}")
        print(f"Saldo Saat Ini: Rp{self.saldo:,}")
        print(f"Batas Minimal : Rp{self.saldoMinimal:,}")
        print(f"==========================")

    def hubungiCallCenter(self):
        print(f"\n=============================================")
        print(f"          CALL CENTER BANK BRI           ")
        print(f"=============================================")
        print(f"• Telepon Darurat   : 1500017 (24 Jam)")
        print(f"• WhatsApp Resmi    : 0812-1214-017")
        print(f"• X / Twitter       : @kontakBRI")
        print(f"• Instagram         : bankbri_id")
        print(f"• Facebook          : BANK BRI")
        print(f"• Website           : www.bri.co.id")
        print(f"• Email Layanan     : callbri@bri.co.id")
        print(f"---------------------------------------------")
        print(f"Sistem: Tiket pengaduan mandiri Anda: #REQ-{id(self)}")
        print(f"=============================================")

    def setorTunai(self, jumlah):
        print(f"\n--- Memproses Setor Tunai: Rp{jumlah:,} ---")
        if jumlah <= 0:
            raise SetoranNegatifEror()

        self.saldo += jumlah
        print(f"Selamat! Setoran Rp{jumlah:,} berhasil dilakukan.")
        print(f"Saldo terbaru Anda: Rp{self.saldo:,}")

    def tarikTunai(self, jumlah):
        print(f"\n--- Memproses Penarikan: Rp{jumlah:,} ---")
        if jumlah <= 0:
            raise PenarikanNegatifEror()

        if self.saldo - jumlah < self.saldoMinimal:
            raise SaldoMinimalEror(
                f"Penarikan gagal! Saldo Anda Rp{self.saldo:,}.\n"
                f"Jika ditarik Rp{jumlah:,}, sisa saldo Anda (Rp{self.saldo - jumlah:,}) "
                f"akan melewati batas minimal Rp{self.saldoMinimal:,}."
            )

        self.saldo -= jumlah
        print(f"Transaksi Anda berhasil! Penarikan Rp{jumlah:,} telah dilakukan.")
        print(f"Sisa saldo Anda sekarang: Rp{self.saldo:,}")

if __name__ == "__main__":
    akunNama = RekeningBank("Ali Murtadlo", 50000000000, "000000")
    print("=== SELAMAT DATANG DI ATM BANK REKENING ===")
    try:
        akunNama.verifikasiPIN()
        while True:
            print("\n===== MENU ATM UTAMA =====")
            print("1. Cek Saldo")
            print("2. Setor Tunai")
            print("3. Tarik Tunai")
            print("4. Hubungi Call Center")
            print("5. Keluar")
            pilihan = input("Pilih menu (1-5): ")
            if pilihan == "1":
                akunNama.cekSaldo()
            elif pilihan == "2":
                try:
                    nominal = int(input("Masukkan jumlah setoran: Rp"))
                    akunNama.setorTunai(nominal)
                except ValueError:
                    print("[ERROR] Masukkan harus berupa angka!")
                except SetoranNegatifEror as e:
                    print(f"[EXCEPTION TERDETEKSI] {e}")
                finally:
                    print("\nPesan Sistem: Validasi setoran selesai.")
            elif pilihan == "3":
                try:
                    nominal = int(input("Masukkan jumlah penarikan: Rp"))
                    akunNama.tarikTunai(nominal)
                except ValueError:
                    print("[ERROR] Masukkan harus berupa angka!")
                except PenarikanNegatifEror as e:
                    print(f"[EXCEPTION TERDETEKSI] {e}")
                except SaldoMinimalEror as e:
                    print(f"[EXCEPTION TERDETEKSI] {e}")
                finally:
                    print("\nPesan Sistem: Validasi penarikan selesai.")
                    print("-> Jika Anda tidak merasa melakukan transaksi ini, segera hubungi Call Center di Menu 4.")
            elif pilihan == "4":
                akunNama.hubungiCallCenter()
            elif pilihan == "5":
                print("\nTerima kasih telah menggunakan layanan ATM kami. Silakan ambil kartu Anda!")
                print("Silahkan Hubungi call center, JIKA ANDA MERASA TIDAK MELAKUKAN TRANSAKSI APAPUN!")
                print("Kembali lagi dan JANGAN MENINGGALKAN SAMPAH DIDALAM SERCVICE CENTER DEMI KENYAMANAN BERSAMA")
                break
            else:
                print("[Peringatan] Pilihan tidak valid! Silakan masukkan angka 1-5.")
    except AkunTerblokirEror as e:
        print(f"\n[KATA SANDI SALAH] {e}")
        print("Sistem: Kartu Anda ditahan. Silakan hubungi Call Center terdekat (1500-888) untuk mengaktifkan kembali.")
    finally:
        print("\n[SISTEM] Sesi mesin ATM telah berakhir.")
