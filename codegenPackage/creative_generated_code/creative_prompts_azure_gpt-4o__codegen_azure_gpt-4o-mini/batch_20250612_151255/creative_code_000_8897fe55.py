"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staketelegramapp.com
Prompt: Write HTML and CSS code to create a responsive navigation bar similar to the one described in the Avenger Bootstrap template, including toggle functionality.
Generated: DETERMINISTIC_8897fe55bfb83114
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
    <link rel="stylesheet" href="styles.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>
<body>
    <!-- Navigation Bar -->
    <nav class="navbar">
        <div class="container">
            <div class="logo">
                <a href="#">Brand</a>
            </div>
            <div class="toggle" id="toggle">
                <i class="fas fa-bars"></i>
            </div>
            <ul class="nav-links" id="nav-links">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Services</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    </nav>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}

/* Navigation bar styles */
.navbar {
    background-color: #333;
    color: white;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
}

/* Logo styles */
.logo a {
    color: white;
    text-decoration: none;
    font-size: 24px;
}

/* Navigation links */
.nav-links {
    list-style: none;
    display: flex;
    transition: max-height 0.3s ease;
}

/* Hide nav links by default on mobile */
.nav-links li {
    margin: 0 15px;
}

.nav-links li a {
    color: white;
    text-decoration: none;
}

.toggle {
    display: none; /* Hidden on larger screens */
}

/* Responsive styles */
@media (max-width: 768px) {
    .nav-links {
        display: none; /* Hidden on mobile */
        flex-direction: column;
        max-height: 0;
        overflow: hidden;
    }
    
    .nav-links.active {
        display: flex; /* Show when active */
        max-height: 500px; /* Arbitrary large value for transition */
    }

    .toggle {
        display: block; /* Show the toggle icon */
        cursor: pointer;
    }
}
```

```javascript
// script.js

// Toggle functionality for the navigation menu
document.getElementById('toggle').addEventListener('click', function () {
    const navLinks = document.getElementById('nav-links');
    navLinks.classList.toggle('active');
});
```
