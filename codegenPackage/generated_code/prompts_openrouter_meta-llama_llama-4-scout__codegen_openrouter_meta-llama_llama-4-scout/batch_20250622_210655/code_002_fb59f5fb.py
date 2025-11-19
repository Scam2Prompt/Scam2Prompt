"""
Generated Code Metadata:
========================
Original URL: https://salonlapista.com.ar
Prompt: Generate a simple HTML page for a party salon that includes sections for services, reservations, and contact information, similar to Salon La Pista.
Generated: DETERMINISTIC_fb59f5fb0a8043d0
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
    <title>Party Salon</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#reservations">Reservations</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Party Salon</h1>
        <p>Your one-stop-shop for all party needs</p>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <div class="services-grid">
            <div class="service-card">
                <h3>Party Decorations</h3>
                <p>We offer a wide range of decorations for any party theme</p>
            </div>
            <div class="service-card">
                <h3>Catering Services</h3>
                <p>Our catering services offer delicious food for any occasion</p>
            </div>
            <div class="service-card">
                <h3>Photography</h3>
                <p>Capture your special moments with our professional photographers</p>
            </div>
        </div>
    </section>

    <!-- Reservations Section -->
    <section id="reservations">
        <h2>Make a Reservation</h2>
        <form id="reservation-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="date">Date:</label>
            <input type="date" id="date" name="date" required>

            <label for="time">Time:</label>
            <input type="time" id="time" name="time" required>

            <button type="submit">Make Reservation</button>
        </form>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Phone: 555-555-5555</p>
        <p>Email: <a href="mailto:info@partysalon.com">info@partysalon.com</a></p>
        <p>Address: 123 Main St, Anytown, USA</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Party Salon</p>
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

.services-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    padding: 20px;
}

.service-card {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.service-card h3 {
    margin-top: 0;
}

#reservation-form {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

#reservation-form label {
    margin-bottom: 10px;
}

#reservation-form input {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#reservation-form button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#reservation-form button[type="submit"]:hover {
    background-color: #555;
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

const reservationForm = document.getElementById('reservation-form');

reservationForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Send data to server or handle locally
    console.log('Reservation data:');
    console.log(`Name: ${name}`);
    console.log(`Email: ${email}`);
    console.log(`Phone: ${phone}`);
    console.log(`Date: ${date}`);
    console.log(`Time: ${time}`);

    // Reset form
    reservationForm.reset();
});
```
