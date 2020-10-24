import sqlite3

conn = sqlite3.connect('api_db.db')
cursor = conn.cursor()

#Create database
#cursor.execute('CREATE TABLE users (id text PRIMARY KEY, name TEXT, email TEXT, password TEXT, birth_day TEXT, state TEXT)')

#Insert values
#cursor.execute("INSERT INTO users (id,name,email,password,birth_day,state) VALUES ('a8098c1a-f86e-11da-bd1a-00112444be1e','Antonia','anto02@gmail.com','anto0902','1998-09-02','active')")
#cursor.execute("INSERT INTO users (id,name,email,password,birth_day,state) VALUES ('6fa459ea-ee8a-3ca4-894e-db77e160355e','Venus','bolita@gatita.com.co','bolita_amorosita','2018-06-24','disable')")

def insert_(values_):
	sql_insert_query = "INSERT INTO users (id,name,email,password,birth_day,state) VALUES (?,?,?,?,?,?)"
	val = (values_.get('id'),values_.get('name'),values_.get('email'),values_.get('password'),values_.get('birth_day'),values_.get('state'))
	cursor.execute(sql_insert_query,val)
	conn.commit()
	print("Data inserted successfully into users")

def update_put(values_):
	sql_update_query = "UPDATE 	users SET name = (?), email = (?), password = (?), birth_day = (?), state =(?) WHERE id = (?)"
	val = (values_.get('name'),values_.get('email'),values_.get('password'),values_.get('birth_day'),values_.get('state'),values_.get('id'))
	cursor.execute(sql_update_query,val)
	conn.commit()
	print("Users update successfully")

def update_patch(values_):
	sql_update_query = "UPDATE users SET state = (?) WHERE id = (?)"
	cursor.execute(sql_update_query,values_)
	conn.commit()
	print("Users update successfully")

def delete_(value_):
	sql_delete_query = "DELETE FROM users WHERE id = (?)"
	cursor.execute(sql_delete_query,(value_,))
	conn.commit()
	print("User delete successfully")

def search_(value_):
	sql_search_query = "SELECT name, email, password, birth_day, state FROM users WHERE id = (?)"
	cursor.execute(sql_search_query,(value_,))
	return cursor.fetchone()

#conn.execute("DROP TABLE users ")
#conn.commit()