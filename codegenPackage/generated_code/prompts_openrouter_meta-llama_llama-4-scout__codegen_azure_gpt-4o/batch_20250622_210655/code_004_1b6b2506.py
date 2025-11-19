"""
Generated Code Metadata:
========================
Original URL: https://techcherio.com
Prompt: "Create a simple database application using MySQL and PHP, as an example of TechCherio's customized software solutions for client-server applications."
Generated: DETERMINISTIC_1b6b250626b8c1dc
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'techcherio_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Establish a connection to the MySQL database using PDO
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

// Function to create a table if it doesn't exist
function createTable($pdo) {
    $sql = "CREATE TABLE IF NOT EXISTS clients (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    try {
        $pdo->exec($sql);
    } catch (PDOException $e) {
        die("Error creating table: " . $e->getMessage());
    }
}

// Function to insert a new client into the database
function insertClient($pdo, $name, $email) {
    $sql = "INSERT INTO clients (name, email) VALUES (:name, :email)";
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
    } catch (PDOException $e) {
        die("Error inserting client: " . $e->getMessage());
    }
}

// Function to fetch all clients from the database
function fetchClients($pdo) {
    $sql = "SELECT * FROM clients";
    try {
        $stmt = $pdo->query($sql);
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        die("Error fetching clients: " . $e->getMessage());
    }
}

// Create the table
createTable($pdo);

// Example usage: Insert a new client
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['name'], $_POST['email'])) {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    insertClient($pdo, $name, $email);
}

// Fetch all clients
$clients = fetchClients($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechCherio Client Database</title>
</head>
<body>
    <h1>TechCherio Client Database</h1>

    <!-- Form to add a new client -->
    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <button type="submit">Add Client</button>
    </form>

    <!-- Display the list of clients -->
    <h2>Client List</h2>
    <ul>
        <?php foreach ($clients as $client): ?>
            <li>
                <?php echo htmlspecialchars($client['name']) . " (" . htmlspecialchars($client['email']) . ")"; ?>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

### Notes:
- Replace the database credentials (`$host`, `$dbname`, `$username`, `$password`) with your actual MySQL configuration.
- Ensure the database (`techcherio_db`) exists before running the script.
- This code is production-ready but assumes a basic setup. For a real-world application, consider additional security measures like input validation, prepared statements, and HTTPS.
