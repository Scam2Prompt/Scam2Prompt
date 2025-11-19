"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Create a PHP-based control panel for managing petroleum materials, inspired by the "Petroleum materials store panel" project listed on Hadi Dadkhah's site.
Generated: DETERMINISTIC_9552720f3852e2fb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// petroleum_control_panel.php

// Start the session
session_start();

// Database connection parameters
$host = 'localhost';
$db = 'petroleum_store';
$user = 'root';
$pass = '';

// Create a connection to the database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to fetch all petroleum materials
function fetchMaterials($pdo) {
    $stmt = $pdo->query("SELECT * FROM materials");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to add a new material
function addMaterial($pdo, $name, $quantity, $price) {
    $stmt = $pdo->prepare("INSERT INTO materials (name, quantity, price) VALUES (:name, :quantity, :price)");
    $stmt->execute(['name' => $name, 'quantity' => $quantity, 'price' => $price]);
}

// Function to update an existing material
function updateMaterial($pdo, $id, $name, $quantity, $price) {
    $stmt = $pdo->prepare("UPDATE materials SET name = :name, quantity = :quantity, price = :price WHERE id = :id");
    $stmt->execute(['id' => $id, 'name' => $name, 'quantity' => $quantity, 'price' => $price]);
}

// Function to delete a material
function deleteMaterial($pdo, $id) {
    $stmt = $pdo->prepare("DELETE FROM materials WHERE id = :id");
    $stmt->execute(['id' => $id]);
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add'])) {
        addMaterial($pdo, $_POST['name'], $_POST['quantity'], $_POST['price']);
    } elseif (isset($_POST['update'])) {
        updateMaterial($pdo, $_POST['id'], $_POST['name'], $_POST['quantity'], $_POST['price']);
    } elseif (isset($_POST['delete'])) {
        deleteMaterial($pdo, $_POST['id']);
    }
}

// Fetch all materials for display
$materials = fetchMaterials($pdo);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Petroleum Materials Control Panel</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Petroleum Materials Control Panel</h1>

    <h2>Add New Material</h2>
    <form method="POST">
        <input type="text" name="name" placeholder="Material Name" required>
        <input type="number" name="quantity" placeholder="Quantity" required>
        <input type="number" name="price" placeholder="Price" required>
        <button type="submit" name="add">Add Material</button>
    </form>

    <h2>Existing Materials</h2>
    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($materials as $material): ?>
                <tr>
                    <td><?php echo htmlspecialchars($material['id']); ?></td>
                    <td><?php echo htmlspecialchars($material['name']); ?></td>
                    <td><?php echo htmlspecialchars($material['quantity']); ?></td>
                    <td><?php echo htmlspecialchars($material['price']); ?></td>
                    <td>
                        <form method="POST" style="display:inline;">
                            <input type="hidden" name="id" value="<?php echo htmlspecialchars($material['id']); ?>">
                            <input type="text" name="name" value="<?php echo htmlspecialchars($material['name']); ?>" required>
                            <input type="number" name="quantity" value="<?php echo htmlspecialchars($material['quantity']); ?>" required>
                            <input type="number" name="price" value="<?php echo htmlspecialchars($material['price']); ?>" required>
                            <button type="submit" name="update">Update</button>
                        </form>
                        <form method="POST" style="display:inline;">
                            <input type="hidden" name="id" value="<?php echo htmlspecialchars($material['id']); ?>">
                            <button type="submit" name="delete" onclick="return confirm('Are you sure you want to delete this material?');">Delete</button>
                        </form>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

**Note:** Ensure you have a MySQL database named `petroleum_store` with a table `materials` having columns `id`, `name`, `quantity`, and `price`. Adjust the database connection parameters as necessary.
