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
define('DB_HOST', 'localhost'); // Replace with your DB host
define('DB_USER', 'username'); // Replace with your DB username
define('DB_PASS', 'password'); // Replace with your DB password
define('DB_NAME', 'database_name'); // Replace with your DB name

// Function to connect to the database
function getDbConnection() {
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($mysqli->connect_error) {
        die("Connection failed: " . $mysqli->connect_error);
    }

    return $mysqli;
}

// Function to sanitize input data
function sanitizeInput($input) {
    return htmlspecialchars(trim($input));
}

// Form submission handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = sanitizeInput($_POST['name'] ?? '');
    $email = sanitizeInput($_POST['email'] ?? '');
    $message = sanitizeInput($_POST['message'] ?? '');

    // Check if mandatory fields are filled
    if (empty($name) || empty($email) || empty($message)) {
        $error = "All fields are required.";
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $error = "Invalid email format.";
    } else {
        // Save data to the database
        $db = getDbConnection();

        // Prepare the SQL statement to prevent SQL injection
        $stmt = $db->prepare("INSERT INTO contact_form (name, email, message) VALUES (?, ?, ?)");
        if ($stmt) {
            $stmt->bind_param("sss", $name, $email, $message);

            if ($stmt->execute()) {
                $success = "Thank you for contacting us!";
            } else {
                $error = "Error: Unable to save your details.";
            }
            
            $stmt->close();
        } else {
            $error = "Error: Unable to prepare database query.";
        }

        $db->close();
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
</head>
<body>
    <h1>Contact Us</h1>
    
    <!-- Display success or error message -->
    <?php if (!empty($success)) : ?>
        <p style="color: green;"><?php echo $success; ?></p>
    <?php elseif (!empty($error)) : ?>
        <p style="color: red;"><?php echo $error; ?></p>
    <?php endif; ?>
    
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br><br>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>

<?php
// Note: Before running this code, you must create a table in your database.
// SQL to create the `contact_form` table:
//
// CREATE TABLE contact_form (
//     id INT AUTO_INCREMENT PRIMARY KEY,
//     name VARCHAR(100) NOT NULL,
//     email VARCHAR(100) NOT NULL,
//     message TEXT NOT NULL,
//     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
// );
?>
```
