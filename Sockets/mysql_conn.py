import mysql.connector


db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "1834df",
    database = "sistemas_distribuidos_db"
)

def sql_funct():

    mycursor = db.cursor()

    sql = "SELECT personas.dir_tel, personas.dir_nombre, personas.dir_direccion, ciudades.ciud_nombre FROM personas INNER JOIN ciudades ON personas.dir_ciud_id = ciudades.ciud_id WHERE personas.dir_tel = %s"

    mycursor.execute(sql, (3103000040, ))

    results = mycursor.fetchall()

    if mycursor.rowcount == 0:
        print("Persona dueña de ese número telefónico no existe")
        
    for result in results:
        print(result)     
        
sql_funct()


