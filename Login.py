import mysql.connector
from getpass import getpass
from passlib.hash import django_pbkdf2_sha256

def login(username:str, password:str) -> bool:
    mydb = mysql.connector.connect(
    host="",
    user="",
    password="",
    database="",
    )

    mycursor = mydb.cursor(buffered=True)

    mycursor.execute("SHOW TABLES")

    mycursor.execute("""
        SELECT
            *
        FROM
            auth_user
        WHERE
            username = %(username)s
    """, {
        'username': username
    })
    user = mycursor.fetchone()

    if user is None:
            print('Incorrect username.')
            return False
    elif not django_pbkdf2_sha256.verify(password, user[1]):
            print('Incorrect password.')
            return False
    
    print('Welcome, ' + user[5] + ' ' + user[6])
    return True

if (__name__ == '__main__'):
    print('Script Spinner - Login')
    username = input('Username: ')
    password = getpass()
    login(username, password)

