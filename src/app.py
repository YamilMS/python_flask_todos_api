from flask import Flask, jsonify, request
app = Flask(__name__)

#                   GLOBAL SCOPE

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

#                   GET METHOD
@app.route('/todos', methods=['GET'])
def todos_exercise():
    list_of_todos=jsonify(todos)
    return list_of_todos

#                   POST METHOD

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    post_json=jsonify(todos)
    return post_json

#                   DELETE METHOD

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    return jsonify(todos)

    
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)