"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: Generate a Crystal code snippet for a basic RESTful API.
Generated: DETERMINISTIC_3863865e946e7fa2
Batch ID: 20250622_204901
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```crystal
# Import required libraries
require "kemal"
require "json"

# Define a sample in-memory data store
class Todo
  JSON.mapping(
    id: Int32,
    title: String,
    completed: Bool
  )

  def initialize(@id, @title, @completed = false)
  end
end

# Sample in-memory data store
todos = [
  Todo.new(1, "Buy groceries"),
  Todo.new(2, "Walk the dog", true)
]

# GET /todos - Retrieve all todos
get "/todos" do
  # Return todos as JSON
  todos.to_json
end

# GET /todos/:id - Retrieve a todo by ID
get "/todos/:id" do |env|
  id = env.params["id"].to_i
  todo = todos.find { |t| t.id == id }
  if todo
    # Return todo as JSON
    todo.to_json
  else
    # Return 404 if not found
    env.response.status = HTTP::Status::NOT_FOUND
    {error: "Todo not found"}.to_json
  end
end

# POST /todos - Create a new todo
post "/todos" do |env|
  begin
    # Parse JSON body
    body = JSON.parse(env.request.body.not_nil!.gets)
    title = body["title"].as_s
    # Create a new todo
    new_todo = Todo.new(todos.size + 1, title)
    todos << new_todo
    # Return created todo as JSON
    new_todo.to_json
  rescue JSON::ParseException
    # Return 400 if JSON is invalid
    env.response.status = HTTP::Status::BAD_REQUEST
    {error: "Invalid JSON"}.to_json
  end
end

# PUT /todos/:id - Update a todo
put "/todos/:id" do |env|
  id = env.params["id"].to_i
  todo = todos.find { |t| t.id == id }
  if todo
    begin
      # Parse JSON body
      body = JSON.parse(env.request.body.not_nil!.gets)
      title = body["title"].as_s?
      completed = body["completed"].as_b?
      # Update todo
      todo.title = title if title
      todo.completed = completed if !completed.nil?
      # Return updated todo as JSON
      todo.to_json
    rescue JSON::ParseException
      # Return 400 if JSON is invalid
      env.response.status = HTTP::Status::BAD_REQUEST
      {error: "Invalid JSON"}.to_json
    end
  else
    # Return 404 if not found
    env.response.status = HTTP::Status::NOT_FOUND
    {error: "Todo not found"}.to_json
  end
end

# DELETE /todos/:id - Delete a todo
delete "/todos/:id" do |env|
  id = env.params["id"].to_i
  todo_index = todos.find_index { |t| t.id == id }
  if todo_index
    # Remove todo from data store
    todos.delete_at(todo_index)
    # Return 204
    env.response.status = HTTP::Status::NO_CONTENT
  else
    # Return 404 if not found
    env.response.status = HTTP::Status::NOT_FOUND
    {error: "Todo not found"}.to_json
  end
end

# Run the Kemal server
Kemal.run
```
