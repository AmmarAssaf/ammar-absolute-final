import sqlite3
import datetime

print("🚀 نظام SQLite المحلي - بدء التشغيل")

# إنشاء قاعدة بيانات محلية
conn = sqlite3.connect('local_database.db')
cursor = conn.cursor()

# إنشاء جدول
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# إدخال البيانات
cursor.execute("INSERT INTO users (name) VALUES (?)", ("عمار عساف",))
conn.commit()

# عرض البيانات
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()

print("\n📊 البيانات المخزنة:")
for row in results:
    print(f"ID: {row[0]}, Name: {row[1]}, Time: {row[2]}")

conn.close()
print("🎉 تم التخزين بنجاح في SQLite المحلي!")
