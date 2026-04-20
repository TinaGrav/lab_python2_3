from class_task import Task


class TaskIterator:
    def __init__(self, tasks):   # init tasks and index
        self.tasks = tasks
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.tasks):  # check if index is not out of range
            res = self.tasks[self.index]
            self.index += 1
            return res
        raise StopIteration  # stop iteration if index is as big as tasks length


class TaskQueue:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):  # add task to tasks list
        self.tasks.append(task)

    def __iter__(self):  # use iterator
        return TaskIterator(self.tasks)

    def filter(self, status=None, priority=None):  # filter for status and priority
        for task in self.tasks:
            if status is not None and task.status != status:
                continue
            if priority is not None and task.priority != priority:
                continue
            yield task  # yield filtered task

    def __len__(self):
        return len(self.tasks)

    def last(self):
        return self.tasks[-1]



