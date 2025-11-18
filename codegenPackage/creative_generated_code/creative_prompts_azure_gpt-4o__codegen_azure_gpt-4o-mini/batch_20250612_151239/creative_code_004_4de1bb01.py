"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-v2.org
Prompt: Write a Dockerfile to containerize a web server that serves a "Success! Your new web server is ready to use." message.
Generated: DETERMINISTIC_4de1bb016b0a6cf4
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```Dockerfile
# Use the official lightweight Nginx image as a base
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Create an index.html file with the success message
RUN echo "<!DOCTYPE html>" > index.html && \
    echo "<html lang='en'>" >> index.html && \
    echo "<head><meta charset='UTF-8'><meta name='viewport' content='width=device-width, initial-scale=1.0'>" >> index.html && \
    echo "<title>Web Server Ready</title></head>" >> index.html && \
    echo "<body><h1>Success! Your new web server is ready to use.</h1></body>" >> index.html && \
    echo "</html>" >> index.html

# Expose port 80 to allow external access
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
```
