import mysql.connector

config = {
    'user': 'root',
    'password': 'admin1',
    'host': 'db',
    'port': '3306',
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


