class TaskManager:
    def __init__(self):
        self.checklist = []
        self.completed_tasks = []
        self.incomplete_tasks = []
    
    def add_task(self, task):
        self.checklist.append(task)
    
    def mark_completed(self, task):
        if task in self.checklist:
            self.completed_tasks.append(task)
            self.checklist.remove(task)
        else:
            print(f"Task '{task}' not found in checklist.")
    
    def finalize_day(self):
        self.incomplete_tasks.extend(self.checklist)
        self.checklist.clear()
    
    def show_summary(self):
        print("Completed Tasks:", self.completed_tasks)
        print("Incomplete Tasks:", self.incomplete_tasks)
        
if __name__ == "__main__":
    manager = TaskManager()
    manager.add_task("Finish Python project")
    manager.add_task("Read AI article")
    manager.add_task("Exercise for 30 minutes")
    
    manager.mark_completed("Finish Python project")
    
    manager.finalize_day()
    manager.show_summary()
