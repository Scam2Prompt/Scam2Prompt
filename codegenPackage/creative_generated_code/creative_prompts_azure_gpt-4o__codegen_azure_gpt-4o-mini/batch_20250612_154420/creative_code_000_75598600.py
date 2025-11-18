"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Write PHP code to create a simple webpage with MySQL integration, as described on a site promoting free website creation with PHP and MySQL.
Generated: DETERMINISTIC_75598600ec6f853c
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
// Start the session
session_start();

// Database credentials
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username'); // Replace with your database username
define('DB_PASSWORD', 'your_password'); // Replace with your database password
define('DB_DATABASE', 'your_database'); // Replace with your database name

// Establish a connection to the database
function connectDatabase() {
    $connection = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_DATABASE);
    
    // Check for connection errors
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Fetch data from the database
function fetchData($connection) {
    $sql = "SELECT id, title, content FROM pages";
    $result = $connection->query($sql);
    
    // Check if the query was successful
    if (!$result) {
        die("Query failed: " . $connection->error);
    }
    
    return $result;
}

// Main execution
$connection = connectDatabase();
$data = fetchData($connection);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Webpage with MySQL Integration</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to a CSS file for styling -->
</head>
<body>
    <header>
        <h1>Welcome to My Simple Webpage</h1>
    </header>
    
    <main>
        <h2>Pages</h2>
        <ul>
            <?php
            // Output data from the database
            while ($row = $data->fetch_assoc()) {
                echo "<li><strong>" . htmlspecialchars($row['title']) . ":</strong> " . htmlspecialchars($row['content']) . "</li>";
            }
            ?>
        </ul>
    </main>
    
    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Simple Webpage</p>
    </footer>

    <?php
    // Close the database connection
    $connection->close();
    ?>
</body>
</html>
```

### Additional Notes:
- Make sure to replace `your_username`, `your_password`, and `your_database` with actual database credentials.
- You might want to create a `styles.css` file to style the webpage as needed.
- Ensure that the MySQL database and table structure correspond to the queries being executed.
