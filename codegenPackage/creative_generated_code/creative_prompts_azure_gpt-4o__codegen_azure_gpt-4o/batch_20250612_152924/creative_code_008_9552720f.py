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
// petroleum_control_panel.php

// Start the session to manage user authentication
session_start();

// Database connection configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'petroleum_store');
define('DB_USER', 'root');
define('DB_PASS', '');

// Function to establish a database connection using PDO
function getDatabaseConnection()
{
    try {
        $pdo = new PDO('mysql:host=' . DB_HOST . ';dbname=' . DB_NAME, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        die("Database Connection Failed: " . $e->getMessage());
    }
}

// Function to handle user authentication
function authenticateUser($username, $password)
{
    $pdo = getDatabaseConnection();

    $stmt = $pdo->prepare("SELECT id, password FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);

    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['user_id'] = $user['id'];
        return true;
    }

    return false;
}

// Function to check if the user is logged in
function isLoggedIn()
{
    return isset($_SESSION['user_id']);
}

// Function to log out the user
function logout()
{
    session_destroy();
    header("Location: login.php");
    exit;
}

// Function to fetch petroleum materials from the database
function fetchMaterials()
{
    $pdo = getDatabaseConnection();

    $stmt = $pdo->query("SELECT * FROM petroleum_materials");
    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Function to add a new petroleum material to the database
function addMaterial($name, $quantity, $price)
{
    try {
        $pdo = getDatabaseConnection();

        $stmt = $pdo->prepare("INSERT INTO petroleum_materials (name, quantity, price) VALUES (:name, :quantity, :price)");
        $stmt->execute(['name' => $name, 'quantity' => $quantity, 'price' => $price]);
    } catch (Exception $e) {
        die("Error Adding Material: " . $e->getMessage());
    }
}

// Function to delete a petroleum material by ID
function deleteMaterial($id)
{
    try {
        $pdo = getDatabaseConnection();

        $stmt = $pdo->prepare("DELETE FROM petroleum_materials WHERE id = :id");
        $stmt->execute(['id' => $id]);
    } catch (Exception $e) {
        die("Error Deleting Material: " . $e->getMessage());
    }
}

// HTML Template for the control panel
function renderControlPanel()
{
    if (!isLoggedIn()) {
        header("Location: login.php");
        exit;
    }

    $materials = fetchMaterials();

    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '<meta charset="UTF-8">';
    echo '<meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '<title>Petroleum Materials Control Panel</title>';
    echo '<link rel="stylesheet" href="styles.css">';
    echo '</head>';
    echo '<body>';
    echo '<h1>Petroleum Materials Control Panel</h1>';
    echo '<table>';
    echo '<thead>';
    echo '<tr>';
    echo '<th>ID</th>';
    echo '<th>Name</th>';
    echo '<th>Quantity</th>';
    echo '<th>Price</th>';
    echo '<th>Actions</th>';
    echo '</tr>';
    echo '</thead>';
    echo '<tbody>';
    foreach ($materials as $material) {
        echo '<tr>';
        echo '<td>' . htmlspecialchars($material['id']) . '</td>';
        echo '<td>' . htmlspecialchars($material['name']) . '</td>';
        echo '<td>' . htmlspecialchars($material['quantity']) . '</td>';
        echo '<td>' . htmlspecialchars($material['price']) . '</td>';
        echo '<td>';
        echo '<form method="POST" action="delete_material.php" style="display:inline-block;">';
        echo '<input type="hidden" name="id" value="' . htmlspecialchars($material['id']) . '">';
        echo '<button type="submit">Delete</button>';
        echo '</form>';
        echo '</td>';
        echo '</tr>';
    }
    echo '</tbody>';
    echo '</table>';
    echo '<h2>Add New Material</h2>';
    echo '<form method="POST" action="add_material.php">';
    echo '<input type="text" name="name" placeholder="Material Name" required>';
    echo '<input type="number" name="quantity" placeholder="Quantity" required>';
    echo '<input type="number" step="0.01" name="price" placeholder="Price" required>';
    echo '<button type="submit">Add Material</button>';
    echo '</form>';
    echo '<form method="POST" action="logout.php">';
    echo '<button type="submit">Logout</button>';
    echo '</form>';
    echo '</body>';
    echo '</html>';
}

// Main script execution
renderControlPanel();
?>
```
