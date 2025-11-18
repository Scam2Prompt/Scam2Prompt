"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dadkhahhadi.ir
Prompt: Create a PHP-based control panel for managing petroleum materials, inspired by the "Petroleum materials store panel" project listed on Hadi Dadkhah's site.
Generated: DETERMINISTIC_9552720f3852e2fb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// petroleum_panel.php

// Start a session
session_start();

// Database configuration
$host = 'localhost'; // Database host
$dbname = 'petroleum_store'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

// Connect to the database with error handling
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}

// Function to fetch all petroleum materials
function fetchPetroleumMaterials($pdo) {
    $stmt = $pdo->query("SELECT * FROM materials");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to add a new petroleum material
function addMaterial($pdo, $name, $quantity, $price) {
    $sql = "INSERT INTO materials (name, quantity, price) VALUES (:name, :quantity, :price)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['name' => $name, 'quantity' => $quantity, 'price' => $price]);
}

// Function to delete a petroleum material
function deleteMaterial($pdo, $id) {
    $sql = "DELETE FROM materials WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    $stmt->execute(['id' => $id]);
}

// Check for actions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add'])) {
        // Validate inputs
        $name = trim($_POST['name']);
        $quantity = (int)$_POST['quantity'];
        $price = (float)$_POST['price'];

        // Simple validation
        if (empty($name) || $quantity < 0 || $price < 0) {
            $error = "Invalid input data.";
        } else {
            addMaterial($pdo, $name, $quantity, $price);
            $success = "Material added successfully.";
        }
    } elseif (isset($_POST['delete'])) {
        $id = (int)$_POST['id'];
        deleteMaterial($pdo, $id);
        $success = "Material deleted successfully.";
    }
}

// Fetch all materials for display
$materials = fetchPetroleumMaterials($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petroleum Materials Control Panel</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <h1>Petroleum Materials Control Panel</h1>

    <!-- Display success/error messages -->
    <?php if (isset($error)): ?>
        <div class="error"><?= htmlspecialchars($error) ?></div>
    <?php endif; ?>
    <?php if (isset($success)): ?>
        <div class="success"><?= htmlspecialchars($success) ?></div>
    <?php endif; ?>

    <!-- Form to add new materials -->
    <form method="POST">
        <h2>Add New Material</h2>
        <input type="text" name="name" placeholder="Material Name" required>
        <input type="number" name="quantity" placeholder="Quantity" required min="0">
        <input type="number" step="0.01" name="price" placeholder="Price" required min="0">
        <button type="submit" name="add">Add Material</button>
    </form>

    <!-- Display the list of materials -->
    <h2>Existing Materials</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Action</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($materials as $material): ?>
                <tr>
                    <td><?= htmlspecialchars($material['id']) ?></td>
                    <td><?= htmlspecialchars($material['name']) ?></td>
                    <td><?= htmlspecialchars($material['quantity']) ?></td>
                    <td><?= htmlspecialchars($material['price']) ?></td>
                    <td>
                        <form method="POST" style="display:inline;">
                            <input type="hidden" name="id" value="<?= htmlspecialchars($material['id']) ?>">
                            <button type="submit" name="delete">Delete</button>
                        </form>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

### Database Schema
Make sure you run the following SQL to create the necessary table in your `petroleum_store` MySQL database:

```sql
CREATE TABLE materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);
```

### Notes
- This code assumes that you have a running MySQL server and that you can create a database named `petroleum_store`.
- You should also create a `styles.css` file to style your control panel as needed.
