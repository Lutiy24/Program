# client.py
import socket

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def write_file(file_path, data):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)

def start_client(input_file, output_file):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    data = read_file(input_file)
    print("Відправка даних на сервер...")
    client.sendall(data.encode("utf-8"))

    processed_data = client.recv(1024).decode("utf-8")
    print("Отримано оброблені дані від сервера:")
    print(processed_data)

    write_file(output_file, processed_data)

    client.close()

if __name__ == "__main__":
    input_file = "input.txt"  # Вхідний файл з текстом
    output_file = "output.txt"  # Вихідний файл для оброблених даних
    start_client(input_file, output_file)