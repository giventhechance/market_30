import sqlite3


connect = sqlite3.connect('db.sqlite3')
cursor = connect.cursor()
#     cursor.execute('INSERT INTO main_category ("name") VALUES ("Вредные студенты")')
# cursor.execute('SELECT * FROM main_category WHERE['name'] = "Автомобили"')
cursor.fetchone()
#
print(cursor.fetchone())
connect.commit()
cursor.close()
#
# except sqlite3.Error as error:
#     print('Ошибка при подключении к sqlite:', error)
#
# finally:
#     print('Я выполняюсь всегда независимо от ошибка была или нет')

