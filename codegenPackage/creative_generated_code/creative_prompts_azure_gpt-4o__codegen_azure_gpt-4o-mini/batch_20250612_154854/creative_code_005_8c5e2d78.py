"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://socrates-gm.com
Prompt: Write a step-by-step guide in HTML and CSS for designing a user-friendly navigation menu similar to the one used in the Socrates GM portal.
Generated: DETERMINISTIC_8c5e2d78b66ac60e
Batch ID: 20250612_154854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
            <div class="logo">Socrates GM</div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
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
            <p>Your journey starts here.</p>
        </section>
        <!-- Additional sections for Services, About Us, and Contact can be added here -->
    </main>

    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header and navbar styles */
header {
    background-color: #333;
    color: #fff;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
}

.logo {
    font-size: 1.5rem;
}

/* Navigation links styles */
.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin-left: 2rem;
}

.nav-links a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s ease;
}

.nav-links a:hover {
    color: #ff6347; /* Tomato color on hover */
}

/* Mobile menu styles */
.menu-toggle {
    display: none;
    flex-direction: column;
    cursor: pointer;
}

.bar {
    height: 3px;
    width: 25px;
    background-color: #fff;
    margin: 3px 0;
}

/* Responsive styles */
@media (max-width: 768px) {
    .nav-links {
        display: none; /* Hide links initially */
        flex-direction: column;
        width: 100%;
        background-color: #333;
        position: absolute;
        top: 60px; /* Adjust based on the navbar height */
        left: 0;
    }

    .nav-links.active {
        display: flex; /* Show links when active */
    }

    .menu-toggle {
        display: flex; /* Show menu toggle on mobile */
    }
}
```

```javascript
// script.js

// Wait for the DOM to load before running the script
document.addEventListener("DOMContentLoaded", function() {
    const mobileMenu = document.getElementById("mobile-menu");
    const navLinks = document.querySelector(".nav-links");

    // Toggle the mobile menu visibility
    mobileMenu.addEventListener("click", function() {
        navLinks.classList.toggle("active");
    });
});
```
