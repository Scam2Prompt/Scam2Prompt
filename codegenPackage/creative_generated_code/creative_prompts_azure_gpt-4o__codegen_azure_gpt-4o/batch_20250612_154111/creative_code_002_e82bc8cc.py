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
-- Import required modules
local mysql = require "resty.mysql"
local cjson = require "cjson"

-- Function to handle requests
local function handle_request()
    -- Retrieve the "query" parameter from the URL
    local args = ngx.req.get_uri_args()
    local query_param = args["query"]

    if not query_param or query_param == "" then
        -- Respond with a 400 error if the query parameter is missing
        ngx.status = ngx.HTTP_BAD_REQUEST
        ngx.say(cjson.encode({ error = "Missing 'query' parameter" }))
        return ngx.exit(ngx.HTTP_BAD_REQUEST)
    end

    -- Create a new MySQL connection
    local db, err = mysql:new()
    if not db then
        ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
        ngx.say(cjson.encode({ error = "Failed to initialize MySQL connection", details = err }))
        return ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
    end

    -- Set connection timeout
    db:set_timeout(5000) -- 5 seconds

    -- Connect to the MySQL database
    local ok, err, errno, sqlstate = db:connect{
        host = "127.0.0.1",  -- Adjust the host as needed
        port = 3306,         -- Default MySQL port
        database = "test",   -- Replace with your database name
        user = "root",       -- Replace with your MySQL username
        password = "password", -- Replace with your MySQL password
        charset = "utf8mb4"
    }

    if not ok then
        ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
        ngx.say(cjson.encode({
            error = "Failed to connect to MySQL",
            details = err,
            errno = errno,
            sqlstate = sqlstate
        }))
        return ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
    end

    -- Perform a query using the provided parameter
    local query = "SELECT * FROM your_table WHERE your_column = ?"
    local res, err, errno, sqlstate = db:query(query, { query_param })

    if not res then
        ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
        ngx.say(cjson.encode({
            error = "Failed to execute query",
            details = err,
            errno = errno,
            sqlstate = sqlstate
        }))
        return ngx.exit(ngx.HTTP_INTERNAL_SERVER_ERROR)
    end

    -- Close the database connection
    local ok, err = db:set_keepalive(10000, 100) -- Keep the connection alive for reuse
    if not ok then
        ngx.log(ngx.ERR, "Failed to set keepalive: ", err)
    end

    -- Respond with the retrieved data as JSON
    ngx.status = ngx.HTTP_OK
    ngx.say(cjson.encode({ data = res }))
end

-- Call the request handler
handle_request()
```
