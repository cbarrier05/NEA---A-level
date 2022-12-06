import sqlite3
import datetime

db = sqlite3.connect("UserInfo.db")
cursor = db.cursor()

def createTables():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
        Username VARCHAR(20) NOT NULL, 
        Password VARCHAR(20) NOT NULL, 
        GameNo INT, 
        DateCreated DATE, 
        PRIMARY KEY (Username)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Saves(
        Username VARCHAR(20) NOT NULL,
        SaveKey INT NOT NULL,
        DateSaved DATE,
        PRIMARY KEY (Username, SaveKey)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS SaveData(
        SaveKey INT NOT NULL,
        Type VARCHAR(20) NOT NULL,
        Name VARCHAR(20) NOT NULL,
        Value INT,
        PRIMARY KEY (SaveKey, Type, Name)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Stats(
        Username VARCHAR(20) NOT NULL,
        StatName VARCHAR(20) NOT NULL,
        StatValue INT,
        PRIMARY KEY (StatName, Username)
    );""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS Scores(
        Username VARCHAR(20) NOT NULL,
        GameNo INT NOT NULL,
        Points INT,
        DateAdded DATE,
        PRIMARY KEY (Username,GameNo)
    );""")


def dropTables():
    cursor.execute("""DROP TABLE Users;""")
    cursor.execute("""DROP TABLE Saves;""")
    cursor.execute("""DROP TABLE SaveData;""")
    cursor.execute("""DROP TABLE Stats;""")
    cursor.execute("""DROP TABLE Scores;""")


def testData():
        usersValues = [["Username1","Password1",1,"2022/12/06"],["Username2","Password2",6,"2020/06/14"]]
        for values in usersValues:
            cursor.execute("""INSERT INTO Users VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))
        print("Users test data added")

        savesValues = [["Username1",0,"2022/12/06"],["Username2",1,"2020/08/01"],["Username2",2,"2021/01/31"],["Username1",3,"2022/12/25"],["Username2",4,"2022/12/25"]]
        for values in savesValues:
            cursor.execute("""INSERT INTO Saves VALUES (?,?,?);""",(values[0],values[1],values[2]))
        print("Saves test data added")

        saveDataValues = [[0,"type1","name1",1],[1,"type1","name1",2],[1,"type1","name2",10],[2,"type1","name3",5],[2,"type2","name4",100],[2,"type2","name5",3],[4,"type2","name4",5]]
        for values in saveDataValues:
            cursor.execute("""INSERT INTO SaveData VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))
        print("SaveData test data added")

        statsValues = [["Username1","stat1",10],["Username1","stat2",23],["Username2","stat1",1]]
        for values in statsValues:
            cursor.execute("""INSERT INTO Stats VALUES (?,?,?);""",(values[0],values[1],values[2]))
        print("Stats test data added")

        scoresValues=[["Username1",1,54,"2022/21/06"],["Username2",1,100,"2020/06/21"],["Username2",2,32,"2021/08/01"]]
        for values in scoresValues:
            cursor.execute("""INSERT INTO Scores VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))
        print("Scores test data added")
        print("\nAll test data added\n\n")


def queryDatabase(query):
    cursor.execute(query)
    inter = cursor.fetchall()
    result = []
    for i in inter:
        i = list(i)
        result.append(i)
    return result




#createTables()
#dropTables()
testData()
db.commit()
#print(queryDatabase("""SELECT * FROM Users"""))
