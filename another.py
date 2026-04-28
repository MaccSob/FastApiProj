from fastapi import FastAPI
from pydantic import BaseModel

api = FastAPI()

some_tasks_idk = [
    {'task_id': 1, 'task_name': 'Cooking', 'task_description': 'Cook something to eat.'},
    {'task_id': 2, 'task_name': 'Reading', 'task_description': 'Read 50 pages.'},
    {'task_id': 3, 'task_name': 'Gaming', 'task_description': 'Play league with ur buddies.'},
    {'task_id': 4, 'task_name': 'Music', 'task_description': 'Play on your keyboard.'},
    {'task_id': 5, 'task_name': 'Running', 'task_description': 'Run 5 miles.'},
    {'task_id': 6, 'task_name': 'Working', 'task_description': 'Go to work.'},

]

@api.get('/tasks/{task_id}')
def get_tasks(task_id):
        for task in some_tasks_idk: 
                if task[task_id] == task_id:
                        return {'result': task}
                

@api.get('/tasks')
def get_task(first_n = None):
        if first_n:
                return some_tasks_idk[:first_n]
        else:
                return some_tasks_idk