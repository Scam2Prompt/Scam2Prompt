"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ammaparivaar.org
Prompt: Can you provide a code example for a simple web form that allows users to donate to an orphanage, similar to the donation process described on ammaparivaar.org?
Generated: DETERMINISTIC_453cd15bdf1c5054
Batch ID: 20250612_161700
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
    <title>Orphanage Donation Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Donate to Orphanage</h1>
        <form id="donationForm" method="POST" action="process_donation.php">
            <!-- User's name input -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <!-- User's email input -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <!-- Donation amount input -->
            <label for="amount">Donation Amount (USD):</label>
            <input type="number" id="amount" name="amount" min="1" required>

            <!-- Donation message input -->
            <label for="message">Optional Message:</label>
            <textarea id="message" name="message" rows="4"></textarea>

            <!-- Submit button -->
            <button type="submit">Donate</button>
        </form>
        
        <div id="responseMessage"></div> <!-- Container for response messages -->
    </div>

    <script>
        // Attach a submit event listener to the donation form
        document.getElementById('donationForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server using Fetch API
            fetch('process_donation.php', {
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
                // Display success message to the user
                document.getElementById('responseMessage').textContent = data.message;
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                // Handle errors and display an error message
                document.getElementById('responseMessage').textContent = 'Error: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// process_donation.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize user inputs
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $amount = htmlspecialchars(trim($_POST['amount']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Basic validation
    if (empty($name) || empty($email) || empty($amount)) {
        echo json_encode(["message" => "All fields are required."]);
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo json_encode(["message" => "Invalid email format."]);
        exit;
    }

    if (!is_numeric($amount) || $amount <= 0) {
        echo json_encode(["message" => "Donation amount must be a positive number."]);
        exit;
    }

    // Here you would typically save the donation details to a database or process the payment
    // For simplicity, we're just simulating a successful donation response

    echo json_encode(["message" => "Thank you for your donation, $name!"]);
} else {
    echo json_encode(["message" => "Invalid request method."]);
}
?>
``` 

```css
/* styles.css */

/* Basic styling for the container */
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Style for headings */
h1 {
    text-align: center;
}

/* Style for form elements */
label {
    display: block;
    margin-top: 10px;
}

/* Style for input fields */
input[type="text"],
input[type="email"],
input[type="number"],
textarea {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border-radius: 4px;
    border: 1px solid #ccc;
}

/* Style for the submit button */
button {
    margin-top: 15px;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

/* Style for response messages */
#responseMessage {
    margin-top: 20px;
    font-weight: bold;
}
``` 

This code consists of an HTML form for donations, a PHP script to process the donations, and accompanying CSS for styling. The JavaScript handles form submission asynchronously, and error handling is included for both the front-end and back-end.
