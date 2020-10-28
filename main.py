import mysql.connector

bd = mysql.connector.connect(user='sergio', password='12345', database='mascotas')

cursor = bd.cursor()

while True:
    print("1) Agregar usuario")
    print("2) Mostrar usuarios")
    print("0) Salir")
    op = input()

    if op == '1':
        nombre = input('nombre: ')
        apellido = input('apellido: ')
        domicilio = input('domicilio: ')
        tel = input('telefono: ')
        email = input('email: ')

        consulta = "INSERT INTO dueno (nombre, apellido, domicilio, telefono, email) " \
                    "VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(consulta,(nombre,apellido,domicilio,tel,email))
        bd.commit()

    elif op == '2':
        consulta = "SELECT * FROM dueno"
        cursor.execute(consulta)

        for row in cursor.fetchall():
            print('id: ', row[0])
            print('nombre: ', row[1])
            print('apellido: ', row[2])
            print('domicilio: ', row[3])
            print('telefono: ', row[4])
            print('email: ', row[5])

    elif op == '0':
        break
    