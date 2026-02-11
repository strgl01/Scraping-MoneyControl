import mysql.connector


"""
This piece of code initialise a db conn in future if required any change in functionality of db this is the module to work with. Code in this module is written in general way and can be used with other scrappers, provided we change Table name and column name and details as per requirement
"""

class Database():

    """
 I have kept below variable class level because the value don't depend on the instaces of class
    """
    host = 'localhost'
    user = 'root'
    passw = 'Wel2046come@'
    database = 'moneycontrol'
    """ 
    This meathod initialise the db and give the cursor to execute queries in future and create table fn is also called
    """
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(host = Database.host, user = Database.user, password = Database.passw, database = Database.database)
            self.cursor = self.conn.cursor()
            self.create_table()

        except Exception as ex:
            print(f'Check the database inputs - {ex!r}')
            self.conn.close()
            self.cursor.close()

    """
    Creates table(s) if they don't exist
    """

    def create_table(self):
        try:
            
            self.cursor.execute(''' CREATE TABLE IF NOT EXISTS loser (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), price FLOAT(6,2), date DATE)''')
            self.cursor.execute(''' CREATE TABLE IF NOT EXISTS gainer (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(25), price FLOAT(6,2), date DATE)''')
        
        except Exception as ex:

            print(f' Check sql query - {ex!r}')
            self.conn.close()
            self.cursor.close()
    '''
    Adds data to table
    '''
    def add_data(self, table, data):

        try:

            self.query = f'INSERT INTO {table} ( name, price, date) VALUES ( %s, %s, %s)'
            self.cursor.executemany(self.query, data)
            self.conn.commit()
            self.conn.close()
            self.cursor.close()

        except Exception as ex:

            print(f' Check sql query - {ex!r}')
            self.conn.close()
            self.cursor.close()


    '''
    Used for reading data
    '''

    def read(self, query):
        self.__init__()
        self.cursor.execute(query)
        self.data = self.cursor. fetchone()
        return self.data




    

