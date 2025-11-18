"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivienprotec.webcindario.com
Prompt: Generate a PHP script to create a user registration form and store the data in a MySQL database, optimized for free hosting environments.
Generated: DETERMINISTIC_d443306c37fcddbd
Batch ID: 20250612_154355
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
$host = 'localhost'; // Database host
$db_name = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create connection to MySQL database
$conn = new mysqli($host, $username, $password, $db_name);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Initialize variables for user input
$fullName = $email = $password = '';
$errorMessages = [];

// Process form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate user input
    if (empty($_POST["full_name"])) {
        $errorMessages[] = "Full name is required.";
    } else {
        $fullName = sanitizeInput($_POST["full_name"]);
    }

    if (empty($_POST["email"])) {
        $errorMessages[] = "Email is required.";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errorMessages[] = "Invalid email format.";
    } else {
        $email = sanitizeInput($_POST["email"]);
    }

    if (empty($_POST["password"])) {
        $errorMessages[] = "Password is required.";
    } else {
        $password = sanitizeInput($_POST["password"]);
        // Hash the password for security
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    }

    // If no errors, proceed to insert data into the database
    if (empty($errorMessages)) {
        // Prepare and bind statement to prevent SQL injection
        $stmt = $conn->prepare("INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $fullName, $email, $hashedPassword);

        // Execute the statement and check for errors
        if ($stmt->execute()) {
            echo "Registration successful!";
        } else {
            echo "Error: " . $stmt->error;
        }

        // Close the statement
        $stmt->close();
    } else {
        // Display error messages
        foreach ($errorMessages as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    }
}

// Close database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration Form</h2>
    <form action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>" method="post">
        <label for="full_name">Full Name:</label><br>
        <input type="text" id="full_name" name="full_name" value="<?php echo $fullName; ?>" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" value="<?php echo $email; ?>" required><br><br>

        <label for="password">Password:</label><br>
        <input type="password" id="password" name="password" required><br><br>

        <input type="submit" value="Register">
    </form>
</body>
</html>
```
