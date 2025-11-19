"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Illustrate how to use CSS to design a webpage that highlights makeup artistry and personal styling, taking cues from the aesthetic of Style & Makeup Effect.
Generated: DETERMINISTIC_0b63add853b57f77
Batch ID: 20250612_155255
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
    <title>Makeup Artistry & Personal Styling</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Makeup Artistry & Personal Styling</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <section id="about">
        <h2>About Us</h2>
        <p>We specialize in makeup artistry and personal styling, bringing out the best in you.</p>
    </section>

    <section id="services">
        <h2>Our Services</h2>
        <ul>
            <li>Bridal Makeup</li>
            <li>Special Occasion Makeup</li>
            <li>Personal Styling Consultations</li>
            <li>Makeup Workshops</li>
        </ul>
    </section>

    <section id="gallery">
        <h2>Gallery</h2>
        <div class="gallery-grid">
            <img src="makeup1.jpg" alt="Makeup Artistry Example 1">
            <img src="makeup2.jpg" alt="Makeup Artistry Example 2">
            <img src="makeup3.jpg" alt="Makeup Artistry Example 3">
            <img src="makeup4.jpg" alt="Makeup Artistry Example 4">
        </div>
    </section>

    <footer id="contact">
        <h2>Contact Us</h2>
        <p>Email: info@makeupartistry.com</p>
        <p>Phone: (123) 456-7890</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background-color: #f9f9f9;
    color: #333;
}

/* Header styles */
header {
    background: linear-gradient(to right, #ff7e5f, #feb47b);
    color: white;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px 0;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Gallery styles */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 10px;
}

.gallery-grid img {
    width: 100%;
    border-radius: 8px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #333;
    color: white;
}
```
