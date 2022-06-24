import sqlite3 as sql

con = sql.connect('fgtime.db')
cur = con.cursor()

new_table= '''CREATE TABLE "relojes"(
"id"INTEGER PRIMARY KEY AUTOINCREMENT,
"modelo"TEXT,
"marca"TEXT,
"precio"TEXT
)'''
cur.execute(new_table)
con.commit()
con.close()