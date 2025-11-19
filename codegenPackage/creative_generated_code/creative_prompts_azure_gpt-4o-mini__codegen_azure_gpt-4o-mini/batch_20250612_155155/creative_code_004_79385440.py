"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbank.app
Prompt: How can I implement a contact form in HTML that collects user information for domain pricing inquiries, similar to the one on dbank.app?
Generated: DETERMINISTIC_79385440d749cd3a
Batch ID: 20250612_155155
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
    <title>Contact Form for Domain Pricing Inquiries</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript for form validation -->
</head>
<body>
    <header>
        <h1>Domain Pricing Inquiry</h1>
    </header>
    <main>
        <form id="contactForm" action="submit_form.php" method="POST" novalidate>
            <label for="name">Name <span class="required">*</span></label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="email">Email <span class="required">*</span></label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="domain">Domain Name <span class="required">*</span></label>
            <input type="text" id="domain" name="domain" required placeholder="Desired Domain Name">

            <label for="message">Message</label>
            <textarea id="message" name="message" rows="4" placeholder="Your Message (optional)"></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
    </main>
    <footer>
        <p>&copy; 2023 Your Company. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f9f9f9;
}

header, footer {
    background-color: #007bff;
    color: white;
    text-align: center;
    padding: 1em 0;
}

main {
    padding: 20px;
    max-width: 600px;
    margin: auto;
    background: white;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
}

input, textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input:focus, textarea:focus {
    border-color: #007bff;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.required {
    color: red;
}
```

```javascript
// script.js
document.getElementById('contactForm').addEventListener('submit', function(event) {
    // Prevent form submission if there are validation errors
    if (!this.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
    }
    
    // Add custom validation or processing here if needed

    // Mark the form as validated
    this.classList.add('was-validated');
});
```

```php
<?php
// submit_form.php

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize form data
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $domain = htmlspecialchars(trim($_POST['domain']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Validate that required fields are not empty
    if (empty($name) || empty($email) || empty($domain)) {
        die("Error: All required fields must be filled out.");
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    // Process the data (e.g., save to database, send email)
    // ...

    // Respond with a success message
    echo "Thank you for your inquiry, $name. We will get back to you shortly!";
} else {
    // Invalid request method
    http_response_code(405);
    echo "Error: Invalid request method.";
}
?>
```

Make sure to configure your server to handle PHP files and adjust the form action URL as needed.
