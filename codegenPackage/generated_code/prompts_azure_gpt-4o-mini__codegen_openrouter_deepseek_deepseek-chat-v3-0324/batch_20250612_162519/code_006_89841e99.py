"""
Generated Code Metadata:
========================
Original URL: https://idn-hosting.com
Prompt: Develop a simple web application using PHP and MySQL that can be hosted on IDN Hosting's SSD shared hosting platform.
Generated: DETERMINISTIC_89841e993bcfe155
Batch ID: 20250612_162519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Simple Web Application for IDN Hosting's SSD Shared Hosting
 * 
 * This script provides a basic CRUD (Create, Read, Update, Delete) interface
 * for managing items in a MySQL database.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');

// Establish database connection
try {
    $pdo = new PDO(
        "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME,
        DB_USER,
        DB_PASS,
        [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]
    );
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Create items table if it doesn't exist
try {
    $createTableQuery = "CREATE TABLE IF NOT EXISTS items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    $pdo->exec($createTableQuery);
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        if (isset($_POST['add'])) {
            // Add new item
            $stmt = $pdo->prepare("INSERT INTO items (name, description) VALUES (?, ?)");
            $stmt->execute([$_POST['name'], $_POST['description']]);
        } elseif (isset($_POST['update'])) {
            // Update existing item
            $stmt = $pdo->prepare("UPDATE items SET name = ?, description = ? WHERE id = ?");
            $stmt->execute([$_POST['name'], $_POST['description'], $_POST['id']]);
        } elseif (isset($_GET['delete'])) {
            // Delete item
            $stmt = $pdo->prepare("DELETE FROM items WHERE id = ?");
            $stmt->execute([$_GET['delete']]);
        }
        // Redirect to prevent form resubmission
        header("Location: " . $_SERVER['PHP_SELF']);
        exit();
    } catch (PDOException $e) {
        die("Database operation failed: " . $e->getMessage());
    }
}

// Fetch all items
try {
    $items = $pdo->query("SELECT * FROM items ORDER BY created_at DESC")->fetchAll();
} catch (PDOException $e) {
    die("Failed to fetch items: " . $e->getMessage());
}

// Check if we're editing an item
$editItem = null;
if (isset($_GET['edit'])) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM items WHERE id = ?");
        $stmt->execute([$_GET['edit']]);
        $editItem = $stmt->fetch();
    } catch (PDOException $e) {
        die("Failed to fetch item for editing: " . $e->getMessage());
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Web App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        form { margin-bottom: 20px; background: #f9f9f9; padding: 20px; border-radius: 5px; }
        input, textarea { width: 100%; padding: 8px; margin: 5px 0 15px; box-sizing: border-box; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; cursor: pointer; }
        button:hover { background: #45a049; }
        .actions a { margin-right: 10px; color: #2196F3; text-decoration: none; }
        .actions a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>Simple Web Application</h1>
    
    <!-- Item Form -->
    <form method="post">
        <h2><?= $editItem ? 'Edit Item' : 'Add New Item' ?></h2>
        <?php if ($editItem): ?>
            <input type="hidden" name="id" value="<?= htmlspecialchars($editItem['id']) ?>">
        <?php endif; ?>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required 
               value="<?= htmlspecialchars($editItem['name'] ?? '') ?>">
        
        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="3"><?= 
            htmlspecialchars($editItem['description'] ?? '') ?></textarea>
        
        <?php if ($editItem): ?>
            <button type="submit" name="update">Update Item</button>
            <a href="<?= $_SERVER['PHP_SELF'] ?>">Cancel</a>
        <?php else: ?>
            <button type="submit" name="add">Add Item</button>
        <?php endif; ?>
    </form>
    
    <!-- Items List -->
    <h2>Items</h2>
    <?php if (empty($items)): ?>
        <p>No items found.</p>
    <?php else: ?>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Description</th>
                    <th>Created At</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($items as $item): ?>
                    <tr>
                        <td><?= htmlspecialchars($item['id']) ?></td>
                        <td><?= htmlspecialchars($item['name']) ?></td>
                        <td><?= htmlspecialchars($item['description']) ?></td>
                        <td><?= htmlspecialchars($item['created_at']) ?></td>
                        <td class="actions">
                            <a href="?edit=<?= $item['id'] ?>">Edit</a>
                            <a href="?delete=<?= $item['id'] ?>" 
                               onclick="return confirm('Are you sure you want to delete this item?')">Delete</a>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    <?php endif; ?>
</body>
</html>
```
