"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Generate a sample HTML page for a hotel website, incorporating essential features like a room gallery, pricing, and contact information, inspired by Vila Vračar's website structure.
Generated: DETERMINISTIC_0c24bbab2a4f43f4
Batch ID: 20250622_210655
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://facebook.com/vilavracar": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://instagram.com/vilavracar": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vila Vračar - Hotel</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Vila Vračar</h1>
        <nav>
            <ul>
                <li><a href="#rooms">Rooms</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="rooms">
            <h2>Our Rooms</h2>
            <div class="gallery">
                <figure>
                    <img src="room1.jpg" alt="Deluxe Room">
                    <figcaption>Deluxe Room</figcaption>
                </figure>
                <figure>
                    <img src="room2.jpg" alt="Standard Room">
                    <figcaption>Standard Room</figcaption>
                </figure>
                <figure>
                    <img src="room3.jpg" alt="Suite">
                    <figcaption>Suite</figcaption>
                </figure>
            </div>
        </section>

        <section id="pricing">
            <h2>Room Pricing</h2>
            <table>
                <thead>
                    <tr>
                        <th>Room Type</th>
                        <th>Price per Night</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Deluxe Room</td>
                        <td>$150</td>
                    </tr>
                    <tr>
                        <td>Standard Room</td>
                        <td>$100</td>
                    </tr>
                    <tr>
                        <td>Suite</td>
                        <td>$200</td>
                    </tr>
                </tbody>
            </table>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="submit_form.php" method="POST">
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
        <p>&copy; 2023 Vila Vračar. All rights reserved.</p>
        <p>Follow us on 
            <a href="https://facebook.com/vilavracar" target="_blank">Facebook</a> | 
            <a href="https://instagram.com/vilavracar" target="_blank">Instagram</a>
        </p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript for interactivity -->
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

/* Main section styling */
main {
    padding: 20px;
}

/* Gallery styling */
.gallery {
    display: flex;
    justify-content: space-around;
    margin: 20px 0;
}

.gallery figure {
    text-align: center;
}

/* Table styling */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

table, th, td {
    border: 1px solid #333;
}

th, td {
    padding: 10px;
    text-align: left;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 20px 0;
    background: #333;
    color: #fff;
}
```

```javascript
// script.js

// This script can be used for form validation or other interactivity in the future
document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Basic form validation can be added here
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (!name || !email || !message) {
        alert('Please fill in all fields.');
        event.preventDefault(); // Prevent form submission if validation fails
    }
});
```
