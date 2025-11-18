"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digielearning.in
Prompt: Write code to implement a "Live Preview" feature for e-books, allowing users to read sample pages before subscribing, as seen on Digielearning.
Generated: DETERMINISTIC_b0e959aa17319271
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import flask
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data representing e-books stored in a database
ebooks = {
    1: {
        "title": "Python Programming Essentials",
        "author": "John Doe",
        "content": [
            "Page 1: Introduction to Python",
            "Page 2: Setting up your environment",
            "Page 3: Variables and Data Types",
            "Page 4: Control Flow",
            "Page 5: Functions",
        ],
        "preview_pages": 3,  # Number of pages available for preview
    },
    2: {
        "title": "Learn Web Development",
        "author": "Jane Smith",
        "content": [
            "Page 1: Basics of HTML",
            "Page 2: Getting Started with CSS",
            "Page 3: Introduction to JavaScript",
            "Page 4: Server-side Programming",
            "Page 5: Building a Web Application",
        ],
        "preview_pages": 2,  # Number of pages available for preview
    },
}

@app.route("/")
def home():
    """Render the home page with a list of available e-books."""
    return render_template("home.html", ebooks=ebooks)

@app.route("/preview/<int:ebook_id>")
def preview_ebook(ebook_id):
    """
    Endpoint to provide a live preview of an e-book.
    Users can read sample pages specified in the preview_pages field.
    """
    try:
        ebook = ebooks.get(ebook_id)
        if not ebook:
            return jsonify({"error": "E-book not found"}), 404

        preview_content = ebook["content"][: ebook["preview_pages"]]
        return render_template(
            "preview.html",
            title=ebook["title"],
            author=ebook["author"],
            preview_content=preview_content,
        )
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

### Additional Notes:
- This code assumes the existence of templates `home.html` and `preview.html` for rendering the home page and preview pages, respectively.
- To run the code, install Flask using `pip install flask`.
