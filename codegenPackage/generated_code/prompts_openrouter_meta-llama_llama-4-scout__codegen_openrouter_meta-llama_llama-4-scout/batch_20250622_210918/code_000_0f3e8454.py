"""
Generated Code Metadata:
========================
Original URL: https://renzostudio.com
Prompt: "Generate HTML and CSS code for a simple architecture portfolio website similar to RENZO Studio de Arquitetura's site."
Generated: DETERMINISTIC_0f3e8454e7ed2243
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Architecture Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h1>Welcome to our Architecture Portfolio</h1>
            <p>We are a team of passionate architects dedicated to creating innovative and sustainable spaces.</p>
            <button>Explore Our Work</button>
        </section>
        <section id="projects">
            <h2>Our Projects</h2>
            <div class="project-grid">
                <div class="project">
                    <img src="project1.jpg" alt="Project 1">
                    <h3>Project 1</h3>
                    <p>A brief description of project 1.</p>
                </div>
                <div class="project">
                    <img src="project2.jpg" alt="Project 2">
                    <h3>Project 2</h3>
                    <p>A brief description of project 2.</p>
                </div>
                <div class="project">
                    <img src="project3.jpg" alt="Project 3">
                    <h3>Project 3</h3>
                    <p>A brief description of project 3.</p>
                </div>
            </div>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>We are a team of experienced architects with a passion for creating beautiful and functional spaces.</p>
            <img src="team.jpg" alt="Our Team">
        </section>
        <section id="contact">
            <h2>Get in Touch</h2>
            <p>Contact us to discuss your next project.</p>
            <form>
                <input type="text" placeholder="Name">
                <input type="email" placeholder="Email">
                <textarea placeholder="Message"></textarea>
                <button>Send</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Architecture Portfolio</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

p {
    margin-bottom: 20px;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.project img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project h3 {
    margin-top: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */
@media only screen and (max-width: 768px) {
    .project-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media only screen and (max-width: 480px) {
    .project-grid {
        grid-template-columns: 1fr;
    }
}
```
