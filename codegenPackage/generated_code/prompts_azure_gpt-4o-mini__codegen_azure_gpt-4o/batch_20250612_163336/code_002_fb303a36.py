"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Create a simple HTML template for a professional website that meets the standards of the Jordanian market, as outlined by IDEX Marketing.
Generated: DETERMINISTIC_fb303a363bff72dc
Batch ID: 20250612_163336
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
    <meta name="description" content="Professional website template tailored for the Jordanian market by IDEX Marketing.">
    <meta name="keywords" content="Jordan, professional website, IDEX Marketing, business, services">
    <meta name="author" content="IDEX Marketing">
    <title>Professional Website - Jordanian Market</title>
    <!-- Link to external CSS file -->
    <link rel="stylesheet" href="styles.css">
    <!-- Favicon -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <!-- Responsive design and cross-browser compatibility -->
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Welcome to Our Professional Website</h1>
            <nav>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main>
        <!-- About Us Section -->
        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>We are a leading company in the Jordanian market, providing top-notch services tailored to your needs.</p>
            </div>
        </section>

        <!-- Services Section -->
        <section id="services">
            <div class="container">
                <h2>Our Services</h2>
                <ul>
                    <li>Marketing Consultation</li>
                    <li>Brand Development</li>
                    <li>Digital Advertising</li>
                </ul>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 IDEX Marketing. All rights reserved.</p>
            <p>Contact us: <a href="mailto:info@idexmarketing.com">info@idexmarketing.com</a></p>
        </div>
    </footer>

    <!-- External JavaScript file -->
    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Container Styling */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header Styling */
header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
}

header nav ul {
    list-style: none;
    text-align: center;
    padding: 0;
}

header nav ul li {
    display: inline;
    margin: 0 10px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section Styling */
section {
    padding: 2rem 0;
    background: #fff;
    margin: 1rem 0;
}

section h2 {
    text-align: center;
    margin-bottom: 1rem;
}

section p, section ul {
    text-align: center;
}

/* Footer Styling */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}

footer a {
    color: #fff;
    text-decoration: none;
}
```

```javascript
// scripts.js

// Example JavaScript functionality for the website

// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', () => {
    console.log('Website loaded successfully.');
    
    // Example: Smooth scrolling for navigation links
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault();
            const targetId = event.target.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});
```
