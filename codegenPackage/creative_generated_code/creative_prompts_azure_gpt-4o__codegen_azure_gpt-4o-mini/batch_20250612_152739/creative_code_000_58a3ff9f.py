"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Write HTML5 and CSS3 code for a corporate design webpage that includes sections for "About Us," "Clients," and "Contact," similar to the structure described on dionlineaja.id.
Generated: DETERMINISTIC_58a3ff9fb18d919e
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Corporate Design Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Company Name</h1>
            <nav>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#clients">Clients</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- About Us Section -->
    <section id="about">
        <div class="container">
            <h2>About Us</h2>
            <p>Welcome to our company! We specialize in providing top-notch services to our clients.</p>
            <p>With a dedicated team of professionals, we ensure quality and satisfaction in every project.</p>
        </div>
    </section>

    <!-- Clients Section -->
    <section id="clients">
        <div class="container">
            <h2>Our Clients</h2>
            <p>We are proud to have worked with a diverse range of clients.</p>
            <ul>
                <li>Client 1</li>
                <li>Client 2</li>
                <li>Client 3</li>
                <li>Client 4</li>
            </ul>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form action="submit_form.php" method="post" id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Company Name. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body and Header Styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
}

header .container {
    width: 80%;
    margin: auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

header nav ul {
    list-style: none;
}

header nav ul li {
    display: inline;
    margin-right: 20px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section Styles */
section {
    padding: 2rem 0;
    background: #fff;
    margin: 1rem 0;
}

section h2 {
    margin-bottom: 1rem;
}

/* Form Styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 0.5rem;
}

form input, form textarea {
    padding: 0.5rem;
    margin-bottom: 1rem;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    padding: 0.7rem;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #555;
}

/* Footer Styles */
footer {
    text-align: center;
    padding: 1rem 0;
    background: #333;
    color: #fff;
}
```

This code provides a simple, structured, and styled corporate design webpage with sections for "About Us," "Clients," and "Contact." The HTML is well-structured, and the CSS offers basic styling adhering to best practices. Adjust the content and styles to match specific branding as needed.
