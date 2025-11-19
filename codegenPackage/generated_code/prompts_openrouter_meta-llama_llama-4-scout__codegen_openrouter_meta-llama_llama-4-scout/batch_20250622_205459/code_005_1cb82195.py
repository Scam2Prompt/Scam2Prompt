"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Write a code example in HTML/CSS to create a responsive and accessible layout for a website promoting education and healthcare initiatives, similar to the NICER Foundation website.
Generated: DETERMINISTIC_1cb82195a336fca2
Batch ID: 20250622_205459
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
    <title>NICER Foundation</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav aria-label="Main Navigation">
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#initiatives">Initiatives</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero" role="banner">
        <h1>Empowering Communities through Education and Healthcare</h1>
        <p>Join us in making a difference</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>The NICER Foundation is a non-profit organization dedicated to improving the lives of individuals and communities through education and healthcare initiatives.</p>
    </section>

    <!-- Initiatives Section -->
    <section id="initiatives">
        <h2>Our Initiatives</h2>
        <div class="initiative-cards">
            <div class="initiative-card">
                <h3>Education for All</h3>
                <p>Providing access to quality education for underprivileged communities</p>
            </div>
            <div class="initiative-card">
                <h3>Healthcare Access</h3>
                <p>Improving healthcare outcomes through community-based initiatives</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Contact us to learn more about our initiatives and how you can get involved</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 NICER Foundation</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --font-family: Arial, sans-serif;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-family);
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

header {
    background-color: var(--primary-color);
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

#hero {
    background-image: linear-gradient(to bottom, #007bff, #0056b3);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#hero h1 {
    font-size: 48px;
}

#hero p {
    font-size: 18px;
}

button {
    background-color: var(--primary-color);
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

#about, #initiatives, #contact {
    padding: 2em;
}

.initiative-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.initiative-card {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    margin: 20px;
    width: calc(50% - 20px);
}

.initiative-card h3 {
    font-size: 18px;
    margin-top: 0;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input, textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive Design */

@media only screen and (max-width: 768px) {
    .initiative-card {
        width: 100%;
    }
}

@media only screen and (max-width: 480px) {
    #hero h1 {
        font-size: 24px;
    }
    #hero p {
        font-size: 14px;
    }
}
```
