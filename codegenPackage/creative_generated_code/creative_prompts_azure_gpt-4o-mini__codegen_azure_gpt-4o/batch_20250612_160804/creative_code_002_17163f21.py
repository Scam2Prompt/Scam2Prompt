"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://surffojotas.com
Prompt: Create a PHP script to handle customer inquiries about personalized flip-flops, similar to the services offered by Surff Ojotas.
Generated: DETERMINISTIC_17163f2144e0c379
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// customer_inquiry.php
// A script to handle customer inquiries about personalized flip-flops.

// Enable strict error reporting for development environment
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to safely sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Process the form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Initialize response array
    $response = ['success' => false, 'message' => ''];

    try {
        // Check if required fields are provided
        if (!isset($_POST['name'], $_POST['email'], $_POST['message'])) {
            throw new Exception("All fields are mandatory.");
        }

        // Sanitize user inputs
        $name = sanitizeInput($_POST['name']);
        $email = sanitizeInput($_POST['email']);
        $message = sanitizeInput($_POST['message']);

        // Validate the email format
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            throw new Exception("Invalid email format.");
        }

        // Simulate storing the inquiry (e.g., to a database or sending email)
        // In a real application, you would replace this with actual database insert or email sending logic.
        // Example: mail($email, "Inquiry Received", "Thank you for your message: $message");
        $inquirySaved = true; // Simulate successful save

        if ($inquirySaved) {
            $response['success'] = true;
            $response['message'] = "Your inquiry has been successfully received. We'll get back to you shortly!";
        } else {
            throw new Exception("Failed to save your inquiry. Please try again later.");
        }
    } catch (Exception $e) {
        // Handle errors and provide feedback to the user
        $response['message'] = $e->getMessage();
    }

    // Respond with JSON (for AJAX requests or API use cases)
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personalized Flip-Flop Inquiry</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        input, textarea {
            display: block;
            width: 100%;
            margin-bottom: 10px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            border: none;
            background-color: #28a745;
            color: white;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <h1>Contact Us for Personalized Flip-Flops</h1>
    <form method="POST" action="customer_inquiry.php">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Your Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit">Send Inquiry</button>
    </form>
</body>
</html>
```
