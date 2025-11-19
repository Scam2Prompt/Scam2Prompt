"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Generate a sample webpage content for a wine and restaurant business in Argentina, including sections for menus, wine lists, and reservation systems, inspired by Bodega Jean Bousquet's website.
Generated: DETERMINISTIC_ad213bdb9fcbb490
Batch ID: 20250622_212059
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
    <title>Bodega Jean Bousquet</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#menu">Menu</a></li>
                <li><a href="#wine-list">Wine List</a></li>
                <li><a href="#reservations">Reservations</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Bodega Jean Bousquet</h1>
        <p>Experience the best of Argentine wine and cuisine</p>
        <button>Learn More</button>
    </section>

    <!-- Menu Section -->
    <section id="menu">
        <h2>Menu</h2>
        <div class="menu-items">
            <div class="menu-item">
                <h3>Asado Argentino</h3>
                <p>Grilled meats and vegetables, served with chimichurri sauce</p>
                <span>$25</span>
            </div>
            <div class="menu-item">
                <h3>Empanadas</h3>
                <p>Beef and onion empanadas, served with salsa criolla</p>
                <span>$15</span>
            </div>
            <div class="menu-item">
                <h3>Choripan</h3>
                <p>Grilled sausage sandwich, served with chimichurri sauce</p>
                <span>$12</span>
            </div>
        </div>
    </section>

    <!-- Wine List Section -->
    <section id="wine-list">
        <h2>Wine List</h2>
        <div class="wine-items">
            <div class="wine-item">
                <h3>Jean Bousquet Malbec</h3>
                <p>Full-bodied Malbec from the Uco Valley</p>
                <span>$10/glass, $40/bottle</span>
            </div>
            <div class="wine-item">
                <h3>Jean Bousquet Cabernet Sauvignon</h3>
                <p>Rich and complex Cabernet Sauvignon from the Uco Valley</p>
                <span>$12/glass, $50/bottle</span>
            </div>
            <div class="wine-item">
                <h3>Jean Bousquet Chardonnay</h3>
                <p>Buttery and oaky Chardonnay from the Uco Valley</p>
                <span>$8/glass, $30/bottle</span>
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

            <label for="party-size">Party Size:</label>
            <input type="number" id="party-size" name="party-size" required>

            <button>Make Reservation</button>
        </form>
    </section>

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
    background-image: url('hero-image.jpg');
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.menu-items, .wine-items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.menu-item, .wine-item {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.menu-item h3, .wine-item h3 {
    margin-top: 0;
}

#reservation-form {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#reservation-form label {
    display: block;
    margin-bottom: 10px;
}

#reservation-form input {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

#reservation-form button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#reservation-form button:hover {
    background-color: #444;
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
    const partySize = document.getElementById('party-size').value;

    // Send reservation data to server or API
    console.log('Reservation data:');
    console.log(`Name: ${name}`);
    console.log(`Email: ${email}`);
    console.log(`Phone: ${phone}`);
    console.log(`Date: ${date}`);
    console.log(`Time: ${time}`);
    console.log(`Party Size: ${partySize}`);

    // Display success message
    alert('Reservation successful!');
});
```
