import tkinter as tk
from tkinter import messagebox

def check_palindrome():
    # Зчитування введеного рядка
    input_text = entry_text.get()

    # Перевірка, чи є рядок паліндромом
    if input_text == input_text[::-1]:
        result_label.config(text="Рядок є паліндромом!", fg="green")
    else:
        result_label.config(text="Рядок не є паліндромом.", fg="red")

# Налаштування вікна tkinter
root = tk.Tk()
root.title("Перевірка паліндрому")

# Створення елементів інтерфейсу
label_text = tk.Label(root, text="Введіть рядок:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Entry(root, width=30)
entry_text.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Перевірити", command=check_palindrome)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Запуск головного циклу програми
root.mainloop()
