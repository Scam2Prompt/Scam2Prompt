"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: How can I use OpenResty to cache API responses for 10 minutes? Provide a Lua script and Nginx configuration.
Generated: DETERMINISTIC_3141f4e6e3a354de
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Nginx Configuration (`nginx.conf`)
```nginx
worker_processes 1;

events {
    worker_connections 1024;
}

http {
    include       mime.types;
    default_type  application/octet-stream;

    # Enable Lua modules
    lua_shared_dict my_cache 10m;

    server {
        listen 8080;
        server_name localhost;

        location /api {
            # Pass request to Lua handler
            content_by_lua_file /path/to/api_cache.lua;
        }
    }
}
```

---

### Lua Script (`api_cache.lua`)
```lua
-- Load the required OpenResty modules
local ngx = require "ngx"
local cjson = require "cjson"

-- Define the shared cache dictionary
local cache = ngx.shared.my_cache

-- Define the cache timeout (in seconds)
local CACHE_TIMEOUT = 600

-- Fetch the API response
local function fetch_api_response()
    -- Simulate an external API call (replace with actual API logic)
    local response = {
        status = "success",
        data = "Sample API response",
        timestamp = os.time()
    }
    return cjson.encode(response)
end

-- Main logic for caching and returning the response
local function get_cached_response()
    local cache_key = ngx.var.uri  -- Use request URI as cache key

    -- Check if the response is cached
    local cached_response = cache:get(cache_key)
    if cached_response then
        -- Return cached response
        ngx.say(cached_response)
        return
    end

    -- If not cached, fetch the response and cache it
    local api_response = fetch_api_response()

    -- Error handling for cache operations
    local success, err, forcible = cache:set(cache_key, api_response, CACHE_TIMEOUT)
    if not success then
        ngx.log(ngx.ERR, "Failed to cache API response: " .. err)
    elseif forcible then
        ngx.log(ngx.WARN, "Cache item was forcibly overwritten!")
    end

    -- Return the new API response
    ngx.say(api_response)
end

-- Call the function to handle caching logic
get_cached_response()
```

---

### Notes:
- Replace `/path/to/api_cache.lua` in the Nginx config with the actual path to the Lua script file.
- This script assumes that the response is in JSON format. Adjust `fetch_api_response()` as needed for your specific API logic.
- Use the `lua_shared_dict` directive to allocate shared memory for caching.
