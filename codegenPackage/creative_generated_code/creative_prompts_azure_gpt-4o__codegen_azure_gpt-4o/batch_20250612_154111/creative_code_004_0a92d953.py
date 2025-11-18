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
-- A Lua module for OpenResty to implement rate limiting for incoming API requests.

local redis = require "resty.redis"

local _M = {}
_M.__index = _M

-- Default configuration values
local DEFAULT_RATE_LIMIT = 100 -- Maximum requests allowed per time window
local DEFAULT_TIME_WINDOW = 60 -- Time window in seconds

-- Initialize the rate limiter with configuration
function _M.new(rate_limit, time_window, redis_host, redis_port)
    local self = setmetatable({}, _M)
    self.rate_limit = rate_limit or DEFAULT_RATE_LIMIT
    self.time_window = time_window or DEFAULT_TIME_WINDOW
    self.redis_host = redis_host or "127.0.0.1"
    self.redis_port = redis_port or 6379
    return self
end

-- Connect to Redis
local function connect_to_redis(redis_host, redis_port)
    local red = redis:new()
    red:set_timeout(1000) -- Set timeout to 1 second

    local ok, err = red:connect(redis_host, redis_port)
    if not ok then
        return nil, "Failed to connect to Redis: " .. err
    end

    return red, nil
end

-- Function to check and update the rate limit for a given key (client IP or API token)
function _M:check_rate_limit(key)
    if not key then
        return false, "Key must be provided for rate limiting."
    end

    -- Connect to Redis
    local red, err = connect_to_redis(self.redis_host, self.redis_port)
    if not red then
        return false, err
    end

    local current_time = ngx.time()
    local redis_key = "rate_limit:" .. key
    local expire_at_key = redis_key .. ":expire_at"

    -- Start a Redis transaction (pipeline)
    red:init_pipeline()
    red:get(redis_key) -- Get the current request count
    red:get(expire_at_key) -- Get the expiration timestamp
    local results, exec_err = red:commit_pipeline()

    if not results then
        return false, "Failed to execute Redis pipeline: " .. exec_err
    end

    local request_count = tonumber(results[1]) or 0
    local expire_at = tonumber(results[2]) or (current_time + self.time_window)

    -- Check if the time window has expired
    if current_time >= expire_at then
        request_count = 0 -- Reset count if time window expired
        expire_at = current_time + self.time_window
    end

    -- If request count exceeds the limit, block the request
    if request_count >= self.rate_limit then
        return false, "Rate limit exceeded."
    end

    -- Increment the request count and update expiration timestamp
    red:init_pipeline()
    red:incr(redis_key) -- Increment the request count
    red:expireat(redis_key, expire_at) -- Set expiration time
    red:set(expire_at_key, expire_at) -- Update expiration timestamp
    local _, update_err = red:commit_pipeline()

    if update_err then
        return false, "Failed to update Redis keys: " .. update_err
    end

    return true, nil
end

-- Close Redis connection
local function close_redis(red)
    if red then
        local ok, err = red:set_keepalive(10000, 100)
        if not ok then
            ngx.log(ngx.ERR, "Failed to set Redis keepalive: " .. err)
        end
    end
end

return _M
```
