"""
Generated Code Metadata:
========================
Original URL: https://workshopgranada.com
Prompt: Create a code snippet in HTML/CSS to design a landing page for Workshop Granada's summer sewing campus, showcasing its community and personalized learning environment.
Generated: DETERMINISTIC_c681fb5a77170c2b
Batch ID: 20250612_162051
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
    <title>Workshop Granada Summer Sewing Campus</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#programs">Programs</a></li>
                <li><a href="#community">Community</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <h1>Welcome to Workshop Granada's Summer Sewing Campus</h1>
        <p>Join our vibrant community of sewists and experience personalized learning in a supportive environment.</p>
        <button>Learn More</button>
        <img src="hero-image.jpg" alt="Sewing Machines and Students">
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>At Workshop Granada, we believe that sewing is more than just a skill - it's a way to express yourself and connect with others. Our summer sewing campus is designed to provide a supportive and inspiring environment where you can learn and grow.</p>
        <img src="about-image.jpg" alt="Workshop Granada Team">
    </section>

    <!-- Programs Section -->
    <section id="programs">
        <h2>Programs</h2>
        <ul>
            <li>
                <h3>Beginner's Sewing</h3>
                <p>Learn the basics of sewing and get started with your own projects.</p>
            </li>
            <li>
                <h3>Intermediate Sewing</h3>
                <p>Take your sewing skills to the next level with our intermediate classes.</p>
            </li>
            <li>
                <h3>Advanced Sewing</h3>
                <p>Challenge yourself with our advanced sewing classes and work on complex projects.</p>
            </li>
        </ul>
    </section>

    <!-- Community Section -->
    <section id="community">
        <h2>Our Community</h2>
        <p>At Workshop Granada, we're proud of our vibrant community of sewists. We believe that sewing is a social activity and encourage our students to connect with each other.</p>
        <img src="community-image.jpg" alt="Students Working Together">
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Ready to join our summer sewing campus? Contact us to learn more and register.</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Workshop Granada. All rights reserved.</p>
    </footer>
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
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 5em;
    text-align: center;
}

#hero h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

#hero p {
    font-size: 18px;
    margin-bottom: 20px;
}

#hero button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#hero img {
    width: 100%;
    height: 300px;
    object-fit: cover;
    margin-top: 20px;
}

section {
    padding: 2em;
}

h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

p {
    font-size: 16px;
    margin-bottom: 20px;
}

#programs ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

#programs li {
    margin-bottom: 20px;
}

#programs h3 {
    font-size: 18px;
    margin-bottom: 10px;
}

#community img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    margin-top: 20px;
}

#contact form {
    max-width: 500px;
    margin: 0 auto;
}

#contact label {
    display: block;
    margin-bottom: 10px;
}

#contact input, #contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#contact input[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
