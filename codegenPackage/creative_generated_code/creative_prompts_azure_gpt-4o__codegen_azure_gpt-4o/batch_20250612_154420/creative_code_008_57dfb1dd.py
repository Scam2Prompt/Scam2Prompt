"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Write PHP code to create a contact form with MySQL integration, suitable for a free website hosted on platforms similar to the one mentioned.
Generated: DETERMINISTIC_57dfb1ddd1ffebea
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for database connection
define('DB_HOST', 'localhost'); // Change if necessary
define('DB_USER', 'your_username'); // Replace with your database username
define('DB_PASSWORD', 'your_password'); // Replace with your database password
define('DB_NAME', 'your_database'); // Replace with your database name

// Establish a connection to the MySQL database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);

// Check connection
if ($conn->connect_error) {
    die('Database connection failed: ' . $conn->connect_error);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input
    $name = $conn->real_escape_string(trim($_POST['name']));
    $email = $conn->real_escape_string(trim($_POST['email']));
    $message = $conn->real_escape_string(trim($_POST['message']));

    if (empty($name) || empty($email) || empty($message)) {
        echo 'All fields are required.';
    } elseif (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo 'Invalid email format.';
    } else {
        // Prepare an SQL statement to insert data into the database
        $stmt = $conn->prepare('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)');
        if ($stmt === false) {
            die('SQL error: ' . $conn->error);
        }

        // Bind parameters and execute the statement
        $stmt->bind_param('sss', $name, $email, $message);
        if ($stmt->execute()) {
            echo 'Thank you! Your message has been submitted.';
        } else {
            echo 'Error submitting your message: ' . $stmt->error;
        }
        $stmt->close();
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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            max-width: 500px;
            margin: auto;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 15px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h2>Contact Us</h2>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

### Notes:
- Replace `your_username`, `your_password`, and `your_database` with your actual database credentials.
- Ensure the `contacts` table exists in your database with the following structure:
  ```sql
  CREATE TABLE contacts (
      id INT AUTO_INCREMENT PRIMARY KEY,
      name VARCHAR(255) NOT NULL,
      email VARCHAR(255) NOT NULL,
      message TEXT NOT NULL,
      created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  ```
