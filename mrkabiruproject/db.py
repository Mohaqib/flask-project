import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    database = 'students',
    user = 'root',
    password = ''
)

mycursor = mydb.cursor(dictionary=True)

mycursor.execute(
    """CREATE TABLE IF NOT EXISTS studentform(
        ID INT NOT NULL AUTO_INCREMENT,
        firstname VARCHAR(255),
        lastname VARCHAR(255),
        email VARCHAR(255),
        address VARCHAR(255),
        age INT,
        gender VARCHAR(255),
        phone_number INT,
        city VARCHAR(255),
        state VARCHAR(255),
        country VARCHAR(255),
        hobbies VARCHAR(255),
        course VARCHAR(255),
        PRIMARY KEY(ID)
    )
    """
)
