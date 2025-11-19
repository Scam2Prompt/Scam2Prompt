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
// Start the session to store form data and error messages
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables and error messages
$name = $email = $phone = $date = $time = $guests = "";
$errors = [];

// Form processing logic
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty($_POST["name"])) {
        $errors['name'] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST["name"]);
    }

    // Validate email
    if (empty($_POST["email"])) {
        $errors['email'] = "Email is required.";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errors['email'] = "Invalid email format.";
    } else {
        $email = sanitizeInput($_POST["email"]);
    }

    // Validate phone
    if (empty($_POST["phone"])) {
        $errors['phone'] = "Phone number is required.";
    } elseif (!preg_match("/^[0-9]{10}$/", $_POST["phone"])) {
        $errors['phone'] = "Invalid phone number. Must be 10 digits.";
    } else {
        $phone = sanitizeInput($_POST["phone"]);
    }

    // Validate date
    if (empty($_POST["date"])) {
        $errors['date'] = "Reservation date is required.";
    } else {
        $date = sanitizeInput($_POST["date"]);
    }

    // Validate time
    if (empty($_POST["time"])) {
        $errors['time'] = "Reservation time is required.";
    } else {
        $time = sanitizeInput($_POST["time"]);
    }

    // Validate number of guests
    if (empty($_POST["guests"]) || !is_numeric($_POST["guests"]) || $_POST["guests"] <= 0) {
        $errors['guests'] = "Number of guests must be a positive number.";
    } else {
        $guests = sanitizeInput($_POST["guests"]);
    }

    // If no errors, proceed with reservation logic (e.g., saving to the database)
    if (empty($errors)) {
        // Here you would typically save the reservation to a database
        // For demonstration, we'll just simulate a successful reservation
        $_SESSION['success'] = "Table reserved successfully for $guests guests on $date at $time.";
        header("Location: confirmation.php"); // Redirect to confirmation page
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
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>Reserve a Table at Amici Italian Cafe</h1>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label>Name:</label>
        <input type="text" name="name" value="<?php echo $name; ?>">
        <span class="error"><?php echo $errors['name'] ?? ''; ?></span><br>

        <label>Email:</label>
        <input type="text" name="email" value="<?php echo $email; ?>">
        <span class="error"><?php echo $errors['email'] ?? ''; ?></span><br>

        <label>Phone:</label>
        <input type="text" name="phone" value="<?php echo $phone; ?>">
        <span class="error"><?php echo $errors['phone'] ?? ''; ?></span><br>

        <label>Date:</label>
        <input type="date" name="date" value="<?php echo $date; ?>">
        <span class="error"><?php echo $errors['date'] ?? ''; ?></span><br>

        <label>Time:</label>
        <input type="time" name="time" value="<?php echo $time; ?>">
        <span class="error"><?php echo $errors['time'] ?? ''; ?></span><br>

        <label>Number of Guests:</label>
        <input type="number" name="guests" value="<?php echo $guests; ?>">
        <span class="error"><?php echo $errors['guests'] ?? ''; ?></span><br>

        <input type="submit" value="Reserve Table">
    </form>
    
    <?php
    // Display success message if available
    if (isset($_SESSION['success'])) {
        echo "<p class='success'>{$_SESSION['success']}</p>";
        unset($_SESSION['success']); // Clear message after displaying
    }
    ?>
</body>
</html>
```
