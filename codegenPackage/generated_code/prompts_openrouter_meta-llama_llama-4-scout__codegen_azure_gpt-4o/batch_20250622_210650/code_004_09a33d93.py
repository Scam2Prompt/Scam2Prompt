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
    <meta name="description" content="Dental Rehabilitation Center - Providing expert care for dental health and rehabilitation.">
    <title>Dental Rehabilitation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">Dental Rehabilitation Center</h1>
            <nav class="navigation">
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#team">Our Team</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Expert Care for Your Dental Health</h2>
            <p>We specialize in dental rehabilitation and advanced treatments to restore your smile.</p>
            <a href="#contact" class="cta-button">Book an Appointment</a>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Our center is dedicated to providing top-notch dental rehabilitation services. With years of experience and cutting-edge technology, we ensure the best care for our patients.</p>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <ul>
                <li>Dental Implants</li>
                <li>Cosmetic Dentistry</li>
                <li>Orthodontics</li>
                <li>Periodontal Therapy</li>
                <li>Full Mouth Rehabilitation</li>
            </ul>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team" class="team">
        <div class="container">
            <h2>Meet Our Team</h2>
            <p>Our team of experienced professionals is committed to providing personalized care and exceptional results.</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <p>Have questions or want to schedule an appointment? Reach out to us!</p>
            <form action="#" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer class="footer">
        <div class="container">
            <p>&copy; 2023 Dental Rehabilitation Center. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, a, form, input, textarea, button {
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
    background-color: #004080;
    color: #fff;
    padding: 1rem 0;
}

.header .logo {
    font-size: 1.8rem;
    font-weight: bold;
}

.header .navigation ul {
    list-style: none;
    display: flex;
    justify-content: flex-end;
}

.header .navigation ul li {
    margin-left: 1.5rem;
}

.header .navigation ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Hero Section */
.hero {
    background-color: #e6f2ff;
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

.hero .cta-button {
    background-color: #004080;
    color: #fff;
    padding: 0.5rem 1rem;
    text-decoration: none;
    border-radius: 5px;
}

/* About Section */
.about {
    padding: 2rem 0;
    text-align: center;
}

/* Services Section */
.services {
    background-color: #f0f8ff;
    padding: 2rem 0;
}

.services ul {
    list-style: none;
    text-align: center;
}

.services ul li {
    margin: 0.5rem 0;
}

/* Team Section */
.team {
    padding: 2rem 0;
    text-align: center;
}

/* Contact Section */
.contact {
    background-color: #e6f2ff;
    padding: 2rem 0;
}

.contact form {
    max-width: 600px;
    margin: 0 auto;
}

.contact form label {
    display: block;
    margin-bottom: 0.5rem;
}

.contact form input, .contact form textarea {
    width: 100%;
    margin-bottom: 1rem;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.contact form button {
    background-color: #004080;
    color: #fff;
    padding: 0.5rem 1rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer */
.footer {
    background-color: #004080;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```
