"""
Generated Code Metadata:
========================
Original URL: https://berachain.stride.co
Prompt: "Design a basic HTML/CSS template for a domain sale landing page, inspired by the layout and content of Stride.co for sale listings."
Generated: DETERMINISTIC_01d162a1946f2379
Batch ID: 20250622_212411
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
    <title>Domain Sale Landing Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>For Sale: Premium Domain Name</h1>
        <p>Your opportunity to own a valuable online asset.</p>
    </header>

    <main>
        <section class="domain-details">
            <h2>Domain Name: <span class="domain-name">example.com</span></h2>
            <p class="description">This domain is perfect for your business, blog, or personal brand. It is short, memorable, and easy to spell.</p>
            <p class="price">Price: <span class="price-value">$5,000</span></p>
        </section>

        <section class="contact-form">
            <h2>Contact Us</h2>
            <form id="inquiryForm" action="submit_form.php" method="POST">
                <label for="name">Your Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Your Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <button type="submit">Send Inquiry</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Domain Seller. All rights reserved.</p>
        <p>Privacy Policy | Terms of Service</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p {
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

/* Header styling */
header {
    background: #007bff;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Main content styling */
main {
    max-width: 800px;
    margin: 20px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Domain details section */
.domain-details {
    margin-bottom: 20px;
}

/* Contact form styling */
.contact-form {
    margin-top: 20px;
}

.contact-form label {
    display: block;
    margin-bottom: 5px;
}

.contact-form input, 
.contact-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.contact-form button {
    background: #007bff;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

.contact-form button:hover {
    background: #0056b3;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px;
    background: #007bff;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const formData = new FormData(this);

    // Send form data to the server
    fetch(this.action, {
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
        alert('Your inquiry has been sent successfully!');
        this.reset(); // Reset the form
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your inquiry. Please try again later.');
    });
});
```
