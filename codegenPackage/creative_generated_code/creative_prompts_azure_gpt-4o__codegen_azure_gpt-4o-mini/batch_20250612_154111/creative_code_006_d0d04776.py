"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancekko.com
Prompt: Generate an OpenResty configuration to implement rate limiting for incoming requests using Lua.
Generated: DETERMINISTIC_d0d04776b92ce687
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# OpenResty configuration file for implementing rate limiting using Lua

# Define the rate limit parameters
lua_shared_dict rate_limit_store 10m;  # Shared memory for rate limiting
local limit_rate = 100                # Maximum requests per minute

# Function to check and update the rate limit
function check_rate_limit()
    local key = ngx.var.remote_addr  -- Use client IP address as the unique key
    local current_time = ngx.now()    -- Get the current time
    local time_window = 60             -- Time window for rate limiting (in seconds)

    local rate_limit_cache = ngx.shared.rate_limit_store
    local requests, last_time = rate_limit_cache:get(key)

    if not requests then
        -- No previous record, initialize it
        requests = 1
        last_time = current_time
        rate_limit_cache:set(key, requests, time_window)
    else
        -- Check if the request is within the time window
        if current_time - last_time < time_window then
            if requests < limit_rate then
                -- Increment the request count
                requests = requests + 1
                rate_limit_cache:set(key, requests, time_window)
            else
                -- Rate limit exceeded
                return false
            end
        else
            -- Reset the request count and timestamp after the time window
            requests = 1
            last_time = current_time
            rate_limit_cache:set(key, requests, time_window)
        end
    end

    return true
end

# Server block
server {
    listen 80;  # Listen on port 80
    server_name localhost;  # Define server name

    location / {
        # Call the rate limiting function
        if not check_rate_limit() then
            return 429;  # Return 429 Too Many Requests if rate limit exceeded
        end

        # Handle normal request processing here
        content_by_lua_block {
            ngx.say("Request successful!")
        }
    }

    # Error handling for invalid requests
    error_page 429 = @error_handling;

    # Custom error handling location
    location @error_handling {
        default_type application/json;
        add_header Content-Type application/json;
        return 429 '{"error": "Too Many Requests", "message": "Rate limit exceeded"}';
    }
}
```
