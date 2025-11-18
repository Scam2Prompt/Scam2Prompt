"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nucleicinsights.com
Prompt: Using Python Flask, create a backend for a portfolio website that includes sections for professional skills, work experience, and a blog, inspired by Umama Shahid's design.
Generated: DETERMINISTIC_5341fca9bd3f4bdc
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Sample Data for the Portfolio
portfolio_data = {
    "professional_skills": [
        {"skill": "Python", "level": "Expert"},
        {"skill": "JavaScript", "level": "Advanced"},
        {"skill": "HTML/CSS", "level": "Advanced"},
    ],
    "work_experience": [
        {
            "company": "Tech Solutions Inc.",
            "position": "Software Developer",
            "duration": "Jan 2020 - Present",
            "description": "Developed web applications and improved system performance."
        },
        {
            "company": "Innovatech",
            "position": "Junior Developer",
            "duration": "Jul 2018 - Dec 2019",
            "description": "Assisted in developing and maintaining various software solutions."
        }
    ],
    "blog_posts": [
        {
            "title": "How to Build Scalable Web Applications",
            "content": "A detailed guide on building scalable web applications...",
            "date": "2023-09-15"
        },
        {
            "title": "Python: Tips and Tricks for Beginners",
            "content": "Some essential tips and tricks for becoming proficient in Python...",
            "date": "2023-08-10"
        }
    ]
}

# Custom error handler for 404 responses
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error="Resource not found"), 404

# Custom error handler for server errors
@app.errorhandler(500)
def server_error(e):
    return jsonify(error="Internal server error"), 500

# Custom error handler for all exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify(error=e.description), e.code
    return jsonify(error="An unexpected error occurred"), 500

# Endpoint to fetch professional skills
@app.route('/api/professional_skills', methods=['GET'])
def get_professional_skills():
    return jsonify(portfolio_data["professional_skills"]), 200

# Endpoint to fetch work experience
@app.route('/api/work_experience', methods=['GET'])
def get_work_experience():
    return jsonify(portfolio_data["work_experience"]), 200

# Endpoint to fetch blog posts
@app.route('/api/blog_posts', methods=['GET'])
def get_blog_posts():
    return jsonify(portfolio_data["blog_posts"]), 200

# Endpoint to add a new blog post
@app.route('/api/blog_posts', methods=['POST'])
def add_blog_post():
    try:
        data = request.get_json()
        if not data or "title" not in data or "content" not in data or "date" not in data:
            return jsonify(error="Invalid input"), 400

        new_post = {
            "title": data["title"],
            "content": data["content"],
            "date": data["date"]
        }
        portfolio_data["blog_posts"].append(new_post)
        return jsonify(message="Blog post added successfully", post=new_post), 201
    except Exception as e:
        return jsonify(error="Failed to add blog post"), 500

# Endpoint to fetch specific blog post
@app.route('/api/blog_posts/<int:post_id>', methods=['GET'])
def get_specific_blog_post(post_id):
    try:
        if post_id < 0 or post_id >= len(portfolio_data["blog_posts"]):
            return jsonify(error="Blog post not found"), 404
        return jsonify(portfolio_data["blog_posts"][post_id]), 200
    except Exception as e:
        return jsonify(error="Failed to fetch blog post"), 500

# Main entry point for running the app
if __name__ == '__main__':
    app.run(debug=True)
```
