"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskxx1.webcindario.com
Prompt: Write code to create a contact form in PHP that stores submissions in a MySQL database, suitable for hosting on free platforms like miarroba.com.
Generated: DETERMINISTIC_18eaee0a312813a3
Batch ID: 20250612_151347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start a session to handle form messages.
session_start();

// Database configuration
$servername = "localhost"; // Change if necessary
$username = "root";        // Replace with your MySQL username
$password = "";            // Replace with your MySQL password
$dbname = "contact_db";    // Replace with your target database name

// Create a connection to MySQL
$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection and handle errors
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// If the form is submitted, process the input
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars(trim($_POST['message']));

    // Check for empty fields
    if (empty($name) || empty($email) || empty($message)) {
        $_SESSION['error'] = "All fields are required.";
        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    }

    // Prepare SQL statement to prevent SQL injection
    $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
    if (!$stmt) {
        $_SESSION['error'] = "Database error. Please try again later.";
        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    }

    // Bind parameters and execute the statement
    $stmt->bind_param("sss", $name, $email, $message);
    if ($stmt->execute()) {
        $_SESSION['success'] = "Your message has been sent successfully!";
    } else {
        $_SESSION['error'] = "Failed to send your message. Please try again.";
    }

    // Close the statement
    $stmt->close();

    // Redirect back to the form
    header("Location: " . $_SERVER['PHP_SELF']);
    exit();
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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .form-container {
            max-width: 400px;
            margin: 0 auto;
        }
        .form-container form {
            display: flex;
            flex-direction: column;
        }
        .form-container input,
        .form-container textarea {
            margin: 10px 0;
            padding: 10px;
            font-size: 16px;
        }
        .form-container button {
            padding: 10px;
            font-size: 16px;
            cursor: pointer;
        }
        .form-container .message {
            margin-bottom: 10px;
            color: red;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <!-- Display success or error messages -->
        <?php
        if (isset($_SESSION['error'])) {
            echo '<div class="message">' . $_SESSION['error'] . '</div>';
            unset($_SESSION['error']); // Clear the message after displaying
        }
        if (isset($_SESSION['success'])) {
            echo '<div class="message" style="color: green;">' . $_SESSION['success'] . '</div>';
            unset($_SESSION['success']); // Clear the message after displaying
        }
        ?>

        <form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
            <button type="submit">Send</button>
        </form>
    </div>
</body>
</html>

<?php
// Ensure the database table exists (run this query in your MySQL server beforehand)
/*
CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/
?>
```
