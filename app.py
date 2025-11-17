import datetime, sys, os, json
# Here starts the program   
def getId():
    temps = "task.json"
    if os.path.getsize(temps) == 0:
        return str(0)
    else:
        temp1 = readFile()
        index = len(temp1["task"])
        return str(index)
    
def readFile():
    with open("task.json", "r", encoding="utf-8") as f:
        var_temp = json.load(f)
    return var_temp

def createTask(chose1):
    now = datetime.datetime.now()
    data1 = {
        "task": [ 
            {
                "Name": chose1,
                "id": getId(), 
                "status": "in-progress",
                "createdAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}",
                "updatedAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"
            }
        ]
    }
    return data1

def addTask(chose1):
    now = datetime.datetime.now()
    temp =  {
                "Name": chose1,
                "id": getId(), 
                "status": "in-progress",
                "createdAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}",
                "updatedAt": f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"
            }
    return temp

def add(chose1):
    if not os.path.exists("task.json"):
        with open("task.json", mode="x", encoding="utf-8"):
            print("File created succesfully.")
    temp = "task.json"
    data2 = createTask(chose1)
    if os.path.getsize(temp) == 0:
        with open("task.json", mode="w", encoding="utf-8") as wFile:
            json.dump(data2, wFile, indent=4)
    else:
        data4 = addTask(chose1)
        data3 = readFile()
        with open("task.json", mode="w") as f2:
            data3["task"].append(data4)
            json.dump(data3, f2, indent=4)

def update(chose1, chose2):
    temp = readFile()
    now = datetime.datetime.now()
    if chose2 == "done":
        for i in range(0, len(temp["task"])):
            if temp["task"][i]["id"] == chose1:
                temp["task"][i]["status"] = "done"
                temp["task"][i]["updatedAt"] = f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"
        with open("task.json", "w", encoding="utf-8") as f:
            json.dump(temp, f, indent=4)
    elif chose2 == "in-progress" or chose2 == "in progress":
        for i in range(0, len(temp["task"])):
            if temp["task"][i]["id"] == chose1:
                temp["task"][i]["status"] = "in-progress"
                temp["task"][i]["updatedAt"] = f"Year: {now.strftime("%G")} Month: {now.strftime("%B")} Day: {now.strftime("%A")} {now.strftime("%d")} Hour: {now.strftime("%I")}:{now.strftime("%M")}{now.strftime("%p")}"
        with open("task.json", "w", encoding="utf-8") as f:
            json.dump(temp, f, indent=4)

def listing(chose1):
    if chose1 == "all":
        temp = readFile()
        print("Printing All Tasks:")
        print("-----------------------------------------------")
        for i in temp["task"]:
            print(f"Name: {i["Name"]}, id: {i["id"]}, Status: {i["status"]}, Created At: {i["createdAt"]}.")
        print("-----------------------------------------------")

    elif chose1 == "done":
        temp = readFile()
        print("Printing Tasks:")
        print("-----------------------------------------------")
        for i in range(0, len(temp["task"])):
            if temp["task"][i]["status"] == "done":
                print(f"Name: {temp["task"][i]["Name"]}, id: {temp["task"][i]["id"]}, Status: {temp["task"][i]["status"]}, Created At: {temp["task"][i]["createdAt"]}.")
        print("-----------------------------------------------")

    elif chose1 == "in progress" or chose1 == "in-progress":
        temp = readFile()
        print("Printing Tasks:")
        print("-----------------------------------------------")
        for i in range(0, len(temp["task"])):
            if temp["task"][i]["status"] == "in-progress":
                print(f"Name: {temp["task"][i]["Name"]}, id: {temp["task"][i]["id"]}, Status: {temp["task"][i]["status"]}, Created At: {temp["task"][i]["createdAt"]}.")
        print("-----------------------------------------------")

def delete(chose1):
    temp = readFile()
    for i in range(len(temp["task"]) -1, -1, -1):
        if temp["task"][i]["id"] == str(chose1):
            del temp["task"][i]
            break
    with open("task.json", "w", encoding="utf-8") as f:
        json.dump(temp, f, indent=4)

if len(sys.argv) == 2:
    chose = sys.argv[1]
elif len(sys.argv) == 3:  
    chose = sys.argv[1]  
    chose1 = sys.argv[2]
elif len(sys.argv) == 4:
    chose = sys.argv[1]
    chose1 = sys.argv[2]
    chose2 = sys.argv[3]
match chose:
    case "add":
        add(chose1)
    case "list":
        listing(chose1)
    case "update":
        update(chose1, chose2)
    case "delete":
        delete(chose1)
    case _:
        print("Select one option.")