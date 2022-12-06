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
    db.commit()
    print("\ncreateTables() successful")      #For testing


def dropTables():
    cursor.execute("""DROP TABLE Users;""")
    cursor.execute("""DROP TABLE Saves;""")
    cursor.execute("""DROP TABLE SaveData;""")
    cursor.execute("""DROP TABLE Stats;""")
    cursor.execute("""DROP TABLE Scores;""")
    db.commit()
    print("\ndropTables() successful")      #For testing


def testData():     #For testing
    usersValues = [["Username1","Password1",1,"2022/12/06"],["Username2","Password2",6,"2020/06/14"]]
    for values in usersValues:
        cursor.execute("""INSERT INTO Users VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))

    savesValues = [["Username1",0,"2022/12/06"],["Username2",1,"2020/08/01"],["Username2",2,"2021/01/31"],["Username1",3,"2022/12/25"],["Username2",4,"2022/12/25"]]
    for values in savesValues:
        cursor.execute("""INSERT INTO Saves VALUES (?,?,?);""",(values[0],values[1],values[2]))

    saveDataValues = [[0,"type1","name1",1],[1,"type1","name1",2],[1,"type1","name2",10],[2,"type1","name3",5],[2,"type2","name4",100],[2,"type2","name5",3],[4,"type2","name4",5]]
    for values in saveDataValues:
        cursor.execute("""INSERT INTO SaveData VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))

    statsValues = [["Username1","stat1",10],["Username1","stat2",23],["Username2","stat1",1]]
    for values in statsValues:
        cursor.execute("""INSERT INTO Stats VALUES (?,?,?);""",(values[0],values[1],values[2]))

    scoresValues=[["Username1",1,54,"2022/21/06"],["Username2",1,100,"2020/06/21"],["Username2",2,32,"2021/08/01"]]
    for values in scoresValues:
        cursor.execute("""INSERT INTO Scores VALUES (?,?,?,?);""",(values[0],values[1],values[2],values[3]))
    print("\ntestData() successful")      #For testing


def queryDatabase(query, data):
    match query:
        case "highscore":       #Displays all scores in order
            cursor.execute("""SELECT Scores.Username, Scores.Points FROM Scores ORDER BY Scores.Points DESC;""")
        case "userScores":      #Displays user's scores in date order
            cursor.execute("""SELECT Scores.Points, Scores.DateAdded FROM Scores WHERE Scores.Username = (?) ORDER BY Scores.GameNo DESC;""",[data])
        case "userSaves":       #Displays user's saves in date order
            cursor.execute("""SELECT Saves.SaveKey, Saves.DateSaved FROM Saves WHERE Saves.Username = (?) ORDER BY Saves.SaveKey DESC;""", [data])
        case "saveData":        #Displays data for a save
            cursor.execute("""SELECT SaveData.Type, SaveData.Name, SaveData.Value FROM SaveData WHERE SaveData.SaveKey = (?) ORDER BY SaveData.Type;""", [data])
        case "userInfo":        #Displays key user info: Username,GameNo,DateCreated,Highscore,HighscoreDate
            cursor.execute("""SELECT Users.Username, Users.GameNo, Users.DateCreated, Scores.Points, Scores.DateAdded FROM Users LEFT OUTER JOIN Scores ON Users.Username = Scores.Username AND Scores.Points = (SELECT MAX(Scores.Points) FROM Scores WHERE Scores.Username = Users.Username)""")


    inter = cursor.fetchall()
    result = []
    for i in inter:     #Reformats the results into 2D Array
        i = list(i)
        result.append(i)
    print("\nqueryDatabase() successful")      #For testing
    return result


def updateDatabase(query, data):
    match query:
        case "addUser":     #Adds a new user
            cursor.execute("""INSERT INTO Users VALUES (?,?,?,?)""", (data[0],data[1],data[2],data[3]))
        case "addSave":     #Adds a new save
            cursor.execute("""INSERT INTO Saves VALUES (?,?,?)""", (data[0], data[1],data[2]))
        case "addSaveData":     #Adds new save data
            cursor.execute("""INSERT INTO SaveData VALUES (?,?,?,?)""", (data[0],data[1],data[2],data[3]))
        case "addScore":        #Adds a new score
            cursor.execute("""INSERT INTO Scores VALUES (?,?,?,?)""", (data[0],data[1],data[2],data[3]))
        case "changeStat":      #Updates a user stat
            cursor.execute("""UPDATE Stats SET StatValue = (?) WHERE Username = (?) AND StatName = (?)""", (data[0],data[1],data[2]))
    db.commit()


#createTables()
#dropTables()
#testData()
#db.commit()
#print(queryDatabase("userInfo", "username2"))
#updateDatabase("changeStat", [15,"Username1","stat1"])
