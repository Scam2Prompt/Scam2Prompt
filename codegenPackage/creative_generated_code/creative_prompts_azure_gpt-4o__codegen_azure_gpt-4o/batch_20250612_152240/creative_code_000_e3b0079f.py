"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Write a code snippet using HTML5 and CSS to create a personal portfolio webpage similar to the structure described on EMFresh2o Digital Resume, including sections for "Home," "About," "Portfolio," and "Contact."
Generated: DETERMINISTIC_e3b0079f779a09ce
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Personal Portfolio Page">
    <title>Personal Portfolio</title>
    <!-- Link to external CSS file -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation bar -->
    <nav>
        <ul class="navigation">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#portfolio">Portfolio</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Home Section -->
    <section id="home" class="section">
        <h1>Welcome to My Portfolio</h1>
        <p>Your one-stop showcase of my skills and projects.</p>
    </section>

    <!-- About Section -->
    <section id="about" class="section">
        <h2>About Me</h2>
        <p>Hello! I'm [Your Name], a professional [Your Profession]. I specialize in [Your Skills].</p>
        <p>With hands-on experience in [Your Experience], I always aim to deliver exceptional results.</p>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="section">
        <h2>Portfolio</h2>
        <p>Here are some of my recent projects:</p>
        <div class="portfolio-grid">
            <div class="portfolio-item">
                <h3>Project 1</h3>
                <p>Description of Project 1.</p>
            </div>
            <div class="portfolio-item">
                <h3>Project 2</h3>
                <p>Description of Project 2.</p>
            </div>
            <div class="portfolio-item">
                <h3>Project 3</h3>
                <p>Description of Project 3.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="section">
        <h2>Contact Me</h2>
        <form id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2023 [Your Name]. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, form, input, textarea, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

nav {
    background-color: #333;
    padding: 10px;
}

.navigation {
    list-style: none;
    display: flex;
    justify-content: center;
}

.navigation li {
    margin: 0 15px;
}

.navigation a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

.navigation a:hover {
    text-decoration: underline;
}

.section {
    padding: 20px;
    text-align: center;
}

#home {
    background-color: #f4f4f4;
    padding: 50px 20px;
}

#about {
    background-color: #e2e2e2;
    padding: 50px 20px;
}

#portfolio {
    background-color: #d4d4d4;
    padding: 50px 20px;
}

.portfolio-grid {
    display: flex;
    justify-content: center;
    gap: 20px;
    flex-wrap: wrap;
}

.portfolio-item {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    width: 30%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

#contact {
    background-color: #c6c6c6;
    padding: 50px 20px;
}

form {
    max-width: 500px;
    margin: 0 auto;
    text-align: left;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea, button {
    width: 100%;
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #333;
    color: #fff;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```
