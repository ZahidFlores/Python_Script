import mysql.connector

config = {
    'user': 'root',
    'password': 'admin1',
    'host': '127.0.0.1',
    'port': '3310',
    'database': 'db_test'
}
## esta es una prueba
conn = mysql.connector.connect(**config)
cursor = conn.cursor()
query = "SELECT * FROM users"
cursor.execute(query)
results = cursor.fetchall()
for row in results:
    print(row)
cursor.close()
conn.close()


