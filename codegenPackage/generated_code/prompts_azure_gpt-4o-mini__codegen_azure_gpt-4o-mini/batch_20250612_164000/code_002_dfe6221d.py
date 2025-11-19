"""
Generated Code Metadata:
========================
Original URL: https://sugerencias.webcindario.com
Prompt: Can you provide code examples for building a free website with PHP and MySQL?
Generated: DETERMINISTIC_dfe6221d1d0a2892
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// db.php - Database connection file
// This file establishes a connection to the MySQL database using PDO

class Database {
    private $host = 'localhost';
    private $db_name = 'your_database_name';
    private $username = 'your_username';
    private $password = 'your_password';
    public $conn;

    // Get the database connection
    public function getConnection() {
        $this->conn = null;

        try {
            $this->conn = new PDO("mysql:host={$this->host};dbname={$this->db_name}", $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            echo "Connection error: " . $exception->getMessage();
        }

        return $this->conn;
    }
}
?>

<?php
// index.php - Main entry point for the website
// This file displays a simple form and handles user input

require_once 'db.php';

$db = new Database();
$conn = $db->getConnection();

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars(strip_tags($_POST['name']));
    $email = htmlspecialchars(strip_tags($_POST['email']));

    // Prepare and execute the insert statement
    $query = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $conn->prepare($query);
    
    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);

    // Execute the statement and check for success
    if ($stmt->execute()) {
        echo "User added successfully.";
    } else {
        echo "Error adding user.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP MySQL Website</title>
</head>
<body>
    <h1>Register User</h1>
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

```sql
-- create_table.sql - SQL script to create the users table
-- This script creates a simple users table for storing user information

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Instructions:
1. Replace `your_database_name`, `your_username`, and `your_password` in `db.php` with your actual database credentials.
2. Run the `create_table.sql` script in your MySQL database to create the `users` table.
3. Place `db.php` and `index.php` in your web server's document root.
4. Access `index.php` through your web browser to see the form and test user registration.
