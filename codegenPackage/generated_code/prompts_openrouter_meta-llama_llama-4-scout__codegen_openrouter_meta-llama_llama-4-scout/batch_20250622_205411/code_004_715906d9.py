"""
Generated Code Metadata:
========================
Original URL: https://justicetree-mint.com
Prompt: "Create a simple webpage layout for a justice-focused non-profit organization."
Generated: DETERMINISTIC_715906d92a3a3102
Batch ID: 20250622_205411
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
    <title>Justice For All</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#our-work">Our Work</a></li>
                <li><a href="#get-involved">Get Involved</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Justice For All</h1>
        <p>Empowering marginalized communities through advocacy and education.</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>Our Mission</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
    </section>

    <!-- Our Work Section -->
    <section id="our-work">
        <h2>Our Initiatives</h2>
        <div class="initiative-cards">
            <div class="card">
                <h3>Education and Advocacy</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
            <div class="card">
                <h3>Community Support</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
            <div class="card">
                <h3>Policy Reform</h3>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
            </div>
        </div>
    </section>

    <!-- Get Involved Section -->
    <section id="get-involved">
        <h2>Make a Difference</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <button>Volunteer Today</button>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <form>
            <input type="email" placeholder="Email" required>
            <textarea placeholder="Message" required></textarea>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Justice For All. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

.initiative-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    width: 200px;
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

// Add event listener to volunteer button
document.querySelector('#get-involved button').addEventListener('click', () => {
    alert('Volunteer form will be available soon!');
});

// Add event listener to send button
document.querySelector('#contact form button').addEventListener('click', (e) => {
    e.preventDefault();
    alert('Message sent successfully!');
});
```
