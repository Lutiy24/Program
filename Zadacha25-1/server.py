# server.py
import socket
import re

def format_date(date):
    # Приведення дати до формату dd.mm.yyyy
    patterns = [
        (r'(\d{2})\.(\d{2})\.(\d{4})', r'\1.\2.\3'),  # dd.mm.yyyy
        (r'(\d{4})-(\d{2})-(\d{2})', r'\3.\2.\1'),      # yyyy-mm-dd
        (r'(\d{2})/(\d{4})/(\d{2})', r'\3.\1.\2')       # mm/yyyy/dd
    ]

    for pattern, replacement in patterns:
        date = re.sub(pattern, replacement, date)
    return date

def process_client_data(data):
    lines = data.splitlines()
    processed_lines = []
    for line in lines:
        processed_line = re.sub(r'(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2}|\d{2}/\d{4}/\d{2})', 
                                 lambda match: format_date(match.group(0)), line)
        processed_lines.append(processed_line)
    return '\n'.join(processed_lines)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Сервер запущено. Очікування з'єднання...")

    conn, addr = server.accept()
    print(f"Підключено до {addr}")

    data = conn.recv(1024).decode("utf-8")
    print("Отримано дані від клієнта:")
    print(data)

    processed_data = process_client_data(data)
    conn.sendall(processed_data.encode("utf-8"))

    conn.close()
    print("З'єднання закрито.")

if __name__ == "__main__":
    start_server()
