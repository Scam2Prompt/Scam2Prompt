"""
Generated Code Metadata:
========================
Original URL: https://perumakers.org
Prompt: Write JavaScript code to display a responsive menu for a website like Perú Makers, including links to "Inicio," "Nosotros," "Proyectos," "Donaciones," and "Blog."
Generated: DETERMINISTIC_a621c13078855c8d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="logo">Perú Makers</div>
            <div class="menu-toggle" id="mobile-menu">
                <span class="bar"></span>
                <span class="bar"></span>
                <span class="bar"></span>
            </div>
            <ul class="nav-list" id="nav-list">
                <li><a href="#inicio">Inicio</a></li>
                <li><a href="#nosotros">Nosotros</a></li>
                <li><a href="#proyectos">Proyectos</a></li>
                <li><a href="#donaciones">Donaciones</a></li>
                <li><a href="#blog">Blog</a></li>
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

/* Body styles */
body {
    font-family: Arial, sans-serif;
}

/* Navbar styles */
.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #333;
    padding: 1rem;
}

/* Logo styles */
.logo {
    color: #fff;
    font-size: 1.5rem;
}

/* Navigation list styles */
.nav-list {
    list-style: none;
    display: flex;
}

/* Navigation links styles */
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

/* Mobile menu toggle styles */
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
        left: 0;
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
const navList = document.getElementById('nav-list');

// Event listener for mobile menu toggle
mobileMenu.addEventListener('click', () => {
    try {
        navList.classList.toggle('active');
    } catch (error) {
        console.error('Error toggling mobile menu:', error);
    }
});
```
