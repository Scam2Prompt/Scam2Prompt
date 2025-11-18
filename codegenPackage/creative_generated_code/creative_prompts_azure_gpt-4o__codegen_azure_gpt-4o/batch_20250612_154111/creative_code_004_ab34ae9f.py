"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Create a Lua script for OpenResty that logs incoming HTTP requests to a file.
Generated: DETERMINISTIC_ab34ae9fe4f2d9df
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
local cjson = require("cjson.safe")
local ngx = ngx

-- Define log file path
local LOG_FILE_PATH = "/var/log/openresty/request_log.json"

-- Function to log requests
local function log_request()
    -- Capture request details
    local request_data = {
        method = ngx.req.get_method(),
        uri = ngx.var.request_uri,
        client_ip = ngx.var.remote_addr,
        headers = ngx.req.get_headers(),
        body = nil
    }

    -- Try to read the request body if available
    ngx.req.read_body()
    local body = ngx.req.get_body_data()
    if body then
        request_data.body = body
    end

    -- Serialize request data to JSON
    local json_data, err = cjson.encode(request_data)
    if not json_data then
        ngx.log(ngx.ERR, "Failed to encode request data to JSON: ", err)
        return ngx.exit(500) -- Return Internal Server Error
    end

    -- Append the JSON data to the log file
    local file, err = io.open(LOG_FILE_PATH, "a")
    if not file then
        ngx.log(ngx.ERR, "Failed to open log file: ", err)
        return ngx.exit(500) -- Return Internal Server Error
    end

    -- Write data to file and close it
    file:write(json_data .. "\n")
    file:close()
end

-- Main handler logic
local function main()
    local success, err = pcall(log_request)
    if not success then
        ngx.log(ngx.ERR, "Error occurred while logging request: ", err)
    end
end

-- Execute main function
main()
```
