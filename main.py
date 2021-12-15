from getpass import getpass
from mysql.connector import connect, Error

user = "backend"
host = "localhost"
db = "geirOppgave"

database  = connect(
	user = user,
	password = getpass(prompt='Password: ', stream=None),
	host = host,
	db = db
)

cursor = database.cursor()

cursor.execute("CREATE DATABASE database1")