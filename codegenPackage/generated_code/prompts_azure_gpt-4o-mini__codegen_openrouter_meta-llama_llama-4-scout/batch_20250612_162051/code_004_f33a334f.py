"""
Generated Code Metadata:
========================
Original URL: https://chile-horseriding.com
Prompt: Design a simple HTML form for users to submit inquiries about tailored horse riding tours at Chile Horse Riding, ensuring it captures essential details like the desired tour and number of participants.
Generated: DETERMINISTIC_f33a334ffee5b248
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

### HTML Form

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chile Horse Riding - Inquiry Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Inquire about a Tailored Horse Riding Tour</h1>
        <form id="inquiry-form" action="process-inquiry.php" method="post">
            <label for="tour-type">Desired Tour:</label>
            <select id="tour-type" name="tour-type" required>
                <option value="">Select a tour</option>
                <option value="andes-mountains">Andes Mountains</option>
                <option value="patagonia">Patagonia</option>
                <option value="colchagua-valley">Colchagua Valley</option>
                <option value="custom">Custom Tour</option>
            </select>

            <label for="num-participants">Number of Participants:</label>
            <input type="number" id="num-participants" name="num-participants" min="1" required>

            <label for="inquiry-details">Additional Details:</label>
            <textarea id="inquiry-details" name="inquiry-details"></textarea>

            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Your Phone:</label>
            <input type="tel" id="phone" name="phone">

            <button type="submit">Submit Inquiry</button>
        </form>
    </div>
</body>
</html>
```

### CSS Styling (in styles.css)

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

.container {
    max-width: 500px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
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

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}
```

### PHP Form Processing (in process-inquiry.php)

```php
<?php
// process-inquiry.php

// Configuration
$toEmail = 'info@chilehorsesriding.com';
$subject = 'Inquiry about Tailored Horse Riding Tour';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate form data
    $tourType = trim($_POST['tour-type']);
    $numParticipants = (int) $_POST['num-participants'];
    $inquiryDetails = trim($_POST['inquiry-details']);
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $phone = trim($_POST['phone']);

    $errors = [];

    if (empty($tourType)) {
        $errors[] = 'Please select a tour type.';
    }

    if ($numParticipants < 1) {
        $errors[] = 'Number of participants must be at least 1.';
    }

    if (empty($name)) {
        $errors[] = 'Please enter your name.';
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'Please enter a valid email address.';
    }

    // Send email if no errors
    if (empty($errors)) {
        $message = "
        <p>Tour Type: $tourType</p>
        <p>Number of Participants: $numParticipants</p>
        <p>Inquiry Details: $inquiryDetails</p>
        <p>Name: $name</p>
        <p>Email: $email</p>
        <p>Phone: $phone</p>
        ";

        $headers = 'From: ' . $email . "\r\n" .
                   'Reply-To: ' . $email . "\r\n" .
                   'X-Mailer: PHP/' . phpversion();

        if (mail($toEmail, $subject, $message, $headers)) {
            echo '<p>Inquiry sent successfully!</p>';
        } else {
            $errors[] = 'Failed to send inquiry. Please try again.';
        }
    }

    // Display errors if any
    if (!empty($errors)) {
        echo '<ul>';
        foreach ($errors as $error) {
            echo "<li>$error</li>";
        }
        echo '</ul>';
    }
} else {
    http_response_code(405);
    echo 'Method Not Allowed';
}
?>
```
