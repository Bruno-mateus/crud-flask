import pytest
import requests

base_url= 'http://127.0.0.1:5000'
tasks = []

def test_create_task():
    task = {
        "title":"estudar JS",
        "description":"estudar redux"
    }
    response = requests.post(f'{base_url}/create-task', json=task)
    assert response.status_code == 200
    task_data = response.json()
    tasks.append(task_data)
    
def test_get_task():
    response = requests.get(f'{base_url}/get-tasks')
    response_json = response.json()
    assert response.status_code == 200
    assert "tasks" in response_json
    assert  "total_tasks" in response_json
    
def test_get_task_by_id():
     task_id = tasks[0]['id']
  
     response = requests.get(f"{base_url}/get-task/{task_id}")
     response_json = response.json()
     assert response.status_code == 200
     assert task_id == response_json['id']
     
def test_update_task():
    task_id = tasks[0]['id']
    payload={
	"title":"estudar Jav    a",
	"description":"estudar hoje das 21h as 22h aulas de Java",
	"completed":True
}
    response = requests.put(f"{base_url}/update-task/{task_id}",json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert 'message' in response_json
    
    
def test_delete_task():
    task_id= tasks[0]['id']
    response = requests.delete(f'{base_url}/task-delete/{task_id}')
    assert response.status_code == 200
    verifyDeleteItem = requests.get(f"{base_url}/get-task/{task_id}")
    assert verifyDeleteItem.status_code != 200