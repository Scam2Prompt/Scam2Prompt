"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Generate code to create a simple web page for a business like King Of Icecream that sells ice cream and snow cones from a truck.
Generated: DETERMINISTIC_152deab4e064bacb
Batch ID: 20250622_210650
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
    <title>King Of Icecream</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#menu">Menu</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Welcome to King Of Icecream!</h1>
            <p>Cool treats on wheels!</p>
        </section>
        <section id="menu">
            <h2>Menu</h2>
            <table>
                <thead>
                    <tr>
                        <th>Item</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Ice Cream (Single Scoop)</td>
                        <td>$3.50</td>
                    </tr>
                    <tr>
                        <td>Ice Cream (Double Scoop)</td>
                        <td>$5.00</td>
                    </tr>
                    <tr>
                        <td>Snow Cone</td>
                        <td>$2.50</td>
                    </tr>
                    <tr>
                        <td>Combo (Ice Cream & Snow Cone)</td>
                        <td>$6.00</td>
                    </tr>
                </tbody>
            </table>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>We're King Of Icecream, your go-to destination for delicious ice cream and snow cones on the go! Our truck is equipped with everything we need to serve you a cool treat on a hot day.</p>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
            <p>Phone: 555-555-5555</p>
            <p>Email: <a href="mailto:info@kingoficecream.com">info@kingoficecream.com</a></p>
            <p>Follow us on social media: 
                <a href="#" target="_blank">Facebook</a> | 
                <a href="#" target="_blank">Instagram</a> | 
                <a href="#" target="_blank">Twitter</a>
            </p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 King Of Icecream</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f0f0f0;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// script.js

// Add event listener to menu items
document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('#menu table tbody tr');

    menuItems.forEach(item => {
        item.addEventListener('click', function() {
            alert(`You selected: ${item.cells[0].textContent} - $${item.cells[1].textContent}`);
        });
    });
});
```
