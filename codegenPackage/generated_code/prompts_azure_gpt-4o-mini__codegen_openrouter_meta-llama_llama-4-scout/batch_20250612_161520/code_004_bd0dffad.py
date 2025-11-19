"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Design a user interface for a roofing service website that includes sections for roof inspections, insurance claims, and customer testimonials, similar to JaraEs Construction LLC's layout.
Generated: DETERMINISTIC_bd0dffadae512967
Batch ID: 20250612_161520
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
    <title>Roofing Service Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#inspections">Roof Inspections</a></li>
                <li><a href="#claims">Insurance Claims</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Expert Roofing Services</h1>
        <p>Trust our professionals for all your roofing needs</p>
        <button>Contact Us</button>
    </section>

    <!-- Roof Inspections Section -->
    <section id="inspections" class="inspections">
        <h2>Roof Inspections</h2>
        <p>Our experts will inspect your roof and provide a detailed report</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone"><br><br>
            <button>Schedule Inspection</button>
        </form>
    </section>

    <!-- Insurance Claims Section -->
    <section id="claims" class="claims">
        <h2>Insurance Claims</h2>
        <p>We'll help you navigate the insurance claims process</p>
        <form>
            <label for="claim-type">Claim Type:</label>
            <select id="claim-type" name="claim-type">
                <option value="">Select Claim Type</option>
                <option value="storm-damage">Storm Damage</option>
                <option value="leak">Leak</option>
                <option value="other">Other</option>
            </select><br><br>
            <label for="claim-description">Claim Description:</label>
            <textarea id="claim-description" name="claim-description"></textarea><br><br>
            <button>Submit Claim</button>
        </form>
    </section>

    <!-- Testimonials Section -->
    <section id="testimonials" class="testimonials">
        <h2>What Our Customers Say</h2>
        <div class="testimonial">
            <p>Excellent service! Highly recommend.</p>
            <p>— John D.</p>
        </div>
        <div class="testimonial">
            <p>Professional and courteous. Fixed my roof quickly.</p>
            <p>— Jane S.</p>
        </div>
        <div class="testimonial">
            <p>Competitive pricing and great workmanship.</p>
            <p>— Bob T.</p>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Roofing Service Website</p>
        <ul>
            <li><a href="#">Terms of Service</a></li>
            <li><a href="#">Privacy Policy</a></li>
        </ul>
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

.inspections, .claims, .testimonials {
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

input, select, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

.testimonial {
    background-color: #f9f9f9;
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

footer ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

footer ul li {
    display: inline-block;
    margin-right: 20px;
}

footer a {
    color: #fff;
    text-decoration: none;
}
```

```javascript
// script.js

// Add event listener to schedule inspection button
document.querySelector('.inspections button').addEventListener('click', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    // Send data to server for processing
    console.log(`Name: ${name}, Email: ${email}, Phone: ${phone}`);
});

// Add event listener to submit claim button
document.querySelector('.claims button').addEventListener('click', (e) => {
    e.preventDefault();
    const claimType = document.getElementById('claim-type').value;
    const claimDescription = document.getElementById('claim-description').value;
    // Send data to server for processing
    console.log(`Claim Type: ${claimType}, Claim Description: ${claimDescription}`);
});
```
