import datetime

class database:
    
    #mysql test
    #source: https://www.youtube.com/watch?v=xgyVilYfJEo, https://dev.mysql.com/doc/connector-python/en/connector-python-api-errors-error.html
    def __init__(self):
        self.conn = 0
        self.mycursor = 0
        self.working = False
        try:
            import mysql.connector
            self.conn=mysql.connector.connect(user='jyang',password='gumy555',host='mysql.eecs.ku.edu',database='jyang')
            self.mycursor=self.conn.cursor()
            self.mycursor.execute("SHOW TABLES")            
            print(mycursor.fetchall())
            self.working = True
        except ImportError:
            print("database() error: MySQL-Connector could not be imported")
        except mysql.connector.Error as err:
            print("database() error: {}".format(err))

    def addScore(self, score):
        if(self.working):
            add_score = ("INSERT INTO scores_alltime (score, name, timestamp) VALUES (%s, %s, %s)")
            score_data = (score, 'test', datetime.datetime.now())
            self.mycursor.execute(add_score, score_data)

    def updateTables(self, score):
        """to be implemented...
        self.mycursor.execute("SELECT COUNT(*) FROM fooTable")
                UPDATE table_name
        SET column1=value1,column2=value2,...
        WHERE some_column=some_value;"""
