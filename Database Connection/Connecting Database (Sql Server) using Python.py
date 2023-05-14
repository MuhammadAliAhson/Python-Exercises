import pyodbc 
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=Enter Your Server Name;"
                      "Database=ali;"
                      "Trusted_Connection=yes;")


cursor=cnxn.cursor()

cursor.execute("Select * from make")

for i in cursor:
    print(i)

sopi= "insert into make (name) values (?)"
data= [('Uop'),('pou'),('fff')]

for i in data:
    cursor.execute(sopi,i)
    


you=('majid')
# cursor.execute("CREATE TABLE lake ( id int identity(1,1), name VARCHAR(128) UNIQUE,PRIMARY KEY(id))")
# cnxn.commit()

cnxn.commit()

cursor.execute("Select * from make")

for i in cursor:
    print(i)