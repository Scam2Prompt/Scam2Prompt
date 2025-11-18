"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iteamworldwide.com
Prompt: Generate JavaScript code to implement a responsive navigation menu similar to the one on the iTeam Worldwide homepage.
Generated: DETERMINISTIC_acf56d94af2097c8
Batch ID: 20250612_151024
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
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">iTeam Worldwide</div>
            <div class="menu-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
            <ul class="nav-list" id="nav-list">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

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

body {
    font-family: Arial, sans-serif;
}

/* Navigation styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 10px 20px;
}

/* Logo styles */
.logo {
    color: #fff;
    font-size: 24px;
}

/* Navigation list styles */
.nav-list {
    list-style: none;
    display: flex;
}

/* Navigation links styles */
.nav-list li {
    margin: 0 15px;
}

.nav-list a {
    color: #fff;
    text-decoration: none;
    padding: 8px 15px;
}

/* Responsive menu toggle */
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

/* Media queries for responsiveness */
@media screen and (max-width: 768px) {
    .nav-list {
        display: none;
        flex-direction: column;
        width: 100%;
        background-color: #333;
        position: absolute;
        top: 60px; /* Adjust based on navbar height */
        left: 0;
        z-index: 1;
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

// Get DOM elements
const mobileMenu = document.getElementById('mobile-menu');
const navList = document.getElementById('nav-list');

// Function to toggle the navigation menu on mobile
function toggleMenu() {
    if (navList.classList.contains('active')) {
        navList.classList.remove('active');
    } else {
        navList.classList.add('active');
    }
}

// Event listener for mobile menu toggle
mobileMenu.addEventListener('click', toggleMenu);

// Optional: Close menu on link click (for better UX)
navList.addEventListener('click', () => {
    if (navList.classList.contains('active')) {
        navList.classList.remove('active');
    }
});
```

This code creates a responsive navigation menu similar to the one on the iTeam Worldwide homepage, with proper styling, JavaScript functionality, and comments to explain each part.
