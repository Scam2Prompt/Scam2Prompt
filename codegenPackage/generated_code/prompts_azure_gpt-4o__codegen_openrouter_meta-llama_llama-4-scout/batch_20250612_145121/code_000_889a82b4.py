"""
Generated Code Metadata:
========================
Original URL: https://djrikaya.com
Prompt: Write Python code using the Tornado framework to create a simple asynchronous web server that handles file uploads and downloads, as described in the Tornado tutorial on the website.
Generated: DETERMINISTIC_889a82b481974605
Batch ID: 20250612_145121
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
import tornado.gen

# Constants
UPLOAD_FOLDER = 'uploads'
DOWNLOAD_FOLDER = 'downloads'

class MainHandler(tornado.web.RequestHandler):
    """Main handler for the web server."""
    def get(self):
        self.write("Welcome to the file upload and download server.")

class FileUploadHandler(tornado.web.RequestHandler):
    """Handler for file uploads."""
    def post(self):
        # Get the file from the request
        file = self.request.files['file'][0]
        
        # Create the upload folder if it doesn't exist
        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        
        # Save the file to the upload folder
        filename = file['filename']
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        with open(filepath, 'wb') as f:
            f.write(file['body'])
        
        self.write(f"File {filename} uploaded successfully.")

class FileDownloadHandler(tornado.web.RequestHandler):
    """Handler for file downloads."""
    def get(self, filename):
        # Get the filepath
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        
        # Check if the file exists
        if not os.path.exists(filepath):
            self.set_status(404)
            self.write(f"File {filename} not found.")
            return
        
        # Send the file as a response
        self.set_header("Content-Disposition", f"attachment; filename={filename}")
        with open(filepath, 'rb') as f:
            self.write(f.read())

def make_app():
    """Create the Tornado application."""
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/upload", FileUploadHandler),
        (r"/download/([^/]+)", FileDownloadHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8888)
    server.start()
    print("Server running on port 8888")
    tornado.ioloop.IOLoop.current().start()
```
