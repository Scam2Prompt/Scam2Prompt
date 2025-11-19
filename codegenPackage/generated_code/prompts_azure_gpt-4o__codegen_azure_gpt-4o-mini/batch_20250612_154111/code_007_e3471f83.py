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

```lua
-- Load required libraries
local pgmoon = require("pgmoon")
local resty = require("resty.core")

-- Configuration for PostgreSQL connection
local pg_config = {
    host = "127.0.0.1",  -- PostgreSQL server address
    port = "5432",       -- PostgreSQL server port
    database = "your_database",  -- Database name
    user = "your_user",  -- Database user
    password = "your_password"  -- User password
}

-- Function to connect to PostgreSQL
local function connect_to_postgres()
    local pg = pgmoon.new(pg_config)

    -- Attempt to connect to the database
    local success, err = pg:connect()
    if not success then
        ngx.log(ngx.ERR, "Failed to connect to PostgreSQL: ", err)
        return nil, err
    end

    return pg
end

-- Function to execute a query
local function execute_query(query, params)
    local pg, err = connect_to_postgres()
    if not pg then
        return nil, err
    end

    -- Execute the query
    local res, err = pg:query(query, params)
    if not res then
        ngx.log(ngx.ERR, "Query execution failed: ", err)
        return nil, err
    end

    -- Close the connection
    pg:keepalive()

    return res
end

-- Example usage: Fetching data from a table
local function fetch_data()
    local query = "SELECT * FROM your_table WHERE id = $1"
    local params = {1}  -- Example parameter

    local res, err = execute_query(query, params)
    if not res then
        ngx.say("Error fetching data: ", err)
        return
    end

    -- Output the result as JSON
    ngx.header.content_type = "application/json"
    ngx.say(require("cjson").encode(res))
end

-- Main execution block
fetch_data()
```

### Notes:
- Replace `your_database`, `your_user`, `your_password`, and `your_table` with actual values.
- Ensure that the `pgmoon` and `cjson` libraries are installed and available in your OpenResty environment.
- This code assumes that you are using OpenResty with Lua and that the necessary modules are properly configured.
