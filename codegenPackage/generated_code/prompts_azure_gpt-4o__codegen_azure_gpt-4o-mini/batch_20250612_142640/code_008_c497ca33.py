"""
Generated Code Metadata:
========================
Original URL: https://rhinoassetfinance.com
Prompt: Write a PHP script for generating a contact form that allows businesses to inquire about financing assets such as agricultural equipment, marine craft, or HGVs, as detailed on Rhino Asset Finance's website.
Generated: DETERMINISTIC_c497ca332ede4913
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// contact_form.php

// Start the session to handle form submissions
session_start();

// Define variables and initialize with empty values
$name = $email = $phone = $asset_type = $message = "";
$name_err = $email_err = $phone_err = $asset_type_err = $message_err = "";

// Process form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $name_err = "Please enter your name.";
    } else {
        $name = trim($_POST["name"]);
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $email_err = "Please enter your email.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $email_err = "Invalid email format.";
    } else {
        $email = trim($_POST["email"]);
    }

    // Validate phone
    if (empty(trim($_POST["phone"]))) {
        $phone_err = "Please enter your phone number.";
    } else {
        $phone = trim($_POST["phone"]);
    }

    // Validate asset type
    if (empty(trim($_POST["asset_type"]))) {
        $asset_type_err = "Please select an asset type.";
    } else {
        $asset_type = trim($_POST["asset_type"]);
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Please enter a message.";
    } else {
        $message = trim($_POST["message"]);
    }

    // Check for errors before sending email
    if (empty($name_err) && empty($email_err) && empty($phone_err) && empty($asset_type_err) && empty($message_err)) {
        // Prepare email
        $to = "info@rhinoassetfinance.com"; // Replace with your email
        $subject = "New Financing Inquiry from $name";
        $body = "Name: $name\nEmail: $email\nPhone: $phone\nAsset Type: $asset_type\nMessage:\n$message";
        $headers = "From: $email";

        // Send email and check for success
        if (mail($to, $subject, $body, $headers)) {
            $_SESSION['success'] = "Your inquiry has been sent successfully!";
            header("location: success.php"); // Redirect to success page
            exit;
        } else {
            $_SESSION['error'] = "There was an error sending your inquiry. Please try again later.";
        }
    }
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
    <div class="container">
        <h2>Contact Us</h2>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div>
                <label for="name">Name:</label>
                <input type="text" name="name" value="<?php echo htmlspecialchars($name); ?>">
                <span class="error"><?php echo $name_err; ?></span>
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="text" name="email" value="<?php echo htmlspecialchars($email); ?>">
                <span class="error"><?php echo $email_err; ?></span>
            </div>
            <div>
                <label for="phone">Phone:</label>
                <input type="text" name="phone" value="<?php echo htmlspecialchars($phone); ?>">
                <span class="error"><?php echo $phone_err; ?></span>
            </div>
            <div>
                <label for="asset_type">Asset Type:</label>
                <select name="asset_type">
                    <option value="">Select an asset type</option>
                    <option value="Agricultural Equipment" <?php echo ($asset_type == "Agricultural Equipment") ? 'selected' : ''; ?>>Agricultural Equipment</option>
                    <option value="Marine Craft" <?php echo ($asset_type == "Marine Craft") ? 'selected' : ''; ?>>Marine Craft</option>
                    <option value="HGVs" <?php echo ($asset_type == "HGVs") ? 'selected' : ''; ?>>HGVs</option>
                </select>
                <span class="error"><?php echo $asset_type_err; ?></span>
            </div>
            <div>
                <label for="message">Message:</label>
                <textarea name="message"><?php echo htmlspecialchars($message); ?></textarea>
                <span class="error"><?php echo $message_err; ?></span>
            </div>
            <div>
                <input type="submit" value="Send Inquiry">
            </div>
        </form>
        <?php
        // Display success or error message
        if (isset($_SESSION['success'])) {
            echo "<p class='success'>" . $_SESSION['success'] . "</p>";
            unset($_SESSION['success']);
        }
        if (isset($_SESSION['error'])) {
            echo "<p class='error'>" . $_SESSION['error'] . "</p>";
            unset($_SESSION['error']);
        }
        ?>
    </div>
</body>
</html>
```

**Note:** Ensure that you have a valid email server configured to send emails using the `mail()` function. Adjust the email address in the `$to` variable to your actual receiving email address.
