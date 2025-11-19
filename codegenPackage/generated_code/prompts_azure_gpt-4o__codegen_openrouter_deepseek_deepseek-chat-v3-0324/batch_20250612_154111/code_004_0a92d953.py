"""
Generated Code Metadata:
========================
Original URL: https://enhancedkk.com
Prompt: Create a Lua module for OpenResty that implements rate limiting for incoming API requests.
Generated: DETERMINISTIC_0a92d953c89a51f5
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```lua
-- rate_limiter.lua
local _M = {}

local resty_lock = require "resty.lock"
local resty_lrucache = require "resty.lrucache"
local ngx = ngx
local tonumber = tonumber
local tostring = tostring
local error = error
local pairs = pairs
local math = math
local os = os

-- Default configuration
local DEFAULT_CONFIG = {
    window = 60, -- time window in seconds
    limit = 100, -- max requests per window
    key_prefix = "rl:", -- redis key prefix
    cache_size = 1000, -- LRU cache size
    cache_ttl = 60, -- cache TTL in seconds
    redis_host = "127.0.0.1",
    redis_port = 6379,
    redis_timeout = 1000, -- in ms
    redis_password = nil,
    redis_database = 0,
}

-- Initialize the module
function _M.new(self, config)
    local instance = {}
    setmetatable(instance, { __index = _M })

    -- Merge default config with user config
    instance.config = {}
    for k, v in pairs(DEFAULT_CONFIG) do
        instance.config[k] = config[k] or v
    end

    -- Initialize LRU cache
    instance.cache, err = resty_lrucache.new(instance.config.cache_size)
    if not instance.cache then
        return nil, "failed to create LRU cache: " .. (err or "unknown")
    end

    -- Initialize Redis connection
    local redis = require "resty.redis"
    instance.redis = redis:new()
    instance.redis:set_timeout(instance.config.redis_timeout)

    return instance
end

-- Connect to Redis
local function connect_redis(self)
    local ok, err = self.redis:connect(self.config.redis_host, self.config.redis_port)
    if not ok then
        return nil, "failed to connect to Redis: " .. (err or "unknown")
    end

    if self.config.redis_password then
        local ok, err = self.redis:auth(self.config.redis_password)
        if not ok then
            return nil, "failed to authenticate with Redis: " .. (err or "unknown")
        end
    end

    if self.config.redis_database ~= 0 then
        local ok, err = self.redis:select(self.config.redis_database)
        if not ok then
            return nil, "failed to select Redis database: " .. (err or "unknown")
        end
    end

    return true
end

-- Generate rate limit key
local function generate_key(self, identifier)
    local current_time = math.floor(ngx.now() / self.config.window)
    return self.config.key_prefix .. identifier .. ":" .. tostring(current_time)
end

-- Check rate limit using token bucket algorithm
function _M.check(self, identifier)
    if not identifier or identifier == "" then
        return nil, "identifier cannot be empty"
    end

    -- Try to get from cache first
    local cached = self.cache:get(identifier)
    if cached then
        if cached.remaining < 0 then
            return nil, "rate limit exceeded", cached.remaining, cached.reset
        end
        return cached.remaining, nil, cached.remaining, cached.reset
    end

    -- Use lock to prevent thundering herd
    local lock, err = resty_lock:new("rate_limit_lock", { exptime = 10, timeout = 5 })
    if not lock then
        return nil, "failed to create lock: " .. (err or "unknown")
    end

    local elapsed, err = lock:lock(identifier)
    if not elapsed then
        return nil, "failed to acquire lock: " .. (err or "unknown")
    end

    -- Release lock when done
    local function unlock()
        local ok, err = lock:unlock()
        if not ok then
            ngx.log(ngx.ERR, "failed to unlock: ", err)
        end
    end

    -- Connect to Redis
    local ok, err = connect_redis(self)
    if not ok then
        unlock()
        return nil, err
    end

    -- Generate key
    local key = generate_key(self, identifier)
    local now = ngx.now()
    local reset = math.ceil(now / self.config.window) * self.config.window

    -- Use Redis to count requests
    local remaining, err
    local newval, err = self.redis:incr(key)
    if not newval then
        unlock()
        return nil, "failed to increment Redis key: " .. (err or "unknown")
    end

    if newval == 1 then
        -- First request in this window, set expiration
        local ok, err = self.redis:expire(key, self.config.window)
        if not ok then
            unlock()
            return nil, "failed to set Redis key expiration: " .. (err or "unknown")
        end
        remaining = self.config.limit - newval
    else
        remaining = self.config.limit - newval
    end

    -- Keep Redis connection alive
    self.redis:set_keepalive(10000, 100)

    -- Prepare result
    local result = {
        remaining = remaining,
        limit = self.config.limit,
        reset = reset
    }

    -- Cache the result
    self.cache:set(identifier, result, self.config.cache_ttl)

    unlock()

    if remaining < 0 then
        return nil, "rate limit exceeded", remaining, reset
    end

    return remaining, nil, remaining, reset
end

-- Get rate limit headers
function _M.get_headers(self, remaining, limit, reset)
    return {
        ["X-RateLimit-Limit"] = limit,
        ["X-RateLimit-Remaining"] = math.max(0, remaining),
        ["X-RateLimit-Reset"] = reset
    }
end

return _M
```
