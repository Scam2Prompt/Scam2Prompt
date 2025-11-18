"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redhorsereflex.com
Prompt: Write a PHP script to implement a contact form for a reflexology service website, including fields for name, email, phone number, and message, and ensure the form data is securely stored in a MySQL database.
Generated: DETERMINISTIC_299ccf8441da9a3f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$servername = "localhost"; // Change this if your MySQL server is on a different host
$username = "db_username"; // Database username
$password = "db_password"; // Database password
$dbname = "reflexology_db"; // Database name

// Create a new MySQLi connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check for connection errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Define variables and initialize with empty values
$name = $email = $phone = $message = "";
$name_err = $email_err = $phone_err = $message_err = "";

// Process the form when it is submitted
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

    // Validate phone
    if (empty(trim($_POST["phone"]))) {
        $phone_err = "Please enter your phone number.";
    } elseif (!preg_match('/^[0-9]{10}$/', trim($_POST["phone"]))) {
        $phone_err = "Phone number must be 10 digits.";
    } else {
        $phone = trim($_POST["phone"]);
    }

    // Validate message
    if (empty(trim($_POST["message"]))) {
        $message_err = "Please enter your message.";
    } else {
        $message = trim($_POST["message"]);
    }

    // Check for errors before inserting into the database
    if (empty($name_err) && empty($email_err) && empty($phone_err) && empty($message_err)) {
        // Prepare an insert statement
        $stmt = $conn->prepare("INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)");
        $stmt->bind_param("ssss", $name, $email, $phone, $message);

        // Attempt to execute the prepared statement
        if ($stmt->execute()) {
            echo "Message sent successfully!";
        } else {
            echo "Error: " . $stmt->error;
        }

        // Close statement
        $stmt->close();
    }
}

// Close connection
$conn->close();
?>

<!-- HTML Form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h2>Contact Us</h2>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <div>
            <label>Name:</label>
            <input type="text" name="name" value="<?php echo htmlspecialchars($name); ?>">
            <span><?php echo $name_err; ?></span>
        </div>
        <div>
            <label>Email:</label>
            <input type="text" name="email" value="<?php echo htmlspecialchars($email); ?>">
            <span><?php echo $email_err; ?></span>
        </div>
        <div>
            <label>Phone:</label>
            <input type="text" name="phone" value="<?php echo htmlspecialchars($phone); ?>">
            <span><?php echo $phone_err; ?></span>
        </div>
        <div>
            <label>Message:</label>
            <textarea name="message"><?php echo htmlspecialchars($message); ?></textarea>
            <span><?php echo $message_err; ?></span>
        </div>
        <div>
            <input type="submit" value="Submit">
        </div>
    </form>
</body>
</html>
```
