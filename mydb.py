import mysql.connector

database = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'v8971'
)

cursorobject = database.cursor()

cursorobject.execute('create database dcrm')

print('all done')