"""
Generated Code Metadata:
========================
Original URL: https://giaodien.4wellmedia.com
Prompt: "Generate code for a responsive website header using HTML, CSS, and JavaScript, inspired by 4 Well Media's designs."
Generated: DETERMINISTIC_9b588929bbe43d62
Batch ID: 20250622_210703
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
    <title>Responsive Header</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="logo">MyWebsite</div>
        <nav class="navbar">
            <ul class="nav-list">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        <div class="menu-toggle" id="mobile-menu">
            <span class="bar"></span>
            <span class="bar"></span>
            <span class="bar"></span>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <section id="home">
            <h1>Welcome to My Website</h1>
        </section>
        <section id="about">
            <h2>About Us</h2>
        </section>
        <section id="services">
            <h2>Our Services</h2>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Header Styles */
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 2rem;
    background-color: #333;
    color: #fff;
}

/* Logo Styles */
.logo {
    font-size: 1.5rem;
    font-weight: bold;
}

/* Navbar Styles */
.navbar {
    display: flex;
}

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

/* Mobile Menu Styles */
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

/* Responsive Styles */
@media (max-width: 768px) {
    .navbar {
        display: none; /* Hide navbar by default */
    }

    .menu-toggle {
        display: flex; /* Show menu toggle */
    }

    .navbar.active {
        display: flex; /* Show navbar when active */
        flex-direction: column;
        position: absolute;
        top: 60px;
        right: 0;
        background-color: #333;
        width: 100%;
    }

    .nav-list {
        flex-direction: column;
        width: 100%;
    }

    .nav-list li {
        margin: 1rem 0;
        text-align: center;
    }
}
```

```javascript
// script.js

// Function to toggle the mobile menu
const mobileMenu = document.getElementById('mobile-menu');
const navbar = document.querySelector('.navbar');

// Event listener for mobile menu toggle
mobileMenu.addEventListener('click', () => {
    try {
        navbar.classList.toggle('active'); // Toggle the active class
    } catch (error) {
        console.error('Error toggling mobile menu:', error); // Log any errors
    }
});
```
