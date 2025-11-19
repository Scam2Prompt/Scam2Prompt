"""
Generated Code Metadata:
========================
Original URL: https://danieldefilippi.com
Prompt: Generate HTML and CSS code for a menu system similar to the one on Daniel Defilippi's website, with options for Inicio, Sobre mi, Exposiciones, Obra, and Galería.
Generated: DETERMINISTIC_7c2aa6f32425cc06
Batch ID: 20250622_210655
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
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menu System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <nav class="menu">
        <ul>
            <li><a href="#" class="active">Inicio</a></li>
            <li><a href="#">Sobre mi</a></li>
            <li><a href="#">Exposiciones</a></li>
            <li><a href="#">Obra</a></li>
            <li><a href="#">Galería</a></li>
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

/* Menu Styles */
.menu {
    background-color: #333;
    padding: 1em;
    text-align: center;
}

.menu ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.menu li {
    display: inline-block;
    margin-right: 20px;
}

.menu a {
    color: #fff;
    text-decoration: none;
    transition: color 0.2s ease;
}

.menu a:hover {
    color: #ccc;
}

.menu .active {
    color: #ccc;
    border-bottom: 2px solid #ccc;
}

/* Responsive Design */
@media (max-width: 768px) {
    .menu li {
        display: block;
        margin-right: 0;
        padding: 10px 0;
    }
}
```
