import unittest
from todo_manager.todo import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        self.todo_list.add_task("Buy groceries")
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0]["task"], "Buy groceries")
        self.assertFalse(self.todo_list.tasks[0]["completed"])

    def test_complete_task(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.complete_task(0)
        self.assertTrue(self.todo_list.tasks[0]["completed"])

    def test_complete_task_invalid_index(self):
        with self.assertRaises(IndexError):
            self.todo_list.complete_task(0)

    def test_list_tasks(self):
        self.todo_list.add_task("Buy groceries")
        self.todo_list.add_task("Walk the dog")
        tasks = self.todo_list.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Buy groceries", tasks[0])
        self.assertIn("Walk the dog", tasks[1])

if __name__ == "__main__":
    unittest.main()