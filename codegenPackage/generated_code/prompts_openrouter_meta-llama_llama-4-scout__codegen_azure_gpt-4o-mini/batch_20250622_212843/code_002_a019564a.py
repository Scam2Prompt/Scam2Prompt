"""
Generated Code Metadata:
========================
Original URL: https://lgin-uphoiolds.godaddysites.com
Prompt: Create a basic home services website template using HTML, CSS, and JavaScript that includes a login and booking feature.
Generated: DETERMINISTIC_a019564a70f2b042
Batch ID: 20250622_212843
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
    <title>Home Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Home Services</h1>
        <nav>
            <ul>
                <li><a href="#login">Login</a></li>
                <li><a href="#booking">Book a Service</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Login Section -->
        <section id="login">
            <h2>Login</h2>
            <form id="loginForm">
                <label for="username">Username:</label>
                <input type="text" id="username" required>
                <label for="password">Password:</label>
                <input type="password" id="password" required>
                <button type="submit">Login</button>
            </form>
            <p id="loginMessage"></p>
        </section>

        <!-- Booking Section -->
        <section id="booking">
            <h2>Book a Service</h2>
            <form id="bookingForm">
                <label for="service">Select Service:</label>
                <select id="service" required>
                    <option value="">--Select a Service--</option>
                    <option value="cleaning">Cleaning</option>
                    <option value="plumbing">Plumbing</option>
                    <option value="electrician">Electrician</option>
                </select>
                <label for="date">Select Date:</label>
                <input type="date" id="date" required>
                <button type="submit">Book Now</button>
            </form>
            <p id="bookingMessage"></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Home Services. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
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

/* Main section styles */
main {
    padding: 20px;
}

/* Form styles */
form {
    background: #ffffff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

form label {
    display: block;
    margin-bottom: 5px;
}

form input, form select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px;
    cursor: pointer;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
}
```

```javascript
// script.js

// Function to handle login form submission
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get username and password values
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simple validation (in a real application, this should be done on the server)
    if (username === 'user' && password === 'pass') {
        document.getElementById('loginMessage').textContent = 'Login successful!';
    } else {
        document.getElementById('loginMessage').textContent = 'Invalid username or password.';
    }
});

// Function to handle booking form submission
document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Get selected service and date values
    const service = document.getElementById('service').value;
    const date = document.getElementById('date').value;

    // Simple validation
    if (service && date) {
        document.getElementById('bookingMessage').textContent = `You have booked ${service} on ${date}.`;
    } else {
        document.getElementById('bookingMessage').textContent = 'Please select a service and date.';
    }
});
```
