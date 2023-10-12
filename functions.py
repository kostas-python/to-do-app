FILEPATH = "todos.txt"


def get_todos(filepath="Todos.txt"):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


print(__name__)

# wrap above functions
if __name__ == "__main__":
    print("hello")
    print(get_todos())