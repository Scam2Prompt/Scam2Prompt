"""
Generated Code Metadata:
========================
Original URL: https://masscompras.com
Prompt: Write code to create a responsive navigation menu for an online store with categories like "Productos" and "Servicios," similar to the menu on "Mass Compras."
Generated: DETERMINISTIC_58687211fc1836e3
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="nav">
        <input type="checkbox" id="nav-check">
        <label for="nav-check" class="nav-toggle">
            <span></span>
            <span></span>
            <span></span>
        </label>
        <ul class="nav-list">
            <li><a href="#" class="nav-link">Productos</a></li>
            <li><a href="#" class="nav-link">Servicios</a></li>
            <li><a href="#" class="nav-link">Acerca de</a></li>
            <li><a href="#" class="nav-link">Contacto</a></li>
        </ul>
    </nav>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --nav-bg: #333;
    --nav-text: #fff;
    --nav-hover: #444;
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: var(--nav-bg);
    padding: 1em;
}

.nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
}

.nav-link {
    color: var(--nav-text);
    text-decoration: none;
    transition: color 0.2s ease;
}

.nav-link:hover {
    color: var(--nav-hover);
}

.nav-toggle {
    display: none;
    cursor: pointer;
}

.nav-toggle span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: var(--nav-text);
    margin: 5px 0;
    transition: all 0.3s;
}

#nav-check {
    display: none;
}

@media (max-width: 768px) {
    .nav {
        flex-direction: column;
        align-items: flex-start;
    }

    .nav-list {
        display: none;
        flex-direction: column;
        width: 100%;
    }

    .nav-list li {
        padding: 0.5em;
        border-bottom: 1px solid var(--nav-bg);
    }

    .nav-toggle {
        display: inline-block;
    }

    #nav-check:checked ~ .nav-list {
        display: flex;
    }
}
```

```javascript
// script.js

const navCheck = document.getElementById('nav-check');
const navToggle = document.querySelector('.nav-toggle');

navToggle.addEventListener('click', () => {
    navCheck.checked = !navCheck.checked;
});

// Add event listener to close menu when link is clicked
document.querySelectorAll('.nav-link').forEach((link) => {
    link.addEventListener('click', () => {
        navCheck.checked = false;
    });
});
```
