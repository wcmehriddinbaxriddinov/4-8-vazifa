from database import db, cursor

def jadval_yarat():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    db.commit()

def vazifa_qoshish(title, description, status, created_at):
    cursor.execute("INSERT INTO task (title, description, status, created_at) VALUES (?, ?, ?, ?)", (title, description, status, created_at))
    db.commit()

def barcha_vazifalar():
    cursor.execute("SELECT * FROM tasks")
    return cursor.fetchall()

def vazifa_qidirish(vazifa_id):
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (vazifa_id,))
    return cursor.fetchone

def vazifa_tahrirlash(vazifa_id, new_nom):
    cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (new_nom, vazifa_id,))
    db.commit()

def vazifa_status(vazifa_id):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", ("bajarildi", vazifa_id,))
    db.commit()

def vazifa_ochirish(vazifa_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (vazifa_id,))
    db.commit()


jadval_yarat()
while True:
    tanlov = int(input("""
================================
    TASK MANAGER
================================

1. Vazifa qo'shish
2. Barcha vazifalarni ko'rish
3. Vazifani qidirish
4. Vazifani tahrirlash
5. Vazifani bajarildi deb belgilash
6. Vazifani o'chirish
0. Chiqish

Tanlovingizni kiriting:"""))
    match tanlov:
        case 1:
            title = input("Nomi: ")
            description = input("Tavsif: ")
            created_at = input("Sana: ")
            vazifa_qoshish(title, description, "kutilmoqda", created_at)

        case 2:
            for vazifa in barcha_vazifalar():
                print(f"ID: {vazifa[0]}\nNomi: {vazifa[1]}\nTavsif: {vazifa[2]}\nHolati: {vazifa[3]}\nSana: {vazifa[4]}")
                print("-------------------------------")

        case 3:
            vazifa_id = input("ID: ")
            print(vazifa_qidirish(vazifa_id))

        case 4:
            vazifa_id = input("ID: ")
            new_nom = input("Yangi nomi: ")
            vazifa_tahrirlash(vazifa_id, new_nom)

        case 5:
            vazifa_id = input("ID: ")
            vazifa_status(vazifa_id)

        case 6:
            vazifa_id = input("ID: ")
            vazifa_ochirish(vazifa_id)

        case 0:
            break

        case _:
            print("Notog'ri tanlov")

