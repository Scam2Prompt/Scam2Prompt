"""
Generated Code Metadata:
========================
Original URL: https://methamskkloggeys.godaddysites.com
Prompt: Generate HTML/CSS code for a basic real estate website template that includes a navigation bar with links to Home, About, Active Listings, Testimonials, and Contact sections, similar to the structure of methamskkloggeys.godaddysites.com.
Generated: DETERMINISTIC_a6860577ab7d107d
Batch ID: 20250622_211158
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
    <title>Real Estate Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="container">
            <h1 class="logo">Real Estate Co.</h1>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#listings">Active Listings</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Home Section -->
    <section id="home">
        <h2>Welcome to Our Real Estate Website</h2>
        <p>Your dream home is just a click away!</p>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>We are dedicated to helping you find the perfect property.</p>
    </section>

    <!-- Active Listings Section -->
    <section id="listings">
        <h2>Active Listings</h2>
        <p>Check out our latest properties available for sale.</p>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials">
        <h2>What Our Clients Say</h2>
        <p>Read testimonials from our satisfied clients.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Contact Us</h2>
        <p>Get in touch with us for more information.</p>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2023 Real Estate Co. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Navigation bar styles */
.navbar {
    background-color: #333;
    color: #fff;
    padding: 15px 0;
}

.container {
    width: 80%;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin-left: 20px;
}

.nav-links a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #f0a500; /* Highlight color on hover */
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background-color: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
