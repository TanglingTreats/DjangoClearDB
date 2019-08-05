import os
import pymysql

USER = os.environ['DB_USER']
PASSWORD = os.environ['DB_PASSWORD']
HOST = os.environ['DB_HOST']
DB = os.environ['DB']

db = pymysql.connect(
        host=HOST,
        user=USER,
        passwd=PASSWORD,
        db=DB
    )
    
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
"""
sql='''
CREATE TABLE messages (
    msg_id INT NOT NULL,
    msg_content VARCHAR(255) NOT NULL,
    CONSTRAINT messages_pk PRIMARY KEY (msg_id)
)
'''
"""
'''
sql = "INSERT INTO messages (msg_id, msg_content) VALUES (1, 'Hii!!')"
'''
#cursor.execute(sql)

#db.commit()

sql = "SELECT * FROM messages"

cursor.execute(sql)

res = cursor.fetchall()
results = []

for r in res:
    results.append(r)

print(results)