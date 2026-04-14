import sqlite3
import os


class Database:
    def __init__(self, db_filename):
        self.__db_path = os.path.dirname(os.path.abspath(__file__)) + f"\\{db_filename}"
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()

        cursor.execute('''
                            CREATE TABLE IF NOT EXISTS todotasks (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                description TEXT,
                                date_added DEFAULT CURRENT_TIMESTAMP
                            )
                        ''')
        
        # date_added field is auto filled with the current date.  No need to manaully add it ourselves.

        conn.commit()
        conn.close()


    def AddTask(self, title, description):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        try:
            cursor.execute(f"INSERT INTO todotasks(title, description) VALUES(?, ?)", (title, description))
            id = cursor.lastrowid

            conn.commit()
            conn.close()
            return id
        except sqlite3.IntegrityError as e:
            print(f"Database Error: {e}")
            return None
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return None


    def RemoveTask(self, task_ID):
        pass # dont forget to remove pass when you finish this function!
        # Connect to the database and remove teh taske by the given ID.
        # Hint: The SQL to correctly remove an item by ID is the following:
        #               "DELETE FROM todotasks WHERE id=?"
        # where the "?" is the ID.
        # look at GetTaskByID as an example to base this solution off of.


    def GetTasks(self):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        try:
            result = cursor.execute(f"SELECT * FROM todotasks").fetchall()
            conn.commit()
            conn.close()

            return result
        
        except sqlite3.IntegrityError as e:
            return None
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return None
    
    def GetTaskByID(self, id):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()
        try:
            result = cursor.execute(f"SELECT * FROM todotasks WHERE id=?", (id,)).fetchall()[0]
            conn.commit()
            conn.close()

            return result
        
        except sqlite3.IntegrityError as e:
            return None
        except sqlite3.Error as e:
            print(f"Database Error: {e}")
            return None
        
    def ResetDatabase(self):
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()

        result = cursor.execute("DELETE FROM todotasks;")
        result = cursor.execute("DELETE FROM SQLITE_SEQUENCE WHERE name=\'todotasks\'")
        
        conn.commit()
        conn.close()

            
    # Run this script to create and reset the database
    def PopulateDB(self):
        self.ResetDatabase()
        self.AddTask("Mow the Lawn", "Need to mow the lawn.  The grass is getting out of hand...")
        self.AddTask("Clean the Garage", "We need to get it ready for the yard sale this weekend.")
        self.AddTask("Do the Laundry", "The hampers are piling up!")
        self.AddTask("Go to The Store", "We need the ingredients for that spaghetti we are making tonight.")
        self.AddTask("Clean My Room", "But then I got....nevermind...")


if __name__ == "__main__":
    test_db = Database("test_todo.db")
    test_db.PopulateDB()

    id = test_db.AddTask("Clean the Bathroom", "It is getting way out of hand.")
    print(id)

    test_db.RemoveTask(id)

    print("Done")