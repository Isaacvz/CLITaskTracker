import os, json, datetime
# Start asking the user what want to do
print("Hello dear user tell me. What do you want to do? \"Create\", \"Delete File\", \"Update\", \"Read\" \"Add\" or \"Write\"")
action = input("Please answer the request: ")

# The code will excute depending on the answer
if action == "Create" or action == "create":
    # Feature Completed
    file = open("task.json", mode="x", buffering=-1, encoding="utf-8")
    print(file)
    print("File Created Succesfully.")
elif action == "Delete File" or action == "delete file":
    # Feature Completed
    FileToDelete = "task.json"
    os.remove(FileToDelete) 
    print("File Deleted Succesfully.")
elif action == "Write" or action == "write":
    # Feature Completed
    NameTask = input("Write the Name of the Task: ")
    NameID = input("Write the ID for the Task: ")
    ShortDescrip = input("Give a Short Descripcion: ")
    now = datetime.datetime.now()
    datos = {
        "task": [
            {
                "Name": NameTask,
                "id": NameID, 
                "description": ShortDescrip,
                "status": "in-progress",
                "createdAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}",
                "updatedAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"
            }
        ]
    }
    print(datos)
    # Write the new json objetc in the file     
    with open("task.json", "w", encoding="utf-8") as write_file:
        json.dump(datos, write_file, indent=4) 
    print("Item Write Succesfully")
elif action == "Read" or action == "read":
    # Feature Completed
    with open("task.json", mode="r", encoding="utf-8") as f:
        task_data = json.load(f)
    print(task_data)
    print("Json Content Read Succesfully.")
elif action == "Add" or action == "add":
    # Feature Completed
    NameTask = input("Write the Name of the Task: ")
    NameID = input("Write the ID for the Task: ")
    ShortDescrip = input("Give a Short Descripcion: ")
    now = datetime.datetime.now()
    y = {"Name": NameTask, "id": NameID, "description": ShortDescrip, "status": "in-progress", "createdAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}", "updatedAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"}
    with open ("task.json", "r") as file:
        data_json = json.load(file)
    data_json["task"].append(y)
    with open ("task.json", "w") as f:
        json.dump(data_json, f, indent=4)
    print("Task Added Succesfully")
else: 
    print("Please Select an option gave.")
#print(file)
#file.close()