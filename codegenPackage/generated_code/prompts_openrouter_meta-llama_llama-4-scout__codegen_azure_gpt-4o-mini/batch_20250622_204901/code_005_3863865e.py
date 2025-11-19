"""
Generated Code Metadata:
========================
Original URL: https://crystal.free.nf
Prompt: Generate a Crystal code snippet for a basic RESTful API.
Generated: DETERMINISTIC_3863865e946e7fa2
Batch ID: 20250622_204901
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://#{address": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```crystal
# Import the necessary modules for building a web application
require "http/server"
require "json"

# Define a simple data structure to represent a resource
struct Item
  # Attributes of the Item
  property id : Int32
  property name : String
  property description : String

  # Convert the Item to JSON format
  def to_json : String
    { id: id, name: name, description: description }.to_json
  end
end

# In-memory storage for items
ITEMS = [] of Item

# Create a new HTTP server
server = HTTP::Server.new do |context|
  # Set the response content type to JSON
  context.response.content_type = "application/json"

  # Handle different HTTP methods and routes
  case context.request.path
  when "/items"
    case context.request.method
    when "GET"
      # Return all items as JSON
      context.response.print ITEMS.to_json
    when "POST"
      # Parse the JSON body to create a new item
      begin
        item_data = JSON.parse(context.request.body.to_s)
        new_item = Item.new(id: ITEMS.size + 1, name: item_data["name"], description: item_data["description"])
        ITEMS << new_item
        context.response.status = 201 # Created
        context.response.print new_item.to_json
      rescue JSON::ParseException
        context.response.status = 400 # Bad Request
        context.response.print { error: "Invalid JSON format" }.to_json
      end
    else
      context.response.status = 405 # Method Not Allowed
      context.response.print { error: "Method not allowed" }.to_json
    end
  else
    context.response.status = 404 # Not Found
    context.response.print { error: "Resource not found" }.to_json
  end
end

# Start the server on port 8080
address = "0.0.0.0:8080"
puts "Listening on http://#{address}"
server.bind_tcp(address)
server.listen
```
