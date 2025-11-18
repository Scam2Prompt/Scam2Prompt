"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeproxy.me
Prompt: Generate a PHP script to create a proxy partner network similar to FreeProxy.me's Free Web Proxy Partners feature.
Generated: DETERMINISTIC_41cdc94e38e6180f
Batch ID: 20250612_150327
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
 * Proxy Partner Network Script
 *
 * This script creates a basic proxy partner network, allowing users to submit and view proxy partner information.
 * It includes basic functionalities for adding, viewing, and deleting proxy partners.
 */

// Database configuration
$host = 'localhost'; // Database host
$db = 'proxy_network'; // Database name
$user = 'root'; // Database user
$pass = ''; // Database password

// Create database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new proxy partner
function addProxyPartner($name, $url) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("INSERT INTO partners (name, url) VALUES (:name, :url)");
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':url', $url);
        $stmt->execute();
        return "Proxy partner added successfully.";
    } catch (PDOException $e) {
        return "Error adding proxy partner: " . $e->getMessage();
    }
}

// Function to fetch all proxy partners
function getProxyPartners() {
    global $pdo;
    try {
        $stmt = $pdo->query("SELECT * FROM partners");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        return "Error fetching proxy partners: " . $e->getMessage();
    }
}

// Function to delete a proxy partner by ID
function deleteProxyPartner($id) {
    global $pdo;
    try {
        $stmt = $pdo->prepare("DELETE FROM partners WHERE id = :id");
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return "Proxy partner deleted successfully.";
    } catch (PDOException $e) {
        return "Error deleting proxy partner: " . $e->getMessage();
    }
}

// Handling form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['add'])) {
        // Add a new proxy partner
        $name = trim($_POST['name']);
        $url = filter_var(trim($_POST['url']), FILTER_VALIDATE_URL);

        if ($name && $url) {
            echo addProxyPartner($name, $url);
        } else {
            echo "Invalid input. Please provide a valid name and URL.";
        }
    } elseif (isset($_POST['delete'])) {
        // Delete a proxy partner
        $id = intval($_POST['id']);
        echo deleteProxyPartner($id);
    }
}

// Fetch all partners to display
$partners = getProxyPartners();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Proxy Partner Network</title>
</head>
<body>
    <h1>Proxy Partner Network</h1>

    <h2>Add Proxy Partner</h2>
    <form method="POST">
        <label for="name">Partner Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="url">Partner URL:</label>
        <input type="text" id="url" name="url" required>
        <br>
        <button type="submit" name="add">Add Partner</button>
    </form>

    <h2>Existing Partners</h2>
    <ul>
        <?php foreach ($partners as $partner): ?>
            <li>
                <?= htmlspecialchars($partner['name']); ?> - <a href="<?= htmlspecialchars($partner['url']); ?>" target="_blank"><?= htmlspecialchars($partner['url']); ?></a>
                <form method="POST" style="display:inline;">
                    <input type="hidden" name="id" value="<?= $partner['id']; ?>">
                    <button type="submit" name="delete">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```

**Note:** Before running this script, ensure that you have a database with a table named `partners` structured as follows:

```sql
CREATE TABLE partners (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL
);
```
