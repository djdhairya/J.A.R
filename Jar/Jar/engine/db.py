import sqlite3
import csv
con=sqlite3.connect("jar.db") #Connect to database
cursor=con.cursor()  #Create cursor object

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query="INSERT INTO sys_command VALUES (null,'Jupyter Notebook','C:\\Users\\Dhairya Hindoriya\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook.lnk')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#query="INSERT INTO web_command VALUES (null,'amazon','https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_7hz2t19t5c_e&adgrpid=155259815513&hvpone=&hvptwo=&hvadid=674842289437&hvpos=&hvnetw=g&hvrand=906829006418168739&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9062095&hvtargid=kwd-10573980&hydadcr=14453_2316415&gad_source=1')"
#cursor.execute(query)
#con.commit()

#testing module
#app_name = "sheets"
#cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
#results = cursor.fetchall()
#print(results[0][0])

#Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
#desired_columns_indices = [0, 30]

# # Read data from CSV and insert into SQLite table for the desired columns
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
 #   for row in csvreader:
  #      selected_data = [row[i] for i in desired_columns_indices]
   #     cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
#con.commit()
#con.close()        

#query = 'rohan'
#query = query.strip().lower()

#cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#results = cursor.fetchall()
#print(results[0][0])