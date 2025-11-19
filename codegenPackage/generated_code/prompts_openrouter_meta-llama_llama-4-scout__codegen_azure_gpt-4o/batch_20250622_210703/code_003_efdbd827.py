"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Create a simple web page using HTML and CSS for an NGO that provides educational programs for children in need, inspired by Youngistaan's projects."
Generated: DETERMINISTIC_efdbd8276cfc99a7
Batch ID: 20250622_210703
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
    <meta name="description" content="An NGO providing educational programs for children in need, inspired by Youngistaan's projects.">
    <title>NGO for Children's Education</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">Bright Futures NGO</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#programs">Programs</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Empowering Children Through Education</h2>
            <p>Join us in making a difference in the lives of children in need.</p>
            <a href="#programs" class="btn">Explore Programs</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Bright Futures NGO is dedicated to providing quality education to underprivileged children. Inspired by Youngistaan's projects, we aim to create opportunities for every child to learn and grow.</p>
        </div>
    </section>

    <!-- Programs Section -->
    <section id="programs" class="programs">
        <div class="container">
            <h2>Our Programs</h2>
            <div class="program-list">
                <div class="program-item">
                    <h3>After-School Tutoring</h3>
                    <p>Helping children improve their academic performance through personalized tutoring sessions.</p>
                </div>
                <div class="program-item">
                    <h3>Skill Development Workshops</h3>
                    <p>Providing workshops to teach essential life skills and vocational training.</p>
                </div>
                <div class="program-item">
                    <h3>Scholarship Opportunities</h3>
                    <p>Offering scholarships to deserving students for higher education.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <p>We would love to hear from you! Reach out to us for more information or to get involved.</p>
            <form action="#" method="POST" class="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Bright Futures NGO. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, a, input, textarea, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
.header {
    background-color: #0078d7;
    color: #fff;
    padding: 1rem 0;
}

.header .logo {
    font-size: 1.8rem;
    font-weight: bold;
}

.nav ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

.nav ul li {
    margin-left: 1rem;
}

.nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Hero Section */
.hero {
    background-color: #0056a3;
    color: #fff;
    text-align: center;
    padding: 2rem 0;
}

.hero h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
}

.hero p {
    margin-bottom: 1.5rem;
}

.hero .btn {
    background-color: #ff9800;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
}

/* About Section */
.about {
    padding: 2rem 0;
    background-color: #fff;
}

.about h2 {
    text-align: center;
    margin-bottom: 1rem;
}

/* Programs Section */
.programs {
    padding: 2rem 0;
    background-color: #f1f1f1;
}

.programs h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.program-list {
    display: flex;
    gap: 1rem;
    flex-wrap: wrap;
}

.program-item {
    flex: 1;
    background-color: #fff;
    padding: 1rem;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Contact Section */
.contact {
    padding: 2rem 0;
    background-color: #fff;
}

.contact h2 {
    text-align: center;
    margin-bottom: 1rem;
}

.contact-form {
    max-width: 600px;
    margin: 0 auto;
}

.contact-form label {
    display: block;
    margin-bottom: 0.5rem;
}

.contact-form input, .contact-form textarea {
    width: 100%;
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.contact-form .btn {
    background-color: #0078d7;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer */
.footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```
