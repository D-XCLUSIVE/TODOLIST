import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edith")

window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 15))
while True:
    # here we are going to collect the
    # event which is the button clicked and the
    # value which is the word entered
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # this will  update the list in realtime
            window['todos'].update(values=todos)
        case "Edith":
            todo_to_edith = values['todos'][0]
            new_todo = values['todo'] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edith)
            todos[index] = new_todo
            functions.write_todos(todos)
            #this will help to update the list in realtime
            window['todos'].update(values=todos)
        # here we want when we click let the clicked item show on the input before editing
        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            # this very line is used to able the program to close without showing error dialogue
            break


window.close()
