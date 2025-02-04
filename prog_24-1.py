import tkinter as tk
from tkinter import messagebox

def calculate_series():
    try:
        # Зчитування введених значень
        x = float(entry_x.get())
        epsilon = float(entry_epsilon.get())

        # Перевірка умови |x| < 1
        if abs(x) >= 1:
            messagebox.showerror("Помилка", "Модуль x має бути меншим за 1 (|x| < 1).")
            return

        # Обчислення суми ряду
        term = 1 / (1 + x)**2  # Перший доданок
        total_sum = 0
        n = 0

        while abs(term) >= epsilon:
            total_sum += term
            n += 1
            term = (-1)**n * (n + 1) * x**n  # Наступний доданок

        # Виведення результату
        result_label.config(text=f"Сума ряду: {total_sum:.6f}")
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числові значення для x та ε.")

# Налаштування вікна tkinter
root = tk.Tk()
root.title("Обчислення суми ряду")

# Створення елементів інтерфейсу
label_x = tk.Label(root, text="Введіть x (|x| < 1):")
label_x.grid(row=0, column=0, padx=10, pady=10)

entry_x = tk.Entry(root)
entry_x.grid(row=0, column=1, padx=10, pady=10)

label_epsilon = tk.Label(root, text="Введіть ε (точність):")
label_epsilon.grid(row=1, column=0, padx=10, pady=10)

entry_epsilon = tk.Entry(root)
entry_epsilon.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Обчислити", command=calculate_series)
calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Запуск головного циклу програми
root.mainloop()
