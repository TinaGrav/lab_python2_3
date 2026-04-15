from file_sourced import File_source
from generator import Generator_source
from input_source import Input_source
from check_sources import check_source
from create_task import create_task

def make_task(tasks, task_list):
    for i in tasks:
        task_list.append(create_task(i))
    return task_list

def choose_option():
    try:
        opt = int(input())
        if (opt == 1) or (opt == 2) or (opt == 3) or (opt == 4) or (opt == 5) or (opt == 6):
            return opt
        else:
            print("Mistake. Try again")
            choose_option()
    except ValueError:
        print("Mistake. Try again")
        choose_option()


def user_part():
    print("Hello! Here you can check how sources work.")
    print("How do you want to create tasks?")
    print("You can create them from file(1), generate them(2), write by yourself(3), "
          "change smth about the last task or exit(5)")
    task_list = []
    while True:
        print("Write in option you prefer: 1, 2, 3, 4 or 5: ")
        opt = choose_option()
        if opt == 1:  # check file source
            print("Now tasks are created from 'input_file.json'. You can change tasks by changing the file")
            file_source = File_source("input_file.json")
            check_source(file_source)
            make_task(file_source.get_tasks(), task_list)

        elif opt == 2:  # check generator
            print("Now descriptions of the tasks are generated from tasks in file 'describ_list.txt'. "
                  "You can change tasks by changing the file")
            generator = Generator_source()
            check_source(generator)
            make_task(generator.get_tasks(), task_list)

        elif opt == 3:  # check input source
            print("Here you need to create tasks by yourself")
            inputed = Input_source()
            check_source(inputed)
            make_task(inputed.get_tasks(), task_list)

        elif opt == 5:
            print("Goodbye! Have a good time!")
            break

        elif opt == 4:
            if task_list:
                task = task_list[-1]
                print(task)
                print("What do you want to change about this task?")
                print("Write id(1), payload(2), priority(3), status(4), creation time(5) or ready status(6):")
                opt = choose_option()
                if opt == 1:
                    task.id = 0
                elif opt == 2:
                    print("Write new payload:")
                    task.payload = input()
                elif opt == 3:
                    print("Write new priority:")
                    task.priority = input()
                elif opt == 4:
                    print("Write new status:")
                    task.status = input()
                elif opt == 5:
                    task.created_at = 0
                else:
                    print("Ready status is updated")
                    if task.is_ready:
                        print("Task is ready to go")
                    else:
                        print("Task is not ready to go")
            else:
                "Task list is empty, there is nothing to change"