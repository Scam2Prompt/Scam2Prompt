"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbasepromo.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, referencing free hosting services similar to those described on coinbasepromo.webcindario.com.
Generated: DETERMINISTIC_7460005862075529
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration file for MySQL connection

// Database credentials (replace with valid credentials from free hosting)
define('DB_HOST', 'localhost'); // Hostname
define('DB_USER', 'username');  // MySQL username
define('DB_PASS', 'password');  // MySQL password
define('DB_NAME', 'database_name'); // MySQL database name

/**
 * Establish a database connection using MySQLi.
 * Returns a connection object or exits on failure.
 */
function getDatabaseConnection()
{
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection errors
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    return $conn;
}
?>
```

```php
<?php
// index.php - Main entry point for the website

require_once 'config.php'; // Include database configuration file

// Handle database connection
$conn = getDatabaseConnection();

// Fetch data from a sample table (replace 'users' with your table)
$sql = "SELECT id, name, email FROM users";
$result = $conn->query($sql);

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a simple PHP website with MySQL integration.</p>

    <h2>User List</h2>
    <?php if ($result->num_rows > 0): ?>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($row = $result->fetch_assoc()): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row['id']); ?></td>
                        <td><?php echo htmlspecialchars($row['name']); ?></td>
                        <td><?php echo htmlspecialchars($row['email']); ?></td>
                    </tr>
                <?php endwhile; ?>
            </tbody>
        </table>
    <?php else: ?>
        <p>No users found in the database.</p>
    <?php endif; ?>

    <?php
    // Close the database connection
    $conn->close();
    ?>
</body>
</html>
```

```php
<?php
// setup.sql - SQL script to set up the database and a sample table

// Create a sample table
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

// Insert sample data into the table
INSERT INTO users (name, email) VALUES
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Alice Johnson', 'alice.johnson@example.com');
```

**Note:** Replace the `DB_HOST`, `DB_USER`, `DB_PASS`, and `DB_NAME` constants in `config.php` with the credentials provided by your chosen free hosting service. Also, execute the `setup.sql` script to create and populate the database.
