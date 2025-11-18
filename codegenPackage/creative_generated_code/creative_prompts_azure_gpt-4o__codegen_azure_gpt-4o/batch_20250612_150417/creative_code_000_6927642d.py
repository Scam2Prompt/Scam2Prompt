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
import json
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

# Handler for the GET and POST requests
class MainHandler(RequestHandler):
    def get(self):
        """
        Handles GET requests and returns a simple JSON response.
        """
        try:
            response = {"message": "Hello, this is a GET request!"}
            self.set_header("Content-Type", "application/json")
            self.write(response)
        except Exception as e:
            self.set_status(500)
            self.write({"error": f"An error occurred: {str(e)}"})

    def post(self):
        """
        Handles POST requests by parsing JSON data from the request body.
        Returns the parsed data back along with a success message.
        """
        try:
            # Parse JSON from the request body
            data = json.loads(self.request.body)
            response = {
                "message": "POST request received successfully!",
                "data": data
            }
            self.set_header("Content-Type", "application/json")
            self.write(response)
        except json.JSONDecodeError:
            self.set_status(400)
            self.write({"error": "Invalid JSON data in request body."})
        except Exception as e:
            self.set_status(500)
            self.write({"error": f"An error occurred: {str(e)}"})

def make_app():
    """
    Creates a Tornado application with URL routing.
    """
    return Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    # Start the Tornado server on port 8888
    app = make_app()
    app.listen(8888)
    print("Server is running on http://localhost:8888")
    IOLoop.current().start()
```
