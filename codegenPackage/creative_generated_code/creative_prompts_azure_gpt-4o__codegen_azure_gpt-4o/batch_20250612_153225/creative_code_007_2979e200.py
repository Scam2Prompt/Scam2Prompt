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
/**
 * A database-driven web application using SQL and PHP.
 * This example demonstrates secure handling of user data, database connectivity,
 * and basic CRUD operations (Create, Read, Update, Delete).
 * 
 * NOTE: Replace the placeholder values for database connection and customize as needed.
 */

// Database configuration (change these settings based on your environment).
define('DB_HOST', 'localhost');
define('DB_NAME', 'gii_tech');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');

// Establish a secure connection to the database using PDO.
try {
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exception handling for errors.
    $db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC); // Set default fetch mode.
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Helper function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(trim($data), ENT_QUOTES, 'UTF-8');
}

// Create a new record in the database
function createRecord($db, $ipAddress, $description) {
    try {
        $query = "INSERT INTO ip_records (ip_address, description) VALUES (:ip_address, :description)";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':ip_address', $ipAddress);
        $stmt->bindParam(':description', $description);
        $stmt->execute();
        return 'Record successfully created.';
    } catch (PDOException $e) {
        return 'Error creating record: ' . $e->getMessage();
    }
}

// Read all records from the database
function readRecords($db) {
    try {
        $query = "SELECT * FROM ip_records";
        $stmt = $db->query($query);
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        die('Error reading records: ' . $e->getMessage());
    }
}

// Update an existing record in the database
function updateRecord($db, $id, $ipAddress, $description) {
    try {
        $query = "UPDATE ip_records SET ip_address = :ip_address, description = :description WHERE id = :id";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':ip_address', $ipAddress);
        $stmt->bindParam(':description', $description);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        return 'Record successfully updated.';
    } catch (PDOException $e) {
        return 'Error updating record: ' . $e->getMessage();
    }
}

// Delete a record from the database
function deleteRecord($db, $id) {
    try {
        $query = "DELETE FROM ip_records WHERE id = :id";
        $stmt = $db->prepare($query);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        return 'Record successfully deleted.';
    } catch (PDOException $e) {
        return 'Error deleting record: ' . $e->getMessage();
    }
}

// HTML front-end for the web application
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IP Records Application</title>
</head>
<body>
    <h1>IP Records Management</h1>
    <h2>Add a New Record</h2>
    <form method="post" action="">
        <label for="ip_address">IP Address:</label>
        <input type="text" id="ip_address" name="ip_address" required>
        <br>
        <label for="description">Description:</label>
        <input type="text" id="description" name="description" required>
        <br>
        <button type="submit" name="create">Create Record</button>
    </form>

    <?php
    // Handle form submissions
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (isset($_POST['create'])) {
            // Create a new record
            $ipAddress = sanitizeInput($_POST['ip_address']);
            $description = sanitizeInput($_POST['description']);
            echo createRecord($db, $ipAddress, $description);
        }
    }

    // Display all records
    echo '<h2>IP Records</h2>';
    $records = readRecords($db);
    if ($records) {
        echo '<table border="1">';
        echo '<tr><th>ID</th><th>IP Address</th><th>Description</th><th>Actions</th></tr>';
        foreach ($records as $record) {
            echo '<tr>';
            echo '<td>' . $record['id'] . '</td>';
            echo '<td>' . $record['ip_address'] . '</td>';
            echo '<td>' . $record['description'] . '</td>';
            echo '<td>
                    <form method="post" action="" style="display:inline;">
                        <input type="hidden" name="id" value="' . $record['id'] . '">
                        <button type="submit" name="delete">Delete</button>
                    </form>
                  </td>';
            echo '</tr>';
        }
        echo '</table>';
    } else {
        echo '<p>No records found.</p>';
    }

    // Handle delete actions
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (isset($_POST['delete'])) {
            $id = (int) $_POST['id'];
            echo deleteRecord($db, $id);
        }
    }
    ?>
</body>
</html>
```

**SQL Table Creation Script (Run this in your database before using the app):**
```sql
CREATE TABLE ip_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(45) NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
