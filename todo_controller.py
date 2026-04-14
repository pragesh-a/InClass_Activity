from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App

class SimpleToDoView(BoxLayout):
    layoutTasks = ObjectProperty()
    new_task_title = StringProperty("")
    new_task_desc = StringProperty("")
    remove_task_id = StringProperty("")
    # Hint: Add a new property to connect to the front end for the ID
    #       used in the removal command.

    def set_model(self, model):
        self.__model = model


    def load_records(self):
        data = self.__model.GetData()

        self.layoutTasks.clear_widgets()
        for value in data.values():
            task_view = Label(
                        text=f"[{value.id}]. {value.title}: {value.desc}",
                        size_hint_y=None,
                        height=40,
                        color=(0.9, 0.9, 0.9, 1)
                    )
            self.layoutTasks.add_widget(task_view)


    def on_click_add_task(self): 
        self.__model.AddTask(self.new_task_title, self.new_task_desc)
        self.load_records()

    #when clickef the remove button, we want to call the RemoveTask method in the model and then reload the records to update the view.  We also need to convert the remove_task_id to an int before passing it to the model.
    def on_click_remove_task(self):
        if self.remove_task_id:
            self.__model.RemoveTask(int(self.remove_task_id))
            self.load_records()
            
    
Builder.load_file("todo_view.kv")

