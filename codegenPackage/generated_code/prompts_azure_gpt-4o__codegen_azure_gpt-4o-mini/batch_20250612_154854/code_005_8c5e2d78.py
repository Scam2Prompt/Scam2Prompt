"""
Generated Code Metadata:
========================
Original URL: https://socrates-gm.com
Prompt: Write a step-by-step guide in HTML and CSS for designing a user-friendly navigation menu similar to the one used in the Socrates GM portal.
Generated: DETERMINISTIC_8c5e2d78b66ac60e
Batch ID: 20250612_154854
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
    <title>User-Friendly Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">
                <a href="#">Socrates GM</a>
            </div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="menu-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </nav>
    </header>

    <main>
        <section id="home">
            <h1>Welcome to Socrates GM</h1>
            <p>Your journey begins here.</p>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>Learn more about our mission and values.</p>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <p>Discover the services we offer.</p>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
            <p>Get in touch with us.</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Socrates GM. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Navigation bar styling */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 10px 20px;
}

/* Logo styling */
.logo a {
    color: #fff;
    text-decoration: none;
    font-size: 24px;
}

/* Navigation links styling */
.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin: 0 15px;
}

.nav-links a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #f0a500; /* Highlight color on hover */
}

/* Mobile menu toggle */
.menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.menu-toggle .bar {
    height: 3px;
    width: 25px;
    background-color: #fff;
    margin: 3px 0;
}

/* Responsive styling */
@media (max-width: 768px) {
    .nav-links {
        display: none; /* Hide links by default */
        flex-direction: column;
        position: absolute;
        top: 60px; /* Position below the navbar */
        left: 0;
        background-color: #333;
        width: 100%;
    }

    .nav-links.active {
        display: flex; /* Show links when active */
    }

    .menu-toggle {
        display: flex; /* Show menu toggle */
    }
}
```

```javascript
// script.js

// Function to toggle the mobile menu
const mobileMenu = document.getElementById('mobile-menu');
const navLinks = document.querySelector('.nav-links');

// Event listener for mobile menu toggle
mobileMenu.addEventListener('click', () => {
    navLinks.classList.toggle('active'); // Toggle the active class
});
```
