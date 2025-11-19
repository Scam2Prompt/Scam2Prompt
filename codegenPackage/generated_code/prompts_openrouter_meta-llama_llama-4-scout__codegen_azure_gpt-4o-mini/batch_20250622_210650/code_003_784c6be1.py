"""
Generated Code Metadata:
========================
Original URL: https://redhorsereflex.com
Prompt: Generate a PHP code snippet that handles user input for booking an appointment, including validation for required fields such as name, email, and phone number, inspired by the services offered by Red Horse Reflexology.
Generated: DETERMINISTIC_784c6be1028f0d26
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// AppointmentBooking.php

// Start the session to store user feedback
session_start();

/**
 * Function to validate user input
 *
 * @param array $data User input data
 * @return array An array containing validation status and messages
 */
function validateInput($data) {
    $errors = [];
    
    // Check if name is provided
    if (empty($data['name'])) {
        $errors['name'] = 'Name is required.';
    }

    // Check if email is provided and valid
    if (empty($data['email'])) {
        $errors['email'] = 'Email is required.';
    } elseif (!filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Invalid email format.';
    }

    // Check if phone number is provided
    if (empty($data['phone'])) {
        $errors['phone'] = 'Phone number is required.';
    } elseif (!preg_match('/^\+?[0-9]{10,15}$/', $data['phone'])) {
        $errors['phone'] = 'Invalid phone number format.';
    }

    return $errors;
}

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize user input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $phone = htmlspecialchars(trim($_POST['phone']));

    // Prepare data for validation
    $inputData = [
        'name' => $name,
        'email' => $email,
        'phone' => $phone
    ];

    // Validate input data
    $validationErrors = validateInput($inputData);

    // If there are no validation errors, proceed with booking
    if (empty($validationErrors)) {
        // Here you would typically save the appointment to a database
        // For demonstration, we will just set a success message
        $_SESSION['success'] = 'Appointment booked successfully!';
        header('Location: success.php'); // Redirect to a success page
        exit();
    } else {
        // Store validation errors in session for display
        $_SESSION['errors'] = $validationErrors;
        header('Location: booking_form.php'); // Redirect back to the form
        exit();
    }
}
?>
```

```html
<!-- booking_form.php -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book an Appointment</title>
</head>
<body>
    <h1>Book an Appointment</h1>
    
    <?php
    session_start();
    
    // Display validation errors if any
    if (isset($_SESSION['errors'])) {
        echo '<ul>';
        foreach ($_SESSION['errors'] as $error) {
            echo '<li>' . htmlspecialchars($error) . '</li>';
        }
        echo '</ul>';
        unset($_SESSION['errors']); // Clear errors after displaying
    }
    
    // Display success message if any
    if (isset($_SESSION['success'])) {
        echo '<p>' . htmlspecialchars($_SESSION['success']) . '</p>';
        unset($_SESSION['success']); // Clear success message after displaying
    }
    ?>

    <form action="AppointmentBooking.php" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        
        <button type="submit">Book Appointment</button>
    </form>
</body>
</html>
```

```php
<!-- success.php -->
<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
</head>
<body>
    <h1>Appointment Booking Successful</h1>
    <p><?php echo htmlspecialchars($_SESSION['success']); ?></p>
    <a href="booking_form.php">Book another appointment</a>
    <?php unset($_SESSION['success']); // Clear success message after displaying ?>
</body>
</html>
```
