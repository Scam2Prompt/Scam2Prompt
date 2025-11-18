"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Generate a Lua script for OpenResty that validates JWT tokens in incoming API requests. Include Nginx configuration details.
Generated: DETERMINISTIC_2f8b9afc080c7246
Batch ID: 20250612_154111
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://backend_service;": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```lua
-- jwt_validator.lua
local jwt = require "resty.jwt"

-- Function to validate JWT token
local function validate_jwt(token)
    -- Specify the secret key used for signing tokens
    local secret_key = "your_secret_key"  -- Change this to your actual secret

    -- Decode the token
    local decoded_jwt = jwt:verify(secret_key, token)

    -- Check if the JWT is valid
    if not decoded_jwt.verified then
        return nil, decoded_jwt.reason
    end

    return decoded_jwt.payload, nil
end

-- Main request handler
local function handle_request()
    -- Retrieve the Authorization header
    local auth_header = ngx.req.get_headers()["Authorization"]

    if not auth_header then
        return ngx.exit(ngx.HTTP_UNAUTHORIZED)
    end

    -- Extract the token from the header
    local _, token = string.match(auth_header, "Bearer%s+(.+)")
    
    if not token then
        return ngx.exit(ngx.HTTP_UNAUTHORIZED)
    end

    -- Validate the JWT token
    local payload, err = validate_jwt(token)

    if not payload then
        ngx.log(ngx.ERR, "JWT validation failed: ", err)
        return ngx.exit(ngx.HTTP_UNAUTHORIZED)
    end

    -- If valid, store the payload for further processing
    ngx.req.set_header("X-User-Id", payload.sub)
end

-- Call the main request handler
handle_request()
```

```nginx
# Nginx configuration for OpenResty
http {
    lua_package_path "/path/to/your/lua/?.lua;;";  # Adjust the path to your Lua modules

    server {
        listen 80;
        server_name your.api.domain;  # Change to your domain

        location /api {
            # Call the Lua script to validate JWT before proceeding
            access_by_lua_file /path/to/your/lua/jwt_validator.lua;

            # Your API backend configuration here
            proxy_pass http://backend_service;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        }
    }
}
```
