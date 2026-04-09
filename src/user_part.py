from file_sourced import File_source
from generator import Generator_source
from input_source import Input_source
from check_sources import check_source
def choose_option():
    try:
        opt = int(input())
        if (opt == 1) or (opt == 2) or (opt == 3) or (opt == 4):
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
    print("You can create them from file(1), generate them(2), write by yourself(3) or exit(4)")
    while True:
        print("Write in option you prefer: 1, 2, 3 or 4: ")
        opt = choose_option()
        if opt == 1:  # check file source
            print("Now tasks are created from 'input_file.json'. You can change tasks by changing the file")
            file_source = File_source("input_file.json")
            check_source(file_source)
        elif opt == 2:  # check generator
            print(
                "Now descriptions of the tasks are generated from tasks in file 'describ_list.txt'. You can change tasks by changing the file")
            generator = Generator_source()
            check_source(generator)
        elif opt == 3:  # check input source
            print("Here you need to create tasks by yourself")
            inputed = Input_source()
            check_source(inputed)
        else:
            print("Goodbye! Have a good time!")
            break