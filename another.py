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
def get_tasks(task_id: int):
        for task in some_tasks_idk: 
                if task['task_id'] == task_id:
                        return {'result': task} 
                

@api.get('/tasks')
def get_task(first_n: int = None):
        if first_n:
                return some_tasks_idk[:first_n]
        else:
                return some_tasks_idk
        
@api.post('/tasks')
def create_task(task: dict):
        new_task_id = max(task['task_id'] for task in some_tasks_idk) + 1

        new_task = {
                'task_id': new_task_id,
                'task_name': task['task_name'],
                'task_description': task['task_description']    
                
        }
        some_tasks_idk.append(new_task)

        return new_task

@api.put('/tasks/{task_id}')
def update_task(task_id: int, updated_task: dict):
        for task in some_tasks_idk:
                if task['task_id'] == task.id:
                    task['task_name'] = update_task['task_name']
                    task['task.description'] = update_task['task.description']
                    return task
                return "404"
        
@api.delet('/task/{task.id}')
def delete_task(task_id: int):
        for index, task in enumerate(some_tasks_idk):
                if task[task_id] == task.id:
                        delete_task == some_tasks_idk.pop(index)
                        return delete_task
                return "404"

