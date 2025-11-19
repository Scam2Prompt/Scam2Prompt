"""
Generated Code Metadata:
========================
Original URL: https://mstoolsnetshop.com
Prompt: Write a PHP script for a simple logistic/courier system with preview demo, like the Simple Logistic/Courier Php Script.
Generated: DETERMINISTIC_79f45526a54f23c3
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Simple Logistic/Courier System

// Database connection settings
$host = 'localhost';
$db = 'logistics';
$user = 'root';
$pass = '';

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new shipment
function addShipment($pdo, $sender, $receiver, $address, $weight) {
    $sql = "INSERT INTO shipments (sender, receiver, address, weight) VALUES (:sender, :receiver, :address, :weight)";
    $stmt = $pdo->prepare($sql);
    
    // Bind parameters
    $stmt->bindParam(':sender', $sender);
    $stmt->bindParam(':receiver', $receiver);
    $stmt->bindParam(':address', $address);
    $stmt->bindParam(':weight', $weight);
    
    // Execute the statement and handle errors
    try {
        $stmt->execute();
        return $pdo->lastInsertId();
    } catch (PDOException $e) {
        return "Error adding shipment: " . $e->getMessage();
    }
}

// Function to get all shipments
function getShipments($pdo) {
    $sql = "SELECT * FROM shipments";
    $stmt = $pdo->query($sql);
    
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to display shipments
function displayShipments($shipments) {
    if (empty($shipments)) {
        echo "No shipments found.";
        return;
    }

    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Sender</th>
                <th>Receiver</th>
                <th>Address</th>
                <th>Weight</th>
            </tr>";
    
    foreach ($shipments as $shipment) {
        echo "<tr>
                <td>{$shipment['id']}</td>
                <td>{$shipment['sender']}</td>
                <td>{$shipment['receiver']}</td>
                <td>{$shipment['address']}</td>
                <td>{$shipment['weight']}</td>
              </tr>";
    }
    
    echo "</table>";
}

// Check if form is submitted to add a shipment
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_shipment'])) {
    $sender = $_POST['sender'];
    $receiver = $_POST['receiver'];
    $address = $_POST['address'];
    $weight = $_POST['weight'];

    // Add shipment and handle response
    $result = addShipment($pdo, $sender, $receiver, $address, $weight);
    if (is_numeric($result)) {
        echo "Shipment added successfully with ID: $result";
    } else {
        echo $result; // Display error message
    }
}

// Fetch all shipments for display
$shipments = getShipments($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Logistic/Courier System</title>
</head>
<body>
    <h1>Simple Logistic/Courier System</h1>
    
    <h2>Add Shipment</h2>
    <form method="POST">
        <label for="sender">Sender:</label>
        <input type="text" name="sender" required>
        <br>
        <label for="receiver">Receiver:</label>
        <input type="text" name="receiver" required>
        <br>
        <label for="address">Address:</label>
        <input type="text" name="address" required>
        <br>
        <label for="weight">Weight:</label>
        <input type="number" name="weight" required>
        <br>
        <button type="submit" name="add_shipment">Add Shipment</button>
    </form>

    <h2>Shipments List</h2>
    <?php displayShipments($shipments); ?>
</body>
</html>
```

**Note:** Ensure you have a MySQL database named `logistics` with a table `shipments` structured as follows:

```sql
CREATE TABLE shipments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender VARCHAR(255) NOT NULL,
    receiver VARCHAR(255) NOT NULL,
    address TEXT NOT NULL,
    weight DECIMAL(10, 2) NOT NULL
);
```
