todo = []

while True:

    print("todo_manager \n"

          "Insert the number corresponding to the action you want to perform:\n"

          "1. insert a new task;\n"

          "2. remove a task;\n "

          "3. show all the tasks;\n"

          "4. close the program.\n "

          "Your choice: \n ")

    n = int(input())

    if n == 1:

        print("input the new task")

        movement = str(input())

        todo.append(movement)

        print(movement, "is added")



    elif n == 2:

        k = 0

        if len(todo) > 0:

            print("which one do u want to remove")

            movement = str(input())

            for do in todo:

                if do == movement:
                    todo.remove(movement)

                    k = 1

                    print(movement, "is removed")

        if k == 0:
            print("not in the list")

    elif n == 3:

        if len(todo) > 0:
        todo = sorted(todo[])
            print(todo)

        else:

            print("the list is empty")

    elif n == 4:

        break

    else:

        print("input error")