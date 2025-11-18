"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinxcash.com
Prompt: Create a PHP script to handle multi-client event proposals and budget comparisons, as described in the webpage's recommendation for comparing quotes from multiple event companies.
Generated: DETERMINISTIC_924d8b319264faea
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// EventProposalHandler.php
// Script for handling multi-client event proposals and budget comparisons.

// Enable error reporting for debugging during development
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Define constants for error responses
define("ERROR_MISSING_DATA", "Missing required data.");
define("ERROR_INVALID_JSON", "Invalid JSON format.");
define("ERROR_GENERAL_FAILURE", "An error occurred while processing your request.");

// Include configuration (e.g., DB credentials)
include_once 'config.php'; // Ensure this file exists and has necessary configurations.

// Database connection setup
function getDatabaseConnection() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=" . DB_CHARSET;
        $pdo = new PDO($dsn, DB_USER, DB_PASSWORD, [
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        ]);
        return $pdo;
    } catch (PDOException $e) {
        error_log("Database connection error: " . $e->getMessage(), 0);
        echo json_encode(["error" => ERROR_GENERAL_FAILURE]);
        exit;
    }
}

// Helper function to validate and sanitize input
function validateInput($data) {
    if (empty($data['eventName']) || !is_string($data['eventName'])) {
        return false;
    }
    if (empty($data['proposals']) || !is_array($data['proposals'])) {
        return false;
    }
    foreach ($data['proposals'] as $proposal) {
        if (empty($proposal['companyName']) || !is_string($proposal['companyName'])) {
            return false;
        }
        if (empty($proposal['budget']) || !is_numeric($proposal['budget'])) {
            return false;
        }
    }
    return true;
}

// Function to handle the event proposals and compare budgets
function handleEventProposals($data) {
    $eventName = htmlspecialchars($data['eventName']);
    $proposals = array_map(function ($proposal) {
        return [
            'companyName' => htmlspecialchars($proposal['companyName']),
            'budget' => (float) $proposal['budget'],
        ];
    }, $data['proposals']);

    // Sort proposals from lowest to highest budget
    usort($proposals, function ($a, $b) {
        return $a['budget'] <=> $b['budget'];
    });

    // Store event and proposals in the database
    try {
        $pdo = getDatabaseConnection();
        $stmt = $pdo->prepare("INSERT INTO events (name) VALUES (:name)");
        $stmt->execute(['name' => $eventName]);
        $eventId = $pdo->lastInsertId();

        $stmt = $pdo->prepare("INSERT INTO proposals (event_id, company_name, budget) VALUES (:event_id, :company_name, :budget)");
        foreach ($proposals as $proposal) {
            $stmt->execute([
                'event_id' => $eventId,
                'company_name' => $proposal['companyName'],
                'budget' => $proposal['budget'],
            ]);
        }
    } catch (PDOException $e) {
        error_log("Database operation error: " . $e->getMessage(), 0);
        echo json_encode(["error" => ERROR_GENERAL_FAILURE]);
        exit;
    }

    // Return the sorted proposals
    return [
        'eventName' => $eventName,
        'proposals' => $proposals,
    ];
}

// Main script logic
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = file_get_contents("php://input");
    if (empty($input)) {
        echo json_encode(["error" => ERROR_MISSING_DATA]);
        exit;
    }

    $data = json_decode($input, true);
    if (json_last_error() !== JSON_ERROR_NONE) {
        echo json_encode(["error" => ERROR_INVALID_JSON]);
        exit;
    }

    if (!validateInput($data)) {
        echo json_encode(["error" => ERROR_MISSING_DATA]);
        exit;
    }

    $result = handleEventProposals($data);
    echo json_encode($result);
} else {
    echo json_encode(["error" => "Invalid request method."]);
}
?>
```

### Notes for Deployment:
1. Make sure to create and configure the `config.php` file with valid database credentials:
   ```php
   <?php
   define('DB_HOST', 'localhost');
   define('DB_NAME', 'event_management');
   define('DB_USER', 'root');
   define('DB_PASSWORD', 'password');
   define('DB_CHARSET', 'utf8mb4');
   ?>
   ```
   
2. Create the necessary database tables:
   ```sql
   CREATE TABLE events (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL
   );

   CREATE TABLE proposals (
       id INT AUTO_INCREMENT PRIMARY KEY,
       event_id INT NOT NULL,
       company_name VARCHAR(255) NOT NULL,
       budget DECIMAL(10, 2) NOT NULL,
       FOREIGN KEY (event_id) REFERENCES events(id)
   );
   ```
