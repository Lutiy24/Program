# server.py
import socket
import os

def receive_file(conn, save_dir):
    file_name = conn.recv(1024).decode("utf-8")
    if not file_name:
        return
    
    file_path = os.path.join(save_dir, file_name)
    with open(file_path, "wb") as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    print(f"Файл {file_name} збережено в {save_dir}")

def send_file(conn, file_path):
    file_name = os.path.basename(file_path)
    conn.send(file_name.encode("utf-8"))
    
    with open(file_path, "rb") as file:
        while (chunk := file.read(1024)):
            conn.send(chunk)
    print(f"Файл {file_name} відправлено.")

def start_server(save_dir):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Сервер запущено. Очікування з'єднання...")

    conn, addr = server.accept()
    print(f"Підключено до {addr}")

    mode = conn.recv(1024).decode("utf-8")
    if mode == "upload":
        receive_file(conn, save_dir)
    elif mode == "download":
        file_path = conn.recv(1024).decode("utf-8")
        send_file(conn, file_path)

    conn.close()
    print("З'єднання закрито.")

if __name__ == "__main__":
    save_dir = "server_files"
    os.makedirs(save_dir, exist_ok=True)
    start_server(save_dir)