"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rope-bunny.com
Prompt: Generate a code snippet for an e-commerce website that showcases handmade leather and faux leather products, similar to the offerings on Rope-Bunny.de.
Generated: DETERMINISTIC_a93ac9c41bd7a3a7
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handmade Leather and Faux Leather Products</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Our Handmade Leather & Faux Leather Shop</h1>
        <nav>
            <ul>
                <li><a href="#products">Products</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="products">
            <h2>Our Products</h2>
            <div class="product-grid">
                <!-- Example product item -->
                <article class="product-item">
                    <img src="images/leather-bag.jpg" alt="Handmade Leather Bag" class="product-image">
                    <h3>Handmade Leather Bag</h3>
                    <p class="product-description">A beautiful handmade leather bag, perfect for everyday use.</p>
                    <span class="product-price">$120.00</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>

                <article class="product-item">
                    <img src="images/faux-leather-jacket.jpg" alt="Faux Leather Jacket" class="product-image">
                    <h3>Faux Leather Jacket</h3>
                    <p class="product-description">Stylish faux leather jacket, ideal for a night out.</p>
                    <span class="product-price">$89.99</span>
                    <button class="add-to-cart">Add to Cart</button>
                </article>
                <!-- Additional products can be added here in similar structure -->
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We specialize in handcrafted leather and faux leather products, committed to quality and sustainability.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" method="POST" action="submit_contact.php">
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
        <p>&copy; 2023 Handmade Leather & Faux Leather Shop. All rights reserved.</p>
    </footer>

    <script src="scripts.js"></script> <!-- Link to external JavaScript for functionality -->
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

.product-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px;
}

.product-item {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 15px;
    padding: 10px;
    text-align: center;
    width: 300px;
}

.product-image {
    max-width: 100%;
    height: auto;
}

.product-description {
    font-size: 0.9em;
}

.product-price {
    font-weight: bold;
    color: #2c3e50;
}

.add-to-cart {
    background-color: #27ae60;
    border: none;
    color: white;
    padding: 10px;
    cursor: pointer;
}

/* Contact form styles */
form {
    display: flex;
    flex-direction: column;
    max-width: 600px;
    margin: 20px auto;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

footer {
    text-align: center;
    padding: 1rem 0;
    background: #333;
    color: #fff;
}
```

```javascript
// scripts.js

// Function to handle "Add to Cart" button clicks
document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', event => {
        // Get the product details from the parent element
        const productItem = event.target.closest('.product-item');
        const productName = productItem.querySelector('h3').textContent;
        const productPrice = productItem.querySelector('.product-price').textContent;

        // Simulate adding to cart (this is where you would integrate with a backend)
        alert(`Added to cart: ${productName} - ${productPrice}`);
    });
});

// Contact form submission handling (optional)
// Consider using fetch API to handle form submission without page reload
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    const formData = new FormData(this); // Collect form data

    // Submit the form data using fetch API
    fetch('submit_contact.php', {
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
    })
    .catch(error => {
        alert('An error occurred: ' + error.message);
    });
});
```

```php
<?php
// submit_contact.php

// Check if the request is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_var(trim($_POST["name"]), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = filter_var(trim($_POST["message"]), FILTER_SANITIZE_STRING);

    // Basic validation
    if (empty($name) || empty($email) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request
        echo json_encode(["status" => "error", "message" => "Invalid input."]);
        exit;
    }

    // Prepare email (this is just an example, adjust according to your needs)
    $to = "contact@example.com";
    $subject = "New Contact Message from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    
    // Send email (consider using PHPMailer or similar for production)
    if (mail($to, $subject, $body)) {
        echo json_encode(["status" => "success", "message" => "Message sent successfully!"]);
    } else {
        http_response_code(500); // Internal Server Error
        echo json_encode(["status" => "error", "message" => "Failed to send message."]);
    }
} else {
    // Handle non-POST requests
    http_response_code(405); // Method Not Allowed
    echo json_encode(["status" => "error", "message" => "Method not allowed."]);
}
?>
```

This code consists of an HTML structure, CSS for styling, JavaScript for interactivity, and a simple PHP script for handling contact form submissions. Each part is modular and follows best practices for production-ready code.
