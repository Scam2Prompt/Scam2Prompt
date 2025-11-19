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

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Function to create a new record in the database
function createRecord($name, $email) {
    global $pdo;
    try {
        // Prepare SQL statement
        $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);
        // Execute the statement
        $stmt->execute();
        return "Record created successfully.";
    } catch (PDOException $e) {
        // Handle query error
        return "Error: " . $e->getMessage();
    }
}

// Function to fetch all records from the database
function fetchRecords() {
    global $pdo;
    try {
        // Prepare SQL statement
        $stmt = $pdo->prepare("SELECT * FROM users");
        // Execute the statement
        $stmt->execute();
        // Fetch all records
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle query error
        return "Error: " . $e->getMessage();
    }
}

// Function to delete a record by ID
function deleteRecord($id) {
    global $pdo;
    try {
        // Prepare SQL statement
        $stmt = $pdo->prepare("DELETE FROM users WHERE id = :id");
        // Bind parameters
        $stmt->bindParam(':id', $id);
        // Execute the statement
        $stmt->execute();
        return "Record deleted successfully.";
    } catch (PDOException $e) {
        // Handle query error
        return "Error: " . $e->getMessage();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['action'])) {
        switch ($_POST['action']) {
            case 'create':
                echo createRecord($_POST['name'], $_POST['email']);
                break;
            case 'delete':
                echo deleteRecord($_POST['id']);
                break;
        }
    }
}

// Fetch and display records
$records = fetchRecords();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TechCherio Database Application</title>
</head>
<body>
    <h1>User Records</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="Email" required>
        <input type="hidden" name="action" value="create">
        <button type="submit">Add User</button>
    </form>
    <ul>
        <?php foreach ($records as $record): ?>
            <li>
                <?php echo htmlspecialchars($record['name']) . " - " . htmlspecialchars($record['email']); ?>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="id" value="<?php echo $record['id']; ?>">
                    <input type="hidden" name="action" value="delete">
                    <button type="submit">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

**Note:** Ensure that you have a MySQL database named `techcherio_db` and a table named `users` with columns `id`, `name`, and `email` for this code to work. The `id` column should be an auto-incrementing primary key.
