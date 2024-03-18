from flask import Flask,request,jsonify
from models.task import Task
## iniciando o flask
app = Flask(__name__)

tasks = []
#rotas
@app.route('/create-task',methods=['POST'])
def create_task():
    data = request.get_json()

    newTask = Task(title=data['title'],description=data.get('description',""))
    tasks.append(newTask.to_dict())
    print(tasks)
    
    return jsonify(f'Tarefa {data['title'].upper()} criada com sucesso')

@app.route('/get-tasks',methods=['GET'])
def get_tasks():
    
    total_tasks = len(tasks)
    return {
        "tasks":tasks,
        "total_tasks":total_tasks
    }
    
@app.route('/get_task/<int:id>', methods=['GET'])
def get_task_by_id(id):
    for task in tasks:
       if task['id'] == id: return task
    return jsonify({"Task não encontrada"}), 404

@app.route('/update_task/<int:id>',methods=['PUT'])
def update_task(id):    
    data = request.get_json()
    for task in tasks:
        if task['id'] == id:  
            task['title'] = data['title']
            task['description'] = data['description']
            task['completed'] = data['completed']
            return jsonify(f'A tarefa {id} foi atualizada com sucesso')
        return jsonify(f'Tarefa não encontrada'), 404
    
@app.route('/task_delete/<int:id>',methods=['DELETE'])
def delete_task(id):
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            return jsonify(f'A tarefa {id} foi excluida com sucesso')
        return jsonify(f'Tarefa não encontrada'), 404
        
    
    
## Só executamos o debug quando estamos em desenvolvimento local
if __name__ == '__main__':
    app.run(debug=True)