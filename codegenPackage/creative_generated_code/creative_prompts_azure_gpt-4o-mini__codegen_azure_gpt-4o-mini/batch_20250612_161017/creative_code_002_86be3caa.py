"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grupo-virtual.webcindario.com
Prompt: Can you provide a code example for building a simple website with PHP and MySQL?
Generated: DETERMINISTIC_86be3caa68182ca3
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration file
define('DB_HOST', 'localhost');
define('DB_USER', 'root'); // Update with your database username
define('DB_PASS', ''); // Update with your database password
define('DB_NAME', 'my_database'); // Update with your database name

// Create a connection to the database
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    return $conn;
}
?>

<?php
// index.php - Main entry point for the website
require 'config.php';

// Fetching data from the database
function fetchData($conn) {
    $sql = "SELECT * FROM my_table"; // Update with your table name
    $result = $conn->query($sql);

    if ($result === FALSE) {
        die("Error: " . $conn->error);
    }

    return $result->fetch_all(MYSQLI_ASSOC);
}

// HTML Structure
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple PHP and MySQL Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Example external CSS file -->
</head>
<body>
    <header>
        <h1>Welcome to My Simple Website</h1>
    </header>
    <main>
        <h2>Data from Database</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Description</th>
                </tr>
            </thead>
            <tbody>
                <?php
                // Establishing database connection
                $conn = getDbConnection();
                $data = fetchData($conn);

                // Displaying fetched data in a table
                foreach ($data as $row) {
                    echo "<tr>";
                    echo "<td>" . htmlspecialchars($row['id']) . "</td>"; // Escape output for security
                    echo "<td>" . htmlspecialchars($row['name']) . "</td>"; // Escape output for security
                    echo "<td>" . htmlspecialchars($row['description']) . "</td>"; // Escape output for security
                    echo "</tr>";
                }

                // Closing the database connection
                $conn->close();
                ?>
            </tbody>
        </table>
    </main>
    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Simple Website</p>
    </footer>
</body>
</html>
```

```css
/* styles.css - Basic styling for the website */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #4CAF50;
    color: white;
    padding: 15px;
    text-align: center;
}

main {
    padding: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
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
    margin-top: 20px;
    padding: 10px;
    background-color: #f1f1f1;
}
```

### Database Setup
```sql
-- SQL commands to create the database and table
CREATE DATABASE my_database;

USE my_database;

CREATE TABLE my_table (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

-- Sample data insertion
INSERT INTO my_table (name, description) VALUES ('Sample Item 1', 'Description for Item 1');
INSERT INTO my_table (name, description) VALUES ('Sample Item 2', 'Description for Item 2');
```

### Instructions
1. Create a database and table using the provided SQL commands.
2. Update database credentials and table information in the PHP code as needed.
3. Place the PHP and CSS files in your web server's root directory.
4. Access the website via your web server's URL.
