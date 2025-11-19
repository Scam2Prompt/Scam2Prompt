"""
Generated Code Metadata:
========================
Original URL: https://xn--strkfysioterapi-ylb.no
Prompt: Create a simple HTML/CSS template for a physiotherapy clinic's homepage, including sections for services offered and contact information.
Generated: DETERMINISTIC_10c29e3f43671f0e
Batch ID: 20250622_204657
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
    <title>Physiotherapy Clinic</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Physiotherapy Clinic</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Physical Therapy</li>
                <li>Sports Rehabilitation</li>
                <li>Post-Surgery Rehabilitation</li>
                <li>Chronic Pain Management</li>
                <li>Massage Therapy</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Information</h2>
            <p>If you have any questions or would like to schedule an appointment, please reach out to us:</p>
            <address>
                <strong>Email:</strong> <a href="mailto:info@physiotherapyclinic.com">info@physiotherapyclinic.com</a><br>
                <strong>Phone:</strong> <a href="tel:+1234567890">+1 (234) 567-890</a><br>
                <strong>Address:</strong> 123 Wellness St, Health City, HC 12345
            </address>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Physiotherapy Clinic. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
body, h1, h2, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Set a basic font and background color */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Style the header */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Navigation styles */
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

/* Section styles */
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
    padding: 10px;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
