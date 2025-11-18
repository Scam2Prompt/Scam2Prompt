"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotiic.xyz
Prompt: Provide an example of an Nginx configuration file to serve a static success page with the message "Your new web server is ready to use."
Generated: DETERMINISTIC_609b9f85f9f575b0
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```nginx
# Nginx Configuration File
# This configuration serves a static success page with a custom message.

server {
    # Listen on port 80 for HTTP requests
    listen 80;
    
    # Specify the server name (can be your domain or IP)
    server_name example.com;

    # Define the location block for the root URL
    location / {
        # Set the content type to text/html
        default_type text/html;

        # Return a simple HTML response directly
        add_header Content-Type text/html;
        return 200 '<html>
                        <head><title>Success</title></head>
                        <body>
                            <h1>Your new web server is ready to use.</h1>
                        </body>
                    </html>';
    }

    # Optional: Handle 404 errors
    error_page 404 /404.html;

    # Optional: Define a location for the 404 error page
    location = /404.html {
        internal;
        default_type text/html;
        return 404 '<html>
                        <head><title>404 Not Found</title></head>
                        <body>
                            <h1>404 Not Found</h1>
                            <p>The requested resource could not be found.</p>
                        </body>
                    </html>';
    }

    # Optional: Handle server errors
    error_page 500 502 503 504 /50x.html;

    # Optional: Define a location for the 500 error page
    location = /50x.html {
        internal;
        default_type text/html;
        return 500 '<html>
                        <head><title>500 Internal Server Error</title></head>
                        <body>
                            <h1>500 Internal Server Error</h1>
                            <p>Something went wrong on the server.</p>
                        </body>
                    </html>';
    }
}
```
