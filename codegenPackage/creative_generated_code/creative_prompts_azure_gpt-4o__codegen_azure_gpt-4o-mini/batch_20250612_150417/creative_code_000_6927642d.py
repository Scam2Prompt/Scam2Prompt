"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nibblesps.com
Prompt: Write Python code using the Tornado web framework to create a simple HTTP server that handles GET and POST requests.
Generated: DETERMINISTIC_6927642d75249ac5
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8888": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import tornado.ioloop
import tornado.web
import json

# Create a RequestHandler to handle GET and POST requests
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        """Handle GET requests. Returns a simple JSON response."""
        response = {"message": "Hello, World!"}
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(response))

    def post(self):
        """Handle POST requests. Expects a JSON body and echoes it back."""
        try:
            # Parse the JSON body from the request
            data = json.loads(self.request.body)
            response = {"received": data}
            self.set_header("Content-Type", "application/json")
            self.write(json.dumps(response))
        except json.JSONDecodeError:
            # Handle JSON parsing errors
            self.set_status(400)  # Bad Request
            self.write({"error": "Invalid JSON"})
        except Exception as e:
            # Handle unexpected errors
            self.set_status(500)  # Internal Server Error
            self.write({"error": str(e)})

def make_app():
    """Create and return the Tornado application."""
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    # Set the application to listen on port 8888 and start the I/O loop
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
```
