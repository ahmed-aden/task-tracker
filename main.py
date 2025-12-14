import json, datetime, random
from collections import defaultdict
from enum import Enum 


def get_id():
    return int(1000 * random.random())

def read_file() -> dict:
    with open("sample.json", "r") as f:
        json_data = json.load(f)
    return json_data

def write_file(data: dict):
    with open("sample.json", "w") as f:
        json.dump(data, f)

def add(description: str, status: str, createdDate: str, updatedDate: None=None) -> None:
    """:add: adds the array to the json file through dictionary"""
    ID = get_id()
    task = [description, status, createdDate, updatedDate]
    # reading and converting the data to a dictionary
    """
    with open("sample.json", "r") as read_file:
        json_data = json.load(read_file)
    """
    json_data = read_file()
    # add task to the dictionary
    json_data[ID] = task
    print(f" task: {json_data[ID]}")
    # write data back to dictionary
    write_file(json_data)
    print(json_data)

def update(ID: int, new_description: str, updatedDate: str) -> None:
    # name 
    # 1. read file d
    json_data = read_file()
    
    # 3 searcg thruv dict
    json_data[ID][0] = new_description
    json_data[ID][3] = updatedDate 

    # write json_data back into json
    write_file(json_data)
    
def delete(ID: int) -> None:
    # ID
    # open file
    
    # del json_data[id]
    json_data = read_file()
    print(json_data[ID], f": {ID} deleted sucessfully")
    del json_data[ID]
    write_file(json_data)

def mark(cmd: str, ID: int) -> None:
    json_data = read_file()
    if cmd == 'mark-in-progress':
        json_data[ID][1] = 'in-progress'
    elif cmd == 'mark-done':
        json_data[ID][1] = 'done'
    print(json_data[ID])



def list(mode: str='') -> None:
    # TODOD: basic print
    json_data = read_file()
    for k, v in json_data.items():
        if v[1] == mode or mode == '':
            print(k, v)




   

# read the current list, 
# convert it to a dictionary, 
# and then add it 


def main(): 
    print("Please choose a command")
    print("add 'task name' ")
    print("delete 'id' ")
    print("mark-in-progress 'id' ")
    print("mark-done 'id'")
    print("list")
    print("list done")
    print("list todo")
    print("list in-progress")
    
    user_inp = input().split()
    print(user_inp)
    
    command = user_inp[0]
    if command == 'add':
        # example prompt: task-cli add "Buy groceries"
        description = ' '.join(user_inp[1:])
        add(description, "todo", str(datetime.datetime.now()), None)
        
    elif command == 'update':
        # example prompt: update 1 "Buy groceries and cook dinner"
        ID = user_inp[1]
        description = ' '.join(user_inp[2:])
        update(ID, description, updatedDate=str(datetime.datetime.now()))

         # take the description, overwrite, it and take the updated time, overwrite it.
    elif command == 'delete':
        ID = user_inp[1]
        delete(ID)
    elif command == 'list':
        if len(user_inp) > 1:
            command_type = user_inp[1]
            list(command_type)
        else:
            list()
    elif command == 'mark-in-progress' or command == 'mark-done':
        print("this branch got pushed!")
        ID = user_inp[1]
        mark(command, ID)
    


if __name__ == '__main__':
    main()