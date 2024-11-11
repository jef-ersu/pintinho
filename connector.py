import mysql.connector


m = mysql.connector.connect(
    host = "host",
    user = "username",
    password = "password"
)

print(m)