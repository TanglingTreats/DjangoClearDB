import os
import mySQLdb

USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
HOST = os.environ.get("HOST")
DB = os.environ.get("DB")

db = mySQLdb.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        db=DB
    )
    
cursor = db.cursor()

print(cursor)