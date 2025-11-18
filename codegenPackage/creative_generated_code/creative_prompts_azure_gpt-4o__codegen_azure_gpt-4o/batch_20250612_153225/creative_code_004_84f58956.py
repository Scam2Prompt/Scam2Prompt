"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nucleicinsights.com
Prompt: Generate code for a contact form in HTML and PHP that matches the design aesthetic of Umama Shahid's website, including fields for name, email, subject, and message.
Generated: DETERMINISTIC_84f58956cc5d46fd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### HTML (Contact Form)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        /* Basic styling to match a modern aesthetic */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }

        .contact-form {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .contact-form h2 {
            margin-bottom: 20px;
            color: #333;
            text-align: center;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #555;
        }

        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }

        input:focus, textarea:focus {
            border-color: #007BFF;
            outline: none;
        }

        button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            color: #ffffff;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }

        .success-message, .error-message {
            margin-top: 20px;
            text-align: center;
            font-weight: bold;
        }

        .success-message {
            color: #28a745;
        }

        .error-message {
            color: #dc3545;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Contact Us</h2>
        <form action="contact.php" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" required></textarea>
            </div>
            
            <button type="submit">Send Message</button>
        </form>
    </div>
</body>
</html>
```

### PHP (`contact.php`)
```php
<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate and sanitize input data
    $name = htmlspecialchars(strip_tags(trim($_POST['name'])));
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $subject = htmlspecialchars(strip_tags(trim($_POST['subject'])));
    $message = htmlspecialchars(strip_tags(trim($_POST['message'])));

    // Error flag
    $errors = [];

    // Simple validation
    if (empty($name)) {
        $errors[] = "Name is required.";
    }

    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Valid email is required.";
    }

    if (empty($subject)) {
        $errors[] = "Subject is required.";
    }

    if (empty($message)) {
        $errors[] = "Message is required.";
    }

    // If there are errors, display them
    if (!empty($errors)) {
        echo "<div class='error-message'>";
        foreach ($errors as $error) {
            echo "<p>$error</p>";
        }
        echo "</div>";
    } else {
        // Email configuration
        $to = "your-email@example.com"; // Replace with the recipient email
        $headers = "From: $email\r\n";
        $headers .= "Reply-To: $email\r\n";
        $emailMessage = "Name: $name\nEmail: $email\nSubject: $subject\n\nMessage:\n$message";

        // Send the email
        if (mail($to, $subject, $emailMessage, $headers)) {
            echo "<div class='success-message'>Your message has been sent successfully!</div>";
        } else {
            echo "<div class='error-message'>Failed to send your message. Please try again later.</div>";
        }
    }
}
?>
```

### Notes:
1. Replace `your-email@example.com` in the PHP file with your actual email address to receive form submissions.
2. Ensure that the server has the `mail()` function configured properly for sending emails.
3. For production, consider using a more robust mail library like PHPMailer or SwiftMailer for enhanced email handling capabilities.
