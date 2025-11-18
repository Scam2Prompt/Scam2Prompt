"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Generate an OpenResty Lua script that connects to a MySQL database and retrieves data based on a query parameter in the URL.
Generated: DETERMINISTIC_e82bc8cc8b01960e
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Load required modules
local mysql = require("resty.mysql")
local cjson = require("cjson.safe")

-- Create a new MySQL connection
local function connect_to_mysql()
    local db = mysql:new()
    
    -- Set MySQL connection parameters
    db:set_timeout(1000)  -- 1 second
    
    -- Connect to the database
    local ok, err, errcode, sqlstate = db:connect{
        host = "127.0.0.1",
        port = 3306,
        database = "your_database_name",
        user = "your_username",
        password = "your_password",
    }
    
    if not ok then
        ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
        ngx.say("Failed to connect to MySQL: ", err)
        ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
    end
    
    return db
end

-- Retrieve data from the database based on query parameter
local function retrieve_data(query_param)
    local db = connect_to_mysql()
    
    -- Prepare SQL query
    local sql = "SELECT * FROM your_table_name WHERE your_column_name = " .. ngx.quote_sql_str(query_param)
    
    -- Execute SQL query
    local res, err, errcode, sqlstate = db:query(sql)
    
    -- Close the database connection
    db:close()
    
    if not res then
        ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
        ngx.say("Failed to query: ", err)
        ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
    end

    return res
end

-- Main execution block
local query_param = ngx.var.arg_query_param  -- Retrieve the query parameter from the URL

-- Check if the query parameter is provided
if not query_param then
    ngx.status = ngx.HTTP_BAD_REQUEST
    ngx.say("Missing query parameter.")
    ngx.exit(ngx.HTTP_BAD_REQUEST)
end

-- Retrieve and return the data as JSON
local data = retrieve_data(query_param)

-- Set response header for JSON
ngx.header.content_type = "application/json; charset=utf-8"

-- Send the response
ngx.say(cjson.encode(data))
```
