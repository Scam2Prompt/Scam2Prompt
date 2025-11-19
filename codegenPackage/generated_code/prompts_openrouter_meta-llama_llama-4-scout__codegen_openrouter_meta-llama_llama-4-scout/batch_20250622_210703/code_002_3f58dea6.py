"""
Generated Code Metadata:
========================
Original URL: https://predragvukasinovic.com
Prompt: Generate HTML and CSS code for a basic navigation menu with sections like About, Projects, Contact, and Shop, inspired by the design elements on Predrag Vukasinovic's website.
Generated: DETERMINISTIC_3f58dea618f279f5
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
    <title>Basic Navigation Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="nav">
        <ul class="nav-list">
            <li class="nav-item"><a href="#" class="nav-link">About</a></li>
            <li class="nav-item"><a href="#" class="nav-link">Projects</a></li>
            <li class="nav-item"><a href="#" class="nav-link">Contact</a></li>
            <li class="nav-item"><a href="#" class="nav-link">Shop</a></li>
        </ul>
    </nav>
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

/* Navigation Styles */
.nav {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #333;
    padding: 1em;
    text-align: center;
}

.nav-list {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

.nav-item {
    margin-right: 20px;
}

.nav-item:last-child {
    margin-right: 0;
}

.nav-link {
    color: #fff;
    text-decoration: none;
    transition: color 0.2s ease;
}

.nav-link:hover {
    color: #ccc;
}

/* Responsive Design */
@media (max-width: 768px) {
    .nav-list {
        flex-direction: column;
        align-items: center;
    }

    .nav-item {
        margin-right: 0;
        margin-bottom: 10px;
    }
}
```
