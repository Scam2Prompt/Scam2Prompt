"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-folks.icu
Prompt: Write code in PHP to implement a contact form that collects user information (name, email, project type) and sends it to the design team, similar to the contact functionality described on Odos Designs' website.
Generated: DETERMINISTIC_3c4aaf14f71ebfc0
Batch ID: 20250612_154219
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
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $projectType = filter_input(INPUT_POST, 'project_type', FILTER_SANITIZE_STRING);

    // Initialize an array to capture errors
    $errors = [];

    // Validate name
    if (empty($name)) {
        $errors['name'] = "Name is required.";
    }

    // Validate email
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "A valid email is required.";
    }

    // Validate project type
    if (empty($projectType)) {
        $errors['project_type'] = "Project type is required.";
    }

    // If no errors, proceed to send the email
    if (empty($errors)) {
        $to = "designteam@example.com"; // Replace with the actual email address of the design team
        $subject = "New Contact Form Submission";
        $message = "You have received a new contact form submission:\n\n" .
                   "Name: $name\n" .
                   "Email: $email\n" .
                   "Project Type: $projectType\n";
        $headers = "From: noreply@example.com\r\n"; // Replace with the appropriate "From" email address
        $headers .= "Reply-To: $email\r\n";

        // Send the email
        if (mail($to, $subject, $message, $headers)) {
            // Redirect to a confirmation page or display success message
            header("Location: confirmation.php");
            exit;
        } else {
            $errors['general'] = "An error occurred while sending your message. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    <?php
    // Display error messages (if any)
    if (!empty($errors)) {
        echo "<ul style='color: red;'>";
        foreach ($errors as $error) {
            echo "<li>$error</li>";
        }
        echo "</ul>";
    }
    ?>

    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" value="<?= htmlspecialchars($name ?? '') ?>"><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" value="<?= htmlspecialchars($email ?? '') ?>"><br><br>

        <label for="project_type">Project Type:</label><br>
        <input type="text" id="project_type" name="project_type" value="<?= htmlspecialchars($projectType ?? '') ?>"><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
