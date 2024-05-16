# here we are introducing error handling
# we improve our code with custom function
# from functions import get_todos, write_todos
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)
while True:
    user_action = input("Type add, show, Edith, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        """we added [4:] just to exclude the add string from being included in the input"""
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        # remember on default filepath is passed into this write_todos.
        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            row = f"{index+1}-{item}"
            print(row.strip())
            """ this index and enumerate function was later included to number the list """
    elif user_action.startswith("edith"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ") + "\n"
            todos[number] = new_todo

            # remember on default filepath is passed into this write_todos.
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not Valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            # remember on default filepath is passed into this write_todos.

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed"
            print(message.strip())
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid")

print('Bye')
