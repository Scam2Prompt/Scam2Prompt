"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: Create a responsive web design template for showcasing a portfolio of work, inspired by La Guarida's "Our Work" section.
Generated: DETERMINISTIC_e81ec64bc9c5033a
Batch ID: 20250612_155000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio Showcase</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
    <header>
        <nav>
            <h1>My Portfolio</h1>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>About Me</h2>
        <p>Welcome to my portfolio! I am a passionate developer with a love for creating beautiful and functional web applications.</p>
    </section>

    <section id="portfolio">
        <h2>My Work</h2>
        <div class="portfolio-grid">
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project Title 1</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project Title 2</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project Title 3</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
            <div class="portfolio-item">
                <img src="project4.jpg" alt="Project 4">
                <h3>Project Title 4</h3>
                <p>Short description of the project.</p>
                <a href="#" class="btn">View Project</a>
            </div>
        </div>
    </section>

    <section id="contact">
        <h2>Contact Me</h2>
        <form id="contact-form" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Send Message</button>
        </form>
    </section>

    <footer>
        <p>&copy; 2023 My Portfolio. All rights reserved.</p>
        <div class="social-icons">
            <a href="#" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
            <a href="#" aria-label="GitHub"><i class="fab fa-github"></i></a>
            <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
        </div>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 2rem;
}

nav ul {
    list-style: none;
    display: flex;
}

nav ul li {
    margin-left: 2rem;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 2rem;
}

/* Portfolio grid styles */
.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 1rem;
}

.portfolio-item {
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    text-align: center;
}

.portfolio-item img {
    width: 100%;
    height: auto;
}

.btn {
    display: inline-block;
    margin: 1rem 0;
    padding: 0.5rem 1rem;
    background: #333;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

.social-icons a {
    margin: 0 0.5rem;
    color: #fff;
    text-decoration: none;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const formData = new FormData(this);

    // Send form data using Fetch API
    fetch(this.action, {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert('Message sent successfully!');
        this.reset(); // Reset form fields
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your message. Please try again later.');
    });
});
```
