import sqlite3 as lite 
db = "e.db"
conn = lite.connect(db)
cur = conn.cursor()
cur.execute("PRAGMA forgein_keys")
cur.execute("drop table if exists departments")
cur.execute('''create table departments (d_id integer not Null primary key,
            d_name text not null);''' )
cur.execute("drop table if exists students")
cur.execute('''create table students (s_id integer not Null primary key,
            s_name text not Null,s_age integer not NUll,d_id integer ,
            foreign key (d_id) references departments(d_id));''')
print("created successfully")
#cur.commit()
cur.executemany("insert or ignore  into departments values(?,?)",[(1,'physics'),
                (2,'maths'),(3,'chemistry')])
cur.executemany("insert or ignore into students values(?,?,?,?)",[(1,'parushrm',20,2),
                (2,'rama',23,3),(3,'ashwad',22,1),(4,'karna',27,None)])

cur.execute('''select s.s_name,d.d_name from students s inner join departments d on s.s_name = d.d_name;''')
rows = cur.fetchall()
for r in rows:
    print(r)
print("***inner****")  
cur.execute("select s.s_age,d.d_name from departments d left outer join students s on d.d_name = s.s_name;")  
for r in cur.fetchall() :
    print(r)
print("***outer***")    
    
cur .execute("select s.s_name,d.d_name from students s cross join departments d;")    
for r in cur.fetchall():
    print(r)
print("***cross***")    

cur.close()


