"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidresponder.net
Prompt: Generate a PHP script that collects user input for a consultation form to assist in recovering lost investments.
Generated: DETERMINISTIC_dd714079aa83d5bb
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// consultation_form.php

// Start the session to retain form input data if needed
session_start();

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables for form fields
$name = $email = $phone = $message = "";
$nameError = $emailError = $phoneError = $messageError = "";

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $isValid = true;

    // Validate name (required, only letters and spaces allowed)
    if (empty($_POST["name"])) {
        $nameError = "Name is required.";
        $isValid = false;
    } else {
        $name = sanitize_input($_POST["name"]);
        if (!preg_match("/^[a-zA-Z\s]+$/", $name)) {
            $nameError = "Name can only contain letters and spaces.";
            $isValid = false;
        }
    }

    // Validate email (required, must follow valid email format)
    if (empty($_POST["email"])) {
        $emailError = "Email is required.";
        $isValid = false;
    } else {
        $email = sanitize_input($_POST["email"]);
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $emailError = "Invalid email format.";
            $isValid = false;
        }
    }

    // Validate phone (optional, only digits allowed)
    if (!empty($_POST["phone"])) {
        $phone = sanitize_input($_POST["phone"]);
        if (!preg_match("/^[0-9]+$/", $phone)) {
            $phoneError = "Phone number can only contain digits.";
            $isValid = false;
        }
    }

    // Validate message (required)
    if (empty($_POST["message"])) {
        $messageError = "Message is required.";
        $isValid = false;
    } else {
        $message = sanitize_input($_POST["message"]);
    }

    // If the form is valid, process the data
    if ($isValid) {
        // Process form data (e.g., save to database, send email)
        // As an example, simulate saving to a file
        $formData = [
            "Name" => $name,
            "Email" => $email,
            "Phone" => $phone,
            "Message" => $message,
        ];

        $file = fopen("consultation_data.txt", "a");
        if ($file) {
            fwrite($file, json_encode($formData) . PHP_EOL);
            fclose($file);
            $successMessage = "Your consultation request has been successfully submitted!";
        } else {
            $errorMessage = "Failed to save your consultation request. Please try again later.";
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Consultation Form</title>
</head>
<body>
    <h1>Consultation Form</h1>
    <?php 
    // Display success or error message
    if (isset($successMessage)) {
        echo "<p style='color:green;'>$successMessage</p>";
    } elseif (isset($errorMessage)) {
        echo "<p style='color:red;'>$errorMessage</p>";
    }
    ?>
    <form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="<?php echo htmlspecialchars($name); ?>">
        <span style="color:red;"><?php echo $nameError; ?></span>
        <br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" value="<?php echo htmlspecialchars($email); ?>">
        <span style="color:red;"><?php echo $emailError; ?></span>
        <br><br>

        <label for="phone">Phone (optional):</label>
        <input type="text" id="phone" name="phone" value="<?php echo htmlspecialchars($phone); ?>">
        <span style="color:red;"><?php echo $phoneError; ?></span>
        <br><br>

        <label for="message">Message:</label>
        <textarea id="message" name="message"><?php echo htmlspecialchars($message); ?></textarea>
        <span style="color:red;"><?php echo $messageError; ?></span>
        <br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
