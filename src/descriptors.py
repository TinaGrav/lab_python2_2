class PriorityCheck:
    def __set_name__(self, owner, priority):  # set name for priority
        self.priority = priority

    def __get__(self, task, owner):  # get priority from task
        return task.__dict__.get(self.priority)

    def __set__(self, task, value):  # set a new priority
        try:
            value = int(value)  # check if value is int
            if (1 <= value <= 5):  # check if value is 1-5
                task.__dict__[self.priority] = value
            else:
                raise ValueError("Wrong priority number")
        except ValueError:
            raise ValueError("Wrong priority type")


class StatusCheck:
    def __set_name__(self, owner, status):  # set name for priority
        self.status = status

    def __get__(self, task, owner):  # get priority from task
        return task.__dict__.get(self.status)

    def __set__(self, task, value):  # set a new status
        if isinstance(value, str):  # check if status is str
            if len(value) > 0:  # check if status is not empty
                task.__dict__[self.status] = value
            else:
                raise ValueError("Wrong status")
        else:
            raise ValueError("Wrong status type")

