import json, datetime, random

# dictionary object makes the most sense

def write_task():
    # opens file 
    # checks if file is empty/doesnt exist
        # writes to file
        # converts file to object 
        # writes in object
        # converts to json
        # writes to json file
    pass
def delete_task(id: int):
    # take json 
        # convert to object    
        # search thru object
        # delete the object
    pass
# update / read, are pretty similar and are jsut variations. finish me in morning
    

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




if __name__ == '__main__':
    main()