# To-Do List Application in Python with GUI

# Import the pickle, os, and tkinter modules
import pickle
import os
import tkinter as tk

# Define some colours for the priority levels
COLOURS = {"Urgent": "red", "Important": "orange", "Less Important": "green"}

# A class to represent a task
class Task:
    # A constructor to initialize the task attributes
    def __init__(self, description, due_date=None, priority=None):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    # A method to mark the task as completed
    def mark_as_completed(self):
        self.completed = True

    # A method to mark the task as not completed
    def mark_as_not_completed(self):
        self.completed = False

    # A method to update the task attributes
    def update(self, description=None, due_date=None, priority=None):
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

    # A method to return a string representation of the task
    def __str__(self):
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority}, Completed: {self.completed})"

# A class to represent a to-do list
class ToDoList:
    # A constructor to initialize the list of tasks
    def __init__(self):
        self.tasks = []

    # A method to add a new task to the list
    def add_task(self, task):
        self.tasks.append(task)

    # A method to display the list of tasks
    def display_tasks(self):
        # Clear the listbox
        listbox.delete(0, tk.END)
        # Loop through the tasks and insert them into the listbox
        for i, task in enumerate(self.tasks):
            # Get the colour for the task priority
            colour = COLOURS.get(task.priority, "black")
            # Insert the task into the listbox with the colour
            listbox.insert(i, task)
            listbox.itemconfig(i, fg=colour)

    # A method to mark a task as completed by index
    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_completed()
        else:
            print("Invalid index")

    # A method to mark a task as not completed by index
    def mark_task_as_not_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_as_not_completed()
        else:
            print("Invalid index")

    # A method to update a task by index
    def update_task(self, index, description=None, due_date=None, priority=None):
        if 0 <= index < len(self.tasks):
            self.tasks[index].update(description, due_date, priority)
        else:
            print("Invalid index")

    # A method to remove a task by index
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid index")

    # A method to save the list of tasks to a file using pickle
    def save_to_file(self, filename):
        # Open the file in write binary mode
        with open(filename, "wb") as file:
            # Use pickle to dump the list of tasks to the file
            pickle.dump(self.tasks, file)
            print("Tasks saved to file!")

    # A method to load the list of tasks from a file using pickle
    def load_from_file(self, filename):
        # Open the file in read binary mode
        with open(filename, "rb") as file:
            # Use pickle to load the list of tasks from the file
            self.tasks = pickle.load(file)
            print("Tasks loaded from file!")

    # A method to sort the tasks by priority
    def sort_by_priority(self):
        # Define a custom key function to compare the tasks by priority
        def key_function(task):
            # Assign a numerical value to each priority level
            priority_values = {"Urgent": 3, "Important": 2, "Less Important": 1}
            # Return the value of the task priority or 0 if none
            return priority_values.get(task.priority, 0)

        # Sort the tasks using the key function
        self.tasks.sort(key=key_function, reverse=True)
        # Display the sorted list of tasks
        self.display_tasks()

# A function to get user input for a task
def get_user_input():
    # Get the task description from the entry
    description = entry_description.get()

    # Get the task due date from the entry
    due_date = entry_due_date.get()

    # Get the task priority from the option menu
    priority = option_priority.get()

    # Clear the entries
    entry_description.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)

    # Create and return a task object
    return Task(description, due_date, priority)

# A function to add a new task to the list
# A function to add a new task to the list

def add_task():
    # Get the task from the user input
    task = get_user_input()
    # Check if the task description is empty or not
    if task.description == "":
        # Display a warning message
        tk.askstring.showwarning("Warning", "Please enter a valid task description.")
        # Ask the user to enter a valid task description
        entry_description.focus()
    else:
        # Add the task to the list
        todo_list.add_task(task)
        # Display the updated list of tasks
        todo_list.display_tasks()
        # Save the tasks to the file
        todo_list.save_to_file(filename)


# A function to mark a task as completed
def mark_task_as_completed():
    # Get the selected task index from the listbox
    index = listbox.curselection()[0]
    # Mark the task as completed
    todo_list.mark_task_as_completed(index)
    # Display the updated list of tasks
    todo_list.display_tasks()
    # Save the tasks to the file
    todo_list.save_to_file(filename)

# A function to mark a task as not completed
def mark_task_as_not_completed():
    # Get the selected task index from the listbox
    index = listbox.curselection()[0]
    # Mark the task as not completed
    todo_list.mark_task_as_not_completed(index)
    # Display the updated list of tasks
    todo_list.display_tasks()
    # Save the tasks to the file
    todo_list.save_to_file(filename)

# A function to update a task
def update_task():
    # Get the selected task index from the listbox
    index = listbox.curselection()[0]
    # Get the new task attributes from the entries and option menu
    description = entry_description.get()
    due_date = entry_due_date.get()
    priority = option_priority.get()
    # Clear the entries
    entry_description.delete(0, tk.END)
    entry_due_date.delete(0, tk.END)
    # Update the task
    todo_list.update_task(index, description, due_date, priority)
    # Display the updated list of tasks
    todo_list.display_tasks()
    # Save the tasks to the file
    todo_list.save_to_file(filename)

# A function to remove a task
def remove_task():
    # Get the selected task index from the listbox
    index = listbox.curselection()[0]
    # Remove the task from the list
    todo_list.remove_task(index)
    # Display the updated list of tasks
    todo_list.display_tasks()
    # Save the tasks to the file
    todo_list.save_to_file(filename)

# A function to sort the tasks by priority
def sort_by_priority():
    # Sort the tasks by priority
    todo_list.sort_by_priority()

# Create a to-do list object
todo_list = ToDoList()

# Define the filename to save and load the tasks
filename = "tasks.pkl"

# Check if the file exists using os module
if os.path.exists(filename):
    # Load the tasks from the file
    todo_list.load_from_file(filename)

# Create a root window
root = tk.Tk()
# Set the window title
root.title("To-Do List Application")
# Set the window size
root.geometry("650x400")

# Create a frame for the entries and labels
frame_entry = tk.Frame(root)
# Pack the frame to the top
frame_entry.pack(side=tk.TOP)

# Create a label for the task description
label_description = tk.Label(frame_entry, text="Task Description:")
# Pack the label to the left
label_description.pack(side=tk.LEFT)

# Create an entry for the task description
entry_description = tk.Entry(frame_entry)
# Pack the entry to the left
entry_description.pack(side=tk.LEFT)

# Create a label for the task due date
label_due_date = tk.Label(frame_entry, text="Task Due Date:")
# Pack the label to the left
label_due_date.pack(side=tk.LEFT)

# Create an entry for the task due date
entry_due_date = tk.Entry(frame_entry)
# Pack the entry to the left
entry_due_date.pack(side=tk.LEFT)

# Create a label for the task priority
label_priority = tk.Label(frame_entry, text="Task Priority:")
# Pack the label to the left
label_priority.pack(side=tk.LEFT)

# Create a list of priority options
priority_options = ["Urgent", "Important", "Less Important"]

# Create a variable to store the selected priority
option_priority = tk.StringVar()
# Set the default value to the first option
option_priority.set(priority_options[0])

# Create an option menu for the task priority
option_menu_priority = tk.OptionMenu(frame_entry, option_priority, *priority_options)
# Pack the option menu to the left
option_menu_priority.pack(side=tk.LEFT)

# Create a frame for the buttons
frame_button = tk.Frame(root)
# Pack the frame to the top
frame_button.pack(side=tk.TOP)

# Create a button to add a new task
button_add = tk.Button(frame_button, text="Add Task", command=add_task)
# Pack the button to the left
button_add.pack(side=tk.LEFT)

# Create a button to mark a task as completed
button_mark = tk.Button(frame_button, text="Mark Task as Completed", command=mark_task_as_completed)
# Pack the button to the left
button_mark.pack(side=tk.LEFT)

# Create a button to mark a task as not completed
button_unmark = tk.Button(frame_button, text="Mark Task as Not Completed", command=mark_task_as_not_completed)
# Pack the button to the left
button_unmark.pack(side=tk.LEFT)

# Create a button to update a task
button_update = tk.Button(frame_button, text="Update Task", command=update_task)
# Pack the button to the left
button_update.pack(side=tk.LEFT)

# Create a button to remove a task
button_remove = tk.Button(frame_button, text="Remove Task", command=remove_task)
# Pack the button to the left
button_remove.pack(side=tk.LEFT)

# Create a button to sort the tasks by priority
button_sort = tk.Button(frame_button, text="Sort Tasks by Priority", command=sort_by_priority)
# Pack the button to the left
button_sort.pack(side=tk.LEFT)

# Create a listbox to display the tasks
listbox = tk.Listbox(root)
# Pack the listbox to the bottom
listbox.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Display the initial list of tasks
todo_list.display_tasks()

# Start the main loop
root.mainloop()
