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
require "kemal"

# Define a simple RESTful API using Kemal framework

# Root route
get "/" do
  { message: "Welcome to the Crystal RESTful API" }.to_json
end

# GET /items - Retrieve all items
get "/items" do
  # Example data (in a real app, this would come from a database)
  items = [
    { id: 1, name: "Item 1", price: 10.0 },
    { id: 2, name: "Item 2", price: 20.0 }
  ]
  items.to_json
end

# GET /items/:id - Retrieve a single item by ID
get "/items/:id" do |id|
  # Example data (in a real app, this would come from a database)
  items = [
    { id: 1, name: "Item 1", price: 10.0 },
    { id: 2, name: "Item 2", price: 20.0 }
  ]

  # Find the item by ID
  item = items.find { |i| i[:id] == id.to_i }

  if item
    item.to_json
  else
    halt 404, { error: "Item not found" }.to_json
  end
end

# POST /items - Create a new item
post "/items" do |env|
  # Parse JSON body
  request_body = env.request.body.gets_to_end
  begin
    new_item = JSON.parse(request_body, Hash(String, JSON::Type))

    # Example response (in a real app, this would save to a database)
    created_item = { id: 3, name: new_item["name"], price: new_item["price"] }
    created_item.to_json
  rescue ex : Exception
    halt 400, { error: "Invalid request body" }.to_json
  end
end

# PUT /items/:id - Update an existing item
put "/items/:id" do |id, env|
  # Parse JSON body
  request_body = env.request.body.gets_to_end
  begin
    updated_data = JSON.parse(request_body, Hash(String, JSON::Type))

    # Example data (in a real app, this would update a database)
    items = [
      { id: 1, name: "Item 1", price: 10.0 },
      { id: 2, name: "Item 2", price: 20.0 }
    ]

    # Find the item by ID
    item = items.find { |i| i[:id] == id.to_i }

    if item
      item[:name] = updated_data["name"] if updated_data["name"]
      item[:price] = updated_data["price"] if updated_data["price"]
      item.to_json
    else
      halt 404, { error: "Item not found" }.to_json
    end
  rescue ex : Exception
    halt 400, { error: "Invalid request body" }.to_json
  end
end

# DELETE /items/:id - Delete an item by ID
delete "/items/:id" do |id|
  # Example data (in a real app, this would delete from a database)
  items = [
    { id: 1, name: "Item 1", price: 10.0 },
    { id: 2, name: "Item 2", price: 20.0 }
  ]

  # Find the item by ID
  item = items.find { |i| i[:id] == id.to_i }

  if item
    # Example response (in a real app, this would delete the item from the database)
    { message: "Item with ID #{id} deleted successfully" }.to_json
  else
    halt 404, { error: "Item not found" }.to_json
  end
end

# Start the Kemal server
Kemal.run
```
