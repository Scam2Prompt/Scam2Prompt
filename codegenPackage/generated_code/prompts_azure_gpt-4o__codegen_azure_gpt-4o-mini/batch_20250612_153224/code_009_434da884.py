"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Generate PHP code for handling NFC tag data on a server, enabling dynamic updates to links and actions, similar to Izikard's platform for managing NFC products.
Generated: DETERMINISTIC_434da8845199f667
Batch ID: 20250612_153224
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
 * NFC Tag Data Handler
 * This script handles NFC tag data, allowing for dynamic updates to links and actions.
 * It provides an API endpoint for managing NFC products similar to Izikard's platform.
 */

// Set content type to JSON
header('Content-Type: application/json');

// Database connection parameters
$host = 'localhost';
$db = 'nfc_database';
$user = 'db_user';
$pass = 'db_password';

try {
    // Create a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db;charset=utf8", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    http_response_code(500);
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Function to get NFC tag data
function getNfcTagData($pdo, $tagId) {
    $stmt = $pdo->prepare("SELECT * FROM nfc_tags WHERE tag_id = :tag_id");
    $stmt->execute(['tag_id' => $tagId]);
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

// Function to update NFC tag data
function updateNfcTagData($pdo, $tagId, $data) {
    $stmt = $pdo->prepare("UPDATE nfc_tags SET link = :link, action = :action WHERE tag_id = :tag_id");
    return $stmt->execute([
        'link' => $data['link'],
        'action' => $data['action'],
        'tag_id' => $tagId
    ]);
}

// Handle incoming requests
$requestMethod = $_SERVER['REQUEST_METHOD'];
$tagId = isset($_GET['tag_id']) ? $_GET['tag_id'] : null;

switch ($requestMethod) {
    case 'GET':
        if ($tagId) {
            // Fetch NFC tag data
            $tagData = getNfcTagData($pdo, $tagId);
            if ($tagData) {
                echo json_encode($tagData);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'NFC tag not found']);
            }
        } else {
            http_response_code(400);
            echo json_encode(['error' => 'Tag ID is required']);
        }
        break;

    case 'POST':
        // Update NFC tag data
        $inputData = json_decode(file_get_contents('php://input'), true);
        if ($tagId && isset($inputData['link']) && isset($inputData['action'])) {
            if (updateNfcTagData($pdo, $tagId, $inputData)) {
                echo json_encode(['success' => 'NFC tag updated successfully']);
            } else {
                http_response_code(500);
                echo json_encode(['error' => 'Failed to update NFC tag']);
            }
        } else {
            http_response_code(400);
            echo json_encode(['error' => 'Tag ID, link, and action are required']);
        }
        break;

    default:
        // Method not allowed
        http_response_code(405);
        echo json_encode(['error' => 'Method not allowed']);
        break;
}
?>
```
