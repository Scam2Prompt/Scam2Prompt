"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: Provide step-by-step code to set up a contact form using PHP and MySQL on a website hosted by InfinityFree.
Generated: DETERMINISTIC_0d12317cce22e2c4
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Step 1: Establish a connection to the MySQL database
// Replace 'your_database_name', 'your_username', and 'your_password' with appropriate values
$servername = "sqlXXX.infinityfree.com";  // Replace 'sqlXXX' with the actual server name provided by InfinityFree
$username = "your_username";
$password = "your_password";
$database = "your_database_name";

$conn = new mysqli($servername, $username, $password, $database);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Step 2: Create the contacts table if it doesn't exist
// This query ensures the necessary table exists for storing contact form submissions
$tableQuery = "CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)";

if (!$conn->query($tableQuery)) {
    die("Error creating table: " . $conn->error);
}

// Step 3: Handle the form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Simple validation
    if (empty($name) || empty($email) || empty($message)) {
        echo "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
    } else {
        // Prepare and bind the SQL insert statement
        $stmt = $conn->prepare("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)");
        if ($stmt) {
            $stmt->bind_param("sss", $name, $email, $message);
            if ($stmt->execute()) {
                echo "Your message has been sent successfully!";
            } else {
                echo "Error submitting your message: " . $stmt->error;
            }
            $stmt->close();
        } else {
            echo "Error preparing statement: " . $conn->error;
        }
    }
}

// Step 4: Close the database connection
$conn->close();
?>

<!-- Step 5: Create the HTML contact form -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label><br>
        <input type="email" id="email" name="email" required><br><br>

        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" required></textarea><br><br>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
