class TaskModel:
    def __init__(self):
        self.tasks = {}
        self.counter = 1

    def add(self, task_data):
        task = task_data.dict()
        task["id"] = self.counter
        self.tasks[self.counter] = task
        self.counter += 1
        return task

    def get(self, task_id):
        return self.tasks.get(task_id)

    def get_all(self):
        return list(self.tasks.values())

    def update(self, task_id, task_data):
        if task_id in self.tasks:
            updated_task = task_data.dict()
            updated_task["id"] = task_id
            self.tasks[task_id] = updated_task
            return updated_task
        return None

    def delete(self, task_id):
        return self.tasks.pop(task_id, None)
