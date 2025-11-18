import os
import psycopg2
import sys

print("=" * 50)
print("🚀 النظام النهائي - بدء التشغيل")
print("=" * 50)
print(f"🐍 إصدار Python: {sys.version}")

def main():
    try:
        # الحصول على رابط قاعدة البيانات
        DATABASE_URL = os.getenv('DATABASE_URL')
        
        if not DATABASE_URL:
            print("❌ DATABASE_URL غير موجود")
            return
            
        print(f"📊 رابط قاعدة البيانات: {DATABASE_URL[:30]}...")
        
        # تحويل الرابط
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        
        # الاتصال بقاعدة البيانات
        print("🔗 جارٍ الاتصال...")
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        print("✅ تم الاتصال!")
        
        # إنشاء جدول
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS ammar_final (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        print("✅ تم إنشاء الجدول!")
        
        # إدخال الاسم
        cur.execute("INSERT INTO ammar_final (name) VALUES (%s)", ("عمار عساف",))
        conn.commit()
        print("✅ تم إدخال 'عمار عساف'!")
        
        # عرض النتائج
        cur.execute("SELECT * FROM ammar_final")
        results = cur.fetchall()
        
        print("\n📋 النتائج:")
        print("=" * 40)
        for row in results:
            print(f"ID: {row[0]} | الاسم: {row[1]} | الوقت: {row[2]}")
        print("=" * 40)
        
        cur.close()
        conn.close()
        print("🎉 تم الانتهاء بنجاح!")
        
    except Exception as e:
        print(f"❌ خطأ: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
