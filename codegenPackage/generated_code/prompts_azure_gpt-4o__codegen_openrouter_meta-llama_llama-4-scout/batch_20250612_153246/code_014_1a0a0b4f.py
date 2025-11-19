"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: Generate a landing page design for a digital marketing agency, incorporating Rankraze's branding principles and 3R formula.
Generated: DETERMINISTIC_1a0a0b4f9e9bf70d
Batch ID: 20250612_153246
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
    <title>Rankraze Digital Marketing Agency</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>Welcome to Rankraze Digital Marketing Agency</h1>
        <p>Unlock your online potential with our expert solutions</p>
        <button>Discover How</button>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="service-cards">
            <div class="card">
                <h3>SEO</h3>
                <p>Improve your search engine rankings with our expert SEO strategies</p>
            </div>
            <div class="card">
                <h3>PPC</h3>
                <p>Drive conversions with targeted pay-per-click advertising</p>
            </div>
            <div class="card">
                <h3>Content Marketing</h3>
                <p>Create engaging content that resonates with your audience</p>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>At Rankraze, we believe in the 3R formula: <strong>Research</strong>, <strong>Recommend</strong>, and <strong>Results</strong>. Our team of experts will work with you to understand your business goals and develop a customized digital marketing strategy that drives real results.</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <form>
            <input type="text" placeholder="Name" required>
            <input type="email" placeholder="Email" required>
            <textarea placeholder="Message" required></textarea>
            <button>Send Message</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Rankraze Digital Marketing Agency</p>
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

#home {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#home h1 {
    font-size: 48px;
}

#home button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#services {
    padding: 2em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #f7f7f7;
    padding: 20px;
    margin: 20px;
    width: calc(33.33% - 20px);
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#about {
    padding: 2em;
}

#contact {
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
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

// Add event listener to the button in the hero section
document.querySelector('#home button').addEventListener('click', () => {
    // Scroll to the services section
    document.querySelector('#services').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to the form submission
document.querySelector('#contact form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Add form submission logic here
    console.log('Form submitted');
});
```
