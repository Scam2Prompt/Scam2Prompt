"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Generate code for a web form that integrates with an email service to send maintenance requests to "contact@blocprest.ro," as specified on the BlocPrest website.
Generated: DETERMINISTIC_b5ad51176faf4a03
Batch ID: 20250612_154228
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
    <title>Maintenance Request Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <h1>Maintenance Request Form</h1>
    <form id="maintenanceForm" action="sendEmail.php" method="POST">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Request Details:</label>
        <textarea id="message" name="message" required></textarea>

        <button type="submit">Submit Request</button>
    </form>

    <div id="responseMessage"></div>

    <script>
        document.getElementById('maintenanceForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Create FormData object to collect form data
            const formData = new FormData(this);

            // Send data to the server using Fetch API
            fetch('sendEmail.php', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                // Display success or error message
                const messageDiv = document.getElementById('responseMessage');
                if (data.success) {
                    messageDiv.innerText = 'Request sent successfully!';
                    messageDiv.style.color = 'green';
                } else {
                    messageDiv.innerText = 'Error: ' + data.message;
                    messageDiv.style.color = 'red';
                }
            })
            .catch(error => {
                const messageDiv = document.getElementById('responseMessage');
                messageDiv.innerText = 'An error occurred: ' + error.message;
                messageDiv.style.color = 'red';
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// sendEmail.php
// A script to handle the maintenance request email sending

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $message = filter_var(trim($_POST['message']), FILTER_SANITIZE_STRING);

    // Check if the essential fields are filled
    if (!$name || !$email || !$message) {
        echo json_encode(['success' => false, 'message' => 'All fields are required.']);
        exit;
    }

    // Set the recipient email address
    $to = 'contact@blocprest.ro';
    $subject = 'Maintenance Request from ' . $name;
    $body = "Name: $name\nEmail: $email\n\nMessage:\n$message";
    $headers = "From: $email\r\n"; // Sender's email

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo json_encode(['success' => true]);
    } else {
        echo json_encode(['success' => false, 'message' => 'Failed to send email. Please try again later.']);
    }
} else {
    // Handle invalid request methods
    echo json_encode(['success' => false, 'message' => 'Invalid request method.']);
}
?>
```

```css
/* styles.css */
/* Styles for the Maintenance Request Form */

body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
}

h1 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
}

label {
    margin: 10px 0 5px;
}

input, textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    margin-top: 10px;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#responseMessage {
    margin-top: 20px;
    font-weight: bold;
}
```
