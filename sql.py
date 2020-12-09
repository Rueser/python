import pymysql

db = pymysql.connect('localhost','root','1765','mydb')

cursor = db.cursor()
while True:
    print('''Введите действие:
Просмотреть-1, Добавить-2, Редактировать-3, Удалить-4, Выход-5''')
    a = input(":::")
    if a == '1':

        cursor.execute("SELECT * FROM `mydb`.`students`;")
        data = cursor.fetchall()

        print(*data, sep="\n")

    elif a == '2':

        surname = input("Введите фамилию товарища:")
        name = input("Введите имя товарища:")
        pat = input("Введите отчество товарища:")

        cursor.execute("INSERT INTO `mydb`.`students` (`Фамилия`, `Имя`, `Отчество`) VALUES (%s, %s, %s);", (surname,name,pat))
        cursor.execute("SELECT * FROM mydb.students;")

        print("Товарищ занесен в таблицу!Ура!")

    elif a == '3':
        id = input("Введите ID товарища которго хотите изменить:")
        surname = input("Введите фамилию товарища:")
        name = input("Введите имя товарища:")
        pat = input('Введите отчетство товарища:')

        sql = "UPDATE `mydb`.`students` SET `Фамилия` = '%s', `Имя` = '%s', `Отчество` = '%s' WHERE (`idStudents` = '%s');"% (surname,name,pat,id)

        cursor.execute(sql)
        cursor.execute("SELECT * FROM mydb.students;")
        print("Товарищ изменен!Ура!")

    elif a == '4':
        id = input("Введите ID товарища которого хотите удалить:")
        sql = "DELETE FROM `mydb`.`students` WHERE (`idStudents` = '%s');"%(id)

        cursor.execute(sql)
        cursor.execute("SELECT * FROM mydb.students;")
        print("Товарищ удален!")

    elif a == '5':
        break
db.commit()

db.close()














