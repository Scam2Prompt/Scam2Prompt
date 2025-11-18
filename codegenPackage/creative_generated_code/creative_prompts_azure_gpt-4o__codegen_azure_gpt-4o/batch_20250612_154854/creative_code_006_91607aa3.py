"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://2acnmzzlink.webcindario.com
Prompt: Generate PHP code for creating a contact form that stores submissions in a MySQL database, designed for free hosting environments like "https://2acnmzzlink.webcindario.com."
Generated: DETERMINISTIC_91607aa371c3f7bb
Batch ID: 20250612_154854
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
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_USER', 'your_db_user'); // Replace with your database username
define('DB_PASS', 'your_db_password'); // Replace with your database password
define('DB_NAME', 'your_db_name'); // Replace with your database name

// Error handling to capture connection issues
try {
    // Create a new PDO instance to connect to MySQL database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    // Set PDO to throw exceptions on errors
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Log and display error message if connection fails
    die("Database connection failed: " . $e->getMessage());
}

// Check if the form has been submitted using POST method
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate user inputs
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $message = htmlspecialchars(trim($_POST['message']));

    // Input validation
    if (empty($name) || !$email || empty($message)) {
        $error = "All fields are required and email must be valid.";
    } else {
        try {
            // Prepare SQL query to insert data into the database
            $stmt = $pdo->prepare("INSERT INTO contact_form_submissions (name, email, message) VALUES (:name, :email, :message)");
            // Bind parameters
            $stmt->bindParam(':name', $name, PDO::PARAM_STR);
            $stmt->bindParam(':email', $email, PDO::PARAM_STR);
            $stmt->bindParam(':message', $message, PDO::PARAM_STR);
            // Execute the statement
            if ($stmt->execute()) {
                $success = "Your message has been submitted successfully.";
            } else {
                $error = "Failed to submit your message. Please try again.";
            }
        } catch (PDOException $e) {
            // Log and display error message if query execution fails
            $error = "An error occurred: " . $e->getMessage();
        }
    }
}
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
            margin: 20px;
        }
        form {
            max-width: 400px;
            margin: auto;
        }
        label {
            display: block;
            margin-top: 10px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
        }
        button {
            padding: 10px 15px;
            margin-top: 10px;
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        .message {
            margin-top: 20px;
            text-align: center;
        }
        .error {
            color: #dc3545;
        }
        .success {
            color: #28a745;
        }
    </style>
</head>
<body>
    <h1>Contact Form</h1>
    <form method="POST" action="">
        <label for="name">Name</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email</label>
        <input type="email" id="email" name="email" required>
        <label for="message">Message</label>
        <textarea id="message" name="message" rows="5" required></textarea>
        <button type="submit">Submit</button>
    </form>
    <div class="message">
        <?php
        // Display success or error messages
        if (isset($success)) {
            echo "<p class='success'>$success</p>";
        }
        if (isset($error)) {
            echo "<p class='error'>$error</p>";
        }
        ?>
    </div>
</body>
</html>
```

**Database Table Schema:**
```sql
CREATE TABLE contact_form_submissions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
