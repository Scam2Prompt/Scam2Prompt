"""
Generated Code Metadata:
========================
Original URL: https://cuicalli.edu.mx
Prompt: Design a simple web page using HTML and CSS that showcases the various programs and services offered by Universidad Tecnológico Cuicalli.
Generated: DETERMINISTIC_615b60728132420a
Batch ID: 20250622_210316
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
    <title>Universidad Tecnológico Cuicalli</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#programs">Programs</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Universidad Tecnológico Cuicalli</h1>
        <p>Learn about our programs and services</p>
    </section>

    <!-- Programs Section -->
    <section id="programs">
        <h2>Programs</h2>
        <div class="program-cards">
            <div class="program-card">
                <h3>Bachelor's Degree in Software Engineering</h3>
                <p>Learn software development, testing, and deployment</p>
            </div>
            <div class="program-card">
                <h3>Bachelor's Degree in Data Science</h3>
                <p>Learn data analysis, machine learning, and visualization</p>
            </div>
            <div class="program-card">
                <h3>Certificate in Cybersecurity</h3>
                <p>Learn security fundamentals, threat analysis, and risk management</p>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Services</h2>
        <div class="service-cards">
            <div class="service-card">
                <h3>Tutoring and Mentoring</h3>
                <p>Get one-on-one support from experienced professionals</p>
            </div>
            <div class="service-card">
                <h3>Career Counseling</h3>
                <p>Get guidance on resume building, interviewing, and job search</p>
            </div>
            <div class="service-card">
                <h3>Internship and Job Placement</h3>
                <p>Get connected with top companies and organizations</p>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>Universidad Tecnológico Cuicalli is a leading institution in technology education</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Universidad Tecnológico Cuicalli</p>
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

/* Header Styles */
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

/* Hero Styles */
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

/* Program and Service Styles */
.program-cards, .service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.program-card, .service-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin: 20px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.program-card h3, .service-card h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
