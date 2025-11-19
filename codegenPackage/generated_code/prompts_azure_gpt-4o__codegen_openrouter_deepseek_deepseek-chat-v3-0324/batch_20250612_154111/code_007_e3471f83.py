"""
Generated Code Metadata:
========================
Original URL: https://enhancekko.com
Prompt: Write a step-by-step guide to integrate OpenResty with a PostgreSQL database using Lua scripts.
Generated: DETERMINISTIC_e3471f836b74366c
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```nginx
# nginx.conf

worker_processes auto;

events {
    worker_connections 1024;
}

http {
    # Include default MIME types
    include mime.types;
    default_type application/octet-stream;

    # PostgreSQL connection settings
    upstream postgresql {
        postgres_server 127.0.0.1 dbname=test user=test password=test;
    }

    server {
        listen 8080;
        server_name localhost;

        location / {
            default_type text/html;
            content_by_lua_block {
                ngx.say("<h1>Welcome to OpenResty with PostgreSQL</h1>")
                ngx.say("<p>Available endpoints:</p>")
                ngx.say("<ul>")
                ngx.say("<li><a href='/users'>/users - List all users</a></li>")
                ngx.say("<li><a href='/users/add'>/users/add - Add a new user</a></li>")
                ngx.say("</ul>")
            }
        }

        location /users {
            content_by_lua_file lua/users.lua;
        }

        location /users/add {
            content_by_lua_file lua/add_user.lua;
        }
    }
}
```

```lua
-- lua/users.lua

-- Connect to PostgreSQL
local pgmoon = require("pgmoon")
local pg = pgmoon.new({
    host = "127.0.0.1",
    port = "5432",
    database = "test",
    user = "test",
    password = "test"
})

-- Establish connection
local ok, err = pg:connect()
if not ok then
    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
    ngx.say("Failed to connect to database: ", err)
    return
end

-- Execute query
local res, err = pg:query("SELECT * FROM users ORDER BY id")
if not res then
    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
    ngx.say("Failed to query database: ", err)
    return
end

-- Return results
ngx.header.content_type = "application/json"
local cjson = require "cjson"
ngx.say(cjson.encode(res))

-- Close connection
pg:keepalive()
```

```lua
-- lua/add_user.lua

-- Only allow POST requests
if ngx.req.get_method() ~= "POST" then
    ngx.status = ngx.HTTP_METHOD_NOT_ALLOWED
    ngx.say("Only POST method is allowed")
    return
end

-- Read request body
ngx.req.read_body()
local args = ngx.req.get_post_args()

-- Validate input
if not args.name or not args.email then
    ngx.status = ngx.HTTP_BAD_REQUEST
    ngx.say("Name and email are required")
    return
end

-- Connect to PostgreSQL
local pgmoon = require("pgmoon")
local pg = pgmoon.new({
    host = "127.0.0.1",
    port = "5432",
    database = "test",
    user = "test",
    password = "test"
})

-- Establish connection
local ok, err = pg:connect()
if not ok then
    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
    ngx.say("Failed to connect to database: ", err)
    return
end

-- Execute insert query
local query = string.format([[
    INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id
]], pg:escape_literal(args.name), pg:escape_literal(args.email))

local res, err = pg:query(query)
if not res then
    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
    ngx.say("Failed to insert record: ", err)
    return
end

-- Return success response
ngx.header.content_type = "application/json"
local cjson = require "cjson"
ngx.say(cjson.encode({
    success = true,
    id = res[1].id
}))

-- Close connection
pg:keepalive()
```

```sql
-- SQL to create the users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
