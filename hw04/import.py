# -*- coding:UTF-8 -*-
import psycopg2

conn = psycopg2.connect(host='localhost',database="hw04", user="dbo", password="123456")

cur = conn.cursor()
cur.execute('''
DROP TABLE IF EXISTS hw_a;
CREATE TABLE IF NOT EXISTS hw_a(
    sn       INTEGER,    --序号
    Name     TEXT,       --姓名
    PRIMARY  KEY(sn)       
);
	''')

for i in range(6):
	sn = 10*(i+1)
	Name = 'A%d' % sn
	cur.execute('''
		INSERT INTO hw_a(sn, Name) VALUES (%(sn)s, %(Name)s) 
	''', {'sn':sn, 'Name':Name} )

cur.execute('''
DROP TABLE IF EXISTS hw_b;
CREATE TABLE IF NOT EXISTS hw_b(
    sn       INTEGER,    --序号
    Name     TEXT,       --姓名
    PRIMARY  KEY(sn)       
);
	''')

for i in range(5):
	sn = 10*(i+4)
	Name = 'B%d' % sn
	cur.execute('''
		INSERT INTO hw_b(sn, Name) VALUES (%(sn)s, %(Name)s) 
	''', {'sn':sn, 'Name':Name} )

conn.commit()
