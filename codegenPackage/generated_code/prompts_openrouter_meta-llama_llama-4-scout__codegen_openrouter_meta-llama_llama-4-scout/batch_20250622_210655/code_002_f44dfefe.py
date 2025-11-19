"""
Generated Code Metadata:
========================
Original URL: https://cefor.org.br
Prompt: Generate a code snippet to create a simple website for a social organization, including sections for services, projects, and contact information, inspired by the CEFOR website.
Generated: DETERMINISTIC_f44dfefef11b1ee8
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Social Organization Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Social Organization</h1>
        <p>Empowering communities through education and support.</p>
        <button>Learn More</button>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="service-card">
                <h3>Education</h3>
                <p>Providing educational resources and workshops.</p>
            </div>
            <div class="service-card">
                <h3>Community Support</h3>
                <p>Offering support and resources for local communities.</p>
            </div>
            <div class="service-card">
                <h3>Advocacy</h3>
                <p>Advocating for social justice and equality.</p>
            </div>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <h2>Our Projects</h2>
        <div class="project-cards">
            <div class="project-card">
                <h3>Project 1: Education Initiative</h3>
                <p>Providing educational resources to underprivileged communities.</p>
            </div>
            <div class="project-card">
                <h3>Project 2: Community Development</h3>
                <p>Supporting local community development through workshops and resources.</p>
            </div>
            <div class="project-card">
                <h3>Project 3: Advocacy Campaign</h3>
                <p>Launching an advocacy campaign for social justice and equality.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Social Organization Website</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.services {
    padding: 2em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.service-card {
    background-color: #f7f7f7;
    padding: 1em;
    margin: 1em;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.projects {
    padding: 2em;
}

.project-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.project-card {
    background-color: #f7f7f7;
    padding: 1em;
    margin: 1em;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact {
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Send contact form data to server
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```

```python
# server.py

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST'])
def handle_contact():
    try:
        data = request.form
        # Process form data
        print(data)
        return jsonify({'message': 'Form submitted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
