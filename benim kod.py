import socket
import threading

# --- AYARLAR ---
PORT = 12345  # Haberleşme kapısı (İHA'larda genelde 14550 kullanılır)
# ----------------

def receive_messages(client_socket):
    """Karşıdan gelen mesajları sürekli dinleyen fonksiyon"""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n[ARKADAŞIN]: {message}")
                print("[SEN]: ", end="", flush=True)
            else:
                break
        except:
            break

def start_server():
    # 1. Soket Oluşturma (IPv4 ve TCP Protokolü)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. IP Adresini Otomatik Bul
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    # 3. Bind (Bağlama) ve Listen (Dinleme)
    server.bind(('0.0.0.0', PORT))
    server.listen(1)
    
    print(f"--- SUNUCU BAŞLATILDI ---")
    print(f"Senin IP Adresin: {local_ip}")
    print(f"Arkadaşına bu IP adresini söyle, bağlanması gerekecek.")
    print("Bağlantı bekleniyor...")

    # 4. Accept (Bağlantı Kabulü - Handshake)
    client_socket, client_address = server.accept()
    print(f"\nBAĞLANTI BAŞARILI! {client_address} bağlandı.")
    print("Sohbet başladı. Çıkmak için 'cikis' yaz.")

    # Gelen mesajları dinlemek için ayrı bir iş parçacığı (Thread) başlat
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Mesaj Gönderme Döngüsü
    while True:
        msg = input("[SEN]: ")
        if msg == 'cikis':
            client_socket.close()
            break
        client_socket.send(msg.encode('utf-8'))

if __name__ == "__main__":
    start_server()