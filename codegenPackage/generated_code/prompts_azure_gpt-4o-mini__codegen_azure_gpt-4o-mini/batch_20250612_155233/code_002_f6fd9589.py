"""
Generated Code Metadata:
========================
Original URL: https://amici.nz
Prompt: Create a PHP code snippet that allows users to reserve a table at Amici Italian Cafe, including form validation for contact details.
Generated: DETERMINISTIC_f6fd9589fdcf565d
Batch ID: 20250612_155233
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Start the session to store form data and error messages
session_start();

// Initialize variables for form data and error messages
$name = $email = $phone = $date = $time = $guests = "";
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty(trim($_POST["name"]))) {
        $errors['name'] = "Name is required.";
    } else {
        $name = htmlspecialchars(trim($_POST["name"]));
    }

    // Validate email
    if (empty(trim($_POST["email"]))) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var(trim($_POST["email"]), FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = htmlspecialchars(trim($_POST["email"]));
    }

    // Validate phone
    if (empty(trim($_POST["phone"]))) {
        $errors['phone'] = "Phone number is required.";
    } elseif (!preg_match('/^\d{10}$/', trim($_POST["phone"]))) {
        $errors['phone'] = "Phone number must be 10 digits.";
    } else {
        $phone = htmlspecialchars(trim($_POST["phone"]));
    }

    // Validate date
    if (empty(trim($_POST["date"]))) {
        $errors['date'] = "Reservation date is required.";
    } else {
        $date = htmlspecialchars(trim($_POST["date"]));
    }

    // Validate time
    if (empty(trim($_POST["time"]))) {
        $errors['time'] = "Reservation time is required.";
    } else {
        $time = htmlspecialchars(trim($_POST["time"]));
    }

    // Validate number of guests
    if (empty(trim($_POST["guests"]))) {
        $errors['guests'] = "Number of guests is required.";
    } elseif (!is_numeric(trim($_POST["guests"])) || (int)trim($_POST["guests"]) <= 0) {
        $errors['guests'] = "Number of guests must be a positive number.";
    } else {
        $guests = htmlspecialchars(trim($_POST["guests"]));
    }

    // If there are no errors, process the reservation
    if (empty($errors)) {
        // Here you would typically save the reservation to a database
        // For demonstration, we'll just store it in the session
        $_SESSION['reservation'] = [
            'name' => $name,
            'email' => $email,
            'phone' => $phone,
            'date' => $date,
            'time' => $time,
            'guests' => $guests
        ];
        // Redirect to a confirmation page (not implemented here)
        header("Location: confirmation.php");
        exit();
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
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="name">Name:</label>
        <input type="text" name="name" value="<?php echo $name; ?>">
        <span><?php echo $errors['name'] ?? ''; ?></span><br>

        <label for="email">Email:</label>
        <input type="email" name="email" value="<?php echo $email; ?>">
        <span><?php echo $errors['email'] ?? ''; ?></span><br>

        <label for="phone">Phone:</label>
        <input type="text" name="phone" value="<?php echo $phone; ?>">
        <span><?php echo $errors['phone'] ?? ''; ?></span><br>

        <label for="date">Reservation Date:</label>
        <input type="date" name="date" value="<?php echo $date; ?>">
        <span><?php echo $errors['date'] ?? ''; ?></span><br>

        <label for="time">Reservation Time:</label>
        <input type="time" name="time" value="<?php echo $time; ?>">
        <span><?php echo $errors['time'] ?? ''; ?></span><br>

        <label for="guests">Number of Guests:</label>
        <input type="number" name="guests" value="<?php echo $guests; ?>">
        <span><?php echo $errors['guests'] ?? ''; ?></span><br>

        <input type="submit" value="Reserve Table">
    </form>
</body>
</html>
```
