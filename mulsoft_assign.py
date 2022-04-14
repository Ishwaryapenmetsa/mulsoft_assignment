import sqlite3
conn = sqlite3.connect('details.db')

c = conn.cursor()

c.execute(""" CREATE TABLE movies (

	name text , 
	actor text,
	actress text,
	director text,
	year integer

)""")

c.execute("INSERT INTO movies VALUES ('RRR', 'NTR','ALIA','RAJAMOULI',2022)")

c.execute("INSERT INTO movies VALUES ('PUSHPA','ALLU ARJUN','RASHMIKA','SUKUMAR',2021)")

c.execute("INSERT INTO movies VALUES ('MIRCHI','PRABHAS','ANUSHKA','SIVA',2013)")

c.execute("INSERT INTO movies VALUES ('BAAHUBALI','PRABHAS','ANUSHKA','RAJAMOULI',2019)")

c.execute("INSERT INTO movies VALUES ('SHYAM SINGH ROY','NANI','SAI PALLAVI','RAHUL',2019)")

c.execute("SELECT * FROM movies")

print(c.fetchall())

c.execute("SELECT name FROM movies where actor='PRABHAS'")
print(c.fetchall())

conn.commit()

conn.close()



