"""
Generated Code Metadata:
========================
Original URL: https://youngistaan.org
Prompt: "Create a simple web page using HTML and CSS for an NGO that provides educational programs for children in need, inspired by Youngistaan's projects."
Generated: DETERMINISTIC_efdbd8276cfc99a7
Batch ID: 20250622_210703
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
    <title>NGO Educational Programs for Children</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Empowering Children Through Education</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#programs">Our Programs</a></li>
                <li><a href="#get-involved">Get Involved</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>We are a non-profit organization dedicated to providing educational opportunities for children in need. Our mission is to empower the next generation through quality education and support.</p>
        </section>

        <section id="programs">
            <h2>Our Programs</h2>
            <ul>
                <li>
                    <h3>Tutoring Services</h3>
                    <p>One-on-one tutoring sessions to help children excel in their studies.</p>
                </li>
                <li>
                    <h3>After-School Programs</h3>
                    <p>Engaging activities and learning opportunities after school hours.</p>
                </li>
                <li>
                    <h3>Scholarship Programs</h3>
                    <p>Financial assistance for underprivileged children to pursue their education.</p>
                </li>
            </ul>
        </section>

        <section id="get-involved">
            <h2>Get Involved</h2>
            <p>Your support can make a difference! Join us in our mission to provide education to children in need.</p>
            <button onclick="alert('Thank you for your interest!')">Donate Now</button>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" onsubmit="return handleSubmit(event)">
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
        <p>&copy; 2023 NGO Educational Programs. All rights reserved.</p>
    </footer>

    <script>
        // Function to handle form submission
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Basic validation
            if (name && email && message) {
                alert('Thank you for your message, ' + name + '!');
                document.getElementById('contact-form').reset(); // Reset form after submission
            } else {
                alert('Please fill in all fields.');
            }
            return false; // Prevent form from submitting
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 10px 0;
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
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Form styles */
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
    background: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007BFF;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
