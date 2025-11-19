"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Create a code snippet in HTML/CSS to design a simple and intuitive navigation menu for a website offering DIY legal forms, inspired by the layout on launchlawinc.com.
Generated: DETERMINISTIC_36f15a8e23b32c0c
Batch ID: 20250622_210856
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
    <title>DIY Legal Forms Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">
                <a href="#">DIY Legal Forms</a>
            </div>
            <ul class="nav-links">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#resources">Resources</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
            <div class="menu-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
        </nav>
    </header>

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

/* Body styling */
body {
    font-family: Arial, sans-serif;
}

/* Navigation bar styling */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 1rem 2rem;
}

/* Logo styling */
.logo a {
    color: #fff;
    text-decoration: none;
    font-size: 1.5rem;
}

/* Navigation links styling */
.nav-links {
    list-style: none;
    display: flex;
}

.nav-links li {
    margin: 0 1rem;
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

.bar {
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
        display: flex; /* Show menu toggle on mobile */
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
