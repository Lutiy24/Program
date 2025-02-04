# client.py
import socket
import os

def send_file(client, file_path):
    file_name = os.path.basename(file_path)
    client.send(file_name.encode("utf-8"))

    with open(file_path, "rb") as file:
        while (chunk := file.read(1024)):
            client.send(chunk)
    print(f"Файл {file_name} відправлено.")

def receive_file(client, save_dir):
    file_name = client.recv(1024).decode("utf-8")
    
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "wb") as file:
        while True:
            data = client.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"Файл {file_name} збережено в {save_dir}")

def start_client(mode, file_path=None, save_dir=None):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    client.send(mode.encode("utf-8"))

    if mode == "upload":
        send_file(client, file_path)
    elif mode == "download":
        client.send(file_path.encode("utf-8"))
        receive_file(client, save_dir)

    client.close()

if __name__ == "__main__":
    mode = input("Введіть режим (upload/download): ").strip()
    if mode == "upload":
        file_path = input("Введіть шлях до файлу для відправки: ").strip()
        start_client(mode, file_path=file_path)
    elif mode == "download":
        file_path = input("Введіть шлях до файлу на сервері для завантаження: ").strip()
        save_dir = "client_files"
        os.makedirs(save_dir, exist_ok=True)
        start_client(mode, file_path=file_path, save_dir=save_dir)
