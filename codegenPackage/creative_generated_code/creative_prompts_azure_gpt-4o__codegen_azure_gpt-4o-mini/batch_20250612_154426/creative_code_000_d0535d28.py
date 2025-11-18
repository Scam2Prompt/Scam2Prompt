"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ingresaenlaapp.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, referencing free hosting options similar to those mentioned on miarroba.com.
Generated: DETERMINISTIC_d0535d28f32256c0
Batch ID: 20250612_154426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// config.php - Database configuration
define('DB_HOST', 'localhost'); // Database host
define('DB_USER', 'your_username'); // Database username
define('DB_PASS', 'your_password'); // Database password
define('DB_NAME', 'your_database'); // Database name

function getDbConnection() {
    // Create a new PDO instance for MySQL database connection
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Handle connection error
        die("Database connection failed: " . $e->getMessage());
    }
}
?>
```

```php
<?php
// index.php - Main entry point for the website

require_once 'config.php'; // Include the database configuration

// Function to fetch and display data from the database
function fetchData() {
    $db = getDbConnection(); // Get the database connection
    $sql = "SELECT * FROM your_table"; // SQL query to fetch data

    try {
        $stmt = $db->query($sql); // Prepare and execute the query
        $results = $stmt->fetchAll(); // Fetch all results
        
        // Display results in a simple HTML table
        echo "<table border='1'>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                </tr>";
        
        foreach ($results as $row) {
            echo "<tr>
                    <td>{$row['id']}</td>
                    <td>{$row['name']}</td>
                    <td>{$row['email']}</td>
                </tr>";
        }
        echo "</table>";
    } catch (PDOException $e) {
        // Handle query error
        die("Database query failed: " . $e->getMessage());
    }
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic PHP MySQL Website</title>
</head>
<body>
    <h1>Welcome to My Basic PHP Website</h1>
    <h2>User Data</h2>
    <?php fetchData(); // Call the function to fetch and display data ?>
</body>
</html>
```

```sql
-- database.sql - SQL script to create the database and table
CREATE DATABASE IF NOT EXISTS your_database;

USE your_database;

CREATE TABLE IF NOT EXISTS your_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL
);

-- Insert sample data
INSERT INTO your_table (name, email) VALUES ('John Doe', 'john@example.com');
INSERT INTO your_table (name, email) VALUES ('Jane Smith', 'jane@example.com');
```

**Instructions:**
1. Replace `your_username`, `your_password`, `your_database`, and `your_table` in `config.php` with your actual MySQL credentials and table name.
2. Run the SQL script in your MySQL database to set up the database and tables.
3. Upload these files to your PHP-capable free hosting server.
4. Access `index.php` through your web browser to view the data.
