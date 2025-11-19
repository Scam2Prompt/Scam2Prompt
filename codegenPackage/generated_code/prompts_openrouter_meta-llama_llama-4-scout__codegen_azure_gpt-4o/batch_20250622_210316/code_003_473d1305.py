"""
Generated Code Metadata:
========================
Original URL: https://dionlineaja.id
Prompt: Create a design portfolio website using Photoshop, Illustrator, and CSS3 for a company that has completed 59 projects and has 18 clients.
Generated: DETERMINISTIC_473d1305079ca2af
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Design Portfolio showcasing projects and clients">
    <title>Design Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Design Portfolio</h1>
            <p>Showcasing our creative work using Photoshop, Illustrator, and CSS3</p>
        </div>
    </header>

    <!-- About Section -->
    <section id="about">
        <div class="container">
            <h2>About Us</h2>
            <p>We are a creative design company specializing in Photoshop, Illustrator, and CSS3. With 59 completed projects and 18 satisfied clients, we bring ideas to life.</p>
        </div>
    </section>

    <!-- Projects Section -->
    <section id="projects">
        <div class="container">
            <h2>Our Projects</h2>
            <div class="project-grid">
                <!-- Example project cards -->
                <div class="project-card">
                    <img src="project1.jpg" alt="Project 1">
                    <h3>Project Title 1</h3>
                    <p>Brief description of the project.</p>
                </div>
                <div class="project-card">
                    <img src="project2.jpg" alt="Project 2">
                    <h3>Project Title 2</h3>
                    <p>Brief description of the project.</p>
                </div>
                <!-- Add more project cards as needed -->
            </div>
        </div>
    </section>

    <!-- Clients Section -->
    <section id="clients">
        <div class="container">
            <h2>Our Clients</h2>
            <ul class="client-list">
                <!-- Example client names -->
                <li>Client Name 1</li>
                <li>Client Name 2</li>
                <li>Client Name 3</li>
                <!-- Add more client names as needed -->
            </ul>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Design Portfolio. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Container */
.container {
    width: 80%;
    margin: 0 auto;
    max-width: 1200px;
}

/* Header Section */
header {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

header h1 {
    font-size: 2.5em;
}

header p {
    font-size: 1.2em;
}

/* About Section */
#about {
    padding: 20px 0;
    background: #fff;
    text-align: center;
}

#about h2 {
    font-size: 2em;
    margin-bottom: 10px;
}

#about p {
    font-size: 1.1em;
    color: #666;
}

/* Projects Section */
#projects {
    padding: 20px 0;
    background: #f9f9f9;
}

#projects h2 {
    text-align: center;
    font-size: 2em;
    margin-bottom: 20px;
}

.project-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.project-card {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    width: 300px;
    text-align: center;
}

.project-card img {
    width: 100%;
    height: auto;
}

.project-card h3 {
    font-size: 1.5em;
    margin: 10px 0;
}

.project-card p {
    font-size: 1em;
    color: #666;
    padding: 0 10px 10px;
}

/* Clients Section */
#clients {
    padding: 20px 0;
    background: #fff;
    text-align: center;
}

#clients h2 {
    font-size: 2em;
    margin-bottom: 10px;
}

.client-list {
    list-style: none;
    padding: 0;
}

.client-list li {
    font-size: 1.2em;
    margin: 5px 0;
}

/* Footer Section */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

footer p {
    font-size: 1em;
}
```

**Note:** Replace `project1.jpg`, `project2.jpg`, etc., with actual image paths for your projects. Add more project cards and client names as needed.
