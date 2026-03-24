import unittest
def add_tasks(task_list, new_task):
    task_list.append(new_task)
    return task_list

class TestAddTasks(unittest.TestCase):
    def test_add_tasks(self):
        task_list = []
        result = add_tasks(task_list, "Завершить лабораторную работу")
        self.assertTrue(result)
        self.assertEqual(len(result), 1)

    def test_add_tasks_empty(self):
        task_list = []
        result = add_tasks(task_list, " ")
        self.assertTrue(result)
if __name__ == '__main__':
    unittest.main()