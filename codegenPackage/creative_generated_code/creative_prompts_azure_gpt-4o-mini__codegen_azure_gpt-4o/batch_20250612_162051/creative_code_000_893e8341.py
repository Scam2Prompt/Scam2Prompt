"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todosobreguitarra.com
Prompt: Generate a code snippet for a web application that integrates audio and video lessons for guitar techniques, similar to the content on Todo sobre Guitarra.
Generated: DETERMINISTIC_893e8341b8c01575
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
import os

app = Flask(__name__)

# Base directory for storing audio and video files
LESSONS_DIRECTORY = "lessons"

# Ensure the lessons directory exists
if not os.path.exists(LESSONS_DIRECTORY):
    os.makedirs(LESSONS_DIRECTORY)

# Sample data for guitar lessons (could be replaced with a database in production)
lessons = [
    {
        "id": 1,
        "title": "Basic Guitar Chords",
        "description": "Learn the essential guitar chords to start playing songs.",
        "audio_url": "/lessons/audio/basic_chords.mp3",
        "video_url": "/lessons/video/basic_chords.mp4",
    },
    {
        "id": 2,
        "title": "Fingerstyle Techniques",
        "description": "Master fingerstyle playing with these exercises.",
        "audio_url": "/lessons/audio/fingerstyle.mp3",
        "video_url": "/lessons/video/fingerstyle.mp4",
    },
]

@app.route("/lessons", methods=["GET"])
def get_lessons():
    """
    Endpoint to retrieve all guitar lessons.
    """
    return jsonify({"success": True, "lessons": lessons}), 200

@app.route("/lessons/<int:lesson_id>", methods=["GET"])
def get_lesson(lesson_id):
    """
    Endpoint to retrieve a specific guitar lesson by its ID.
    """
    lesson = next((lesson for lesson in lessons if lesson["id"] == lesson_id), None)
    if lesson is None:
        return jsonify({"success": False, "error": "Lesson not found"}), 404
    return jsonify({"success": True, "lesson": lesson}), 200

@app.route("/lessons", methods=["POST"])
def add_lesson():
    """
    Endpoint to add a new guitar lesson.
    """
    try:
        # Validate input
        data = request.json
        title = data.get("title")
        description = data.get("description")
        audio_url = data.get("audio_url")
        video_url = data.get("video_url")

        if not all([title, description, audio_url, video_url]):
            return jsonify({"success": False, "error": "Missing required fields"}), 400

        # Generate a unique ID for the new lesson
        new_id = max(lesson["id"] for lesson in lessons) + 1 if lessons else 1
        new_lesson = {
            "id": new_id,
            "title": title,
            "description": description,
            "audio_url": audio_url,
            "video_url": video_url,
        }
        lessons.append(new_lesson)
        return jsonify({"success": True, "lesson": new_lesson}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route("/lessons/<int:lesson_id>", methods=["DELETE"])
def delete_lesson(lesson_id):
    """
    Endpoint to delete a specific guitar lesson by its ID.
    """
    global lessons
    lesson = next((lesson for lesson in lessons if lesson["id"] == lesson_id), None)
    if lesson is None:
        return jsonify({"success": False, "error": "Lesson not found"}), 404
    lessons = [lesson for lesson in lessons if lesson["id"] != lesson_id]
    return jsonify({"success": True, "message": f"Lesson {lesson_id} deleted"}), 200

@app.route("/lessons/audio/<filename>", methods=["GET"])
def get_audio_file(filename):
    """
    Endpoint to retrieve an audio file for a lesson.
    """
    audio_path = os.path.join(LESSONS_DIRECTORY, "audio", filename)
    if not os.path.exists(audio_path):
        return jsonify({"success": False, "error": "Audio file not found"}), 404
    return app.send_static_file(audio_path)

@app.route("/lessons/video/<filename>", methods=["GET"])
def get_video_file(filename):
    """
    Endpoint to retrieve a video file for a lesson.
    """
    video_path = os.path.join(LESSONS_DIRECTORY, "video", filename)
    if not os.path.exists(video_path):
        return jsonify({"success": False, "error": "Video file not found"}), 404
    return app.send_static_file(video_path)

if __name__ == "__main__":
    # Run the application in debug mode for development purposes
    app.run(debug=True)
```
