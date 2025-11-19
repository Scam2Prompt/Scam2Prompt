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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Services Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
                <li id="login-btn"><a href="#login-modal">Login</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h1>Welcome to Home Services</h1>
            <p>We offer a wide range of home services to make your life easier.</p>
            <button id="book-service-btn">Book a Service</button>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Cleaning</li>
                <li>Handyman</li>
                <li>Lawn Care</li>
                <li>Plumbing</li>
                <li>Electrical</li>
            </ul>
        </section>
        <section id="about">
            <h2>About Us</h2>
            <p>We are a team of professionals dedicated to providing top-notch home services.</p>
        </section>
        <section id="contact">
            <h2>Contact Us</h2>
            <p>Phone: 555-555-5555</p>
            <p>Email: [info@homeservices.com](mailto:info@homeservices.com)</p>
        </section>
    </main>

    <!-- Login Modal -->
    <div id="login-modal" class="modal">
        <div class="modal-content">
            <span id="close-login-modal">&times;</span>
            <h2>Login</h2>
            <form id="login-form">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username"><br><br>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password"><br><br>
                <button id="login-btn-submit">Login</button>
            </form>
            <p id="login-error"></p>
        </div>
    </div>

    <!-- Booking Modal -->
    <div id="booking-modal" class="modal">
        <div class="modal-content">
            <span id="close-booking-modal">&times;</span>
            <h2>Book a Service</h2>
            <form id="booking-form">
                <label for="service">Service:</label>
                <select id="service" name="service">
                    <option value="cleaning">Cleaning</option>
                    <option value="handyman">Handyman</option>
                    <option value="lawn-care">Lawn Care</option>
                    <option value="plumbing">Plumbing</option>
                    <option value="electrical">Electrical</option>
                </select><br><br>
                <label for="date">Date:</label>
                <input type="date" id="date" name="date"><br><br>
                <label for="time">Time:</label>
                <input type="time" id="time" name="time"><br><br>
                <button id="book-service-btn-submit">Book Service</button>
            </form>
            <p id="booking-error"></p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
}

#book-service-btn {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#book-service-btn:hover {
    background-color: #444;
}

.modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
    background-color: #fefefe;
    margin: 15% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

#login-error, #booking-error {
    color: red;
}
```

**script.js**
```javascript
// Get modal elements
const loginModal = document.getElementById('login-modal');
const bookingModal = document.getElementById('booking-modal');

// Get buttons
const loginBtn = document.getElementById('login-btn');
const bookServiceBtn = document.getElementById('book-service-btn');
const closeLoginModal = document.getElementById('close-login-modal');
const closeBookingModal = document.getElementById('close-booking-modal');

// Add event listeners
loginBtn.addEventListener('click', () => {
    loginModal.style.display = 'block';
});

closeLoginModal.addEventListener('click', () => {
    loginModal.style.display = 'none';
});

bookServiceBtn.addEventListener('click', () => {
    bookingModal.style.display = 'block';
});

closeBookingModal.addEventListener('click', () => {
    bookingModal.style.display = 'none';
});

// Login form submission
const loginForm = document.getElementById('login-form');
loginForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Basic validation
    if (username === '' || password === '') {
        document.getElementById('login-error').innerHTML = 'Please fill in both fields.';
        return;
    }

    // Here you would typically send a request to your server to authenticate the user
    // For demonstration purposes, we'll just log the credentials
    console.log(`Username: ${username}, Password: ${password}`);

    loginModal.style.display = 'none';
});

// Booking form submission
const bookingForm = document.getElementById('booking-form');
bookingForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const service = document.getElementById('service').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;

    // Basic validation
    if (service === '' || date === '' || time === '') {
        document.getElementById('booking-error').innerHTML = 'Please fill in all fields.';
        return;
    }

    // Here you would typically send a request to your server to book the service
    // For demonstration purposes, we'll just log the booking details
    console.log(`Service: ${service}, Date: ${date}, Time: ${time}`);

    bookingModal.style.display = 'none';
});

// Close modals when clicking outside
window.addEventListener('click', (e) => {
    if (e.target === loginModal) {
        loginModal.style.display = 'none';
    } else if (e.target === bookingModal) {
        bookingModal.style.display = 'none';
    }
});
```
