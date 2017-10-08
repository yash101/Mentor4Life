cursor = connection.cursor()
sql_command = """
CREATE TABLE cookie (
     cookieuser varchar2(50),
     cookiepass varchar2(50),
     expired varchar2(1)
    );"""

cursor.execute(sql_command)

sql_command = """INSERT INTO cookie (cookieuser, cookiepass, expired) VALUES ("pritiyadav", "password", "Y");"""
cursor.execute(sql_command)

cursor.execute(sql_command)

connection.commit()

connection.close()


