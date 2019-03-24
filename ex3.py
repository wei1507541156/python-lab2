from sys import argv


if __name__ == '__main__':
    filename = ""
    todo = []
    ended = 0
    if (len(argv)>1):
        filename = argv[1]
        try:
            txt = open(filename)
            todo = txt.read().splitlines()
            txt.close()
        except IOError:
            print("file does not exist")


    while True:

        print("todo_manager \n"

              "Insert the number corresponding to the action you want to perform:\n"

              "1. insert a new task;\n"

              "2. remove a task;\n "

              "3. show all the tasks;\n"

              "4. close the program.\n "
              "5. delete cantain keyword's tasks"

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
                todo = sorted(todo)
                print(todo)

            else:

                print("the list is empty")

        elif n == 4:
             ended = 1
             break
        elif n==5:
            remove=[]
            keyword=input("type the keyword")
            for do in todo:
                if(keyword in todo):
                    remove.append(do)
            if(len(remove)>0):
                for do_remove in remove:
                    if(do_remove in todo):
                        todo.remove(do_remove)
                        print("the task with "do_remove" is removed ")



        else:

             print("input error")
    if (ended==1 and filename!=""):
        try:
            txt = open(filename,w)
            for do in todo:
                txt.write(do+"\n")
            txt.close()
        except IOError:
            print("problem in saving list in file")



