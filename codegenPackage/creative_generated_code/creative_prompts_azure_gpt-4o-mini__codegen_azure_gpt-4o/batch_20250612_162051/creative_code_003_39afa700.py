"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todosobreguitarra.com
Prompt: Suggest an API for managing online guitar courses and integrating video tutorials, based on the offerings from Todo sobre Guitarra.
Generated: DETERMINISTIC_39afa7008679bc0c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import uuid

app = Flask(__name__)

# Data storage (mock database for demonstration purposes)
courses = {}
video_tutorials = {}

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Routes

@app.route('/api/courses', methods=['GET'])
def get_courses():
    """
    Get all guitar courses.
    Returns a list of all available courses.
    """
    return jsonify({"courses": list(courses.values())}), 200

@app.route('/api/courses/<course_id>', methods=['GET'])
def get_course(course_id):
    """
    Get a specific guitar course by ID.
    """
    course = courses.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404
    return jsonify({"course": course}), 200

@app.route('/api/courses', methods=['POST'])
def create_course():
    """
    Create a new guitar course.
    Expects JSON payload with 'name' and 'description' keys.
    """
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        if not name or not description:
            return jsonify({"error": "Name and description are required"}), 400

        course_id = str(uuid.uuid4())  # Generate unique ID for course
        courses[course_id] = {"id": course_id, "name": name, "description": description}

        return jsonify({"course": courses[course_id]}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create course: {str(e)}"}), 500

@app.route('/api/courses/<course_id>', methods=['PUT'])
def update_course(course_id):
    """
    Update an existing guitar course.
    Expects JSON payload with 'name' and/or 'description' keys.
    """
    course = courses.get(course_id)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')

        if name:
            course['name'] = name
        if description:
            course['description'] = description

        return jsonify({"course": course}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to update course: {str(e)}"}), 500

@app.route('/api/courses/<course_id>', methods=['DELETE'])
def delete_course(course_id):
    """
    Delete a guitar course by ID.
    """
    course = courses.pop(course_id, None)
    if not course:
        return jsonify({"error": "Course not found"}), 404

    return jsonify({"message": f"Course {course_id} deleted successfully"}), 200

@app.route('/api/courses/<course_id>/videos', methods=['GET'])
def get_videos(course_id):
    """
    Get all video tutorials for a specific guitar course.
    """
    if course_id not in courses:
        return jsonify({"error": "Course not found"}), 404

    course_videos = [video for video in video_tutorials.values() if video['course_id'] == course_id]
    return jsonify({"videos": course_videos}), 200

@app.route('/api/videos', methods=['POST'])
def create_video():
    """
    Create a new video tutorial.
    Expects JSON payload with 'title', 'url', and 'course_id' keys.
    """
    try:
        data = request.get_json()
        title = data.get('title')
        url = data.get('url')
        course_id = data.get('course_id')

        if not title or not url or not course_id:
            return jsonify({"error": "Title, URL, and Course ID are required"}), 400

        if course_id not in courses:
            return jsonify({"error": "Course not found"}), 404

        video_id = str(uuid.uuid4())  # Generate unique ID for video
        video_tutorials[video_id] = {"id": video_id, "title": title, "url": url, "course_id": course_id}

        return jsonify({"video": video_tutorials[video_id]}), 201
    except Exception as e:
        return jsonify({"error": f"Failed to create video: {str(e)}"}), 500

@app.route('/api/videos/<video_id>', methods=['DELETE'])
def delete_video(video_id):
    """
    Delete a video tutorial by ID.
    """
    video = video_tutorials.pop(video_id, None)
    if not video:
        return jsonify({"error": "Video not found"}), 404

    return jsonify({"message": f"Video {video_id} deleted successfully"}), 200

# Server startup
if __name__ == '__main__':
    app.run(debug=True)
```
