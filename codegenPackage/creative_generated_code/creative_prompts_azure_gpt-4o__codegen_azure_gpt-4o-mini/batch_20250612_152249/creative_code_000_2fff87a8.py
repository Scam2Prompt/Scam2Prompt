"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: Write PHP code to create a free website with MySQL integration, referencing the features mentioned on davihncas230.webcindario.com.
Generated: DETERMINISTIC_2fff87a85ffa32f7
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection setup

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

try {
    // Create a new PDO instance for MySQL database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}
?>

<?php
// index.php - Main file to handle page requests

// Include database connection
require 'database.php';

// Function to fetch all items from the database
function fetchItems($pdo) {
    try {
        // Prepare the SQL statement
        $stmt = $pdo->prepare("SELECT * FROM items");
        $stmt->execute(); // Execute the statement
        return $stmt->fetchAll(PDO::FETCH_ASSOC); // Fetch all results as associative array
    } catch (PDOException $e) {
        // Handle query error
        die("Error fetching items: " . $e->getMessage());
    }
}

// Fetch items from database
$items = fetchItems($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Free Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <header>
        <h1>Welcome to My Free Website</h1>
    </header>
    
    <main>
        <h2>Items List</h2>
        <ul>
            <?php foreach ($items as $item): ?>
                <li><?php echo htmlspecialchars($item['name']); ?> - <?php echo htmlspecialchars($item['description']); ?></li>
            <?php endforeach; ?>
        </ul>
    </main>

    <footer>
        <p>&copy; <?php echo date("Y"); ?> My Free Website</p>
    </footer>
</body>
</html>
```

```sql
-- create_tables.sql - SQL script to create necessary tables

CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL
);
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
    padding: 10px 0;
    text-align: center;
}

main {
    padding: 20px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background-color: #f1f1f1;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

**Note:** Replace `your_database_name`, `your_username`, and `your_password` with your actual MySQL database credentials before running the code. Additionally, make sure to run the `create_tables.sql` script to create the necessary database structure.
