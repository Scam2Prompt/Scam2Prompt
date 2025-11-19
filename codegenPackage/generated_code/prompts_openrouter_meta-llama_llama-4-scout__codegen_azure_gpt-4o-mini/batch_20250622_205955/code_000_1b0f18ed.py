"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Generate a code snippet for a construction company's website, including sections for about, sectors, and contact us, with a focus on groundworks solutions and health and safety."
Generated: DETERMINISTIC_1b0f18ede2a347f5
Batch ID: 20250622_205955
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
    <title>Construction Company</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Our Construction Company</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#sectors">Sectors</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- About Section -->
        <section id="about">
            <h2>About Us</h2>
            <p>We specialize in groundworks solutions, providing top-notch services with a focus on health and safety.</p>
            <p>Our team is dedicated to delivering quality construction projects that meet the highest standards.</p>
        </section>

        <!-- Sectors Section -->
        <section id="sectors">
            <h2>Our Sectors</h2>
            <ul>
                <li>Residential Groundworks</li>
                <li>Commercial Groundworks</li>
                <li>Infrastructure Development</li>
                <li>Health and Safety Compliance</li>
            </ul>
            <p>We ensure that all our projects adhere to strict health and safety regulations.</p>
        </section>

        <!-- Contact Us Section -->
        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" action="submit_form.php" method="POST">
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
        <p>&copy; 2023 Construction Company. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handling
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server
            fetch('submit_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                alert('Message sent successfully!');
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error sending your message. Please try again later.');
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
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
    color: #ffffff;
    text-decoration: none;
}

/* Main section styling */
main {
    padding: 20px;
}

/* Section styling */
section {
    margin-bottom: 20px;
    background: #ffffff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    padding: 10px;
    background: #35424a;
    color: #ffffff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #2c3e50;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
