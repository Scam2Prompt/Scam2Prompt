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
-- OpenResty Lua script to log incoming request details (IP address, headers, and request method) to a file
local function log_request_details()
    -- Define log file path
    local log_file_path = "/var/log/openresty/request_logs.log"

    -- Retrieve client IP address
    local client_ip = ngx.var.remote_addr or "unknown"

    -- Retrieve request method
    local request_method = ngx.req.get_method()

    -- Retrieve request headers
    ngx.req.read_body()
    local headers = ngx.req.get_headers()

    -- Format headers into a string
    local headers_string = ""
    for k, v in pairs(headers) do
        headers_string = headers_string .. k .. ": " .. v .. "\n"
    end

    -- Prepare log entry
    local log_message = string.format(
        "Timestamp: %s\nClient IP: %s\nRequest Method: %s\nHeaders:\n%s\n\n",
        os.date("%Y-%m-%d %H:%M:%S"),
        client_ip,
        request_method,
        headers_string
    )

    -- Open log file in append mode
    local file, err = io.open(log_file_path, "a")
    if not file then
        ngx.log(ngx.ERR, "Failed to open log file: ", err)
        return
    end

    -- Write log entry to file
    file:write(log_message)
    file:close()
end

-- Call the logging function
log_request_details()

-- Send a response back to the client
ngx.say("Request details logged successfully.")
```
