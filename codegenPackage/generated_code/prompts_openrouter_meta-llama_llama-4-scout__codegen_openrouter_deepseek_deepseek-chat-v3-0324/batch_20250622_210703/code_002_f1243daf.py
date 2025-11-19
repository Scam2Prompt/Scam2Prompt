"""
Generated Code Metadata:
========================
Original URL: https://36destinations.com
Prompt: Generate a short "Hello World" style post for a new travel blog, similar to the content on 36destinations.com.
Generated: DETERMINISTIC_f1243daf018134d6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
travel_blog_post.py
A simple 'Hello World' style post for a new travel blog.
"""

def generate_blog_post():
    """
    Generates a welcome post for a new travel blog.
    
    Returns:
        str: Formatted blog post HTML content
    """
    post_title = "Welcome to Our Travel Adventures!"
    post_date = "June 1, 2023"
    author = "The Travel Team"
    
    content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{post_title}</title>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                line-height: 1.6;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                color: #333;
            }}
            h1 {{
                color: #2c3e50;
                border-bottom: 2px solid #3498db;
                padding-bottom: 10px;
            }}
            .meta {{
                font-style: italic;
                color: #7f8c8d;
                margin-bottom: 30px;
            }}
            .content {{
                margin-top: 20px;
            }}
        </style>
    </head>
    <body>
        <h1>{post_title}</h1>
        <div class="meta">
            Posted on {post_date} by {author}
        </div>
        <div class="content">
            <p>Hello fellow travelers!</p>
            <p>We're thrilled to launch this new space where we'll share our journeys, tips, 
            and unforgettable experiences from around the globe. From hidden gems to popular 
            destinations, we'll take you along on our adventures.</p>
            <p>Our first official post is coming soon, but in the meantime, pack your bags 
            (metaphorically, for now) and get ready to explore the world with us!</p>
            <p>Where should our first destination be? Let us know in the comments!</p>
        </div>
    </body>
    </html>
    """
    
    return content

if __name__ == "__main__":
    print(generate_blog_post())
```
