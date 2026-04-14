from kivy.app import App
import todo_controller
import todo_model
import database


class SimpleToDoApp(App):
    def build(self):
        db = database.Database("todo.db")
        self.controller = todo_controller.SimpleToDoView()
        self.controller.set_model(todo_model.TaskListModel(db, False)) # Make true if you want to reset the db and add sample data.
        return self.controller
    
    def on_start(self):
        self.controller.load_records()
    

if __name__ == "__main__":
    app = SimpleToDoApp()
    app.run()
