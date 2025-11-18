"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamas.com.mx
Prompt: Write PHP code to implement a contact form for Meta+, allowing customers to submit inquiries about stainless steel, aluminum, and other metals, with email notifications sent to dcomercial@aymc.com.mx.
Generated: DETERMINISTIC_bf64e12d3d398a62
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact Form Processing Script for Meta+

// Configuration
$recipientEmail = "dcomercial@aymc.com.mx"; // Email to receive inquiries
$subjectPrefix = "Meta+ Contact Form Inquiry"; // Email subject prefix

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);
    $category = filter_input(INPUT_POST, 'category', FILTER_SANITIZE_STRING);

    // Error handling: Check required fields
    if (empty($name) || empty($email) || empty($message) || empty($category)) {
        echo json_encode(["success" => false, "error" => "All required fields must be filled."]);
        exit;
    }

    // Prepare email content
    $emailSubject = "$subjectPrefix - $category";
    $emailBody = "You have received a new inquiry:\n\n" .
                 "Name: $name\n" .
                 "Email: $email\n" .
                 "Phone: $phone\n" .
                 "Category: $category\n" .
                 "Message:\n$message\n";

    $headers = "From: $email\r\n" .
               "Reply-To: $email\r\n" .
               "Content-Type: text/plain; charset=UTF-8";

    // Send email
    if (mail($recipientEmail, $emailSubject, $emailBody, $headers)) {
        // Respond with JSON success
        echo json_encode(["success" => true, "message" => "Your inquiry has been sent successfully."]);
    } else {
        // Respond with JSON error
        echo json_encode(["success" => false, "error" => "Failed to send your inquiry. Please try again later."]);
    }
} else {
    // Respond with JSON error for invalid request method
    echo json_encode(["success" => false, "error" => "Invalid request method."]);
}
?>

<!-- HTML Contact Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Meta+</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone"><br><br>

        <label for="category">Category:</label>
        <select id="category" name="category" required>
            <option value="stainless_steel">Stainless Steel</option>
            <option value="aluminum">Aluminum</option>
            <option value="other_metals">Other Metals</option>
        </select><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="5" required></textarea><br><br>

        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```
