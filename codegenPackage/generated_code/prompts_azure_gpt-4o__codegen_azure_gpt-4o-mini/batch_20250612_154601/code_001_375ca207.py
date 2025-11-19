"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Generate HTML and CSS code for a sleek real estate business website, ensuring the design aligns with the unique features highlighted by Solutech System's real estate website design services.
Generated: DETERMINISTIC_375ca20736bfa729
Batch ID: 20250612_154601
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
    <title>Real Estate Business</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Solutech Real Estate</h1>
            <nav>
                <ul>
                    <li><a href="#home">Home</a></li>
                    <li><a href="#properties">Properties</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="home" class="hero">
        <div class="container">
            <h2>Your Dream Home Awaits</h2>
            <p>Find the perfect property with us.</p>
            <a href="#properties" class="btn">View Properties</a>
        </div>
    </section>

    <section id="properties" class="properties">
        <div class="container">
            <h2>Featured Properties</h2>
            <div class="property-list">
                <div class="property">
                    <img src="property1.jpg" alt="Property 1">
                    <h3>Luxury Villa</h3>
                    <p>$1,200,000</p>
                    <a href="#" class="btn">View Details</a>
                </div>
                <div class="property">
                    <img src="property2.jpg" alt="Property 2">
                    <h3>Modern Apartment</h3>
                    <p>$850,000</p>
                    <a href="#" class="btn">View Details</a>
                </div>
                <div class="property">
                    <img src="property3.jpg" alt="Property 3">
                    <h3>Cozy Cottage</h3>
                    <p>$450,000</p>
                    <a href="#" class="btn">View Details</a>
                </div>
            </div>
        </div>
    </section>

    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>We are dedicated to helping you find your dream home. Our team of experts is here to guide you through the process.</p>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form" action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit" class="btn">Send Message</button>
            </form>
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Solutech Real Estate. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
    list-style: none;
}

/* Set a basic font and background */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Container for layout */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
}

header h1 {
    float: left;
}

header nav {
    float: right;
}

header nav ul {
    display: flex;
}

header nav ul li {
    margin-left: 20px;
}

header nav a {
    color: #ffffff;
    text-decoration: none;
}

/* Hero section styles */
.hero {
    background: url('hero-bg.jpg') no-repeat center center/cover;
    color: #ffffff;
    padding: 100px 0;
    text-align: center;
}

/* Button styles */
.btn {
    display: inline-block;
    padding: 10px 20px;
    background: #e8491d;
    color: #ffffff;
    text-decoration: none;
    border-radius: 5px;
}

/* Properties section styles */
.properties {
    padding: 20px 0;
    background: #ffffff;
}

.property-list {
    display: flex;
    justify-content: space-between;
}

.property {
    border: 1px solid #dddddd;
    border-radius: 5px;
    padding: 10px;
    text-align: center;
}

.property img {
    max-width: 100%;
    border-radius: 5px;
}

/* About section styles */
.about {
    padding: 20px 0;
    background: #e4e4e4;
    text-align: center;
}

/* Contact section styles */
.contact {
    padding: 20px 0;
    background: #ffffff;
}

.contact form {
    max-width: 600px;
    margin: auto;
}

.contact label {
    display: block;
    margin: 10px 0 5px;
}

.contact input, .contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #dddddd;
    border-radius: 5px;
}

/* Footer styles */
footer {
    background: #35424a;
    color: #ffffff;
    text-align: center;
    padding: 10px 0;
}
```
