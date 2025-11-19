"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: "Create a web page template for a construction company's portfolio, featuring sections for project showcases, client testimonials, and service descriptions, inspired by Albatros SPA's website design."
Generated: DETERMINISTIC_3fe463b4a88aaca5
Batch ID: 20250622_211510
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
    <title>Construction Company Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#services">Services</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Portfolio</h1>
        <p>We're a leading construction company with a passion for building exceptional projects.</p>
        <button>Learn More</button>
    </section>

    <!-- Projects Section -->
    <section id="projects" class="projects">
        <h2>Our Projects</h2>
        <div class="project-grid">
            <div class="project-card">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project 1</h3>
                <p> Description of project 1.</p>
            </div>
            <div class="project-card">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project 2</h3>
                <p> Description of project 2.</p>
            </div>
            <div class="project-card">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project 3</h3>
                <p> Description of project 3.</p>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials">
        <h2>What Our Clients Say</h2>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <p>&#8220; We were impressed with the professionalism and quality of work. &#8221;</p>
                <cite>John Doe, Client</cite>
            </div>
            <div class="testimonial-card">
                <p>&#8220; The team was responsive and delivered the project on time. &#8221;</p>
                <cite>Jane Smith, Client</cite>
            </div>
            <div class="testimonial-card">
                <p>&#8220; We couldn't be happier with the final result. &#8221;</p>
                <cite>Bob Johnson, Client</cite>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <h2>Our Services</h2>
        <div class="service-grid">
            <div class="service-card">
                <h3>Residential Construction</h3>
                <p>We specialize in building custom homes and renovations.</p>
            </div>
            <div class="service-card">
                <h3>Commercial Construction</h3>
                <p>We deliver high-quality commercial spaces for businesses.</p>
            </div>
            <div class="service-card">
                <h3>Project Management</h3>
                <p>Our experienced team manages projects from start to finish.</p>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Construction Company</p>
        <ul>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Privacy Policy</a></li>
        </ul>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #3498db;
    --secondary-color: #f1c40f;
}

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

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 5em;
    text-align: center;
}

.hero h1 {
    font-size: 2.5em;
    margin-bottom: 10px;
}

.hero p {
    font-size: 1.2em;
    margin-bottom: 20px;
}

.hero button {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 1.2em;
    cursor: pointer;
}

.projects {
    padding: 5em;
}

.project-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.project-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project-card h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

.testimonials {
    padding: 5em;
    background-color: #f9f9f9;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.testimonial-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.testimonial-card p {
    font-style: italic;
    margin-bottom: 10px;
}

.testimonial-card cite {
    font-size: 1.2em;
    font-weight: bold;
}

.services {
    padding: 5em;
}

.service-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.service-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.service-card h3 {
    font-size: 1.5em;
    margin-bottom: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

footer ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

footer li {
    display: inline-block;
    margin-right: 20px;
}

footer a {
    color: #fff;
    text-decoration: none;
}
```

```javascript
// script.js

// Add event listener to hero button
document.querySelector('.hero button').addEventListener('click', () => {
    // Scroll to projects section
    document.querySelector('#projects').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to testimonial grid
document.querySelector('.testimonial-grid').addEventListener('mouseover', (e) => {
    if (e.target.classList.contains('testimonial-card')) {
        e.target.style.transform = 'scale(1.05)';
    }
});

document.querySelector('.testimonial-grid').addEventListener('mouseout', (e) => {
    if (e.target.classList.contains('testimonial-card')) {
        e.target.style.transform = 'scale(1)';
    }
});
```
