import os
# Start asking the user what want to do
print("Hello dear user tell me. What do you want to do? \"Create\", \"Delete File\", \"Update\", \"Read\" or \"Write\"")
action = input("Please answer the request: ")

# The code will excute depending on the answer
if action == "Create":
    file = open("task.json", mode="x", buffering=-1, encoding="utf-8")
    print(file)
    print("File Created Succesfully")
elif action == "Delete File":
    FileToDelete = "task.json"
    os.remove(FileToDelete)
    print("File Deleted Succesfully.")
elif action == "Write":
    NameTask = "Write the Name of the Task: "
    Proggres
    file.open("task.json", mode="a", buffering=-1, enconding="utf-8")

else: 
    print("Please Select a option gave")
#print(file)
#file.close()