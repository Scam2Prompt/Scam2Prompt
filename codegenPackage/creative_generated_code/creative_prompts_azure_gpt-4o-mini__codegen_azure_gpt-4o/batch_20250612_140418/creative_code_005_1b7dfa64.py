"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-ai.web.app
Prompt: Develop a simple web application that allows users to view and evaluate AI start-up projects listed on the InQubeta platform.
Generated: DETERMINISTIC_1b7dfa644d1308dd
Batch ID: 20250612_140418
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for a simple web application using Python and Flask for the backend and HTML/CSS/JavaScript for the frontend. This application allows users to view and evaluate AI start-up projects.

---

### Backend (`app.py`)

```python
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Mock data for AI projects
PROJECTS = [
    {"id": 1, "name": "AI Project Alpha", "description": "A cutting-edge AI project for healthcare.", "rating": 0, "votes": 0},
    {"id": 2, "name": "AI Project Beta", "description": "AI-powered analysis for financial markets.", "rating": 0, "votes": 0},
    {"id": 3, "name": "AI Project Gamma", "description": "AI-based educational tools for schools.", "rating": 0, "votes": 0},
]

@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")

@app.route("/api/projects", methods=["GET"])
def get_projects():
    """API endpoint to fetch all projects."""
    return jsonify(PROJECTS)

@app.route("/api/evaluate/<int:project_id>", methods=["POST"])
def evaluate_project(project_id):
    """
    API endpoint to evaluate a project.
    Expects a JSON payload: {"rating": <value between 1 and 5>}
    """
    try:
        # Get the rating from the request body
        data = request.get_json()
        rating = data.get("rating")
        
        # Validate the rating
        if not (1 <= rating <= 5):
            return jsonify({"error": "Rating must be between 1 and 5."}), 400

        # Find the project
        project = next((p for p in PROJECTS if p["id"] == project_id), None)
        if not project:
            return jsonify({"error": "Project not found."}), 404

        # Update the project's rating and votes
        project["votes"] += 1
        project["rating"] = ((project["rating"] * (project["votes"] - 1)) + rating) / project["votes"]
        
        return jsonify(project), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

---

### Frontend (`templates/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>InQubeta Projects</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>InQubeta - AI Start-up Projects</h1>
    </header>
    <main>
        <section id="project-list">
            <h2>AI Projects</h2>
            <div id="projects"></div>
        </section>
    </main>
    <script src="/static/scripts.js"></script>
</body>
</html>
```

---

### Frontend Styles (`static/styles.css`)

```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f9;
}

header {
    background-color: #556cd6;
    color: white;
    text-align: center;
    padding: 1em 0;
}

main {
    padding: 20px;
}

#project-list {
    max-width: 800px;
    margin: 0 auto;
}

.project {
    background-color: #ffffff;
    margin: 10px 0;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
}

.project h3 {
    margin: 0;
    font-size: 1.5em;
}

.project p {
    margin: 5px 0;
}

.project button {
    background-color: #556cd6;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

.project button:hover {
    background-color: #405bb5;
}
```

---

### Frontend Logic (`static/scripts.js`)

```javascript
document.addEventListener("DOMContentLoaded", () => {
    const projectsContainer = document.getElementById("projects");

    // Fetch projects from the backend and display them
    fetch("/api/projects")
        .then(response => response.json())
        .then(projects => {
            projects.forEach(project => {
                const projectDiv = document.createElement("div");
                projectDiv.classList.add("project");
                projectDiv.innerHTML = `
                    <h3>${project.name}</h3>
                    <p>${project.description}</p>
                    <p>Rating: ${project.rating.toFixed(2)} (Votes: ${project.votes})</p>
                    <label for="rating-${project.id}">Your Rating:</label>
                    <select id="rating-${project.id}" class="rating">
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                    </select>
                    <button onclick="submitRating(${project.id})">Submit Rating</button>
                `;
                projectsContainer.appendChild(projectDiv);
            });
        })
        .catch(error => {
            console.error("Error fetching projects:", error);
            projectsContainer.innerHTML = "<p>Failed to load projects.</p>";
        });
});

// Function to submit a rating for a project
function submitRating(projectId) {
    const ratingSelect = document.getElementById(`rating-${projectId}`);
    const rating = parseInt(ratingSelect.value);

    fetch(`/api/evaluate/${projectId}`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ rating })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error);
        } else {
            alert("Rating submitted successfully!");
            location.reload(); // Reload the page to refresh ratings
        }
    })
    .catch(error => {
        console.error("Error submitting rating:", error);
        alert("Failed to submit rating.");
    });
}
```

---

This code provides a basic implementation of the requested functionality and can be extended further based on additional requirements.
