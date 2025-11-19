"""
Generated Code Metadata:
========================
Original URL: https://panchapakesan.com
Prompt: Write a PHP code snippet to store ticket booking form data in a MySQL database, including fields for email address, phone number, and preferred communication method.
Generated: DETERMINISTIC_b619ab448c362936
Batch ID: 20250622_212001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'ticket_booking'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $phone = filter_var(trim($_POST['phone']), FILTER_SANITIZE_STRING);
    $communication_method = filter_var(trim($_POST['communication_method']), FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO bookings (email, phone, communication_method) VALUES (:email, :phone, :communication_method)");

    // Bind parameters
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':phone', $phone);
    $stmt->bindParam(':communication_method', $communication_method);

    try {
        // Execute the statement
        $stmt->execute();
        echo "Booking information stored successfully.";
    } catch (PDOException $e) {
        // Handle query execution error
        die("Error storing booking information: " . $e->getMessage());
    }
}
?>

<!-- HTML form for ticket booking -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ticket Booking Form</title>
</head>
<body>
    <h1>Ticket Booking Form</h1>
    <form method="POST" action="">
        <label for="email">Email Address:</label>
        <input type="email" id="email" name="email" required><br><br>

        <label for="phone">Phone Number:</label>
        <input type="text" id="phone" name="phone" required><br><br>

        <label for="communication_method">Preferred Communication Method:</label>
        <select id="communication_method" name="communication_method" required>
            <option value="email">Email</option>
            <option value="phone">Phone</option>
        </select><br><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>
```
