#using fetchall()
'''
import sqlite3 as lite 
db = "e.db"
con = lite.connect(db)
with con:                       # using (with)  we can avoid (con.close())
    cur = con.cursor()
    cur.execute("select * from company")
    rows = cur.fetchall()
    for r in rows:
        print(r)
'''       
#using fetchone() 
"""
import sqlite3 as lite 
db = 'e.db'
conn = lite.connect(db)

with conn: 
    cur = conn.cursor()
    cur.execute("select *from company")
    while True : 
        row = cur.fetchone()
        
        if row is None:
            break
        
        print(row[0], row[1],row[2],row[3],row[4])
           """
           
# fetch many
"""import sqlite3 as lite
db = "e.db" 
conn=lite.connect(db)   
cursor = conn.cursor() 
cursor.execute("select *from company")

while True: 
    records = cursor.fetchmany(2)
    if not records:
        break
    print(f"-----Retrived {len(records)} rows ---")
    for row in records : 
        print("id  ",row[0])
        print("name     ",row[1])   
cursor.close()
conn.close()   """         
           
           
#PARAMETERIZED QUERIES

"""
import sqlite3 as lite 
db = "e.db"
conn = lite.connect("e.db")

cur = conn.cursor()
cur.execute("drop table if exists lang")
cur.execute('create table lang (subjects text, marks integer)')

cur.execute('insert into lang (subjects, marks) values (?,?)',('c',100));
cur.execute('insert into lang(subjects,marks) values(?,?)', ('java',200));
cur.execute('insert into lang (subjects,marks) values(?,?)', ('python',300))

conn.commit()

cur.execute('select subjects,marks from lang')
for row in cur: 
    print(row)
    
    """
    
"""import sqlite3 
db = "e.db"
con = sqlite3.connect("e,db")
cur = con.cursor() 
cur.execute("drop table if exists users")
cur.execute(''' create table if not exists users (id integer primary key autoincrement, name text not NULL, age ineger not NULL)''')
#inserting 
name = input("enter a name ")
age = int(input("enter age : "))
cur.execute("insert into users (name,age) values (?,?) ", (name,age))
print(f"inserted {cur.rowcount} row(s)")

#updating the same record 
n_age = int(input(f"enter new age for {name} : "))
cur.execute("update users set age = ? where name = ? ", (n_age,name))
print(f"updated {cur.rowcount} row(s)")

cur.execute("select * from users where name = ? ",(name,))
rows = cur.fetchall()

print('\nfinal record(s)')
for row in rows:
    print(row)
    
    """