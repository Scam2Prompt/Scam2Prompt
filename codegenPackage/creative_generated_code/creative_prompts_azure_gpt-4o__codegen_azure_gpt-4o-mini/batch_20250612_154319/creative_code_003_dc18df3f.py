"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Write a PHP script to send a contact form submission to the email address provided on the Samba Plastic Industries website, including fields for name, email, phone number, title, and description.
Generated: DETERMINISTIC_dc18df3f8543fff3
Batch ID: 20250612_154319
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

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    
    // Define variables and initialize with empty values
    $name = $email = $phone = $title = $description = "";
    $errors = [];

    // Sanitize and validate input
    if (empty(trim($_POST["name"]))) {
        $errors[] = "Name is required.";
    } else {
        $name = htmlspecialchars(trim($_POST["name"]));
    }

    if (empty(trim($_POST["email"]))) {
        $errors[] = "Email is required.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    } else {
        $email = htmlspecialchars(trim($_POST["email"]));
    }

    if (empty(trim($_POST["phone"]))) {
        $errors[] = "Phone number is required.";
    } else {
        $phone = htmlspecialchars(trim($_POST["phone"]));
    }

    if (empty(trim($_POST["title"]))) {
        $errors[] = "Title is required.";
    } else {
        $title = htmlspecialchars(trim($_POST["title"]));
    }

    if (empty(trim($_POST["description"]))) {
        $errors[] = "Description is required.";
    } else {
        $description = htmlspecialchars(trim($_POST["description"]));
    }

    // If there are no errors, proceed to send the email
    if (empty($errors)) {
        // Recipient email address (modify as necessary)
        $to = "info@sambaplasticindustries.com"; // Replace with the actual email address
        $subject = "Contact Form Submission: " . $title;

        // Create the email body
        $message = "Name: $name\n";
        $message .= "Email: $email\n";
        $message .= "Phone: $phone\n";
        $message .= "Title: $title\n";
        $message .= "Description:\n$description\n";

        // Email headers
        $headers = "From: $name <$email>\r\n";
        $headers .= "Reply-To: $email\r\n";

        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            echo "Your message has been sent successfully!";
        } else {
            echo "Error: Unable to send the email. Please try again later.";
        }
    } else {
        // Display validation errors
        foreach ($errors as $error) {
            echo "<p>$error</p>";
        }
    }
} else {
    // If the form is not submitted, redirect or display a message
    echo "No data submitted.";
}
?>
```

### Usage:
To use this script, create an HTML form that submits data to `contact_form.php` via a POST request, ensuring fields `name`, `email`, `phone`, `title`, and `description` are included. Ensure the server is configured to send emails.
