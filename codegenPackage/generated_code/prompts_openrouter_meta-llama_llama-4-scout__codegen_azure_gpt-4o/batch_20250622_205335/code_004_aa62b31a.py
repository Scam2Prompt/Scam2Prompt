"""
Generated Code Metadata:
========================
Original URL: https://cham-transfers.com
Prompt: Create a simple web form using HTML and PHP to collect user information for booking a transfer from Geneva to Les Gets, similar to the one on cham-transfers.com.
Generated: DETERMINISTIC_aa62b31a536d012c
Batch ID: 20250622_205335
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
    <title>Transfer Booking Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: auto;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 8px;
            margin-bottom: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #007BFF;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Transfer Booking Form</h1>
    <form action="process_booking.php" method="POST">
        <!-- Full Name -->
        <label for="full_name">Full Name:</label>
        <input type="text" id="full_name" name="full_name" required>
        
        <!-- Email -->
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- Phone Number -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>
        
        <!-- Pickup Date -->
        <label for="pickup_date">Pickup Date:</label>
        <input type="date" id="pickup_date" name="pickup_date" required>
        
        <!-- Pickup Time -->
        <label for="pickup_time">Pickup Time:</label>
        <input type="time" id="pickup_time" name="pickup_time" required>
        
        <!-- Number of Passengers -->
        <label for="passengers">Number of Passengers:</label>
        <input type="number" id="passengers" name="passengers" min="1" max="50" required>
        
        <!-- Special Requests -->
        <label for="special_requests">Special Requests:</label>
        <textarea id="special_requests" name="special_requests" rows="4"></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Book Transfer</button>
    </form>
</body>
</html>
```

```php
<?php
// process_booking.php

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $full_name = htmlspecialchars(trim($_POST['full_name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(trim($_POST['phone']));
    $pickup_date = htmlspecialchars(trim($_POST['pickup_date']));
    $pickup_time = htmlspecialchars(trim($_POST['pickup_time']));
    $passengers = filter_var(trim($_POST['passengers']), FILTER_VALIDATE_INT);
    $special_requests = htmlspecialchars(trim($_POST['special_requests']));

    // Initialize an array to store errors
    $errors = [];

    // Validate required fields
    if (!$full_name) {
        $errors[] = "Full Name is required.";
    }
    if (!$email) {
        $errors[] = "A valid Email Address is required.";
    }
    if (!$phone) {
        $errors[] = "Phone Number is required.";
    }
    if (!$pickup_date) {
        $errors[] = "Pickup Date is required.";
    }
    if (!$pickup_time) {
        $errors[] = "Pickup Time is required.";
    }
    if (!$passengers || $passengers < 1) {
        $errors[] = "Number of Passengers must be at least 1.";
    }

    // If there are errors, display them
    if (!empty($errors)) {
        echo "<h1>Booking Errors</h1>";
        echo "<ul class='error'>";
        foreach ($errors as $error) {
            echo "<li>" . htmlspecialchars($error) . "</li>";
        }
        echo "</ul>";
        echo "<a href='javascript:history.back()'>Go Back</a>";
        exit;
    }

    // Process the booking (e.g., save to database, send email, etc.)
    // For demonstration purposes, we'll just display the submitted data
    echo "<h1>Booking Confirmation</h1>";
    echo "<p>Thank you for your booking, $full_name!</p>";
    echo "<p>Email: $email</p>";
    echo "<p>Phone: $phone</p>";
    echo "<p>Pickup Date: $pickup_date</p>";
    echo "<p>Pickup Time: $pickup_time</p>";
    echo "<p>Number of Passengers: $passengers</p>";
    echo "<p>Special Requests: $special_requests</p>";
    echo "<p>Your transfer from Geneva to Les Gets has been successfully booked.</p>";
} else {
    // If the form was not submitted, redirect to the form page
    header("Location: index.html");
    exit;
}
?>
```
