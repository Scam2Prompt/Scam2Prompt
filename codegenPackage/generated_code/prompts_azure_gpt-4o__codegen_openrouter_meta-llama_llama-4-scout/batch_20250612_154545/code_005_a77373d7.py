"""
Generated Code Metadata:
========================
Original URL: https://bearmybrand.com
Prompt: Write HTML and CSS code for a brand kit design page that includes sections for logo design, stationary design, and social media thumbnails, reflecting Bear My Brand's graphic design services.
Generated: DETERMINISTIC_a77373d71fda5ebd
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bear My Brand - Brand Kit Design</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#logo-design">Logo Design</a></li>
                <li><a href="#stationary-design">Stationary Design</a></li>
                <li><a href="#social-media-thumbnails">Social Media Thumbnails</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Bear My Brand</h1>
        <p>Expert graphic design services for your brand</p>
    </section>

    <!-- Logo Design Section -->
    <section id="logo-design" class="section">
        <h2>Logo Design</h2>
        <p>Our logo design services include:</p>
        <ul>
            <li>Custom logo design</li>
            <li>Vector file formats (AI, EPS, SVG)</li>
            <li>Raster file formats (JPEG, PNG)</li>
        </ul>
        <div class="image-container">
            <img src="logo-design-example.jpg" alt="Logo Design Example">
        </div>
    </section>

    <!-- Stationary Design Section -->
    <section id="stationary-design" class="section">
        <h2>Stationary Design</h2>
        <p>Our stationary design services include:</p>
        <ul>
            <li>Business card design</li>
            <li>Letterhead design</li>
            <li>Envelope design</li>
        </ul>
        <div class="image-container">
            <img src="stationary-design-example.jpg" alt="Stationary Design Example">
        </div>
    </section>

    <!-- Social Media Thumbnails Section -->
    <section id="social-media-thumbnails" class="section">
        <h2>Social Media Thumbnails</h2>
        <p>Our social media thumbnail design services include:</p>
        <ul>
            <li>Facebook page design</li>
            <li>Twitter header design</li>
            <li>Instagram post design</li>
        </ul>
        <div class="image-container">
            <img src="social-media-thumbnails-example.jpg" alt="Social Media Thumbnails Example">
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Bear My Brand. All rights reserved.</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

/* Section Styles */
.section {
    padding: 2em;
    background-color: #fff;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.section h2 {
    margin-top: 0;
}

.image-container {
    max-width: 100%;
    height: auto;
    margin: 20px auto;
}

.image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
