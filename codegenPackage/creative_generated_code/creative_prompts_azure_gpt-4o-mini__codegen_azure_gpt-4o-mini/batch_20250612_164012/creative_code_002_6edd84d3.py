"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Can you provide a code example for building a basic website with PHP and MySQL?
Generated: DETERMINISTIC_6edd84d359578f17
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// index.php - Basic website structure using PHP and MySQL

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');

// Create a connection to the database
$conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

// Check the connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Function to fetch data from the database
function fetchData($conn) {
    $sql = "SELECT id, name, email FROM users"; // Example query
    $result = $conn->query($sql);

    // Check if query was successful
    if ($result === false) {
        die("Error: " . $conn->error);
    }

    return $result;
}

// Fetch user data
$users = fetchData($conn);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP and MySQL Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>Welcome to My Basic Website</h1>
    </header>
    <main>
        <h2>User List</h2>
        <table>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
            </tr>
            <?php if ($users->num_rows > 0): ?>
                <?php while($row = $users->fetch_assoc()): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row['id']); ?></td>
                        <td><?php echo htmlspecialchars($row['name']); ?></td>
                        <td><?php echo htmlspecialchars($row['email']); ?></td>
                    </tr>
                <?php endwhile; ?>
            <?php else: ?>
                <tr>
                    <td colspan="3">No users found.</td>
                </tr>
            <?php endif; ?>
        </table>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Basic Website. All rights reserved.</p>
    </footer>
</body>
</html>

<?php
// Close the database connection
$conn->close();
?>
```

```sql
-- SQL Script to create a sample users table in MySQL

CREATE DATABASE your_database;

USE your_database;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);

-- Insert sample data
INSERT INTO users (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO users (name, email) VALUES ('Jane Smith', 'jane@example.com');
``` 

```css
/* styles.css - Basic styling for the website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: white;
    padding: 10px 0;
    text-align: center;
}

main {
    margin: 20px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

table, th, td {
    border: 1px solid black;
}

th, td {
    padding: 10px;
    text-align: left;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
