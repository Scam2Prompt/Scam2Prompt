"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.izikard.com
Prompt: Generate PHP code for handling NFC tag data on a server, enabling dynamic updates to links and actions, similar to Izikard's platform for managing NFC products.
Generated: DETERMINISTIC_434da8845199f667
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// NFC Tag Management System
// This script handles NFC tag data and enables dynamic updates to links and actions.

// Include database configuration
require_once 'config.php'; // Ensure this file contains proper DB connection settings

// Enable error reporting for development (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to establish a database connection
function getDatabaseConnection()
{
    try {
        $pdo = new PDO(DB_DSN, DB_USERNAME, DB_PASSWORD, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        error_log("Database connection failed: " . $e->getMessage());
        http_response_code(500);
        echo json_encode(["error" => "Internal Server Error"]);
        exit;
    }
}

// Function to handle NFC tag data updates
function updateNFCTag($tagId, $actionType, $actionData)
{
    $pdo = getDatabaseConnection();

    try {
        $query = "UPDATE nfc_tags SET action_type = :actionType, action_data = :actionData, updated_at = NOW() WHERE tag_id = :tagId";
        $stmt = $pdo->prepare($query);
        $stmt->execute([
            ':tagId' => $tagId,
            ':actionType' => $actionType,
            ':actionData' => $actionData,
        ]);

        if ($stmt->rowCount() > 0) {
            return ["success" => true, "message" => "NFC tag updated successfully."];
        } else {
            return ["success" => false, "message" => "No changes made. Tag ID might not exist."];
        }
    } catch (PDOException $e) {
        error_log("Database query error: " . $e->getMessage());
        return ["success" => false, "message" => "Failed to update NFC tag data."];
    }
}

// Function to retrieve NFC tag data
function getNFCTag($tagId)
{
    $pdo = getDatabaseConnection();

    try {
        $query = "SELECT tag_id, action_type, action_data, updated_at FROM nfc_tags WHERE tag_id = :tagId";
        $stmt = $pdo->prepare($query);
        $stmt->execute([':tagId' => $tagId]);
        $result = $stmt->fetch();

        if ($result) {
            return ["success" => true, "data" => $result];
        } else {
            return ["success" => false, "message" => "Tag ID not found."];
        }
    } catch (PDOException $e) {
        error_log("Database query error: " . $e->getMessage());
        return ["success" => false, "message" => "Failed to retrieve NFC tag data."];
    }
}

// API endpoint handling
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Handle NFC tag update
    $input = json_decode(file_get_contents('php://input'), true);

    if (isset($input['tag_id'], $input['action_type'], $input['action_data'])) {
        $response = updateNFCTag($input['tag_id'], $input['action_type'], $input['action_data']);
    } else {
        $response = ["success" => false, "message" => "Invalid input. Missing required fields."];
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET' && isset($_GET['tag_id'])) {
    // Handle NFC tag retrieval
    $response = getNFCTag($_GET['tag_id']);
} else {
    $response = ["success" => false, "message" => "Invalid request method or missing parameters."];
}

// Return JSON response
header('Content-Type: application/json');
echo json_encode($response);
?>
```

---

This code assumes you have a database table `nfc_tags` with columns `tag_id`, `action_type`, `action_data`, and `updated_at`. Replace `DB_DSN`, `DB_USERNAME`, and `DB_PASSWORD` with your actual database connection details in the `config.php` file.
