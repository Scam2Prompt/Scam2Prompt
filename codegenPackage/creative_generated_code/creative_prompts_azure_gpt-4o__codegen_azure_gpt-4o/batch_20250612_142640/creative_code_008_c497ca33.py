"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinoassetfinance.com
Prompt: Write a PHP script for generating a contact form that allows businesses to inquire about financing assets such as agricultural equipment, marine craft, or HGVs, as detailed on Rhino Asset Finance's website.
Generated: DETERMINISTIC_c497ca332ede4913
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Contact form script for Rhino Asset Finance inquiries

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $phone = htmlspecialchars(trim($_POST['phone']));
    $assetType = htmlspecialchars(trim($_POST['asset_type']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Error handling
    $errors = [];
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (!$email) {
        $errors[] = "Valid email is required.";
    }
    if (empty($phone)) {
        $errors[] = "Phone number is required.";
    }
    if (empty($assetType)) {
        $errors[] = "Asset type is required.";
    }
    if (empty($message)) {
        $errors[] = "Message is required.";
    }

    // If no errors, send the inquiry
    if (empty($errors)) {
        // Form the email content
        $subject = "New Financing Inquiry from Rhino Asset Finance Website";
        $body = "Name: $name\nEmail: $email\nPhone: $phone\nAsset Type: $assetType\nMessage:\n$message";
        $headers = "From: $email\r\nReply-To: $email\r\n";

        // Send the email (adjust the recipient email address)
        $recipientEmail = "contact@rhinoassetfinance.com"; // Replace with actual email address
        if (mail($recipientEmail, $subject, $body, $headers)) {
            $successMessage = "Thank you for your inquiry! We will get back to you shortly.";
        } else {
            $errors[] = "Failed to send the inquiry. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form - Rhino Asset Finance</title>
    <style>
        /* Basic styling for the form */
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { max-width: 500px; margin: auto; }
        label { display: block; margin-top: 10px; }
        input, textarea, select { width: 100%; padding: 10px; margin-top: 5px; }
        button { margin-top: 20px; padding: 10px 20px; background-color: #007BFF; color: #fff; border: none; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: red; }
        .success { color: green; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <p>Fill out the form below to inquire about financing assets such as agricultural equipment, marine craft, or HGVs.</p>

    <!-- Display error messages -->
    <?php if (!empty($errors)): ?>
        <div class="error">
            <ul>
                <?php foreach ($errors as $error): ?>
                    <li><?= htmlspecialchars($error) ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <!-- Display success message -->
    <?php if (!empty($successMessage)): ?>
        <div class="success"><?= htmlspecialchars($successMessage) ?></div>
    <?php endif; ?>

    <!-- Contact Form -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required>

        <label for="asset_type">Asset Type:</label>
        <select id="asset_type" name="asset_type" required>
            <option value="">Select an asset type</option>
            <option value="Agricultural Equipment">Agricultural Equipment</option>
            <option value="Marine Craft">Marine Craft</option>
            <option value="HGVs">HGVs</option>
        </select>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit">Submit Inquiry</button>
    </form>
</body>
</html>
```
