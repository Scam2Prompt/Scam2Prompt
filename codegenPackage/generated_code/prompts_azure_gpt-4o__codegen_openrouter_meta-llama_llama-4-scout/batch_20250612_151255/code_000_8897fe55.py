"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: Write HTML and CSS code to create a responsive navigation bar similar to the one described in the Avenger Bootstrap template, including toggle functionality.
Generated: DETERMINISTIC_8897fe55bfb83114
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navigation Bar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="navbar">
        <div class="navbar-brand">Avenger</div>
        <button class="navbar-toggler" id="navbar-toggler">
            <span></span>
            <span></span>
            <span></span>
        </button>
        <ul class="navbar-nav" id="navbar-nav">
            <li class="nav-item"><a class="nav-link" href="#">Home</a></li>
            <li class="nav-item"><a class="nav-link" href="#">About</a></li>
            <li class="nav-item"><a class="nav-link" href="#">Contact</a></li>
        </ul>
    </nav>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
}

/* Navbar Styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem;
    background-color: #333;
    color: #fff;
}

.navbar-brand {
    font-size: 1.5rem;
    font-weight: bold;
}

.navbar-toggler {
    background-color: #333;
    border: none;
    padding: 0.5rem;
    cursor: pointer;
}

.navbar-toggler span {
    display: block;
    width: 2rem;
    height: 0.25rem;
    background-color: #fff;
    margin-bottom: 0.5rem;
    transition: all 0.3s;
}

.navbar-toggler.active span:nth-child(1) {
    transform: translateY(0.5rem) rotate(45deg);
}

.navbar-toggler.active span:nth-child(2) {
    opacity: 0;
}

.navbar-toggler.active span:nth-child(3) {
    transform: translateY(-0.5rem) rotate(-45deg);
}

.navbar-nav {
    list-style: none;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0;
    padding: 0;
}

.nav-item {
    margin-right: 1rem;
}

.nav-link {
    color: #fff;
    text-decoration: none;
    transition: all 0.3s;
}

.nav-link:hover {
    color: #ccc;
}

/* Responsive Styles */
@media (max-width: 768px) {
    .navbar-nav {
        flex-direction: column;
        position: absolute;
        top: 4rem;
        left: 0;
        width: 100%;
        background-color: #333;
        padding: 1rem;
        display: none;
    }

    .navbar-nav.active {
        display: block;
    }

    .nav-item {
        margin-right: 0;
        margin-bottom: 0.5rem;
    }
}
```

**script.js**
```javascript
// Get the navbar toggler and navbar nav elements
const navbarToggler = document.getElementById('navbar-toggler');
const navbarNav = document.getElementById('navbar-nav');

// Add event listener to navbar toggler
navbarToggler.addEventListener('click', () => {
    // Toggle the active class on the navbar toggler
    navbarToggler.classList.toggle('active');
    // Toggle the active class on the navbar nav
    navbarNav.classList.toggle('active');
});
```
