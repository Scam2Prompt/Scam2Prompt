"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Generate HTML and CSS code for a photography portfolio website with a "Gallery" section showcasing wedding, maternity, and family photos, inspired by Yaisa Tangwell's services.
Generated: DETERMINISTIC_099f851ee0af8432
Batch ID: 20250612_154207
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
    <meta name="description" content="Photography portfolio showcasing wedding, maternity, and family photos inspired by Yaisa Tangwell's services.">
    <title>Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <h1 class="logo">Photography Portfolio</h1>
            <nav class="nav">
                <ul>
                    <li><a href="#gallery">Gallery</a></li>
                    <li><a href="#about">About</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Capturing Life's Beautiful Moments</h2>
            <p>Wedding, maternity, and family photography inspired by Yaisa Tangwell.</p>
        </div>
    </section>

    <!-- Gallery Section -->
    <section id="gallery" class="gallery">
        <div class="container">
            <h2>Gallery</h2>
            <p>Explore our portfolio showcasing life's precious moments.</p>
            <div class="grid">
                <div class="grid-item">
                    <img src="wedding1.jpg" alt="Wedding Photo 1">
                    <p>Wedding</p>
                </div>
                <div class="grid-item">
                    <img src="wedding2.jpg" alt="Wedding Photo 2">
                    <p>Wedding</p>
                </div>
                <div class="grid-item">
                    <img src="maternity1.jpg" alt="Maternity Photo 1">
                    <p>Maternity</p>
                </div>
                <div class="grid-item">
                    <img src="maternity2.jpg" alt="Maternity Photo 2">
                    <p>Maternity</p>
                </div>
                <div class="grid-item">
                    <img src="family1.jpg" alt="Family Photo 1">
                    <p>Family</p>
                </div>
                <div class="grid-item">
                    <img src="family2.jpg" alt="Family Photo 2">
                    <p>Family</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2>About</h2>
            <p>Welcome to our photography portfolio. We specialize in capturing the beauty, emotion, and essence of life's special moments.</p>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact</h2>
            <form>
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
            <p>&copy; 2023 Photography Portfolio | All Rights Reserved</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset and base styles */
body {
    margin: 0;
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header styles */
.header {
    background-color: #222;
    color: #fff;
    padding: 1rem 0;
}

.logo {
    font-size: 1.5rem;
    margin: 0;
}

.nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    gap: 1rem;
}

.nav a {
    color: #fff;
    text-decoration: none;
    font-size: 1rem;
}

.nav a:hover {
    text-decoration: underline;
}

/* Hero styles */
.hero {
    background: url('hero-image.jpg') no-repeat center center/cover;
    color: #fff;
    text-align: center;
    padding: 4rem 0;
}

.hero h2 {
    font-size: 2.5rem;
    margin: 0;
}

.hero p {
    font-size: 1.2rem;
}

/* Gallery styles */
.gallery {
    padding: 2rem 0;
}

.gallery h2 {
    text-align: center;
}

.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1rem;
}

.grid-item {
    text-align: center;
}

.grid-item img {
    width: 100%;
    height: auto;
    border-radius: 8px;
}

/* About styles */
.about {
    background-color: #f4f4f4;
    padding: 2rem 0;
}

.about h2 {
    text-align: center;
}

/* Contact styles */
.contact {
    padding: 2rem 0;
}

.contact h2 {
    text-align: center;
}

form {
    max-width: 600px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
}

form label {
    margin-top: 1rem;
}

form input, form textarea, form button {
    width: 100%;
    padding: 0.5rem;
    margin-top: 0.5rem;
}

form button {
    background-color: #222;
    color: #fff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background-color: #555;
}

/* Footer styles */
.footer {
    background-color: #222;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```
