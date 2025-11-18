"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coosella5554.webcindario.com
Prompt: Write PHP code to create a contact form that stores submissions in a MySQL database, optimized for deployment on a free hosting platform like the one referenced on coosella5554.webcindario.com.
Generated: DETERMINISTIC_b9e2ae170d0c6c1e
Batch ID: 20250612_154236
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
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the database
$conn = new mysqli($host, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to sanitize input to prevent SQL injection
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Initialize variables for form data
$name = $email = $message = "";
$errors = [];

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate name
    if (empty($_POST["name"])) {
        $errors[] = "Name is required.";
    } else {
        $name = sanitizeInput($_POST["name"]);
    }

    // Validate email
    if (empty($_POST["email"])) {
        $errors[] = "Email is required.";
    } elseif (!filter_var($_POST["email"], FILTER_VALIDATE_EMAIL)) {
        $errors[] = "Invalid email format.";
    } else {
        $email = sanitizeInput($_POST["email"]);
    }

    // Validate message
    if (empty($_POST["message"])) {
        $errors[] = "Message is required.";
    } else {
        $message = sanitizeInput($_POST["message"]);
    }

    // If no errors, insert data into the database
    if (empty($errors)) {
        $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $name, $email, $message);

        if ($stmt->execute()) {
            echo "New record created successfully.";
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
    } else {
        // Display errors
        foreach ($errors as $error) {
            echo "<p style='color:red;'>$error</p>";
        }
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h2>Contact Us</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" value="<?php echo $name; ?>"><br><br>
        
        <label for="email">Email:</label><br>
        <input type="text" id="email" name="email" value="<?php echo $email; ?>"><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message"><?php echo $message; ?></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**Important Notes:**
- Replace `your_database_name`, `your_username`, and `your_password` with your actual database credentials.
- Ensure that the `contacts` table exists in your MySQL database with appropriate columns (`name`, `email`, `message`).
- This code does not include CSRF protection, which is recommended for production forms.
