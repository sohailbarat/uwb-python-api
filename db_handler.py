import mysql.connector
from config import db_info

db = mysql.connector.connect(
    host=db_info[0],
    user=db_info[1],
    password=db_info[2],
    database=db_info[3]
)
