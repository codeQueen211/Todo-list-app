# A To-Do list using phthon 
#Created by sara omar

#initialize an empty list
toDo=[]

#Add task function
def addTask(task):
    toDo.append({"task":task, "state":False})
    
#Remove task function
def removeTask(tasknum):
    if not toDo:
        print("No tasks in the list.")
    if 0 < tasknum<= len(toDo):
     del toDo[tasknum-1] 
    else:
        print("invalid task number!") 

#View all tasks
def viewTasks():
     if not toDo:
        print("No tasks in the list.")
        return
     for index, task in enumerate(toDo):
        status = "Complete" if task["state"] else "Incomplete"
        print(f"{index + 1}. {task['task']} - {status}")

#Mark task as completed
def markTask(tasknum):
    if 0 < tasknum<= len(toDo):
      toDo[tasknum-1]["state"]=True        

#Exit function
def exit():
    del toDo

#Display menue function
def displayMenue():
    print("TO-DO list app")
    print("1. Add task")
    print("2. Remove task")
    print("3. View all tasks")
    print("4. Mark task as completed")
    print("5. Exit")          
    
#Main function
def main():
    while(True):
     displayMenue()
     choice=input("Enter a choice number: ")
    
     if choice=="1":
         task=input("Enter a task to add:")
         addTask(task)
     elif choice=="2":
         tasknum=int(input("Enter a task number to remove: "))
        #  if tasknum
         removeTask(tasknum)
     elif choice=="3":
         viewTasks()
     elif choice=="4":
         comp=int(input("Enter a task number to mark as completed: "))
         markTask(comp)
     elif choice=="5":
         print("Exiting app now all tasks will be deleted ")
         exit()
         break
     else:
         print("wrong input please try again")
            
# Run the application
if __name__ == "__main__":
    main()            
