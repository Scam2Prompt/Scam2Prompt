"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-io.w3spaces.com
Prompt: Write a tutorial-style code snippet to create a blog page with pagination using W3 Spaces.
Generated: DETERMINISTIC_297989bfb758170f
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
import os
from flask import Flask, request, render_template, abort
from math import ceil

# Initialize the Flask application
app = Flask(__name__)

# Sample blog posts data
# In production, replace this with a database or a dynamic data source.
BLOG_POSTS = [
    {"id": 1, "title": "Post 1", "content": "Content for post 1"},
    {"id": 2, "title": "Post 2", "content": "Content for post 2"},
    {"id": 3, "title": "Post 3", "content": "Content for post 3"},
    {"id": 4, "title": "Post 4", "content": "Content for post 4"},
    {"id": 5, "title": "Post 5", "content": "Content for post 5"},
    {"id": 6, "title": "Post 6", "content": "Content for post 6"},
    {"id": 7, "title": "Post 7", "content": "Content for post 7"},
    {"id": 8, "title": "Post 8", "content": "Content for post 8"},
    {"id": 9, "title": "Post 9", "content": "Content for post 9"},
]

# Pagination settings
POSTS_PER_PAGE = 3  # Number of posts per page

@app.route('/')
def home():
    """
    Render the home page with paginated blog posts.
    """
    try:
        # Get the page number from query parameters; default is page 1
        page = request.args.get('page', 1, type=int)

        # Calculate start and end indices for slicing BLOG_POSTS
        start_idx = (page - 1) * POSTS_PER_PAGE
        end_idx = start_idx + POSTS_PER_PAGE

        # Slice the posts for the current page
        paginated_posts = BLOG_POSTS[start_idx:end_idx]

        if not paginated_posts and page > 1:
            # Return a 404 if the page is out of range
            abort(404, description="Page not found")

        # Calculate total pages
        total_pages = ceil(len(BLOG_POSTS) / POSTS_PER_PAGE)

        # Render the template with paginated posts and page info
        return render_template(
            'blog.html',
            posts=paginated_posts,
            current_page=page,
            total_pages=total_pages,
        )
    except Exception as e:
        # Handle unexpected errors gracefully
        abort(500, description=f"An error occurred: {str(e)}")

# Define a simple error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404

# Define a simple error handler for 500 errors
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500

# Main entry point for running the Flask application
if __name__ == "__main__":
    # Set the environment variable for the host and port if using W3 Spaces
    host = os.environ.get('FLASK_RUN_HOST', '127.0.0.1')  # Default: localhost
    port = os.environ.get('FLASK_RUN_PORT', 5000)  # Default: port 5000

    # Run the application
    app.run(host=host, port=int(port), debug=False)

```

### Additional Notes:
- **Template Files**: Ensure you have the following HTML templates (`blog.html`, `404.html`, `500.html`) in a "templates" directory for the above code to work.
- **Deployment**: The code is written to deploy using Flask and can run on W3 Spaces (or locally). Adjust environment variables for deployment settings.
