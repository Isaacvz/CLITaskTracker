# 💥 **Basic CLI Task Tracker**
This project is a straightforward Command-Line Interface (CLI) Task Tracker built in Python. It allows users to manage their daily to-dos directly from the terminal, leveraging a local task.json file for persistent storage. It's designed for developers and power users who prefer keyboard-based productivity over graphical interfaces.
## 🪄 Features 
- ➕ **Add**
  
  Creates a new task and assigns an ID.
- 🪓 **Delete**
  
  Permanently removes a task from the list.
- ✅ **Update**
  
  Marks a specified task as completed.
- 📋  **List**
  
  Displays all tasks, or filters by status (all, done, in-progress).
## 💯 **How to use it**
- **Add**

  This command is used to create a new task. The initial status will always be "in-progress"

  Syntax python [script_name].py add "<Task_Name>"

  Example python task_tracker.py add "Call the 3pm client"
- **Delete**

  This command permanently removes a task from the list using its ID.
  
  Syntax	python [script_name].py delete <Task_ID>
  
  Example	python task_tracker.py delete 5
  
  Important	After deleting a task, the IDs of the remaining tasks are not renumbered. The next assigned ID will follow the sequence at the end of the list
- **Update**

  update Command (Update Status)

  This command allows you to change the status of a specific task using its ID.
  
  Syntax	python [script_name].py update <Task_ID> <New_Status>
  
  New Status	Only done or in-progress are accepted.
  
  Example 1 (Complete)	python task_tracker.py update 2 done (Marks task with ID 2 as complete).
  
  Example 2 (Reopen)	python task_tracker.py update 2 in-progress (Marks task with ID 2 as in progress).
- **List**

  This command is used to view the list of tasks. You must specify a filter for the listing.
  
  Filter Option ------Shows----------------------------------------Syntax
  
  all	----------------All tasks (both complete and in progress).---python task_tracker.py list all
  
  done----------------Only tasks with "done" status.--------------python task_tracker.py list done
  
  in-progress---------Only tasks with "in-progress" status.-------python task_tracker.py list in-progress
  
## ⚠️ **File Handling**

Your task system relies on the task.json file.

- If the file does not exist when you run the add command, the script will create it automatically.

- All modifications (add, update, delete) are performed directly on this file. Do not edit it manually unless you know exactly how the JSON is structured, as you could corrupt the task list.

Here is a thank-you note to the roadmap.sh website.

## 💡 **Recommendations & Feedback Welcome**

If you have any suggestions for new features, ideas for improving the user experience, or if you've spotted a bug, please feel free to:

  1. Open an issue on this repository.

  2. Submit a Pull Request with your proposed changes.

Your input is highly valued! 🙋‍♂️

 ## 😄 **Thank You, roadmap.sh**

  The roadmaps are exceptionally well-structured, clear, and comprehensive. They provide a much-needed sense of direction, transforming overwhelming fields into manageable, step-by-step learning paths. Knowing the next step to take—and understanding why that step is important—is crucial for both beginners and experienced developers looking to upskill.

  https://roadmap.sh/projects/task-tracker
