import eel

			# CLASS TO WORK WITH USERS
			# ДОБАВЛЕНИЕ КЛАССА ДЛЯ РАБОТ С ПОЛЬЗОВАТЕЛЯМИ
class Users():
	sessionActive = False
	loginInsideSession = ''

	def checkSession():
		return session_active

	def signOut(self):
		log = self.loginInsideSession

		logging.info("Succesfull signed out, login: " + loginInSession)
		# SESSION RESET
		# Сброс сессии
		self.loginInsideSession = ""
		self.sessionActive = False
		return log

	def signIn(self, login, password):
		# If already in database
		# Если есть в базе
		if sql.execute("SELECT * FROM users"):
			for value in sql.execute("SELECT * FROM users"):
				if (value[0] == login and value[1] == password):
					logging.info("Succesfull signing in, login: " + login)
					self.loginInsideSession = login
					self.sessionActive = True
					return True
		return False

	def signUp(self, login, password):
		# If login or password field is empty
		# Если не введен пароль или логин
		if len(login) < 1 or len(password) < 1:
			return False
		else:
			# Adding new user to database
			# Добавление нового пользователя
			if sql.execute("SELECT * FROM users"):
				for value in sql.execute("SELECT * FROM users"):
					# Checking if user already exists
					# Проверка есть ли такой пользователь в базе
					if(value[0] == login):
						logging.warning("Attempt to create existing profile")
						return False	
			sql.execute("INSERT INTO users VALUES (?, ?)", (login, password))
			db.commit()
			#  Логирование
			logging.info("Succesful registration, login: " + login)
		print('Signed up: ' + login)
		return True

					#	ДЛЯ ИСПОЛЬЗОВАНИЯ ВМЕСТЕ С EEL
					#	TO USE WITH EEL 
# В самом начале файла
user = Users()		
					#   DUBLING EVERY FUNCTION
					#	ДУБЛИРОВАНИЕ КАЖДОЙ ФУНКЦИИ
@eel.expose()
def singUp(login, password):
	return user.signUp()
@eel.expose()
def singIn(login, password):
	return user.signIn()
@eel.expose()
def signOut():
	return user.signOut()
@eel.expose()      				
def checkSession(login, password):
	return user.checkSession()