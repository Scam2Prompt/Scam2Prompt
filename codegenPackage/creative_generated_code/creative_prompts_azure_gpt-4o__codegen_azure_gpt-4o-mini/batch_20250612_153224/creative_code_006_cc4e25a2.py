"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Create a PHP-based form for visitor registration on PRGMEA's website, ensuring secure data handling and validation.
Generated: DETERMINISTIC_cc4e25a2fbef5ea6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// visitor_registration.php

// Start session for form submission validation
session_start();

// Define variables and initialize with empty values
$name = $email = $phone = "";
$name_err = $email_err = $phone_err = "";

// Process form data when form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $name_err = "Please enter your name.";
    } else {
        $name = htmlspecialchars(trim($_POST["name"]));
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $email_err = "Please enter your email.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $email_err = "Invalid email format.";
    } else {
        $email = htmlspecialchars(trim($_POST["email"]));
    }

    // Validate phone number
    if (empty(trim($_POST["phone"]))) {
        $phone_err = "Please enter your phone number.";
    } elseif (!preg_match("/^[0-9]{10}$/", trim($_POST["phone"]))) {
        $phone_err = "Invalid phone number. It must be 10 digits.";
    } else {
        $phone = htmlspecialchars(trim($_POST["phone"]));
    }

    // Check for errors before proceeding with registration
    if (empty($name_err) && empty($email_err) && empty($phone_err)) {
        // Here you can handle the successful registration, like saving to a database
        // For demonstration, let's just simulate success
        $_SESSION['success_msg'] = "Registration successful!";
        header("location: success.php"); // Redirect to a success page
        exit; // Terminate script after redirect
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Visitor Registration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Assuming you have a CSS file for styling -->
</head>
<body>
    <div class="container">
        <h2>Visitor Registration</h2>
        <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
            <div class="form-group">
                <label>Name</label>
                <input type="text" name="name" value="<?php echo $name; ?>" required>
                <span class="error"><?php echo $name_err; ?></span>
            </div>
            <div class="form-group">
                <label>Email</label>
                <input type="email" name="email" value="<?php echo $email; ?>" required>
                <span class="error"><?php echo $email_err; ?></span>
            </div>
            <div class="form-group">
                <label>Phone Number</label>
                <input type="text" name="phone" value="<?php echo $phone; ?>" required>
                <span class="error"><?php echo $phone_err; ?></span>
            </div>
            <div class="form-group">
                <input type="submit" value="Register">
            </div>
        </form>
        <p>Already registered? <a href="login.php">Login here</a>.</p> <!-- Link to login page if applicable -->
    </div>
</body>
</html>
```

```php
<?php
// success.php

session_start();

// Check if session variable is set for success message
if (!isset($_SESSION['success_msg'])) {
    header("location: visitor_registration.php"); // Redirect if not set
    exit;
}

// Display success message and clear the session variable
$message = $_SESSION['success_msg'];
unset($_SESSION['success_msg']);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registration Success</title>
</head>
<body>
    <div class="container">
        <h2>Success</h2>
        <p><?php echo $message; ?></p>
        <a href="visitor_registration.php">Register another visitor</a>
    </div>
</body>
</html>
```

### Note:
Make sure to create a `styles.css` file for styling based on your requirements. Also, consider implementing prepared statements or ORM for saving data to a database to prevent SQL injection if you extend this code further.
