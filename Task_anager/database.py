import sqlite3

db  = sqlite3.connect("Task_anager/tasks.db")
cursor = db.cursor()
print("DATABASE ulandi!")