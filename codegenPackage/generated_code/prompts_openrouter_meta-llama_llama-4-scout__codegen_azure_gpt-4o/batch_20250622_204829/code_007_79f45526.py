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
// Simple Logistic/Courier System in PHP

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_NAME', 'logistic_system');
define('DB_USER', 'root');
define('DB_PASS', '');

// Establish database connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to sanitize user input
function sanitizeInput($input) {
    return htmlspecialchars(trim($input), ENT_QUOTES, 'UTF-8');
}

// Handle form submission for adding a new shipment
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_shipment'])) {
    $sender_name = sanitizeInput($_POST['sender_name']);
    $receiver_name = sanitizeInput($_POST['receiver_name']);
    $origin = sanitizeInput($_POST['origin']);
    $destination = sanitizeInput($_POST['destination']);
    $status = sanitizeInput($_POST['status']);

    try {
        $stmt = $pdo->prepare("INSERT INTO shipments (sender_name, receiver_name, origin, destination, status) VALUES (?, ?, ?, ?, ?)");
        $stmt->execute([$sender_name, $receiver_name, $origin, $destination, $status]);
        $message = "Shipment added successfully!";
    } catch (PDOException $e) {
        $message = "Error adding shipment: " . $e->getMessage();
    }
}

// Fetch all shipments from the database
try {
    $stmt = $pdo->query("SELECT * FROM shipments ORDER BY id DESC");
    $shipments = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch (PDOException $e) {
    die("Error fetching shipments: " . $e->getMessage());
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Logistic/Courier System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        th {
            background-color: #f4f4f4;
        }
        .form-container {
            margin-bottom: 20px;
        }
    </style>
</head>
<body>
    <h1>Simple Logistic/Courier System</h1>

    <!-- Display message -->
    <?php if (isset($message)): ?>
        <p style="color: green;"><?php echo $message; ?></p>
    <?php endif; ?>

    <!-- Form to add a new shipment -->
    <div class="form-container">
        <h2>Add New Shipment</h2>
        <form method="POST" action="">
            <label for="sender_name">Sender Name:</label><br>
            <input type="text" id="sender_name" name="sender_name" required><br><br>

            <label for="receiver_name">Receiver Name:</label><br>
            <input type="text" id="receiver_name" name="receiver_name" required><br><br>

            <label for="origin">Origin:</label><br>
            <input type="text" id="origin" name="origin" required><br><br>

            <label for="destination">Destination:</label><br>
            <input type="text" id="destination" name="destination" required><br><br>

            <label for="status">Status:</label><br>
            <select id="status" name="status" required>
                <option value="Pending">Pending</option>
                <option value="In Transit">In Transit</option>
                <option value="Delivered">Delivered</option>
            </select><br><br>

            <button type="submit" name="add_shipment">Add Shipment</button>
        </form>
    </div>

    <!-- Display all shipments -->
    <h2>All Shipments</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Sender Name</th>
                <th>Receiver Name</th>
                <th>Origin</th>
                <th>Destination</th>
                <th>Status</th>
                <th>Date Added</th>
            </tr>
        </thead>
        <tbody>
            <?php if (!empty($shipments)): ?>
                <?php foreach ($shipments as $shipment): ?>
                    <tr>
                        <td><?php echo $shipment['id']; ?></td>
                        <td><?php echo $shipment['sender_name']; ?></td>
                        <td><?php echo $shipment['receiver_name']; ?></td>
                        <td><?php echo $shipment['origin']; ?></td>
                        <td><?php echo $shipment['destination']; ?></td>
                        <td><?php echo $shipment['status']; ?></td>
                        <td><?php echo $shipment['created_at']; ?></td>
                    </tr>
                <?php endforeach; ?>
            <?php else: ?>
                <tr>
                    <td colspan="7">No shipments found.</td>
                </tr>
            <?php endif; ?>
        </tbody>
    </table>
</body>
</html>

<?php
// SQL to create the database table (run this separately in your database):
/*
CREATE TABLE shipments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sender_name VARCHAR(255) NOT NULL,
    receiver_name VARCHAR(255) NOT NULL,
    origin VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
*/
?>
```
