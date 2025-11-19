"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write code to create a dynamic website landing page for a digital branding agency, incorporating features like client testimonials, project highlights, and downloadable resources, as described on Naikreatif's website.
Generated: DETERMINISTIC_9ef257efa674510f
Batch ID: 20250612_153224
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
    <title>Naikreatif Digital Branding Agency</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Naikreatif</h1>
        <p>We craft digital experiences that elevate your brand.</p>
        <button>Discover More</button>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <h2>What Our Clients Say</h2>
        <div class="testimonial-cards">
            <!-- Testimonial Card -->
            <div class="testimonial-card">
                <img src="client1.jpg" alt="Client 1">
                <p>&#8220;Naikreatif helped us rebrand and we're loving the new look!&#8221;</p>
                <span>John Doe, CEO of Example Inc.</span>
            </div>
            <!-- Testimonial Card -->
            <div class="testimonial-card">
                <img src="client2.jpg" alt="Client 2">
                <p>&#8220;Their team's creativity and expertise are top-notch!&#8221;</p>
                <span>Jane Smith, Marketing Director at ABC Corp.</span>
            </div>
        </div>
    </section>

    <!-- Project Highlights Section -->
    <section class="projects">
        <h2>Our Recent Projects</h2>
        <div class="project-cards">
            <!-- Project Card -->
            <div class="project-card">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project Title 1</h3>
                <p>Brief description of project 1.</p>
            </div>
            <!-- Project Card -->
            <div class="project-card">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project Title 2</h3>
                <p>Brief description of project 2.</p>
            </div>
        </div>
    </section>

    <!-- Resources Section -->
    <section class="resources">
        <h2>Downloadable Resources</h2>
        <div class="resource-cards">
            <!-- Resource Card -->
            <div class="resource-card">
                <img src="resource1.jpg" alt="Resource 1">
                <h3>Resource Title 1</h3>
                <p>Brief description of resource 1.</p>
                <a href="resource1.pdf" download>Download Now</a>
            </div>
            <!-- Resource Card -->
            <div class="resource-card">
                <img src="resource2.jpg" alt="Resource 2">
                <h3>Resource Title 2</h3>
                <p>Brief description of resource 2.</p>
                <a href="resource2.pdf" download>Download Now</a>
            </div>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Naikreatif Digital Branding Agency</p>
        <ul>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Contact Us</a></li>
        </ul>
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

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 100px;
    text-align: center;
}

.hero h1 {
    font-size: 48px;
}

.hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

.hero button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

.testimonials {
    padding: 50px;
}

.testimonial-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.testimonial-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: 300px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.testimonial-card img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    margin-bottom: 10px;
}

.testimonial-card p {
    font-size: 16px;
    margin-bottom: 10px;
}

.testimonial-card span {
    font-size: 14px;
    color: #666;
}

.projects {
    padding: 50px;
}

.project-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.project-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: 300px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.project-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.project-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.project-card p {
    font-size: 16px;
    margin-bottom: 20px;
}

.resources {
    padding: 50px;
}

.resource-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.resource-card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: 300px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.resource-card img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.resource-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

.resource-card p {
    font-size: 16px;
    margin-bottom: 20px;
}

.resource-card a {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    text-decoration: none;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

footer ul {
    list-style: none;
    padding: 0;
    margin: 0;
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
    // Scroll to testimonials section
    document.querySelector('.testimonials').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to resource card downloads
document.querySelectorAll('.resource-card a').forEach((link) => {
    link.addEventListener('click', () => {
        // Track download event
        console.log('Resource downloaded!');
    });
});
```
