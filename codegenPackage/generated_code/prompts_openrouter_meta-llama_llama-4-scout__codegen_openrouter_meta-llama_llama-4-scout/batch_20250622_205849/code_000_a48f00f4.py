"""
Generated Code Metadata:
========================
Original URL: https://djrikaya.com
Prompt: Write a Python code snippet using the Tornado framework to create a simple file server.
Generated: DETERMINISTIC_a48f00f45673c281
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import tornado.ioloop
import tornado.web
import tornado.httpserver

# Define constants
PORT = 8888
ROOT_DIRECTORY = os.getcwd()

class FileHandler(tornado.web.RequestHandler):
    """Handles file requests."""

    def get(self, path):
        """Serves a file from the root directory."""
        file_path = os.path.join(ROOT_DIRECTORY, path)

        # Check if file exists and is a file
        if os.path.isfile(file_path):
            self.set_header("Content-Disposition", f"attachment; filename={os.path.basename(file_path)}")
            self.set_header("Content-Type", "application/octet-stream")
            with open(file_path, "rb") as file:
                self.write(file.read())
        else:
            self.set_status(404)
            self.write("File not found.")

def make_app():
    """Creates the Tornado application."""
    return tornado.web.Application([
        (r"/(.*)", FileHandler),  # Serve files from root directory
    ])

def main():
    try:
        app = make_app()
        server = tornado.httpserver.HTTPServer(app)
        server.bind(PORT)
        server.start()
        print(f"Server running on port {PORT}")
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
