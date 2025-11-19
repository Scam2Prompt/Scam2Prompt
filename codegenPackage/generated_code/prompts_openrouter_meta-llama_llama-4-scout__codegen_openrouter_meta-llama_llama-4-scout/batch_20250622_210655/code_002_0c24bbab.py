"""
Generated Code Metadata:
========================
Original URL: https://www.vracarbvk.rs
Prompt: Generate a sample HTML page for a hotel website, incorporating essential features like a room gallery, pricing, and contact information, inspired by Vila Vračar's website structure.
Generated: DETERMINISTIC_0c24bbab2a4f43f4
Batch ID: 20250622_210655
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
    <title>Hotel Vila Vračar</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#gallery">Room Gallery</a></li>
                <li><a href="#pricing">Pricing</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Hotel Vila Vračar</h1>
        <p>Experience the best of hospitality in the heart of the city.</p>
    </section>

    <!-- Room Gallery Section -->
    <section id="gallery" class="gallery">
        <h2>Room Gallery</h2>
        <div class="gallery-container">
            <div class="gallery-item">
                <img src="images/room1.jpg" alt="Room 1">
                <p>Deluxe Room</p>
            </div>
            <div class="gallery-item">
                <img src="images/room2.jpg" alt="Room 2">
                <p>Suite</p>
            </div>
            <div class="gallery-item">
                <img src="images/room3.jpg" alt="Room 3">
                <p>Standard Room</p>
            </div>
        </div>
    </section>

    <!-- Pricing Section -->
    <section id="pricing" class="pricing">
        <h2>Pricing</h2>
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
                    <td>Suite</td>
                    <td>$250</td>
                </tr>
                <tr>
                    <td>Standard Room</td>
                    <td>$100</td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Get in Touch</h2>
        <p>Contact us for reservations and inquiries.</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea><br><br>
            <input type="submit" value="Send">
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Hotel Vila Vračar. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.gallery {
    padding: 2em;
}

.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery-item {
    margin: 10px;
    width: calc(33.33% - 20px);
}

.gallery-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

.pricing {
    padding: 2em;
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

.contact {
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
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

// Add event listener to form submission
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic form validation
    if (name && email && message) {
        console.log('Form submitted:', { name, email, message });
        // Add logic for sending data to server or email service
    } else {
        alert('Please fill out all fields.');
    }
});
```
