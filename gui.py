import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clocks')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button(size=2, image_source="adds.png", key="Add", tooltip="Add Items")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edith")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],

                   font=('Helvetica', 15))
while True:

    event, values = window.read(timeout=10)
    window["clocks"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # --------------------------------------------
    # here we are going to collect the
    # event which is the button clicked and the
    # value which is the word entered
    # print(1, event)
    # print(2, values)
    # print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # this will  update the list in realtime
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Edith":
            try:
                todo_to_edith = values['todos'][0]
                new_todo = values['todo'] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edith)
                todos[index] = new_todo
                functions.write_todos(todos)
                #this will help to update the list in realtime
                window['todos'].update(values=todos)
            # here we want when we click let the clicked item show on the input before editing
            except IndexError:
                sg.popup("Please select an Item", font=("Helvetica", 20))


        case 'Complete':
            try:
                # we are writing this very line to get the particular todos from the list. remember the todos is a refrence key in line 8
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                # here we are make sure the value is no more on the input after removing it from the todo list
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an Item", font=("Helvetica", 20))

        case 'todos':
            # remember here we are making anything we click to also appear on input
            window['todo'].update(value=values['todos'][0])
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            # this very line is used to able the program to close without showing error dialogue
            break


window.close()
