import sqlite3

with sqlite3.connect("Test.db") as db:
    cursor = db.cursor()
db.commit()

cursor.execute("""DROP TABLE test;""")
cursor.execute("""CREATE TABLE IF NOT EXISTS test(
    Name VARCHAR(20),
    Number INT,
    Info VARCHAR(20),
    PRIMARY KEY (Name)
);""")

value1 = "abc"
value2 = 11

cursor.execute("""INSERT INTO test(Name, Number, Info) VALUES (?,?,?);""",(value1, value2, "qwerty"))
cursor.execute("""INSERT INTO test(Name, Number, Info) VALUES (?,?,?)""",("def", 232, "wasd"))
db.commit
selectAll = """SELECT * FROM test;"""

def queryTable(query):
    cursor.execute(query)
    inter = cursor.fetchall()
    result = []
    for i in inter:
        i = list(i)
        result.append(i)
    return result

value = queryTable(selectAll)
print(value)