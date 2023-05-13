# Python
 All codes using Python


# README

This guide provides step-by-step instructions on how to run a Python script that connects to a SQL Server database, reads data from a table, inserts new data, and prints the updated table. 

The script uses `pyodbc`, a Python library that facilitates connections to ODBC databases.

## Prerequisites

1. Python 3.6 or above installed. If you do not have Python installed, you can download it from the official site - https://www.python.org/downloads/

2. SQL Server Database: You should have a SQL Server database set up with the appropriate permissions to read and write data.

3. pyodbc module: The pyodbc module should be installed on your system. If it's not, you can install it using pip:

```bash
pip install pyodbc
```

## Steps

1. Clone the repository to your local machine or download the python script.

2. Open the Python file in your preferred code editor.

3. Update the SQL Server connection string with your server details:

```python
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=Enter Your Server Name;"
                      "Database=ali;"
                      "Trusted_Connection=yes;")
```

Replace `Enter Your Server Name` with the name of your SQL Server. Make sure that the `Database` value matches the name of your database.

4. The script is set to select all records from the table named `make`:

```python
cursor.execute("Select * from make")
```

If your table has a different name, replace `make` with your table's name.

5. The script inserts three new records into the `make` table:

```python
sopi= "insert into make (name) values (?)"
data= [('Uop'),('pou'),('fff')]

for i in data:
    cursor.execute(sopi,i)
```

If you wish to add different records, modify the `data` variable accordingly.

