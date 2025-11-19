"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelax.io
Prompt: Generate a code snippet to create an index page similar to the one found on stelax.io.
Generated: DETERMINISTIC_e126909a55d643e7
Batch ID: 20250612_162728
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
    <title>Stelax-like Index Page</title>
    <!-- Link to CSS for styling -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Stelax Clone</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- About Section -->
        <section id="about">
            <h2>About Us</h2>
            <p>We provide top-notch solutions tailored to your business needs.</p>
        </section>

        <!-- Services Section -->
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Web Development</li>
                <li>Mobile App Development</li>
                <li>Cloud Solutions</li>
            </ul>
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" method="post" action="submit_form.php">
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
        <p>&copy; 2023 Stelax Clone. All rights reserved.</p>
    </footer>

    <script>
        // Check if the form is valid before submission
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            // Perform any necessary validation here
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !message) {
                event.preventDefault(); // Prevent form submission
                alert('All fields are required!');
            }
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default margin and padding */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styling */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styling */
section {
    padding: 20px;
    margin: 20px 0;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```
