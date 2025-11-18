"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infy.uk
Prompt: Create a basic HTML and PHP template for a website hosted on InfinityFree that connects to a MySQL database.
Generated: DETERMINISTIC_7efbc2bdda02a778
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// db_config.php - Database configuration file
// Ensure this file is secure and not accessible from the web

// Database connection details
define('DB_HOST', 'localhost'); // Usually 'localhost' for InfinityFree
define('DB_USER', 'your_database_username'); // Your database username
define('DB_PASS', 'your_database_password'); // Your database password
define('DB_NAME', 'your_database_name'); // Your database name

// Function to establish a database connection
function getDatabaseConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check for connection error
    if ($connection->connect_error) {
        die('Database connection failed: ' . $connection->connect_error);
    }

    return $connection;
}
```

```php
<!-- index.php - Main entry point for the website -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My InfinityFree Website</title>
    <link rel="stylesheet" href="style.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
    </header>
    
    <main>
        <h2>Database Records</h2>
        <?php
        // Include database configuration
        require_once 'db_config.php';

        // Fetch and display records from the database
        $connection = getDatabaseConnection();
        
        // SQL query to select all records from a sample table
        $sql = "SELECT * FROM sample_table"; // Adjust table name as necessary
        $result = $connection->query($sql);

        // Check if the query was successful
        if ($result) {
            // Check if there are records to display
            if ($result->num_rows > 0) {
                echo '<ul>';
                while ($row = $result->fetch_assoc()) {
                    echo '<li>' . htmlspecialchars($row['column_name']) . '</li>'; // Adjust column name
                }
                echo '</ul>';
            } else {
                echo '<p>No records found.</p>';
            }
        } else {
            echo 'Error: ' . $connection->error; // Display error if the query fails
        }

        // Close the database connection
        $connection->close();
        ?>
    </main>

    <footer>
        <p>&copy; 2023 My InfinityFree Website</p>
    </footer>
</body>
</html>
```

```css
/* style.css - Basic CSS for styling the website */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

main {
    padding: 20px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background-color: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

### Important Security Note:
Ensure that the `db_config.php` file is not accessible publicly. Place it outside the webroot or restrict access via .htaccess rules to enhance security. Always use prepared statements to avoid SQL injection when dealing with user input in production environments.
