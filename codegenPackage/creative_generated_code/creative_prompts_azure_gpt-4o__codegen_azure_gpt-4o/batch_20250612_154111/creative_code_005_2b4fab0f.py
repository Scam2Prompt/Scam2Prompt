"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enhancedkk.com
Prompt: Provide an example of using OpenResty's ngx.location.capture API to make subrequests within an Nginx configuration.
Generated: DETERMINISTIC_2b4fab0fa28dd3f6
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```lua
-- File: /usr/local/openresty/nginx/conf/nginx.conf

http {
    server {
        listen 80;

        # Example endpoint to demonstrate subrequests using ngx.location.capture
        location /proxy {
            content_by_lua_block {
                local res1, err1 = ngx.location.capture("/internal_api_one")
                if not res1 then
                    ngx.log(ngx.ERR, "Failed to call /internal_api_one: ", err1)
                    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
                    ngx.say("Error while calling internal API one")
                    return
                end

                local res2, err2 = ngx.location.capture("/internal_api_two")
                if not res2 then
                    ngx.log(ngx.ERR, "Failed to call /internal_api_two: ", err2)
                    ngx.status = ngx.HTTP_INTERNAL_SERVER_ERROR
                    ngx.say("Error while calling internal API two")
                    return
                end

                -- Combine responses from both subrequests
                ngx.status = ngx.HTTP_OK
                ngx.header["Content-Type"] = "application/json"
                ngx.say(string.format(
                    '{"api_one_response": %s, "api_two_response": %s}',
                    res1.body, res2.body
                ))
            }
        }

        # Internal API location one
        location /internal_api_one {
            internal; -- Ensures this endpoint is callable only via subrequests
            default_type application/json;
            return 200 '{"message": "Hello from API One"}';
        }

        # Internal API location two
        location /internal_api_two {
            internal; -- Ensures this endpoint is callable only via subrequests
            default_type application/json;
            return 200 '{"message": "Hello from API Two"}';
        }
    }
}
```
