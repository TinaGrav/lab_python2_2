import datetime

class Task:
    def __init__(self, id, payload, priority = 3, status = "uncompleted"):
        self.id = id
        self.payload = payload
        self._priority = priority
        self.creation_time = datetime.time
        self.status = status

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if not(1 <= value <= 5):
            raise ValueError("Wrong priority number")
        self._priority = value

task = Task(12, "ask", 1, "done")

