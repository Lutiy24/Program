import tkinter as tk
import re

def remove_parentheses():
    # Зчитування введеного рядка
    input_text = entry_text.get()

    # Видалення груп символів між '(' та ')', включаючи дужки
    result_text = re.sub(r'\(.*?\)', '', input_text)

    # Виведення результату
    result_label.config(text=f"Результат: {result_text}")

# Налаштування вікна tkinter
root = tk.Tk()
root.title("Видалення тексту в дужках")

# Створення елементів інтерфейсу
label_text = tk.Label(root, text="Введіть рядок:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Entry(root, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=10)

remove_button = tk.Button(root, text="Видалити текст у дужках", command=remove_parentheses)
remove_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Запуск головного циклу програми
root.mainloop()

