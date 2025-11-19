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
require "json"

# Represents a simple model for a blog post
class Post
  include JSON::Serializable

  property id : Int32
  property title : String
  property content : String

  def initialize(@id : Int32, @title : String, @content : String)
  end
end

# In-memory database for demo purposes
posts = [
  Post.new(1, "First Post", "This is the content of the first post"),
  Post.new(2, "Second Post", "This is the content of the second post")
]

# Helper method to find a post by ID or return 404
def find_post(posts, id)
  posts.find { |post| post.id == id } || raise "Post not found"
end

# GET /posts - List all posts
get "/posts" do |env|
  env.response.content_type = "application/json"
  posts.to_json
end

# GET /posts/:id - Get a specific post
get "/posts/:id" do |env|
  begin
    id = env.params.url["id"].to_i
    post = find_post(posts, id)
    env.response.content_type = "application/json"
    post.to_json
  rescue
    env.response.status_code = 404
    {error: "Post not found"}.to_json
  end
end

# POST /posts - Create a new post
post "/posts" do |env|
  begin
    data = JSON.parse(env.request.body.not_nil!)
    id = posts.size + 1
    post = Post.new(id, data["title"].as_s, data["content"].as_s)
    posts << post
    env.response.status_code = 201
    env.response.content_type = "application/json"
    post.to_json
  rescue ex : JSON::ParseException
    env.response.status_code = 400
    {error: "Invalid JSON"}.to_json
  rescue ex : KeyError
    env.response.status_code = 400
    {error: "Missing required fields"}.to_json
  end
end

# PUT /posts/:id - Update a post
put "/posts/:id" do |env|
  begin
    id = env.params.url["id"].to_i
    post = find_post(posts, id)
    data = JSON.parse(env.request.body.not_nil!)
    
    post.title = data["title"].as_s if data["title"]?
    post.content = data["content"].as_s if data["content"]?
    
    env.response.content_type = "application/json"
    post.to_json
  rescue ex : JSON::ParseException
    env.response.status_code = 400
    {error: "Invalid JSON"}.to_json
  rescue
    env.response.status_code = 404
    {error: "Post not found"}.to_json
  end
end

# DELETE /posts/:id - Delete a post
delete "/posts/:id" do |env|
  begin
    id = env.params.url["id"].to_i
    post = find_post(posts, id)
    posts.delete(post)
    env.response.status_code = 204
  rescue
    env.response.status_code = 404
    {error: "Post not found"}.to_json
  end
end

# Start the Kemal server
Kemal.run
```
