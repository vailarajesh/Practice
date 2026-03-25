import sqlite3 as lite

db = "movies.db"
def get_f():
    return lite.connect(db)
def create():
    with get_f() as conn:
        conn.execute('''drop table if exists movies''')
        conn.execute('''create table if not exists movies(title text not Null ,director text not Null,
                     year int not Null,rating real not Null,watched bool not Null,primary key(title,year))''')
def add_m():
    title = input("enter the title :  ").strip()
    director =input("directors name :  ").strip()
    try:
        year = int(input("enter the year : "))
        rating =float(input("enter the imdb (0.0 - 10.0):  "))
    except ValueError:
        print("invalid year or imdb value ?!")
    with get_f() as conn:
        conn.execute("insert or ignore into movies(title,director,year,rating,watched) values(?,?,?,?,?)",(title,director,year,rating,0))
    print("movie added successful")
def display(row):
    watched = 'yes' if row[4] else 'no'
    print(f"{row[0]} directe by {row[1]} released in {row[2]} - imdb {row[3]} watched {row[4]}")
def show_m():
    with get_f() as conn:
        cur = conn.cursor()
        cur.execute("select* from movies")
        rows = cur.fetchall()
            
        if not rows:
            print("movie not found")
        for row in rows:
            display(row)    
def watched_m():
    title = input("enter the watched movie titles : ").strip()
    with get_f() as conn:
        conn.execute("update movies set watched = 1 where title= ? ",(title,))
        print("movie updated")
def find_m():
    s_opt = {'t':"TITLE",'d':"DIRECTOR",'y':"YEAR",'r':"RATING"}
    while True:
        choice = input("\nsearch:\nt-> Title\nd->Director\ny->Year\nr->Rating\nq-> Quite search\nenter your choice: ").strip().lower()
        if choice == 'q':
            break
        column = s_opt.get(choice)
        if not column:
            print("invalid choice .Try again")
            continue
        s_value = input(f"enter the {column.lower()}:  ").strip()
        query = f"select * from movies wher{column} like ? "
        par = f"%{s_value}%" if column in ["title","director"] else s_value
        with  get_f() as conn:
            cur = conn.cursor()
            cur.execute(query(par,))
            rows = cur.fetchall()
                 
            if not rows:
                print("no movies found")
            for row in rows:
                display(row)
                     
def update_m():
    title = input("enter the title to update :  ").strip() 
    u_opt = {
        't' : "title",'d':'director','y':'year','r':'rating'
    }                    
    while True: 
        choice = input("\nupdate:\nt-> title\nd-> director\ny-> year\nr-> rating\nq-> update done\nyour choice").strip().lower()
        if choice == 'q':
            break
        column = u_opt.get(choice)
        if not column:
            print("invalid choice ")
            continue
        new_v = input(f"enter new valu{column.lower()} : ").strip()
        try:
            if column == "year":
                new_v = int(new_v)
            elif column == "rating":
                new_v = float(new_v)
        except ValueError:
            print("innvalid input .try again ")
            continue
        with get_f() as conn:
            conn.execute(f"update movies set {column} = ? where title = ?  ",(new_v,title))
            print(f"{column} is updated sucessfully ")       
def delete_m():
    title = "enter the movie title to delete ".strip()
    with get_f() as conn:
        conn.execute("delete from movies where title = ? ",(title,))
        print("movie deleted sucessfully")
        
def clear_m(): 
    confirm = input("are you sure you want to clear all movies ? (y/n) :  ").strip().lower()
    if confirm == "y":
        with get_f() as conn:
            conn.execute("delete from movies ")
            print("All movies are clearedd ")
            
def menu():
    options = {'a': add_m,'l':show_m,'w' : watched_m,'f':find_m,'u': update_m,'d': delete_m,'c': clear_m}  
    while True: 
        choice = input("""enter: 
                       a-> Add movie
                       l-> list movie
                       w-> movies watchedd 
                       f-> find movies 
                       u-> update movies 
                       d-> delete movies 
                       c-> clear all movies
                       q -> quite
                       your choice : """).strip().lower()
        if choice == "q":
            print("Good Bayee")
            break
        elif choice in options:
            options[choice]()
        else:
            print("unknown command ? try again. ")
            
if __name__ == "__main__":
    create()
    menu()                
                 
            
                   
        

                
            
                      
                         
                    
            
            