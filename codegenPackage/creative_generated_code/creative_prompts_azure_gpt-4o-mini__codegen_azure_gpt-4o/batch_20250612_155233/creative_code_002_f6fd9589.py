"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amici.nz
Prompt: Create a PHP code snippet that allows users to reserve a table at Amici Italian Cafe, including form validation for contact details.
Generated: DETERMINISTIC_f6fd9589fdcf565d
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Define constants for database connection
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'restaurant_reservations');

// Helper function for sanitizing input
function sanitizeInput($data)
{
    return htmlspecialchars(strip_tags(trim($data)));
}

// Error messages container
$errors = [];

// Check if the form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user input
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $phone = sanitizeInput($_POST['phone'] ?? '');
    $reservation_date = sanitizeInput($_POST['reservation_date'] ?? '');
    $reservation_time = sanitizeInput($_POST['reservation_time'] ?? '');
    $guest_count = sanitizeInput($_POST['guest_count'] ?? '');

    // Basic validation
    if (empty($name)) {
        $errors['name'] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = 'Valid email is required.';
    }
    if (empty($phone) || !preg_match('/^\+?[0-9]{7,15}$/', $phone)) {
        $errors['phone'] = 'Valid phone number is required.';
    }
    if (empty($reservation_date) || !strtotime($reservation_date)) {
        $errors['reservation_date'] = 'Valid reservation date is required.';
    }
    if (empty($reservation_time) || !preg_match('/^([01]?[0-9]|2[0-3]):[0-5][0-9]$/', $reservation_time)) {
        $errors['reservation_time'] = 'Valid reservation time is required.';
    }
    if (empty($guest_count) || !filter_var($guest_count, FILTER_VALIDATE_INT) || $guest_count <= 0) {
        $errors['guest_count'] = 'Valid number of guests is required.';
    }

    // Proceed if no errors
    if (empty($errors)) {
        // Connect to the database
        $conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

        // Check connection
        if ($conn->connect_error) {
            die('Database connection failed: ' . $conn->connect_error);
        }

        // Prepare and bind the SQL statement
        $stmt = $conn->prepare("INSERT INTO reservations (name, email, phone, reservation_date, reservation_time, guest_count) VALUES (?, ?, ?, ?, ?, ?)");
        if (!$stmt) {
            die('Database statement preparation failed: ' . $conn->error);
        }

        $stmt->bind_param("sssssi", $name, $email, $phone, $reservation_date, $reservation_time, $guest_count);

        // Execute the statement
        if ($stmt->execute()) {
            echo 'Reservation successful!';
        } else {
            echo 'Reservation failed: ' . $stmt->error;
        }

        // Close the statement and connection
        $stmt->close();
        $conn->close();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reserve a Table - Amici Italian Cafe</title>
</head>
<body>
    <h1>Reserve a Table at Amici Italian Cafe</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <?php if (!empty($errors['name'])) echo "<p style='color:red;'>{$errors['name']}</p>"; ?>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <?php if (!empty($errors['email'])) echo "<p style='color:red;'>{$errors['email']}</p>"; ?>

        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <?php if (!empty($errors['phone'])) echo "<p style='color:red;'>{$errors['phone']}</p>"; ?>

        <label for="reservation_date">Reservation Date:</label>
        <input type="date" id="reservation_date" name="reservation_date" required>
        <?php if (!empty($errors['reservation_date'])) echo "<p style='color:red;'>{$errors['reservation_date']}</p>"; ?>

        <label for="reservation_time">Reservation Time:</label>
        <input type="time" id="reservation_time" name="reservation_time" required>
        <?php if (!empty($errors['reservation_time'])) echo "<p style='color:red;'>{$errors['reservation_time']}</p>"; ?>

        <label for="guest_count">Number of Guests:</label>
        <input type="number" id="guest_count" name="guest_count" required>
        <?php if (!empty($errors['guest_count'])) echo "<p style='color:red;'>{$errors['guest_count']}</p>"; ?>

        <button type="submit">Reserve</button>
    </form>
</body>
</html>
```
