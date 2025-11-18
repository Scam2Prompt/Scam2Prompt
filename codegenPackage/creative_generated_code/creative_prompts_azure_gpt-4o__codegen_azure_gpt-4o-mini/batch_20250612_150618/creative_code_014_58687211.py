"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Write code to create a responsive navigation menu for an online store with categories like "Productos" and "Servicios," similar to the menu on "Mass Compras."
Generated: DETERMINISTIC_58687211fc1836e3
Batch ID: 20250612_150618
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
    <title>Responsive Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <!-- Navigation Menu -->
    <nav class="navbar">
        <div class="container">
            <div class="logo">
                <a href="#">Online Store</a>
            </div>
            <ul class="nav-links">
                <li><a href="#productos">Productos</a></li>
                <li><a href="#servicios">Servicios</a></li>
                <li><a href="#contacto">Contacto</a></li>
            </ul>
            <div class="menu-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </div>
    </nav>

    <section id="productos">
        <h1>Productos</h1>
        <!-- Product content goes here -->
    </section>

    <section id="servicios">
        <h1>Servicios</h1>
        <!-- Service content goes here -->
    </section>

    <section id="contacto">
        <h1>Contacto</h1>
        <!-- Contact content goes here -->
    </section>
    
    <!-- Footer -->
    <footer>
        <p>&copy; 2023 Online Store. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

/* Navigation styles */
.navbar {
    background-color: #333;
    color: white;
    padding: 1rem 0;
}

.container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: auto;
    padding: 0 20px;
}

.logo a {
    color: white;
    text-decoration: none;
    font-size: 1.5rem;
}

.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin: 0 15px;
}

.nav-links a {
    color: white;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #f0a500;
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
    background-color: white;
    margin: 4px 0;
}

/* Responsive styles */
@media (max-width: 768px) {
    .nav-links {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: #333;
        width: 100%;
    }
    
    .nav-links.active {
        display: flex;
    }

    .menu-toggle {
        display: flex;
    }
}
```

```javascript
// script.js

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    // Toggle mobile menu visibility
    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // Close mobile menu when a link is clicked
    navLinks.addEventListener('click', () => {
        if (navLinks.classList.contains('active')) {
            navLinks.classList.remove('active');
        }
    });
});
```

This code provides a responsive navigation menu for an online store, including categories like "Productos" and "Servicios," with proper structure, styling, and functionality.
