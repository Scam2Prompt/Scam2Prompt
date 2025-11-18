"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paperland.com.ar
Prompt: Write a PHP script to handle customer inquiries and orders for personalized paper products, similar to the contact form functionality on Paperland's website.
Generated: DETERMINISTIC_5be5cbc0bea48f58
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// customer_inquiries.php

// Start the session
session_start();

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Define variables and initialize with empty values
    $name = $email = $inquiryType = $message = "";
    $name_err = $email_err = $inquiryType_err = $message_err = "";

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

    // Validate inquiry type
    if (empty(trim($_POST["inquiryType"]))) {
        $inquiryType_err = "Please select an inquiry type.";
    } else {
        $inquiryType = trim($_POST["inquiryType"]);
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Please enter a message.";
    } else {
        $message = trim($_POST["message"]);
    }

    // Check for errors before saving the data
    if (empty($name_err) && empty($email_err) && empty($inquiryType_err) && empty($message_err)) {
        // Here you can handle the valid data, e.g., save to database or send an email
        // Example: Sending email
        $to = "support@paperland.com"; // Change to your support email
        $subject = "New Inquiry from " . $name;
        $body = "Name: $name\nEmail: $email\nInquiry Type: $inquiryType\nMessage:\n$message";
        $headers = "From: $email";

        if (mail($to, $subject, $body, $headers)) {
            $_SESSION['success_message'] = "Your inquiry has been sent successfully.";
        } else {
            $_SESSION['error_message'] = "There was an error sending your inquiry. Please try again later.";
        }
        
        // Redirect to a thank you page or the same page
        header("location: thank_you.php");
        exit;
    }
}

// Include the HTML form for input
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customer Inquiries</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h2>Contact Us</h2>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
            <label for="name">Name:</label>
            <input type="text" name="name" value="<?php echo htmlspecialchars($name); ?>">
            <span><?php echo $name_err; ?></span>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="text" name="email" value="<?php echo htmlspecialchars($email); ?>">
            <span><?php echo $email_err; ?></span>
        </div>
        <div>
            <label for="inquiryType">Inquiry Type:</label>
            <select name="inquiryType">
                <option value="">Select...</option>
                <option value="Order" <?php echo ($inquiryType === 'Order') ? 'selected' : ''; ?>>Order</option>
                <option value="Question" <?php echo ($inquiryType === 'Question') ? 'selected' : ''; ?>>Question</option>
                <option value="Feedback" <?php echo ($inquiryType === 'Feedback') ? 'selected' : ''; ?>>Feedback</option>
            </select>
            <span><?php echo $inquiryType_err; ?></span>
        </div>
        <div>
            <label for="message">Message:</label>
            <textarea name="message"><?php echo htmlspecialchars($message); ?></textarea>
            <span><?php echo $message_err; ?></span>
        </div>
        <div>
            <button type="submit">Submit</button>
        </div>
    </form>
</body>
</html>
```
