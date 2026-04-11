from src.descriptors import StatusCheck, PriorityCheck
import unittest

class TestDescriptors:
   def test_get_tasks_success(self):
      tasks = source.get_tasks()
      assert type(tasks) == list
      assert len(tasks) == 2
      assert tasks[0]["id"] == 1
      assert tasks[0]["payload"] == "Задача 1"
