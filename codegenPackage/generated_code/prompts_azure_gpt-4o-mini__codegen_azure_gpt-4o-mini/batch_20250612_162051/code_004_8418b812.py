"""
Generated Code Metadata:
========================
Original URL: https://www.efeotokurtarma.com.tr
Prompt: Illustrate how to implement a contact form in HTML that connects users to a towing service like Efem Oto Çekici, ensuring it highlights 24/7 support.
Generated: DETERMINISTIC_8418b8128ec43128
Batch ID: 20250612_162051
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
    <title>Contact Us - Efem Oto Çekici</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Efem Oto Çekici</h1>
        <p>Your reliable towing service available 24/7</p>
    </header>

    <main>
        <section>
            <h2>Contact Us</h2>
            <form id="contactForm" action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Your Name">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Your Email">

                <label for="phone">Phone:</label>
                <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">

                <label for="message">Message:</label>
                <textarea id="message" name="message" required placeholder="Your Message"></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>Contact us anytime, we are here to help you 24/7!</p>
        <p>&copy; 2023 Efem Oto Çekici. All rights reserved.</p>
    </footer>

    <script>
        // Form submission handler
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

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
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                alert('There was an error sending your message. Please try again later.');
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for valid email
    if (!$email) {
        http_response_code(400);
        echo json_encode(['error' => 'Invalid email address.']);
        exit;
    }

    // Here you would typically send the email or save the data to a database
    // For demonstration, we will just simulate a successful response
    // mail($to, $subject, $message, $headers); // Uncomment to send email

    // Send a success response
    echo json_encode(['success' => 'Message sent successfully!']);
} else {
    // If the request method is not POST, return a 405 Method Not Allowed response
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed.']);
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

h1 {
    margin: 0;
}

main {
    padding: 20px;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background: #28a745;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #218838;
}

footer {
    text-align: center;
    padding: 20px;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
