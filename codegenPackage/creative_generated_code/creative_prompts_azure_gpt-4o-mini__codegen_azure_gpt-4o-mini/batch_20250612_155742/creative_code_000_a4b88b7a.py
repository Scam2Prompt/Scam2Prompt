"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Generate code for a web form that allows users to request a free estimate for residential spray foam insulation services.
Generated: DETERMINISTIC_a4b88b7a7867f06f
Batch ID: 20250612_155742
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
    <title>Free Estimate Request - Spray Foam Insulation</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Free Estimate</h1>
        <form id="estimateForm" action="submit_estimate.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required placeholder="Enter your address">

            <label for="message">Additional Information:</label>
            <textarea id="message" name="message" rows="4" placeholder="Any specific requirements or questions?"></textarea>

            <button type="submit">Request Estimate</button>
        </form>
    </div>

    <script>
        // Client-side form validation
        document.getElementById('estimateForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const address = document.getElementById('address').value;
            
            // Simple validation for empty fields
            if (!name || !email || !phone || !address) {
                event.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_estimate.php

// Start session for error handling and message display
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize variables
    $name = $email = $phone = $address = $message = "";
    
    // Sanitize and validate input
    try {
        if (empty($_POST["name"]) || empty($_POST["email"]) || empty($_POST["phone"]) || empty($_POST["address"])) {
            throw new Exception("All fields are required.");
        }
        
        $name = sanitizeInput($_POST["name"]);
        $email = sanitizeInput($_POST["email"]);
        $phone = sanitizeInput($_POST["phone"]);
        $address = sanitizeInput($_POST["address"]);
        $message = sanitizeInput($_POST["message"]); // Optional field

        // Validate email
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format.");
        }

        // Here you would typically send the data to the database or an email service
        // For demonstration, we will just simulate a success message
        $_SESSION['success_message'] = "Your request for a free estimate has been submitted successfully!";
        header("Location: thank_you.php");
        exit();
        
    } catch (Exception $e) {
        // Store error message in session and redirect to form
        $_SESSION['error_message'] = $e->getMessage();
        header("Location: form_page.php"); // Redirect back to the form
        exit();
    }
} else {
    // Redirect if accessed directly without form submission
    header("Location: form_page.php");
    exit();
}
?>
```

```html
<!-- thank_you.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Thank You</title>
</head>
<body>
    <div class="container">
        <h1>Thank You!</h1>
        <?php
        session_start();
        // Display success message if set
        if (isset($_SESSION['success_message'])) {
            echo "<p>" . $_SESSION['success_message'] . "</p>";
            unset($_SESSION['success_message']); // Clear message after displaying
        }
        ?>
        <a href="form_page.php">Request Another Estimate</a>
    </div>
</body>
</html>
```

```html
<!-- form_page.php (This file contains the form) -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Free Estimate Request - Spray Foam Insulation</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Request a Free Estimate</h1>
        <?php
        session_start();
        // Display error message if set
        if (isset($_SESSION['error_message'])) {
            echo "<p style='color:red;'>" . $_SESSION['error_message'] . "</p>";
            unset($_SESSION['error_message']); // Clear message after displaying
        }
        ?>
        <form id="estimateForm" action="submit_estimate.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">

            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="Enter your phone number">

            <label for="address">Address:</label>
            <input type="text" id="address" name="address" required placeholder="Enter your address">

            <label for="message">Additional Information:</label>
            <textarea id="message" name="message" rows="4" placeholder="Any specific requirements or questions?"></textarea>

            <button type="submit">Request Estimate</button>
        </form>
    </div>

    <script>
        // Client-side form validation
        document.getElementById('estimateForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const phone = document.getElementById('phone').value;
            const address = document.getElementById('address').value;
            
            // Simple validation for empty fields
            if (!name || !email || !phone || !address) {
                event.preventDefault();
                alert('Please fill out all required fields.');
            }
        });
    </script>
</body>
</html>
```

Note: Remember to create a `styles.css` file for styling, and adjust paths as necessary based on your project structure. Additionally, ensure your server is configured to handle PHP files.
