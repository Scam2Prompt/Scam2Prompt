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
// contact_form.php

// Start the session to handle errors and feedback
session_start();

// Define constants for the email
define('TO_EMAIL', 'info@rhinoassetfinance.com'); // replace with the actual recipient email
define('SUBJECT', 'Financing Inquiry');

// Function to send email
function sendInquiryEmail($data) {
    $headers = "From: " . $data['email'] . "\r\n" .
               "Reply-To: " . $data['email'] . "\r\n" .
               "Content-Type: text/plain; charset=utf-8\r\n";

    $message = "Name: " . $data['name'] . "\n" .
               "Email: " . $data['email'] . "\n" .
               "Phone: " . $data['phone'] . "\n" .
               "Asset Type: " . $data['asset_type'] . "\n" .
               "Message: " . $data['message'] . "\n";

    return mail(TO_EMAIL, SUBJECT, $message, $headers);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $errors = [];

    // Validate input data
    $name = trim($_POST['name']);
    $email = trim($_POST['email']);
    $phone = trim($_POST['phone']);
    $asset_type = trim($_POST['asset_type']);
    $message = trim($_POST['message']);

    if (empty($name)) {
        $errors['name'] = "Name is required.";
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "A valid email is required.";
    }
    if (empty($phone)) {
        $errors['phone'] = "Phone number is required.";
    }
    if (empty($asset_type)) {
        $errors['asset_type'] = "Asset type is required.";
    }
    if (empty($message)) {
        $errors['message'] = "Message is required.";
    }

    // If no errors, send the email
    if (empty($errors)) {
        if (sendInquiryEmail($_POST)) {
            $_SESSION['success'] = "Your inquiry has been sent successfully.";
            header("Location: contact_form.php");
            exit();
        } else {
            $errors['mail'] = "There was an error sending your email. Please try again later.";
        }
    }

    // Store errors in session
    $_SESSION['errors'] = $errors;
    header("Location: contact_form.php");
    exit();
}

// Clear session errors after displaying
if (isset($_SESSION['errors'])) {
    $errors = $_SESSION['errors'];
    unset($_SESSION['errors']);
}
if (isset($_SESSION['success'])) {
    $success = $_SESSION['success'];
    unset($_SESSION['success']);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Rhino Asset Finance</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Contact Us</h1>
    <form action="contact_form.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required value="<?php echo htmlspecialchars($name ?? '', ENT_QUOTES); ?>">
        <?php if (isset($errors['name'])) echo '<p class="error">'.$errors['name'].'</p>'; ?>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required value="<?php echo htmlspecialchars($email ?? '', ENT_QUOTES); ?>">
        <?php if (isset($errors['email'])) echo '<p class="error">'.$errors['email'].'</p>'; ?>

        <label for="phone">Phone:</label>
        <input type="tel" id="phone" name="phone" required value="<?php echo htmlspecialchars($phone ?? '', ENT_QUOTES); ?>">
        <?php if (isset($errors['phone'])) echo '<p class="error">'.$errors['phone'].'</p>'; ?>

        <label for="asset_type">Asset Type:</label>
        <select id="asset_type" name="asset_type" required>
            <option value="">Select an asset type</option>
            <option value="Agricultural Equipment" <?php if (isset($asset_type) && $asset_type === 'Agricultural Equipment') echo 'selected'; ?>>Agricultural Equipment</option>
            <option value="Marine Craft" <?php if (isset($asset_type) && $asset_type === 'Marine Craft') echo 'selected'; ?>>Marine Craft</option>
            <option value="HGVs" <?php if (isset($asset_type) && $asset_type === 'HGVs') echo 'selected'; ?>>HGVs</option>
        </select>
        <?php if (isset($errors['asset_type'])) echo '<p class="error">'.$errors['asset_type'].'</p>'; ?>

        <label for="message">Message:</label>
        <textarea id="message" name="message" required><?php echo htmlspecialchars($message ?? '', ENT_QUOTES); ?></textarea>
        <?php if (isset($errors['message'])) echo '<p class="error">'.$errors['message'].'</p>'; ?>

        <button type="submit">Submit Inquiry</button>
    </form>

    <?php if (isset($success)) echo '<p class="success">'.$success.'</p>'; ?>
</body>
</html>
```
