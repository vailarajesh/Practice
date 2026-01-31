# to delete the database file
"""
import os  
db_path = "e.db"      
if os.path.exists(db_path):
    os.remove(db_path)
    print("daabase dleted successfullyt")
else:
  print("db file not exists")   
  
  """
  
  
 # to create a DB file and tabels in DB file using create,insert,drop
 
import sqlite3 
db = "e.db"
conn = sqlite3.connect(db)
conn.row_factory = sqlite3.Row
conn.execute('''create table if not exists company (
            id   integer    primary key,
             name      text  not null,
             age      int     not null,
             address char(30),
             salary      real);''')

conn.execute("insert or replace into company (id,name,age,address,salary) values(1, 'dharama raj', 30, 'hill', 30000)");
conn.execute("insert or replace into company(id,name,age,address,salary) values(2, 'arjuna', 27, 'padmavyuham', 20000)");
conn.execute("insert  or replace into company(id,name,age,address,salary) values(3, 'bheema', 25, 'vasvai', 28000)");
conn.execute("insert or replace into company(id,name,age,address,salary) values(4,'saha deva',22, 'duroyodhana',50000)");
conn.execute("insert or replace into company(id,name,age,address,salary) values(5,'nakula',20,'raavi', 70000)");

#conn.execute("delete from  company where id IN ( 132,432,543,876)");

conn.execute("update company set age = 32 ,address = 'hasthina puram' where id = 1")
conn.commit()

print(" total number of rows updated : ", conn.total_changes)
'''
inf= conn.execute("select id, name, age, address, salary from company")
for r in inf:
    print("id = ",r[0])
    print("name = ",r[1])
    print("age = ", r[2])
    print("addess = ",r[3])
    print("salary = ",r[4])
    print("------******------")
    print("  ")   '''
    
#conn.row_factory = sqlite3.Row  ( by activating this only 
# we can execute below query with column names) check it on top

data_r = conn.execute("select * from company")
for r in data_r:
    print("id = ",r["id"])  
    print("name = ",r["name"])
    print("age = ", r["age"])
    print("addess = ",r["address"])
    print("salary = ",r["salary"])
    print("------******------")
    print("  ")  


conn.close()  