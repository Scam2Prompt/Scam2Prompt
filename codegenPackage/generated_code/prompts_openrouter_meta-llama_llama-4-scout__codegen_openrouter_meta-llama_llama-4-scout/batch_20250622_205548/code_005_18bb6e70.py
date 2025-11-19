"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Create a basic HTML/CSS template for a beauty services website that highlights the artist's portfolio, including sections for bridal makeup and personal styling.
Generated: DETERMINISTIC_18bb6e7056455b85
Batch ID: 20250622_205548
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
    <title>Beauty Services Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#bridal-makeup">Bridal Makeup</a></li>
                <li><a href="#personal-styling">Personal Styling</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to [Artist Name]'s Beauty Services</h1>
        <p>Expert makeup and styling services for your special day</p>
        <button>Discover More</button>
    </section>

    <!-- Portfolio Section -->
    <section id="portfolio" class="portfolio">
        <h2>Portfolio</h2>
        <div class="portfolio-grid">
            <div class="portfolio-item">
                <img src="image1.jpg" alt="Portfolio Image 1">
                <p>Makeup Look 1</p>
            </div>
            <div class="portfolio-item">
                <img src="image2.jpg" alt="Portfolio Image 2">
                <p>Makeup Look 2</p>
            </div>
            <div class="portfolio-item">
                <img src="image3.jpg" alt="Portfolio Image 3">
                <p>Makeup Look 3</p>
            </div>
        </div>
    </section>

    <!-- Bridal Makeup Section -->
    <section id="bridal-makeup" class="bridal-makeup">
        <h2>Bridal Makeup Services</h2>
        <p>Expert bridal makeup for your special day</p>
        <ul>
            <li>Customized makeup looks</li>
            <li>Trained and certified artists</li>
            <li>High-quality products</li>
        </ul>
        <button>Book Your Bridal Makeup</button>
    </section>

    <!-- Personal Styling Section -->
    <section id="personal-styling" class="personal-styling">
        <h2>Personal Styling Services</h2>
        <p>Expert personal styling for any occasion</p>
        <ul>
            <li>Wardrobe consultations</li>
            <li>Personal shopping</li>
            <li>Style coaching</li>
        </ul>
        <button>Book Your Personal Styling</button>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Get in Touch</h2>
        <p>Contact us for more information or to book your appointment</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <button>Send Message</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; [Artist Name] 2023</p>
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
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

/* Portfolio Styles */
.portfolio {
    padding: 2em;
}

.portfolio-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 20px;
}

.portfolio-item {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.portfolio-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

/* Bridal Makeup and Personal Styling Styles */
.bridal-makeup, .personal-styling {
    padding: 2em;
}

.bridal-makeup ul, .personal-styling ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.bridal-makeup li, .personal-styling li {
    margin-bottom: 10px;
}

.bridal-makeup button, .personal-styling button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Contact Styles */
.contact {
    padding: 2em;
}

.contact form {
    max-width: 500px;
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
}

.contact button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
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
