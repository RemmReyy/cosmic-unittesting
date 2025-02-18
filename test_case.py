import unittest
from  to_do_list import ToDoList, Task

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo = ToDoList()
        self.todo.add_task("Make homework", "You need to do your python homework", "20.02.2025", "Medium")
        self.todo.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")

    def test_add_task(self):
        self.todo.add_task("Buy some products", "Buy milk, cheese and beef", "17.02.2025", "Low")
        self.assertTrue(self.todo.task_exists("Buy some products"))

    def test_add_duplicated(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("Call mom", "Call mom and wish happy birthday", "18.02.2025", "High")

