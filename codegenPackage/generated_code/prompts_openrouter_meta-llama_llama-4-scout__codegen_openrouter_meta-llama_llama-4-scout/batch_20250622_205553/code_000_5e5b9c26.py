"""
Generated Code Metadata:
========================
Original URL: https://smartcats.vip
Prompt: "Generate a website layout for an educational institution that emphasizes nature-inspired learning and creativity, similar to Cats, Cats, Cats, and Lasagna."
Generated: DETERMINISTIC_5e5b9c2643d51afb
Batch ID: 20250622_205553
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
    <title>Nature-Inspired Learning</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#programs">Programs</a></li>
                <li><a href="#admissions">Admissions</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <h1>Welcome to Nature-Inspired Learning</h1>
        <p>Emphasizing creativity and growth through nature-based education</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>Our Mission</h2>
        <p>At Nature-Inspired Learning, we believe that education should be a holistic experience that fosters a deep connection with the natural world. Our mission is to provide a nurturing environment that encourages creativity, curiosity, and growth.</p>
        <img src="nature-image.jpg" alt="Nature Image">
    </section>

    <!-- Programs Section -->
    <section id="programs">
        <h2>Our Programs</h2>
        <ul>
            <li>
                <h3>Early Childhood Education</h3>
                <p>Our early childhood program is designed for children aged 3-5 and focuses on play-based learning and exploration of the natural world.</p>
            </li>
            <li>
                <h3>Elementary Education</h3>
                <p>Our elementary program is designed for children aged 6-10 and emphasizes hands-on learning and project-based education.</p>
            </li>
        </ul>
    </section>

    <!-- Admissions Section -->
    <section id="admissions">
        <h2>Admissions Process</h2>
        <p>We are now accepting applications for the upcoming academic year. Please contact us to schedule a tour and learn more about our admissions process.</p>
        <button>Apply Now</button>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Phone: 555-555-5555</p>
        <p>Email: [info@natureinspiredlearning.org](mailto:info@natureinspiredlearning.org)</p>
        <p>Address: 123 Main St, Anytown, USA</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Nature-Inspired Learning</p>
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

#hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #ddd);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #333;
}

#hero h1 {
    font-size: 48px;
}

#hero p {
    font-size: 18px;
}

#hero button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#about {
    padding: 2em;
}

#about img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

#programs {
    padding: 2em;
}

#programs ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

#programs li {
    margin-bottom: 20px;
}

#admissions {
    padding: 2em;
}

#admissions button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#contact {
    padding: 2em;
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

// Add event listener to hero button
document.querySelector('#hero button').addEventListener('click', () => {
    // Scroll to about section
    document.querySelector('#about').scrollIntoView({ behavior: 'smooth' });
});

// Add event listener to admissions button
document.querySelector('#admissions button').addEventListener('click', () => {
    // Open application form in new tab
    window.open('application-form.html', '_blank');
});

// Handle form submission (example)
// const form = document.querySelector('#contact-form');
// form.addEventListener('submit', (e) => {
//     e.preventDefault();
//     // Send form data to server
// });
```
