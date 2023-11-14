import tkinter as tk
import sqlite3

# Создание базы данных и таблицы (если они еще не существуют)
conn = sqlite3.connect('employee.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS employee (
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             position TEXT NOT NULL,
             department TEXT NOT NULL,
             email TEXT NOT NULL,
             phone TEXT NOT NULL,
             salary REAL NOT NULL)''')
conn.commit()

# Функции для работы с базой данных
def add_employee():
    name = name_entry.get()
    position = position_entry.get()
    department = department_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    salary = salary_entry.get()
    if name and position and salary:
        c.execute('INSERT INTO employee (name, position, department, email, phone, salary) VALUES (?, ?, ?, ?, ?, ?)',
                  (name, position, department, email, phone, salary))
        conn.commit()
        name_entry.delete(0, tk.END)
        position_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        salary_entry.delete(0, tk.END)
        show_all_employees()

def delete_employee():
    name = name_entry.get()
    if name:
        c.execute('DELETE FROM employee WHERE name=?', (name,))
        conn.commit()
        name_entry.delete(0, tk.END)
        show_all_employees()

def search_employee():
    name = name_entry.get()
    if name:
        c.execute('SELECT * FROM employee WHERE name=?', (name,))
        employee = c.fetchone()
        if employee:
            result_label.config(text=f"ID: {employee[0]}, Position: {employee[2]}, Salary: {employee[6]}")
        else:
            result_label.config(text="Сотрудник не найден")
        name_entry.delete(0, tk.END)

def show_all_employees():
    c.execute('SELECT * FROM employee')
    employees = c.fetchall()
    for employee in employees:
        print(employee)

# Создание графического интерфейса
root = tk.Tk()
root.title("База данных сотрудников")

name_label = tk.Label(root, text="Имя:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

position_label = tk.Label(root, text="Должность:")
position_label.pack()
position_entry = tk.Entry(root)
position_entry.pack()

department_label = tk.Label(root, text="Отдел:")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Телефон:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

salary_label = tk.Label(root, text="Зарплата:")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

add_button = tk.Button(root, text="Добавить сотрудника", command=add_employee)
add_button.pack()

delete_button = tk.Button(root, text="Удалить сотрудника", command=delete_employee)
delete_button.pack
search_button = tk.Button(root, text="Поиск сотрудника", command=search_employee)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

show_employees_button = tk.Button(root, text="Показать сотрудника", command=show_all_employees)
show_employees_button.pack()

root.mainloop()