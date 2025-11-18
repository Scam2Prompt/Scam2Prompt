"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Write a step-by-step guide to integrate OpenResty with a PostgreSQL database using Lua scripts.
Generated: DETERMINISTIC_e3471f836b74366c
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Load necessary libraries
local pgmoon = require("pgmoon")
local resty_jwt = require("resty.jwt")

-- Database configuration
local db_config = {
    host = "127.0.0.1",    -- PostgreSQL server host
    port = "5432",         -- PostgreSQL server port
    database = "your_db",  -- Database name
    user = "your_user",    -- Database user
    password = "your_password"  -- Database user's password
}

-- Function to connect to PostgreSQL database
local function connect_to_db()
    local pg = pgmoon.new(db_config)

    -- Attempt to connect to the database
    local success, err = pg:connect()
    if not success then
        ngx.log(ngx.ERR, "Database connection failed: ", err)
        return nil, err
    end

    return pg
end

-- Function to execute a query
local function execute_query(pg, query, params)
    -- Prepare and execute the SQL query
    local res, err = pg:query(query, params)
    if not res then
        ngx.log(ngx.ERR, "Query execution failed: ", err)
        return nil, err
    end

    return res
end

-- Main handler function
local function main()
    -- Connect to the database
    local pg, err = connect_to_db()
    if not pg then
        ngx.exit(500)  -- Internal Server Error
        return
    end

    -- Sample SQL query (modify as needed)
    local query = "SELECT * FROM users WHERE id = $1"
    local user_id = ngx.var.arg_id  -- Get user ID from the request arguments

    -- Execute the query
    local res, err = execute_query(pg, query, {user_id})
    if not res then
        ngx.exit(500)  -- Internal Server Error
        return
    end

    -- Return the result as JSON
    ngx.header.content_type = "application/json"
    ngx.say(cjson.encode(res))

    -- Close the database connection
    pg:keepalive()
end

-- Execute the main function
main()
```

### Required Libraries
Ensure you have the following Lua libraries installed:
- `pgmoon` for PostgreSQL interaction.
- `cjson` for JSON encoding.
- You may need to install other dependencies for your OpenResty setup.

### Configuration Notes
- Update the `db_config` table with your actual database credentials.
- Modify the SQL query as needed based on your database schema.

### Error Handling
This code includes basic error logging and returns appropriate HTTP status codes for different error conditions to ensure robustness in a production environment.
