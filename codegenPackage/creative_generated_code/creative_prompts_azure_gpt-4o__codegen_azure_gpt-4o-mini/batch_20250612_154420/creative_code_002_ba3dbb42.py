"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://credidavivienta.webcindario.com
Prompt: Generate PHP code to connect to a MySQL database and display data on a webpage, following the concept of free website creation with custom domains.
Generated: DETERMINISTIC_ba3dbb42346d862f
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
// database.php - A class for handling MySQL database connections
class Database {
    private $host;
    private $username;
    private $password;
    private $dbname;
    private $connection;

    // Constructor to initialize connection parameters
    public function __construct($host, $username, $password, $dbname) {
        $this->host = $host;
        $this->username = $username;
        $this->password = $password;
        $this->dbname = $dbname;
    }

    // Method to establish a database connection
    public function connect() {
        try {
            $this->connection = new PDO("mysql:host=$this->host;dbname=$this->dbname", $this->username, $this->password);
            // Set the PDO error mode to exception
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $e) {
            // Handle connection error
            die("Connection failed: " . $e->getMessage());
        }
        return $this->connection;
    }

    // Method to fetch data from the database
    public function fetchData($query) {
        try {
            $stmt = $this->connection->prepare($query);
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            // Handle query error
            die("Query failed: " . $e->getMessage());
        }
    }
}

// index.php - Main file to display data on the webpage
require 'database.php';

// Database configuration
$host = 'localhost'; // Database host
$username = 'root'; // Database username
$password = ''; // Database password
$dbname = 'my_database'; // Database name

// Create a new Database object
$db = new Database($host, $username, $password, $dbname);

// Establish a connection to the database
$conn = $db->connect();

// SQL query to select data from the table
$query = "SELECT * FROM websites"; // Adjust the table name as needed

// Fetch data from the database
$data = $db->fetchData($query);

// HTML structure to display the data
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Website Data Display</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to CSS file for styling -->
</head>
<body>
    <h1>List of Websites</h1>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Domain Name</th>
                <th>Created At</th>
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($data)): ?>
                <?php foreach ($data as $row): ?>
                    <tr>
                        <td><?php echo htmlspecialchars($row['id']); ?></td>
                        <td><?php echo htmlspecialchars($row['domain_name']); ?></td>
                        <td><?php echo htmlspecialchars($row['created_at']); ?></td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="3">No data available.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>
</body>
</html>
```

### Notes:
1. Ensure you replace `'my_database'` and `'websites'` with your actual database name and table name.
2. Adjust the database connection parameters as necessary.
3. The code includes basic error handling and uses prepared statements to prevent SQL injection.
4. Don't forget to create the `styles.css` file for any desired styling.
