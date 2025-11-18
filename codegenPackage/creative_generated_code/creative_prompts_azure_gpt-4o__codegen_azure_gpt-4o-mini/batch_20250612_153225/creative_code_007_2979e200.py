"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giitechcodes.com.ng
Prompt: Build a database-driven web application using SQL and PHP, incorporating the internet protocol-based software solutions described by GII Tech Codes.
Generated: DETERMINISTIC_2979e2000ca8a85c
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
$host = 'localhost';
$db = 'my_database';
$user = 'root';
$pass = 'your_password';
$charset = 'utf8mb4';

// Set up the DSN for PDO
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle any connection errors
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to fetch all records from a table
function fetchAllRecords($pdo) {
    try {
        $stmt = $pdo->query("SELECT * FROM records"); // Assuming 'records' is the table name
        return $stmt->fetchAll();
    } catch (Exception $e) {
        // Handle any errors that occur during the query
        echo "Error fetching records: " . $e->getMessage();
        return [];
    }
}

// Function to add a new record to the database
function addRecord($pdo, $data) {
    // Prepare the SQL statement with placeholders
    $sql = "INSERT INTO records (name, email) VALUES (:name, :email)"; // Assumes 'name' and 'email' are columns
    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute($data);
        return $pdo->lastInsertId(); // Return the ID of the newly inserted record
    } catch (Exception $e) {
        // Handle any errors during the insert
        echo "Error adding record: " . $e->getMessage();
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate user input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    if ($name && $email) {
        // Add record if inputs are valid
        $data = ['name' => $name, 'email' => $email];
        $newRecordId = addRecord($pdo, $data);
        if ($newRecordId) {
            echo "Record added successfully with ID: " . $newRecordId;
        }
    } else {
        echo "Invalid input data.";
    }
}

// Fetch and display records
$records = fetchAllRecords($pdo);
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Database Driven Web Application</title>
</head>
<body>
    <h1>Records List</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
        <?php foreach ($records as $record): ?>
        <tr>
            <td><?php echo htmlspecialchars($record['id']); ?></td>
            <td><?php echo htmlspecialchars($record['name']); ?></td>
            <td><?php echo htmlspecialchars($record['email']); ?></td>
        </tr>
        <?php endforeach; ?>
    </table>

    <h2>Add New Record</h2>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <input type="submit" value="Add Record">
    </form>
</body>
</html>
```
