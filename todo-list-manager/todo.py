class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add a new task to the to-do list."""
        self.tasks.append({"task": task, "completed": False})

    def complete_task(self, task_index):
        """Mark a task as completed."""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
        else:
            raise IndexError("Task index out of range")

    def list_tasks(self):
        """List all tasks in the to-do list."""
        return [f"{i}. [{'X' if task['completed'] else ' '}] {task['task']}"
              for i, task in enumerate(self.tasks)]