"""
Generated Code Metadata:
========================
Original URL: https://kiddooplayway.com
Prompt: Write a code for a simple webpage that showcases the curriculum and activities offered by a play school like Kiddoo Playway, which has 75% activity-based learning.
Generated: DETERMINISTIC_72181fdd1f4e878b
Batch ID: 20250622_210655
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
    <title>Kiddoo Playway</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#curriculum">Curriculum</a></li>
                <li><a href="#activities">Activities</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Kiddoo Playway</h1>
        <p>75% Activity-Based Learning for a fun and engaging education</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>Kiddoo Playway is a play school dedicated to providing a nurturing and engaging environment for young learners. Our approach focuses on 75% activity-based learning, ensuring that children have fun while developing essential skills.</p>
    </section>

    <!-- Curriculum Section -->
    <section id="curriculum">
        <h2>Our Curriculum</h2>
        <ul>
            <li>Play-based learning</li>
            <li>Interactive storytelling</li>
            <li>Art and craft sessions</li>
            <li>Music and movement classes</li>
            <li>Science experiments</li>
        </ul>
    </section>

    <!-- Activities Section -->
    <section id="activities">
        <h2>Our Activities</h2>
        <div class="activity-grid">
            <div class="activity-card">
                <h3>Yoga and Meditation</h3>
                <p>Introducing children to mindfulness and relaxation techniques</p>
            </div>
            <div class="activity-card">
                <h3>Cooking and Baking</h3>
                <p>Teaching children essential life skills through culinary activities</p>
            </div>
            <div class="activity-card">
                <h3>Outdoor Games</h3>
                <p>Encouraging physical activity and teamwork through outdoor games</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Phone: 123-456-7890</p>
        <p>Email: <a href="mailto:info@kiddooplayway.com">info@kiddooplayway.com</a></p>
        <p>Address: 123 Main St, Anytown, USA</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Kiddoo Playway</p>
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
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;
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
    background-color: #444;
}

#about, #curriculum, #activities, #contact {
    padding: 2em;
}

.activity-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

.activity-card {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
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

// Add event listener to button
document.querySelector('.hero button').addEventListener('click', () => {
    // Scroll to about section
    document.querySelector('#about').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to nav links
document.querySelectorAll('header nav a').forEach((link) => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const sectionId = link.getAttribute('href');
        document.querySelector(sectionId).scrollIntoView({ behavior: 'smooth' });
    });
});
```
