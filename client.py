import requests
import sys

BASE_URL = "http://127.0.0.1:5000/api"

STATE = {
    'token': None,
    'role_type': None
}

def get_headers():
    if STATE['token']:
        return {'Authorization': f"Bearer {STATE['token']}"}
    return {}

# ==========================================
# CHECKPOINT 5: INTEGRASI HTTP REQUEST
# ==========================================
def login():
    print("\n--- LOGIN SISTEM ---")
    username = input("Username: ")
    password = input("Password: ")
    
    raise NotImplementedError("[Checkpoint-5] Request API untuk Login belum diimplementasikan")

def view_polls():
    print("\n--- DAFTAR POLLING ---")
    
    raise NotImplementedError("[Checkpoint-5] Request API untuk Lihat Polling belum diimplementasikan")

def create_poll():
    print("\n--- BUAT POLLING (ADMIN) ---")
    question = input("Pertanyaan: ")
    opt_a = input("Teks Opsi A: ")
    opt_b = input("Teks Opsi B: ")
    
    raise NotImplementedError("[Checkpoint-5] Request API untuk Buat Polling belum diimplementasikan")

def archive_poll():
    print("\n--- ARSIPKAN POLLING (ADMIN) ---")
    poll_id = input("Masukkan ID Polling yang akan diarsipkan: ")
    
    raise NotImplementedError("[Checkpoint-5] Request API untuk Arsip Polling belum diimplementasikan")

def vote():
    print("\n--- LAKUKAN VOTE ---")
    poll_id = input("Masukkan ID Polling: ")
    choice = input("Pilihan Anda (A/B): ").upper()
    
    raise NotImplementedError("[Checkpoint-5] Request API untuk Vote belum diimplementasikan")

# ==========================================
# CHECKPOINT 4: STRUKTUR MENU DINAMIS
# ==========================================
def main():
    while True:
        try:
            if not STATE['token']:
                print("\n=== E-POLLING SYSTEM ===")
                print("1. Login")
                print("2. Keluar")
                pilihan = input("Pilih menu: ")
                
                if pilihan == '1':
                    login()
                elif pilihan == '2':
                    print("Keluar dari aplikasi.")
                    sys.exit()
                else:
                    print("Pilihan tidak valid.")
            else:
                raise NotImplementedError("[Checkpoint-4] Percabangan menu CLI belum dibuat")
                
        except NotImplementedError as e:
            print(f"\n[!] FITUR BELUM SELESAI: {e}")
            print("    Silakan lengkapi kode pada fungsi tersebut agar fitur ini dapat berjalan.")

if __name__ == '__main__':
    main()