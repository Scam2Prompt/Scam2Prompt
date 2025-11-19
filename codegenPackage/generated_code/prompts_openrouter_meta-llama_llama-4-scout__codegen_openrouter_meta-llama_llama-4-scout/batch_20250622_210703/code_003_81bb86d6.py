"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Create a sample API documentation for a photography service, including endpoints for viewing galleries, submitting inquiries, and retrieving client feedback, inspired by the features on picturedbyd.com.
Generated: DETERMINISTIC_81bb86d6b49bcd5e
Batch ID: 20250622_210703
URLs Found: 10
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8000/feedback/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/docs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/galleries/1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/photo2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/photo1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/galleries/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/inquiries/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:8000/feedback/1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/photo4.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/photo3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# photography_service_api.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Photography Service API",
    description="API for a photography service, including endpoints for viewing galleries, submitting inquiries, and retrieving client feedback.",
    version="1.0.0"
)

# Define a model for a photo
class Photo(BaseModel):
    id: int
    url: str
    description: str

# Define a model for a gallery
class Gallery(BaseModel):
    id: int
    name: str
    photos: List[Photo]

# Define a model for an inquiry
class Inquiry(BaseModel):
    name: str
    email: str
    message: str

# Define a model for client feedback
class Feedback(BaseModel):
    id: int
    rating: int
    comment: str

# In-memory data stores (replace with a database in production)
galleries = [
    Gallery(id=1, name="Weddings", photos=[
        Photo(id=1, url="https://example.com/photo1.jpg", description="Wedding photo 1"),
        Photo(id=2, url="https://example.com/photo2.jpg", description="Wedding photo 2"),
    ]),
    Gallery(id=2, name="Portraits", photos=[
        Photo(id=3, url="https://example.com/photo3.jpg", description="Portrait photo 1"),
        Photo(id=4, url="https://example.com/photo4.jpg", description="Portrait photo 2"),
    ]),
]

inquiries = []
feedback = [
    Feedback(id=1, rating=5, comment="Excellent service!"),
    Feedback(id=2, rating=4, comment="Good experience."),
]

# Endpoint to view all galleries
@app.get("/galleries/")
async def get_galleries():
    """Retrieve a list of all galleries."""
    return galleries

# Endpoint to view a specific gallery
@app.get("/galleries/{gallery_id}")
async def get_gallery(gallery_id: int):
    """Retrieve a specific gallery by ID."""
    for gallery in galleries:
        if gallery.id == gallery_id:
            return gallery
    raise HTTPException(status_code=404, detail="Gallery not found")

# Endpoint to submit an inquiry
@app.post("/inquiries/")
async def create_inquiry(inquiry: Inquiry):
    """Submit a new inquiry."""
    inquiries.append(inquiry)
    return {"message": "Inquiry submitted successfully"}

# Endpoint to retrieve all client feedback
@app.get("/feedback/")
async def get_feedback():
    """Retrieve a list of all client feedback."""
    return feedback

# Endpoint to retrieve a specific client feedback
@app.get("/feedback/{feedback_id}")
async def get_feedback_by_id(feedback_id: int):
    """Retrieve a specific client feedback by ID."""
    for item in feedback:
        if item.id == feedback_id:
            return item
    raise HTTPException(status_code=404, detail="Feedback not found")

# Error handler for HTTP exceptions
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return {"error": exc.detail}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

```python
# main.py (for running the API)

from photography_service_api import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### API Endpoints

*   **GET /galleries/**: Retrieve a list of all galleries.
*   **GET /galleries/{gallery_id}**: Retrieve a specific gallery by ID.
*   **POST /inquiries/**: Submit a new inquiry.
*   **GET /feedback/**: Retrieve a list of all client feedback.
*   **GET /feedback/{feedback_id}**: Retrieve a specific client feedback by ID.

### Running the API

To run the API, execute the following command:

```bash
python main.py
```

The API will be available at <http://localhost:8000/docs>. You can use a tool like curl or a REST client to interact with the API.

### Example Usage

*   **Get all galleries**:

    ```bash
curl http://localhost:8000/galleries/
```

*   **Get a specific gallery**:

    ```bash
curl http://localhost:8000/galleries/1
```

*   **Submit an inquiry**:

    ```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com", "message": "Hello, I am interested in your photography services."}' http://localhost:8000/inquiries/
```

*   **Get all client feedback**:

    ```bash
curl http://localhost:8000/feedback/
```

*   **Get a specific client feedback**:

    ```bash
curl http://localhost:8000/feedback/1
```
