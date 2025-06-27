# python -m eel main.py web --onefile --hidden-import=sqlite3 --noconsole
import eel
import hashlib
import zlib

# For password generating
# Для генерации паролей
import secrets
import string

# Logging
# Логирование
from time import strftime
import time
import os

# Getting base directory :: Получаем путь к корню проекта (поднимаемся на уровень выше src)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Full path to the folder :: Полный путь к папке логов
logs_path = os.path.join(BASE_DIR, "logs")

# Checking and creating log folder :: Проверяем и создаём папку, если нет
if not os.path.exists(logs_path):
    os.makedirs(logs_path)
    print(f"[INFO] Log folder created: {logs_path}")
else:
    print(f"[INFO] Log folder already exists: {logs_path}")


import logging
logging.basicConfig(level=logging.INFO, filename=f"{logs_path}/{strftime('%a_%d_%b_%Y_%I_%M')}_LogFile.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")
logging.info("Created log file")

# Database folder :: Путь к папке с базой данных
db_folder = os.path.join(BASE_DIR, "db")
os.makedirs(db_folder, exist_ok=True)  # Creating folder :: Создаём папку, если нет

# Database :: База данных
import sqlite3

# Database path :: Путь к самой базе данных
db_path = os.path.join(db_folder, "users.db")
# Connecting to db :: Создание подключения к базе
with sqlite3.connect(db_path) as db:
	sql = db.cursor()

# Creating table :: Создание таблицы, если её нет
sql.execute("""
CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    password TEXT
)
""")
db.commit()
print(f"[INFO] Database is active: {db_path}")


# Session variable :: Переменная сессии
loginInSession = ""
session = False

@eel.expose
# Text encryption function :: Функция шифрования текста
def funcText(text, md, crc, sha, sha2, sha5, duck):
	if(md):
		h = hashlib.new('md5')
		h.update(text.encode())
		# Logging :: Логирование
		logging.info("Used md5 encrypting")

		return h.hexdigest()
	elif crc:
		# Logging :: Логирование
		logging.info("Used crc32 encrypting")
		# Delete 0x :: Возможно нужно удалить 0x
		return hex(zlib.crc32(text.encode()))
	elif sha:
		h = hashlib.new('sha1')
		h.update(text.encode())
		# Logging :: Логирование
		logging.info("Used sha1 encrypting")

		return h.hexdigest()
	elif sha2:
		h = hashlib.new('sha256')
		h.update(text.encode())
		# Logging :: Логирование
		logging.info("Used sha256 encrypting")

		return h.hexdigest()

	elif sha5:
		h = hashlib.new('sha512')
		h.update(text.encode())
		return h.hexdigest()
		logging.info("Used sha512 encrypting")
	elif duck:
		# My own simple encryption method, which flips the word and adds 'duck' after every second letter
		# Мой придуманный простой метод, который переворачивает слово и добавляет 'duck' после каждой второй буквы
		text = text[::-1]
		duckText = []
		for i in range(len(text)):
			if i % 2 == 0:
				duckText.append(text[i])
				duckText.append("duck")
			else:
				duckText.append(text[i])
		logging.info("Duck ducked succesfully :)")
		return "".join(duckText)
	else:
		# If not a single checkbox is active :: Если не активировали ни один чекбокс
		logging.warning("Didn't choose encrypting mode")
		return "Please choose encryption method"
@eel.expose
# Password generating function :: Функция генерации пароля
def passGeneration(length, lowerCase, upperCase, numbers, symbols):
	# Creating alphabet for password generating :: Создание алфавита для генерации пароля
	lCase = string.ascii_lowercase if lowerCase else ""
	uCase = string.ascii_uppercase if upperCase else ""
	nums = string.digits if numbers else ""
	symbs = string.punctuation if symbols else ""
	alphabet = lCase + uCase + nums + symbs

	# Alert if alphabet is empty :: Предупреждение если алфавит пустой
	if len(alphabet) == 0:
		# Logging :: Логирование
		logging.warning("Didn't choose alphabet for password generation")
		return "Please choose alphabet for password generating"
	# Password generating :: Генерация пароля
	pwd = ""
	for i in range(int(length)):
		pwd += "".join(secrets.choice(alphabet))
	# Logging :: Логирование
	logging.info("Succesfull password generation")
	return pwd



# Sign in, sign up functions :: Функции регистрации и входа
@eel.expose
def signUp(login, password):
	# If login or password field is empty :: Если не введен пароль или логин
	if len(login) < 1 or len(password) < 1:
		return False
	else:
		# Adding new user :: Добавление нового пользователя
		if sql.execute("SELECT * FROM users"):
			for value in sql.execute("SELECT * FROM users"):
				# Checking if user exists :: Проверка есть ли такой пользователь в базе
				if(value[0] == login):
					logging.warning("Attempt to create existing profile")
					return False	
		sql.execute("INSERT INTO users VALUES (?, ?)", (login, password))
		db.commit()
		#  Logging :: Логирование
		logging.info("Succesful registration, login: " + login)
		return True
@eel.expose
def signIn(login, password):
	global session
	global loginInSession
	# If exist in database :: Если есть в базе
	if sql.execute("SELECT * FROM users"):
		for value in sql.execute("SELECT * FROM users"):
			if (value[0] == login and value[1] == password):
				logging.info("Succesfull signing in, login: " + login)
				loginInSession = login
				session = True
				return True
	return False
# Session check function :: Функция проверки сессии
@eel.expose
def checkSession():
	return session
# Sign out function :: Функция выхода
@eel.expose
def signOut():
	global loginInSession
	global session
	log = loginInSession
	logging.info("Succesfull signed out, login: " + loginInSession)
	# Session reset  :: Сброс сессии
	loginInSession = ""
	session = False
	return log


# App launch :: Запуск приложения
eel.init("web")

eel.start("main.html", size=(1920, 1080))