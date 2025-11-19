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

**openresty_postgres_integration.lua**
```lua
-- Define PostgreSQL database connection settings
local pg_host = "localhost"
local pg_port = 5432
local pg_database = "mydatabase"
local pg_username = "myusername"
local pg_password = "mypassword"

-- Define OpenResty configuration
local ngx_config = {
  -- PostgreSQL database connection pool settings
  pool_size = 10,
  pool_timeout = 30000, -- 30 seconds
}

-- Import required Lua modules
local ngx = ngx
local ngx_req = ngx.req
local ngx_res = ngx.response
local ngx_log = ngx.log
local ngx_err = ngx.ERR
local ngx_warn = ngx.WARN

-- Import pgmoon Lua module for PostgreSQL interactions
local pgmoon = require "pgmoon"

-- Create a PostgreSQL connection pool
local pool = assert(pgmoon.create_pool({
  host = pg_host,
  port = pg_port,
  database = pg_database,
  user = pg_username,
  password = pg_password,
  pool_size = ngx_config.pool_size,
  pool_timeout = ngx_config.pool_timeout,
}))

-- Define a function to execute a PostgreSQL query
local function execute_query(sql, params)
  -- Acquire a connection from the pool
  local conn, err = pool:acquire()
  if not conn then
    ngx_log(ngx_err, "Failed to acquire PostgreSQL connection: ", err)
    return nil, err
  end

  -- Execute the query
  local res, err = conn:execute(sql, params)
  if not res then
    ngx_log(ngx_err, "Failed to execute PostgreSQL query: ", err)
    pool:release(conn)
    return nil, err
  end

  -- Release the connection back to the pool
  pool:release(conn)

  return res
end

-- Define an OpenResty content handler
local function content_handler()
  -- Get the request method and URI
  local method = ngx_req.get_method()
  local uri = ngx_req.get_uri()

  -- Handle GET requests
  if method == "GET" then
    -- Execute a sample query
    local sql = "SELECT * FROM mytable"
    local res, err = execute_query(sql)
    if not res then
      ngx_res.send_headers(500, "Internal Server Error")
      ngx_res.send_body("Error executing query: " .. err)
      return
    end

    -- Send the response
    ngx_res.send_headers(200, "OK")
    ngx_res.send_body(ngx.encode_json(res))
  else
    ngx_res.send_headers(405, "Method Not Allowed")
  end
end

-- Register the content handler
ngx.content_by_lua(content_handler)
```

**nginx.conf**
```nginx
worker_processes  1;
events {
    worker_connections  1024;
}
http {
    server {
        listen       8080;
        server_name  localhost;

        location / {
            content_by_lua_file openresty_postgres_integration.lua;
        }
    }
}
```

**Dockerfile**
```dockerfile
FROM openresty/openresty:1.21.4.3

# Copy nginx configuration
COPY nginx.conf /usr/local/nginx/conf/nginx.conf

# Copy Lua script
COPY openresty_postgres_integration.lua /usr/local/nginx/lua/

# Install pgmoon Lua module
RUN luar install pgmoon

# Expose port 8080
EXPOSE 8080

# Run command
CMD ["nginx", "-g", "daemon off;"]
```

**docker-compose.yml**
```yml
version: '3'
services:
  openresty:
    build: .
    ports:
      - "8080:8080"
    depends_on:
      - postgres

  postgres:
    image: postgres:14
    environment:
      POSTGRES_USER: myusername
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
```

**init.sql**
```sql
CREATE TABLE mytable (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL
);

INSERT INTO mytable (name) VALUES ('Sample Data');
```
