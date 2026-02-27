import socket
import threading

PORT = 12345

def receive_messages(sock):
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message:
                print(f"\n[ARKADAŞIN]: {message}")
                print("[SEN]: ", end="", flush=True)
            else:
                break
        except:
            print("\nBağlantı koptu.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input("Arkadaşının Yerel IP adresini gir: ")
    
    try:
        client.connect((server_ip, PORT))
        print("BAĞLANTI BAŞARILI!")
    except Exception as e:
        print(f"Hata: {e}")
        return

    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

    while True:
        msg = input("[SEN]: ")
        if msg.lower() == 'cikis':
            client.close()
            break
        client.send(msg.encode('utf-8'))

if __name__ == "__main__":
    start_client()
