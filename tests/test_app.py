import unittest
from app import app
from flask import request
import pytest

class TestTasks(unittest.TestCase):

    @app.route('/tasks', methods=['GET'])
    def get_tasks(self):
        return jsonify([{'id': 1, 'title': 'Task 1', 'description': 'Description 1', 'priority': 'High', 'due_date': '2026-03-20'}])

    def test_get_tasks(self):
        response = app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['title'], 'Task 1')
        self.assertEqual(response.json()[0]['priority'], 'High')
        self.assertEqual(response.json()[0]['due_date'], '2026-03-20')

    @app.route('/tasks/<int:id>', methods=['GET'])
    def get_task(self, id):
        if id == 1:
            return jsonify({'id': 1, 'title': 'Task 1', 'description': 'Description 1', 'priority': 'High', 'due_date': '2026-03-20'})
        else:
            return jsonify({'error': 'Task not found'}), 404

    def test_get_task(self):
        response = app.get('/tasks/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['title'], 'Task 1')
        self.assertEqual(response.json()['priority'], 'High')
        self.assertEqual(response.json()['due_date'], '2026-03-20')

    @app.route('/tasks', methods=['POST'])
    def create_task(self):
        return jsonify({'id': 2, 'title': 'Task 2', 'description': 'Description 2', 'priority': 'Medium', 'due_date': '2026-03-21'}), 201

    def test_create_task(self):
        data = {'title': 'Task 2', 'description': 'Description 2', 'priority': 'Medium', 'due_date': '2026-03-21'}
        response = app.get('/tasks?priority=Medium')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()[0]['id'], 2)
        self.assertEqual(response.json()[0]['title'], 'Task 2')
        self.assertEqual(response.json()[0]['description'], 'Description 2')
        self.assertEqual(response.json()[0]['priority'], 'Medium')
        self.assertEqual(response.json()[0]['due_date'], '2026-03-21')

if __name__ == '__main__':
    unittest.main()