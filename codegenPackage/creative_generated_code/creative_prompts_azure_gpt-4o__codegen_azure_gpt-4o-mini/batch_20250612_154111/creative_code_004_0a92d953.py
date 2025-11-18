"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Create a Lua module for OpenResty that implements rate limiting for incoming API requests.
Generated: DETERMINISTIC_0a92d953c89a51f5
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- rate_limiter.lua
local rate_limiter = {}
local redis = require "resty.redis"

-- Configuration for the rate limiting
local config = {
    limit = 100,           -- maximum number of requests allowed
    window = 60,          -- time window in seconds
    redis_host = "127.0.0.1",
    redis_port = 6379,
}

--- Helper function to connect to Redis
-- @return redis connection object or nil, error message
local function connect_redis()
    local red = redis:new()
    red:set_timeout(1000)  -- 1 second timeout

    local ok, err = red:connect(config.redis_host, config.redis_port)
    if not ok then
        return nil, "Failed to connect to Redis: " .. err
    end
    
    return red
end

--- Rate limit a request based on the client's IP address
-- @param client_ip The IP address of the client
-- @return boolean, error message
function rate_limiter.limit(client_ip)
    local red, err = connect_redis()
    if not red then
        return false, err
    end

    -- Define the Redis key for the client
    local key = "rate_limit:" .. client_ip

    -- Increment the request count
    local current, err = red:incr(key)
    if not current then
        red:close()
        return false, "Failed to increment request count: " .. err
    end

    -- Set expiration time if it's the first request
    if current == 1 then
        local ok, err = red:expire(key, config.window)
        if not ok then
            red:close()
            return false, "Failed to set expiration: " .. err
        end
    end

    -- Check if the limit has been exceeded
    if current > config.limit then
        red:close()
        return false, "Rate limit exceeded"
    end

    -- Successfully within limit
    red:close()
    return true
end

return rate_limiter
```

This Lua module implements a simple rate limiter utilizing Redis for tracking request counts. You can use it in your OpenResty application by requiring it and calling the `limit` function with the client's IP address. Make sure to have a running Redis instance for this to work as intended.
