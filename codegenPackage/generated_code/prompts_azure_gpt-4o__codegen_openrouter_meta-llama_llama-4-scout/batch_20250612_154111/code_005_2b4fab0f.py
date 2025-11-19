"""
Generated Code Metadata:
========================
Original URL: https://enhancedkk.com
Prompt: Provide an example of using OpenResty's ngx.location.capture API to make subrequests within an Nginx configuration.
Generated: DETERMINISTIC_2b4fab0fa28dd3f6
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- File: ngx_location_capture_example.lua

-- Define a function to handle the main request
local function main_handler()
    -- Make a subrequest to /subrequest
    local res = ngx.location.capture("/subrequest", {
        -- Set a timeout for the subrequest
        timeout = 5,
        -- Set a buffer size for the subrequest response
        buffer_size = 1024,
    })

    -- Check if the subrequest was successful
    if res.status == 200 then
        -- Return the response from the subrequest
        ngx.say(res.body)
    else
        -- Return an error message if the subrequest failed
        ngx.say("Error: ", res.status)
    end
end

-- Define a function to handle the subrequest
local function subrequest_handler()
    -- Return a simple response
    ngx.say("Hello from subrequest!")
end

-- Check if we're in the main request context
if ngx.var.uri == "/" then
    -- Call the main handler
    main_handler()
elseif ngx.var.uri == "/subrequest" then
    -- Call the subrequest handler
    subrequest_handler()
end
```

```nginx
# File: nginx.conf

http {
    server {
        listen 8080;

        location / {
            default_type 'text/plain';
            content_by_lua_file ngx_location_capture_example.lua;
        }

        location /subrequest {
            default_type 'text/plain';
            content_by_lua_file ngx_location_capture_example.lua;
        }
    }
}
```
