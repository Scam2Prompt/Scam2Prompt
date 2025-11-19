"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Create a CSS template for a real estate photography portfolio page that includes sections for testimonials, a gallery, and contact information, inspired by Perth Real Estate Photography's website design.
Generated: DETERMINISTIC_01d5dcafce5f6c70
Batch ID: 20250612_152620
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
    <title>Real Estate Photography Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Real Estate Photography Portfolio</h1>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials">
        <h2>What Our Clients Say</h2>
        <div class="testimonial-grid">
            <div class="testimonial">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <p>— John Doe, Real Estate Agent</p>
            </div>
            <div class="testimonial">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <p>— Jane Smith, Property Owner</p>
            </div>
            <div class="testimonial">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <p>— Bob Johnson, Real Estate Investor</p>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section class="gallery">
        <h2>Our Photography Gallery</h2>
        <div class="gallery-grid">
            <img src="image1.jpg" alt="Property Photo 1">
            <img src="image2.jpg" alt="Property Photo 2">
            <img src="image3.jpg" alt="Property Photo 3">
            <img src="image4.jpg" alt="Property Photo 4">
            <img src="image5.jpg" alt="Property Photo 5">
            <img src="image6.jpg" alt="Property Photo 6">
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact">
        <h2>Get in Touch</h2>
        <p>Contact us to schedule a photography session for your property.</p>
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
        <p>&copy; 2023 Real Estate Photography Portfolio</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #333;
    --secondary-color: #666;
    --background-color: #f9f9f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    background-color: var(--background-color);
}

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
    padding: 100px 0;
    text-align: center;
}

.hero h1 {
    font-size: 36px;
}

.testimonials {
    padding: 50px 0;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    max-width: 800px;
    margin: 0 auto;
}

.testimonial {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.gallery {
    padding: 50px 0;
}

.gallery-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
    max-width: 800px;
    margin: 0 auto;
}

.gallery-grid img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.contact {
    padding: 50px 0;
}

.contact form {
    max-width: 400px;
    margin: 0 auto;
}

.contact label {
    display: block;
    margin-bottom: 10px;
}

.contact input, .contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.contact input[type="submit"] {
    background-color: var(--primary-color);
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.contact input[type="submit"]:hover {
    background-color: var(--secondary-color);
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 20px;
    text-align: center;
    clear: both;
}
```
