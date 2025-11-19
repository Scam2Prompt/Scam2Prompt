"""
Generated Code Metadata:
========================
Original URL: https://tizianotestori.com
Prompt: Create a basic webpage layout using HTML and CSS for a dental rehabilitation center, inspired by Tiziano Testori's website design and content organization.
Generated: DETERMINISTIC_09a33d935c1943b8
Batch ID: 20250622_210650
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
    <title>Dental Rehabilitation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Dental Rehabilitation Center</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="hero">
            <div class="container">
                <h2>Your Smile, Our Priority</h2>
                <p>Providing comprehensive dental rehabilitation services to restore your smile.</p>
                <a href="#services" class="btn">Learn More</a>
            </div>
        </section>

        <section id="services">
            <div class="container">
                <h2>Our Services</h2>
                <ul>
                    <li>Dental Implants</li>
                    <li>Cosmetic Dentistry</li>
                    <li>Orthodontics</li>
                    <li>Periodontics</li>
                </ul>
            </div>
        </section>

        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>Our team of experienced professionals is dedicated to providing the highest quality dental care.</p>
            </div>
        </section>

        <section id="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <form action="#" method="post" id="contact-form">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                    
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                    
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>
                    
                    <button type="submit">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Dental Rehabilitation Center. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Container for layout */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Hero section styles */
#hero {
    background: #e9ecef;
    padding: 50px 0;
    text-align: center;
}

#hero h2 {
    font-size: 2.5em;
}

.btn {
    background: #007BFF;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Section styles */
section {
    padding: 20px 0;
}

section h2 {
    text-align: center;
    margin-bottom: 20px;
}

/* Form styles */
form {
    max-width: 600px;
    margin: auto;
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    background: #007BFF;
    color: #fff;
    padding: 10px 15px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```
