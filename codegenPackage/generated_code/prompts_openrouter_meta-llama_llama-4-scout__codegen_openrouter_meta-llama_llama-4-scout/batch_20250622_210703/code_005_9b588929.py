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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Website Header</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#" class="logo">Well Media</a></li>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
                <li class="hamburger" aria-label="Open menu">
                    <span></span>
                    <span></span>
                    <span></span>
                </li>
            </ul>
        </nav>
    </header>
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
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

nav a {
    color: #fff;
    text-decoration: none;
    transition: color 0.2s ease;
}

nav a:hover {
    color: #ccc;
}

.logo {
    font-size: 1.5em;
    font-weight: bold;
    margin-right: 1em;
}

.hamburger {
    display: none;
    cursor: pointer;
}

.hamburger span {
    display: block;
    width: 25px;
    height: 3px;
    background-color: #fff;
    margin-bottom: 5px;
    transition: transform 0.2s ease;
}

.hamburger.active span:nth-child(1) {
    transform: translateY(8px) rotate(45deg);
}

.hamburger.active span:nth-child(2) {
    opacity: 0;
}

.hamburger.active span:nth-child(3) {
    transform: translateY(-8px) rotate(-45deg);
}

/* Responsive Styles */
@media (max-width: 768px) {
    .hamburger {
        display: block;
    }

    nav ul {
        flex-direction: column;
        align-items: flex-start;
    }

    nav li:not(.hamburger) {
        display: none;
    }

    nav li.hamburger {
        margin-top: 1em;
    }
}

@media (max-width: 480px) {
    header {
        padding: 0.5em;
    }
}
```

**script.js**
```javascript
// Get the hamburger element
const hamburger = document.querySelector('.hamburger');

// Add event listener to hamburger
hamburger.addEventListener('click', () => {
    // Toggle active class on hamburger
    hamburger.classList.toggle('active');

    // Get the nav links
    const navLinks = document.querySelectorAll('nav li:not(.hamburger)');

    // Toggle display of nav links
    navLinks.forEach(link => {
        if (hamburger.classList.contains('active')) {
            link.style.display = 'block';
        } else {
            link.style.display = 'none';
        }
    });
});
```
