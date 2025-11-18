"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cancelar-ahorat.webcindario.com
Prompt: Create a PHP script for managing domain redirects, suitable for free hosting platforms like miarroba.com.
Generated: DETERMINISTIC_a285aab7ca9d7741
Batch ID: 20250612_154422
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
 * Domain Redirect Manager
 * 
 * This script manages domain redirects. It allows users to add, update, and delete redirects.
 * The script is suitable for free hosting platforms and is designed to be lightweight and efficient.
 */

// Database connection settings (Adjust these values as necessary)
$host = 'localhost';
$dbname = 'redirect_manager';
$username = 'root';
$password = 'your_password';

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Connection failed: " . $e->getMessage());
}

/**
 * Function to add a new redirect
 *
 * @param string $source Source URL to redirect from
 * @param string $destination Destination URL to redirect to
 * @return bool Success status of the operation
 */
function addRedirect($source, $destination) {
    global $pdo;
    $sql = "INSERT INTO redirects (source, destination) VALUES (:source, :destination)";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['source' => $source, 'destination' => $destination]);
        return true;
    } catch (PDOException $e) {
        // Handle SQL errors
        error_log("Error adding redirect: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to update an existing redirect
 *
 * @param int $id Redirect ID
 * @param string $source Source URL to redirect from
 * @param string $destination Destination URL to redirect to
 * @return bool Success status of the operation
 */
function updateRedirect($id, $source, $destination) {
    global $pdo;
    $sql = "UPDATE redirects SET source = :source, destination = :destination WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['id' => $id, 'source' => $source, 'destination' => $destination]);
        return true;
    } catch (PDOException $e) {
        // Handle SQL errors
        error_log("Error updating redirect: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to delete a redirect by ID
 *
 * @param int $id Redirect ID
 * @return bool Success status of the operation
 */
function deleteRedirect($id) {
    global $pdo;
    $sql = "DELETE FROM redirects WHERE id = :id";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute(['id' => $id]);
        return true;
    } catch (PDOException $e) {
        // Handle SQL errors
        error_log("Error deleting redirect: " . $e->getMessage());
        return false;
    }
}

/**
 * Function to fetch all redirects
 *
 * @return array List of redirects
 */
function fetchRedirects() {
    global $pdo;
    $sql = "SELECT * FROM redirects";
    $stmt = $pdo->query($sql);

    return $stmt->fetchAll(PDO::FETCH_ASSOC);
}

// Example usage of the redirect manager functions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Add, update, or delete redirects based on submitted form data
    $action = $_POST['action'] ?? '';
    
    if ($action === 'add') {
        addRedirect($_POST['source'], $_POST['destination']);
    } elseif ($action === 'update') {
        updateRedirect($_POST['id'], $_POST['source'], $_POST['destination']);
    } elseif ($action === 'delete') {
        deleteRedirect($_POST['id']);
    }
}

// Fetch all redirects to display them
$redirects = fetchRedirects();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Domain Redirect Manager</title>
</head>
<body>
    <h1>Domain Redirect Manager</h1>
    <form method="post">
        <input type="hidden" name="id" value="">
        <label for="source">Source URL:</label>
        <input type="text" name="source" required>
        <label for="destination">Destination URL:</label>
        <input type="text" name="destination" required>
        <button type="submit" name="action" value="add">Add Redirect</button>
        <button type="submit" name="action" value="update">Update Redirect</button>
        <button type="submit" name="action" value="delete">Delete Redirect</button>
    </form>

    <h2>Existing Redirects</h2>
    <ul>
        <?php foreach ($redirects as $redirect): ?>
            <li>
                <?php echo htmlspecialchars($redirect['source']) . ' -> ' . htmlspecialchars($redirect['destination']); ?>
                <!-- Include edit and delete options -->
                <form method="post" style="display:inline;">
                    <input type="hidden" name="id" value="<?php echo $redirect['id']; ?>">
                    <input type="hidden" name="source" value="<?php echo $redirect['source']; ?>">
                    <input type="hidden" name="destination" value="<?php echo $redirect['destination']; ?>">
                    <button type="submit" name="action" value="update">Edit</button>
                    <button type="submit" name="action" value="delete">Delete</button>
                </form>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>
```
