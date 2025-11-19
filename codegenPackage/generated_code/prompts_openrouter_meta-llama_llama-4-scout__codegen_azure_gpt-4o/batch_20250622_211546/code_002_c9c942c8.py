"""
Generated Code Metadata:
========================
Original URL: https://cybersamurai.live
Prompt: Generate HTML and CSS code for a basic website template that includes a public_html directory structure.
Generated: DETERMINISTIC_c9c942c8bae70f55
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```plaintext
public_html/
├── index.html
├── css/
│   └── styles.css
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Basic website template">
    <meta name="author" content="Your Name">
    <title>Basic Website Template</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Welcome to My Website</h1>
            <nav>
                <ul class="nav-links">
                    <li><a href="#about">About</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content Section -->
    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>This is a basic website template designed for demonstration purposes.</p>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <p>We offer a variety of services to meet your needs.</p>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Your Name. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

**css/styles.css**
```css
/* General Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Container Styling */
.container {
    width: 80%;
    margin: 0 auto;
    max-width: 1200px;
}

/* Header Styling */
header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

header h1 {
    text-align: center;
    margin-bottom: 0.5rem;
}

header nav {
    text-align: center;
}

header .nav-links {
    list-style: none;
    padding: 0;
}

header .nav-links li {
    display: inline;
    margin: 0 10px;
}

header .nav-links a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

header .nav-links a:hover {
    text-decoration: underline;
}

/* Main Content Styling */
main {
    padding: 2rem 0;
}

main h2 {
    margin-bottom: 1rem;
    color: #333;
}

main p {
    margin-bottom: 1rem;
}

/* Footer Styling */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
    margin-top: 2rem;
}

footer p {
    margin: 0;
}
```
