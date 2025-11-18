"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staketelegramapp.com
Prompt: Write HTML and CSS code to create a responsive navigation bar similar to the one described in the Avenger Bootstrap template, including toggle functionality.
Generated: DETERMINISTIC_8897fe55bfb83114
Batch ID: 20250612_151255
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
    <title>Responsive Navigation Bar</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Navigation bar -->
    <nav class="navbar">
        <div class="navbar-container">
            <!-- Logo -->
            <a href="#" class="navbar-logo">Avenger</a>
            <!-- Toggle button for small screens -->
            <button class="navbar-toggle" id="navbar-toggle" aria-label="Toggle navigation">
                &#9776; <!-- Hamburger icon -->
            </button>
            <!-- Navigation links -->
            <ul class="navbar-menu" id="navbar-menu">
                <li class="navbar-item"><a href="#" class="navbar-link">Home</a></li>
                <li class="navbar-item"><a href="#" class="navbar-link">About</a></li>
                <li class="navbar-item"><a href="#" class="navbar-link">Services</a></li>
                <li class="navbar-item"><a href="#" class="navbar-link">Portfolio</a></li>
                <li class="navbar-item"><a href="#" class="navbar-link">Contact</a></li>
            </ul>
        </div>
    </nav>

    <!-- Link to external JavaScript -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body {
    margin: 0;
    font-family: Arial, sans-serif;
}

/* Navbar styling */
.navbar {
    background-color: #333; /* Dark background */
    color: #fff; /* White text */
    padding: 0.5rem 1rem;
}

.navbar-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
}

.navbar-logo {
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
    color: #fff;
}

.navbar-toggle {
    font-size: 1.5rem;
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
    display: none; /* Hidden by default */
}

.navbar-menu {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
}

.navbar-item {
    margin: 0 0.5rem;
}

.navbar-link {
    text-decoration: none;
    color: #fff;
    padding: 0.5rem 1rem;
    transition: background-color 0.3s ease;
}

.navbar-link:hover {
    background-color: #575757; /* Hover effect */
    border-radius: 4px;
}

/* Responsive styling */
@media (max-width: 768px) {
    .navbar-toggle {
        display: block; /* Show toggle button on smaller screens */
    }

    .navbar-menu {
        display: none; /* Hide menu initially */
        flex-direction: column;
        width: 100%;
        background-color: #333;
        position: absolute;
        top: 100%;
        left: 0;
    }

    .navbar-menu.active {
        display: flex; /* Show menu when active */
    }

    .navbar-item {
        text-align: center;
    }
}
```

```javascript
// script.js

// Select menu and toggle button elements
const navbarToggle = document.getElementById('navbar-toggle');
const navbarMenu = document.getElementById('navbar-menu');

// Add click event listener to the toggle button
navbarToggle.addEventListener('click', () => {
    // Toggle the "active" class on the menu
    navbarMenu.classList.toggle('active');
});

// Optional: Close the menu if clicked outside (for better UX)
document.addEventListener('click', (event) => {
    const isClickInsideNavbar = navbarToggle.contains(event.target) || navbarMenu.contains(event.target);
    if (!isClickInsideNavbar) {
        navbarMenu.classList.remove('active');
    }
});
```
