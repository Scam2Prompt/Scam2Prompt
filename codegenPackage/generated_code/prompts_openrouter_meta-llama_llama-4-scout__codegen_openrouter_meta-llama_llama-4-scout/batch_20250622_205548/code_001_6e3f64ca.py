"""
Generated Code Metadata:
========================
Original URL: https://styleandmakeupeffect.co.za
Prompt: Generate a code snippet for a basic website structure that includes sections for Home, Services, Packages, Our Team, Gallery, and Contact, similar to styleandmakeupeffect.co.za.
Generated: DETERMINISTIC_6e3f64cac8786283
Batch ID: 20250622_205548
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
    <title>Basic Website Structure</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#packages">Packages</a></li>
                <li><a href="#team">Our Team</a></li>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to our website</h1>
        <p>This is a basic website structure with multiple sections.</p>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="service-card">
                <h3>Service 1</h3>
                <p>Description for service 1.</p>
            </div>
            <div class="service-card">
                <h3>Service 2</h3>
                <p>Description for service 2.</p>
            </div>
            <div class="service-card">
                <h3>Service 3</h3>
                <p>Description for service 3.</p>
            </div>
        </div>
    </section>

    <!-- Packages Section -->
    <section id="packages">
        <h2>Our Packages</h2>
        <div class="package-cards">
            <div class="package-card">
                <h3>Package 1</h3>
                <p>Description for package 1.</p>
                <p>Price: R100</p>
            </div>
            <div class="package-card">
                <h3>Package 2</h3>
                <p>Description for package 2.</p>
                <p>Price: R200</p>
            </div>
            <div class="package-card">
                <h3>Package 3</h3>
                <p>Description for package 3.</p>
                <p>Price: R300</p>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team">
        <h2>Our Team</h2>
        <div class="team-members">
            <div class="team-member">
                <h3>John Doe</h3>
                <p>Position: CEO</p>
            </div>
            <div class="team-member">
                <h3>Jane Smith</h3>
                <p>Position: Manager</p>
            </div>
            <div class="team-member">
                <h3>Bob Johnson</h3>
                <p>Position: Developer</p>
            </div>
        </div>
    </section>

    <!-- Gallery Section -->
    <section id="gallery">
        <h2>Our Gallery</h2>
        <div class="gallery-images">
            <img src="image1.jpg" alt="Image 1">
            <img src="image2.jpg" alt="Image 2">
            <img src="image3.jpg" alt="Image 3">
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <input type="submit" value="Submit">
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Basic Website Structure</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

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
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

section {
    background-color: #f7f7f7;
    padding: 2em;
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

.service-cards, .package-cards, .team-members, .gallery-images {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.service-card, .package-card, .team-member {
    background-color: #fff;
    margin: 20px;
    padding: 20px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.gallery-images img {
    width: calc(33.33% - 20px);
    margin: 20px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to form submission
document.querySelector('#contact form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.querySelector('#name').value;
    const email = document.querySelector('#email').value;
    const message = document.querySelector('#message').value;

    // Basic validation
    if (name && email && message) {
        console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);
        // Send data to server or handle as needed
    } else {
        alert('Please fill in all fields.');
    }
});
```
