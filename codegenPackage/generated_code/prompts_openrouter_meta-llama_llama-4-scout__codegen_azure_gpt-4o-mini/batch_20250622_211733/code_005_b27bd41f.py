"""
Generated Code Metadata:
========================
Original URL: https://tante4dx41.com
Prompt: Write a JavaScript code snippet to implement a responsive and interactive navigation menu, like the one on TANTE4D, that adapts to different screen sizes and devices.
Generated: DETERMINISTIC_b27bd41f3dbc19fd
Batch ID: 20250622_211733
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
    <title>Responsive Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="logo">MyLogo</div>
        <div class="menu-toggle" id="mobile-menu">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </div>
        <ul class="nav-list">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#services">Services</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <script src="script.js"></script>
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

/* Navbar styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 1rem;
}

.logo {
    color: #fff;
    font-size: 1.5rem;
}

/* Navigation list styles */
.nav-list {
    list-style: none;
    display: flex;
}

.nav-list li {
    margin: 0 1rem;
}

.nav-list a {
    color: #fff;
    text-decoration: none;
    transition: color 0.3s;
}

.nav-list a:hover {
    color: #f0a500;
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

/* Responsive styles */
@media (max-width: 768px) {
    .nav-list {
        display: none;
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: #333;
        width: 100%;
    }

    .nav-list.active {
        display: flex;
    }

    .menu-toggle {
        display: flex;
    }
}
```

```javascript
// script.js

// Function to toggle the mobile menu
const mobileMenu = document.getElementById('mobile-menu');
const navList = document.querySelector('.nav-list');

// Event listener for mobile menu toggle
mobileMenu.addEventListener('click', () => {
    // Toggle the 'active' class to show/hide the menu
    navList.classList.toggle('active');
});

// Close the mobile menu when a link is clicked
navList.addEventListener('click', () => {
    if (navList.classList.contains('active')) {
        navList.classList.remove('active');
    }
});
```

This code provides a responsive navigation menu that adapts to different screen sizes, with a mobile toggle feature. It includes basic styling, JavaScript functionality for interactivity, and follows best practices for clean and maintainable code.
