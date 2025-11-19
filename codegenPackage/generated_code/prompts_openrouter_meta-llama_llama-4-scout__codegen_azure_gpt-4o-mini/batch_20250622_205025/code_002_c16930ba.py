"""
Generated Code Metadata:
========================
Original URL: https://haus-alpenrose.com
Prompt: Generate HTML and CSS code for a simple website homepage, similar to Haus Alpenrose, with sections for accommodations, location, and contact information.
Generated: DETERMINISTIC_c16930ba63053b8b
Batch ID: 20250622_205025
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
    <title>Haus Alpenrose</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Haus Alpenrose</h1>
        <nav>
            <ul>
                <li><a href="#accommodations">Accommodations</a></li>
                <li><a href="#location">Location</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="accommodations">
            <h2>Accommodations</h2>
            <p>Experience comfort and luxury in our beautifully designed rooms.</p>
            <ul>
                <li>Single Room</li>
                <li>Double Room</li>
                <li>Family Suite</li>
            </ul>
        </section>

        <section id="location">
            <h2>Location</h2>
            <p>Located in the heart of the Alps, Haus Alpenrose offers breathtaking views and easy access to local attractions.</p>
            <p>Address: 123 Alpine Road, Mountain Town, Country</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>For inquiries, please reach out via email or phone.</p>
            <p>Email: info@hausalpenrose.com</p>
            <p>Phone: +123 456 7890</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Haus Alpenrose. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: white;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: white;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

section {
    margin-bottom: 40px;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
