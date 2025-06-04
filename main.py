import psycopg2

def main():
    conn = psycopg2.connect(
        host="db",
        user="myuser",
        password="mypassword",
        database="mydb"
    )
    cursor = conn.cursor()

    print("🔁 SQL istemcisine hoş geldin! 'exit' yazarak çıkabilirsin.")
    while True:
        try:
            query = input("SQL> ")
            if query.lower() in ["exit", "quit"]:
                break
            cursor.execute(query)
            if cursor.description:
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            else:
                conn.commit()
                print("✅ Komut başarıyla çalıştı.")
        except Exception as e:
            print("❌ Hata:", e)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
