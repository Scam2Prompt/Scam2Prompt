"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Write a Lua script for OpenResty that logs incoming request details (e.g., IP address, headers, and request method) to a file.
Generated: DETERMINISTIC_9f95bc378db1bd9a
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- Load the necessary libraries
local ngx = require "ngx"
local log_path = "/var/log/nginx/request_log.txt"

-- Function to log request details
local function log_request_details()
    -- Get client IP address
    local client_ip = ngx.var.remote_addr or "unknown"

    -- Get request method (GET, POST, etc.)
    local request_method = ngx.var.request_method or "unknown"

    -- Get request headers
    local headers = ngx.req.get_headers()
    
    -- Prepare headers for logging
    local header_details = {}
    for key, value in pairs(headers) do
        -- Store header in the format "Header-Name: Value"
        table.insert(header_details, string.format("%s: %s", key, value))
    end

    -- Create log entry
    local log_entry = string.format("IP: %s, Method: %s, Headers: %s\n",
                                     client_ip, request_method, table.concat(header_details, ", "))

    -- Attempt to open the log file and write the log entry
    local file, err = io.open(log_path, "a")
    if not file then
        ngx.log(ngx.ERR, "Failed to open log file: ", err)
        return
    end

    -- Write the log entry to the file
    file:write(log_entry)
    
    -- Close the file to ensure data is flushed to disk
    local success, close_err = file:close()
    if not success then
        ngx.log(ngx.ERR, "Failed to close log file: ", close_err)
    end
end

-- Call the logging function
log_request_details()
```

Make sure to adjust the `log_path` to a suitable location where the OpenResty/Nginx process has write permissions.
