import json, datetime, random
from collections import defaultdict
from enum import Enum 

tasks = defaultdict()

def get_id():
    return int(1000 * random.random())

def read_file() -> dict:
    with open("sample.json", "r") as f:
        json_data = json.load(f)
    return json_data

def write_file(data: dict):
    with open("sample.json", "w") as f:
        json.dump(data, f)
    

def search():
    ":search:"
    pass
    # name 
    # 1. read file d
    # 3 searcg thruv dict
    # update dict value od=f desctiotion and updated time 



def add(description: str, status: bool, createdDate: str, updatedDate: None=None):
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

def update(ID: int, new_description: str, updatedDate: str):
    pass
    # name 
    # 1. read file d
    with open("sample.json", "r") as read_file:
        json_data = json.load(read_file)
    
    # 3 searcg thruv dict
    json_data[ID][0] = new_description
    json_data[ID][3] = updatedDate 

    # write json_data back into json
    with open("sample.json", "w") as f:
        json.dump(json_data, f)
    
def delete(ID: int):
    # ID
    # open file
    
    # del json_data[id]

    pass

def mark():
    pass

def list():
    pass




   

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
        delete(ID)
    elif command ==  'list':
        list()
    elif command == ('mark-in-progress' or 'mark-done'):
        mark()


    


        






if __name__ == '__main__':
    main()