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
/**
 * NFC Tag Data Handler
 * This script enables dynamic updates to links and actions for NFC tags.
 * It interacts with a database to store and retrieve NFC tag information.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'nfc_tags');
define('DB_USER', 'root');
define('DB_PASS', 'password');

/**
 * Connect to the database
 * 
 * @return PDO
 * @throws Exception
 */
function connectDatabase() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME;
        $pdo = new PDO($dsn, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        return $pdo;
    } catch (PDOException $e) {
        throw new Exception('Database connection failed: ' . $e->getMessage());
    }
}

/**
 * Retrieve NFC tag data by ID
 * 
 * @param int $id
 * @return array|null
 * @throws Exception
 */
function getNfcTag($id) {
    $pdo = connectDatabase();
    $stmt = $pdo->prepare("SELECT * FROM nfc_tags WHERE id = :id");
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);
    $stmt->execute();
    return $stmt->fetch(PDO::FETCH_ASSOC);
}

/**
 * Update NFC tag data
 * 
 * @param int $id
 * @param string $link
 * @param string $action
 * @return bool
 * @throws Exception
 */
function updateNfcTag($id, $link, $action) {
    $pdo = connectDatabase();
    $stmt = $pdo->prepare("UPDATE nfc_tags SET link = :link, action = :action WHERE id = :id");
    $stmt->bindParam(':link', $link);
    $stmt->bindParam(':action', $action);
    $stmt->bindParam(':id', $id, PDO::PARAM_INT);
    return $stmt->execute();
}

/**
 * Handle incoming request
 */
function handleRequest() {
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        // Validate input
        $id = filter_input(INPUT_POST, 'id', FILTER_VALIDATE_INT);
        $link = filter_input(INPUT_POST, 'link', FILTER_SANITIZE_URL);
        $action = filter_input(INPUT_POST, 'action', FILTER_SANITIZE_STRING);

        if (!$id || !$link || !$action) {
            http_response_code(400);
            echo json_encode(['error' => 'Invalid input']);
            return;
        }

        try {
            // Update NFC tag in the database
            if (updateNfcTag($id, $link, $action)) {
                http_response_code(200);
                echo json_encode(['success' => 'NFC tag updated successfully']);
            } else {
                http_response_code(500);
                echo json_encode(['error' => 'Failed to update NFC tag']);
            }
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    } elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
        $id = filter_input(INPUT_GET, 'id', FILTER_VALIDATE_INT);
        if (!$id) {
            http_response_code(400);
            echo json_encode(['error' => 'Invalid NFC tag ID']);
            return;
        }

        try {
            // Retrieve NFC tag data
            $tagData = getNfcTag($id);
            if ($tagData) {
                http_response_code(200);
                echo json_encode($tagData);
            } else {
                http_response_code(404);
                echo json_encode(['error' => 'NFC tag not found']);
            }
        } catch (Exception $e) {
            http_response_code(500);
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        // Method not allowed
        http_response_code(405);
        echo json_encode(['error' => 'Method not allowed']);
    }
}

// Execute the request handler
handleRequest();
?>
```
