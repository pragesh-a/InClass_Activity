from dataclasses import dataclass
from kivy.app import App
from datetime import datetime
from database import Database

@dataclass
class TaskModel:
    id: int
    title: str
    desc: str
    date: datetime


class TaskListModel:
    def __init__(self, db, simulate=False):
        self.__db = db
        
        if simulate:
            self.Simulate_Data()
        
        self.LoadData()


    def LoadData(self):
        self.__data = {}
        result = self.__db.GetTasks()
    
        for task in result:
            date = datetime.fromisoformat(task[3])
            self.__data[task[0]] = TaskModel(task[0], task[1], task[2], date)

    
    def Simulate_Data(self):
        self.__db.PopulateDB()


    def GetData(self):
        return self.__data
    

    def AddTask(self, title, desc):
        id = self.__db.AddTask(title, desc)
        result = self.__db.GetTaskByID(id)
        self.__data[id] = TaskModel(id, title, desc, result[3])


    def RemoveTask(self, id):
        pass
        # Use a try/except clause here (except a general exception)
        # should remove the task by the passed in ID in both the local model data
        # and the sqlite data.  Return true if the removal from both places is 
        # successful and false if not.

        
if __name__ == "__main__":
    db = Database("todo_test.db")
    test_model = TaskListModel(db, True)
    test_model.AddTask("Clean the Bathroom", "It's getting filthy!")

    print("Done")

    