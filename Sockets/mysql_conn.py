import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1834df",
    database = "sistemas_distribuidos_db"
)

mycursor = db.cursor()

sql = "SELECT personas.dir_tel, personas.dir_nombre, personas.dir_direccion, ciudades.ciud_nombre FROM personas INNER JOIN ciudades ON personas.dir_ciud_id = ciudades.ciud_id WHERE personas.dir_tel = 3103000050"

mycursor.execute(sql)

results = mycursor.fetchall()

for result in results:
    print(result)
    

