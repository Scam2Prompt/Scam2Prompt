"""
Generated Code Metadata:
========================
Original URL: https://kingroofing.com
Prompt: Develop a basic web page using HTML and CSS that showcases King Roofing's portfolio, including images and testimonials from previous clients.
Generated: DETERMINISTIC_e7afea976ebb61a6
Batch ID: 20250622_212830
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
    <title>King Roofing Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>King Roofing</h1>
        <nav>
            <ul>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="gallery">
                <img src="roof1.jpg" alt="Residential Roofing Project" />
                <img src="roof2.jpg" alt="Commercial Roofing Project" />
                <img src="roof3.jpg" alt="Roof Repair Project" />
                <img src="roof4.jpg" alt="New Roof Installation" />
            </div>
        </section>

        <section id="testimonials">
            <h2>What Our Clients Say</h2>
            <blockquote>
                <p>"King Roofing did an amazing job on our new roof! Highly recommend!"</p>
                <footer>- Jane Doe</footer>
            </blockquote>
            <blockquote>
                <p>"Professional and efficient service. Our roof looks fantastic!"</p>
                <footer>- John Smith</footer>
            </blockquote>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 King Roofing. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, blockquote {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
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
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Gallery styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.gallery img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Testimonials styles */
blockquote {
    background: #ffffff;
    border-left: 5px solid #35424a;
    margin: 20px 0;
    padding: 10px 20px;
}

/* Contact form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    margin-top: 10px;
    padding: 10px;
    background: #35424a;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
}
```
