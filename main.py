import json, datetime, random
from collections import defaultdict
from enum import Enum 

tasks = defaultdict()

def get_id():
    return int(1000 * random.random())

def add(description: str, status: bool, createdDate: str, updatedDate: str | None=None):
    """:add: adds the array to the json file through dictionary"""
    ID = get_id()
    task = [description, status, createdDate, updatedDate]
    # reading and converting the data to a dictionary
    with open("sample.json", "r") as read_file:
        json_data = json.load(read_file)
    # add task to the dictionary
    json_data[ID] = task
    print(f" task: {json_data[ID]}")
    # write data back to dictionary
    with open("sample.json", "w") as f:
        json.dump(json_data, f)
    print(json_data)


   

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
    """
    # example of reading json file
    with open("sample.json", "r") as f:
        x = json.load(f)
    print(type(x))
    """

    user_inp = input().split()
    print(user_inp)
    if user_inp[0] == 'add':
        description = ' '.join(user_inp[1:])
        add(description, False, str(datetime.datetime.now()), None)

        






if __name__ == '__main__':
    main()