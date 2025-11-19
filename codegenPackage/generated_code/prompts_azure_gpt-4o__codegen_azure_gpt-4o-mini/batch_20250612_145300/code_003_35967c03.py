"""
Generated Code Metadata:
========================
Original URL: https://enjin.pro
Prompt: Generate PHP code to create a contact form for car inquiries, including fields for name, email, phone number, and specific car details, similar to the "お問い合わせ" section on the "縁陣 -ENJIN-" website.
Generated: DETERMINISTIC_35967c030d20d03e
Batch ID: 20250612_145300
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
$name = $email = $phone = $car_details = "";
$name_err = $email_err = $phone_err = $car_details_err = "";

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

    // Validate phone number
    if (empty(trim($_POST["phone"]))) {
        $phone_err = "Please enter your phone number.";
    } elseif (!preg_match('/^[0-9]{10,15}$/', trim($_POST["phone"]))) {
        $phone_err = "Invalid phone number format.";
    } else {
        $phone = trim($_POST["phone"]);
    }

    // Validate car details
    if (empty(trim($_POST["car_details"]))) {
        $car_details_err = "Please provide details about the car.";
    } else {
        $car_details = trim($_POST["car_details"]);
    }

    // Check for errors before sending email
    if (empty($name_err) && empty($email_err) && empty($phone_err) && empty($car_details_err)) {
        // Prepare email
        $to = "info@yourdomain.com"; // Change to your email address
        $subject = "Car Inquiry from $name";
        $message = "Name: $name\nEmail: $email\nPhone: $phone\nCar Details: $car_details";
        $headers = "From: $email";

        // Send email and check for success
        if (mail($to, $subject, $message, $headers)) {
            $_SESSION['success'] = "Your inquiry has been sent successfully!";
            header("location: success.php"); // Redirect to a success page
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
    <title>Contact Form - Car Inquiries</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Contact Us for Car Inquiries</h1>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
            <label for="name">Name:</label>
            <input type="text" name="name" value="<?php echo htmlspecialchars($name); ?>">
            <span><?php echo $name_err; ?></span>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" name="email" value="<?php echo htmlspecialchars($email); ?>">
            <span><?php echo $email_err; ?></span>
        </div>
        <div>
            <label for="phone">Phone Number:</label>
            <input type="text" name="phone" value="<?php echo htmlspecialchars($phone); ?>">
            <span><?php echo $phone_err; ?></span>
        </div>
        <div>
            <label for="car_details">Car Details:</label>
            <textarea name="car_details"><?php echo htmlspecialchars($car_details); ?></textarea>
            <span><?php echo $car_details_err; ?></span>
        </div>
        <div>
            <input type="submit" value="Submit Inquiry">
        </div>
    </form>
    <?php
    // Display success or error messages
    if (isset($_SESSION['success'])) {
        echo "<p>" . $_SESSION['success'] . "</p>";
        unset($_SESSION['success']);
    }
    if (isset($_SESSION['error'])) {
        echo "<p>" . $_SESSION['error'] . "</p>";
        unset($_SESSION['error']);
    }
    ?>
</body>
</html>
```

**Note:** Ensure to replace `info@yourdomain.com` with your actual email address where you want to receive inquiries. Also, create a `success.php` page to handle successful submissions.
