"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cerlalinda.edu.co
Prompt: How can I implement a contact form for a school website similar to Centro Educativo Rural La Linda?
Generated: DETERMINISTIC_5899c2fa5012f260
Batch ID: 20250612_161246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Centro Educativo Rural La Linda</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Contact Us</h1>
    </header>
    <main>
        <form id="contactForm" action="sendEmail.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required></textarea>
            
            <button type="submit">Send Message</button>
        </form>
        <div id="responseMessage"></div> <!-- Div for displaying response messages -->
    </main>
    <script src="script.js"></script> <!-- Link to external JavaScript for form handling -->
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    text-align: center;
}

form {
    background: white;
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
    background-color: #5cb85c;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

#responseMessage {
    margin-top: 20px;
    font-weight: bold;
}
```

```php
<?php
// sendEmail.php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $message = trim($_POST['message']);

    // Basic validation
    if (empty($name) || empty($email) || empty($message)) {
        http_response_code(400);
        echo "All fields are required.";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Invalid email format.";
        exit;
    }

    // Set the recipient email address
    $to = "info@centroeducativorurallalinda.com"; // Change to your email
    $subject = "Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200);
        echo "Message sent successfully.";
    } else {
        http_response_code(500);
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // If the request method is not POST, return a 405 Method Not Allowed response
    http_response_code(405);
    echo "Method Not Allowed.";
}
?>
```

```javascript
// script.js
document.getElementById("contactForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the default form submission
    
    const formData = new FormData(this); // Create FormData object

    // Send form data using Fetch API
    fetch("sendEmail.php", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Network response was not ok " + response.statusText);
        }
        return response.text();
    })
    .then(data => {
        document.getElementById("responseMessage").innerText = data; // Display response message
    })
    .catch(error => {
        document.getElementById("responseMessage").innerText = "There was a problem: " + error.message; // Handle errors
    });
});
```
