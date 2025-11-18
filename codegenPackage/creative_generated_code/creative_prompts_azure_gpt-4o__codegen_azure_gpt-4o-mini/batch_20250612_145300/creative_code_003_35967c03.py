"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enjin.pro
Prompt: Generate PHP code to create a contact form for car inquiries, including fields for name, email, phone number, and specific car details, similar to the "お問い合わせ" section on the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_35967c030d20d03e
Batch ID: 20250612_145300
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

// Start session for error handling
session_start();

// Function to sanitize user input
function sanitize_input($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables for form fields
$name = $email = $phone = $car_details = "";
$errors = [];

// Form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitize_input($_POST["name"]);
    }

    // Validate and sanitize email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = sanitize_input($_POST["email"]);
    }

    // Validate and sanitize phone number
    if (empty($_POST["phone"])) {
        $errors['phone'] = "Phone number is required.";
    } else {
        $phone = sanitize_input($_POST["phone"]);
    }

    // Validate and sanitize car details
    if (empty($_POST["car_details"])) {
        $errors['car_details'] = "Car details are required.";
    } else {
        $car_details = sanitize_input($_POST["car_details"]);
    }

    // If no errors, proceed to send email or save the inquiry
    if (empty($errors)) {
        // Email configuration
        $to = "info@enjinsite.com"; // Replace with your email
        $subject = "Car Inquiry from $name";
        $message = "Name: $name\nEmail: $email\nPhone: $phone\nCar Details: $car_details";
        $headers = "From: $email";

        // Send email
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = "Your inquiry has been sent successfully.";
            header("Location: thank_you.php");
            exit();
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
    <title>Contact Us - Car Inquiry</title>
    <link rel="stylesheet" href="styles.css"> <!-- Include your CSS here -->
</head>
<body>
    <h1>Contact Us</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" id="name" value="<?php echo $name; ?>">
        <span class="error"><?php echo $errors['name'] ?? ''; ?></span>

        <label for="email">Email:</label>
        <input type="email" name="email" id="email" value="<?php echo $email; ?>">
        <span class="error"><?php echo $errors['email'] ?? ''; ?></span>

        <label for="phone">Phone Number:</label>
        <input type="text" name="phone" id="phone" value="<?php echo $phone; ?>">
        <span class="error"><?php echo $errors['phone'] ?? ''; ?></span>

        <label for="car_details">Car Details:</label>
        <textarea name="car_details" id="car_details"><?php echo $car_details; ?></textarea>
        <span class="error"><?php echo $errors['car_details'] ?? ''; ?></span>

        <input type="submit" value="Submit Inquiry">
    </form>

    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p class='success'>{$_SESSION['success']}</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p class='error'>{$_SESSION['error']}</p>";
        unset($_SESSION['error']);
    }
    ?>
</body>
</html>
```

**Note:** Ensure to replace `info@enjinsite.com` with the actual email address where inquiries should be sent. Also, create a `thank_you.php` page to redirect users after a successful submission.
