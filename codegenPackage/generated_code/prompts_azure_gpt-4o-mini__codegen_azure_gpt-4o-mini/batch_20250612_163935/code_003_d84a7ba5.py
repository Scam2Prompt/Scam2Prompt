"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: Develop a simple HTML layout for a real estate portfolio page, referencing the structure and design elements of 2ms.pt.
Generated: DETERMINISTIC_d84a7ba59323e41c
Batch ID: 20250612_163935
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.gstatic.com": {
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
    <title>Real Estate Portfolio</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <div class="container">
            <h1>Real Estate Portfolio</h1>
            <nav>
                <ul>
                    <li><a href="#about">About</a></li>
                    <li><a href="#properties">Properties</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>We are dedicated to providing the best real estate services in the industry. Our portfolio showcases a variety of properties that meet the needs of our clients.</p>
            </div>
        </section>

        <section id="properties">
            <div class="container">
                <h2>Our Properties</h2>
                <div class="property-list">
                    <article class="property-item">
                        <img src="property1.jpg" alt="Property 1">
                        <h3>Luxury Villa</h3>
                        <p>Located in the heart of the city, this luxury villa offers stunning views and modern amenities.</p>
                        <a href="#" class="btn">View Details</a>
                    </article>
                    <article class="property-item">
                        <img src="property2.jpg" alt="Property 2">
                        <h3>Cozy Apartment</h3>
                        <p>A cozy apartment perfect for city living, close to shops and restaurants.</p>
                        <a href="#" class="btn">View Details</a>
                    </article>
                    <article class="property-item">
                        <img src="property3.jpg" alt="Property 3">
                        <h3>Spacious Townhouse</h3>
                        <p>This spacious townhouse is ideal for families, featuring a large backyard and multiple bedrooms.</p>
                        <a href="#" class="btn">View Details</a>
                    </article>
                </div>
            </div>
        </section>

        <section id="contact">
            <div class="container">
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
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Real Estate Portfolio. All rights reserved.</p>
        </div>
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

/* Set font family for the entire document */
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    color: #333;
}

/* Container for consistent width */
.container {
    width: 90%;
    max-width: 1200px;
    margin: auto;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
}

header h1 {
    text-align: center;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px 0;
}

h2 {
    margin-bottom: 15px;
}

/* Property list styles */
.property-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.property-item {
    border: 1px solid #ccc;
    border-radius: 5px;
    overflow: hidden;
    width: calc(33.333% - 20px);
}

.property-item img {
    width: 100%;
    height: auto;
}

.property-item h3 {
    margin: 10px;
}

/* Button styles */
.btn {
    display: inline-block;
    background: #007BFF;
    color: #fff;
    padding: 10px 15px;
    text-decoration: none;
    border-radius: 5px;
    margin: 10px;
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

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```

```javascript
// script.js

// Simple form submission handler
document.getElementById('contact-form').addEventListener('submit', function (event) {
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
        this.reset(); // Reset the form
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your message. Please try again later.');
    });
});
```
