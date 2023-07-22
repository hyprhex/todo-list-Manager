import os

# Print all todo list features for users 
print("To add a task use: A")
print("To view a tasks use: V")
print("To mark as complete use: M")
print("To remove a task use: R")
print("To Exit a task use: E")

fileName = 'list.md'

while True:
    # Make options for user 
    userOption = input("What you want to do?: ")
    if os.path.isfile(fileName):
        with open(fileName, 'r') as file:
            userListTasks = file.readlines()

    # Add Task
    if userOption == 'A':
        userTask = input('Write your task: ');
        with open(fileName, 'a') as file:
            file.write(f"- [ ] {userTask}\n")

    # View all tasks
    if userOption == 'V':
        for userTasks in userListTasks:
            print(userTasks)
    
    # Make task completed
    if userOption == 'M':
        completedTask = int(input('Number of task: '))
        userListTasks[completedTask - 1] = userListTasks[completedTask - 1].replace('- [ ]', '- [x]')
        with open(fileName, 'w') as file:
            for userTasks in userListTasks:
                file.write(userTasks)
    
    # Remove task
    if userOption == 'R':
        removedTask = int(input('Number of task: '))
        confirmRemoveTask = input('Remove task (y/n): ')
        if confirmRemoveTask == 'y':
            userListTasks[removedTask - 1] = ''
            with open(fileName, 'w') as file:
                for userTasks in userListTasks:
                    file.write(userTasks)
        else:
            continue

    # Exist Program
    if userOption == 'E':
        break