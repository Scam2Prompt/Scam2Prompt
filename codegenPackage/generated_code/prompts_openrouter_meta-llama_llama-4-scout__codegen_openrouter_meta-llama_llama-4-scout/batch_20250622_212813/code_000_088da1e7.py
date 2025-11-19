"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Generate a website homepage content for an IT agency and institute of technology that emphasizes real skills, real projects, and real success.
Generated: DETERMINISTIC_088da1e7ad215c80
Batch ID: 20250622_212813
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
    <title>IT Agency & Institute of Technology</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#success-stories">Success Stories</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <h1>Real Skills, Real Projects, Real Success</h1>
        <p>Welcome to our IT agency and institute of technology, where we focus on delivering high-quality solutions and educating the next generation of tech professionals.</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>Our IT agency and institute of technology are dedicated to providing innovative solutions to businesses and individuals. We believe in hands-on learning and real-world experience, which is why our students and professionals work on actual projects that make a difference.</p>
        <ul>
            <li><strong>Our Mission:</strong> To empower individuals and organizations through technology and education.</li>
            <li><strong>Our Values:</strong> Innovation, Excellence, Collaboration, and Customer Satisfaction.</li>
        </ul>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="card">
                <h3>Software Development</h3>
                <p>We design, develop, and deploy custom software solutions that meet the unique needs of our clients.</p>
            </div>
            <div class="card">
                <h3>IT Consulting</h3>
                <p>Our experts provide strategic guidance and support to help businesses optimize their IT infrastructure and operations.</p>
            </div>
            <div class="card">
                <h3>Education and Training</h3>
                <p>We offer a range of educational programs and training courses to help individuals develop the skills they need to succeed in the tech industry.</p>
            </div>
        </div>
    </section>

    <!-- Success Stories Section -->
    <section id="success-stories">
        <h2>Success Stories</h2>
        <div class="story-cards">
            <div class="card">
                <h3>Project: E-commerce Platform</h3>
                <p>We developed a custom e-commerce platform for a leading retail company, resulting in a 30% increase in sales and a 25% reduction in operational costs.</p>
            </div>
            <div class="card">
                <h3>Project: Cybersecurity Solution</h3>
                <p>Our team implemented a comprehensive cybersecurity solution for a financial institution, protecting sensitive data and preventing potential threats.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Ready to learn more about our services or programs? Fill out the form below to contact us.</p>
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
        <p>&copy; 2023 IT Agency & Institute of Technology. All rights reserved.</p>
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

#hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#hero h1 {
    font-size: 48px;
}

#hero p {
    font-size: 18px;
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
    background-color: #555;
}

#about {
    padding: 2em;
}

#services {
    padding: 2em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.card h3 {
    margin-top: 0;
}

#success-stories {
    padding: 2em;
}

.story-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

#contact {
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

// Add event listener to the learn more button
document.querySelector('#hero button').addEventListener('click', () => {
    // Scroll to the about section
    document.querySelector('#about').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to the send button
document.querySelector('#contact button').addEventListener('click', (e) => {
    e.preventDefault();
    // Get the form data
    const formData = new FormData(document.querySelector('#contact form'));
    // Send the form data to the server
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```
