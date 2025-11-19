"""
Generated Code Metadata:
========================
Original URL: https://jlelectricista.com
Prompt: Generate a code snippet that integrates a contact form for an electrician service, similar to the one found on JLelectricista, including fields for name, phone number, and service request.
Generated: DETERMINISTIC_ec103638c19597cb
Batch ID: 20250612_161700
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
    <title>Contact Form - Electrician Service</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us for Electrician Services</h1>
        <form id="contactForm" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">

            <label for="serviceRequest">Service Request:</label>
            <textarea id="serviceRequest" name="serviceRequest" required placeholder="Describe your service request"></textarea>

            <button type="submit">Submit</button>
        </form>
        <div id="formResponse"></div> <!-- Placeholder for form submission response -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server using Fetch API
            fetch('submit_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('formResponse').innerText = data; // Display response
                this.reset(); // Reset form fields
            })
            .catch(error => {
                document.getElementById('formResponse').innerText = 'Error: ' + error.message; // Display error
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
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $serviceRequest = filter_input(INPUT_POST, 'serviceRequest', FILTER_SANITIZE_STRING);

    // Check for empty fields
    if (empty($name) || empty($phone) || empty($serviceRequest)) {
        http_response_code(400); // Bad Request
        echo "All fields are required.";
        exit;
    }

    // Here you would typically send the data to a database or an email
    // For demonstration, we will just return a success message
    echo "Thank you, $name! Your service request has been received.";
} else {
    // If the request method is not POST, return a 405 Method Not Allowed response
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"],
input[type="tel"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
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

#formResponse {
    margin-top: 20px;
    text-align: center;
    color: green;
}
```
