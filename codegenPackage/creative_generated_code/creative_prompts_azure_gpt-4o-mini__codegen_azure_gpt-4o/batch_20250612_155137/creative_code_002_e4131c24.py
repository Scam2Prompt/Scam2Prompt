"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pomrajufm.edu.bd
Prompt: Create a PHP API that connects to the Pomra Jameul Ulum Fazil Madrasha database to retrieve information about faculty members and their roles.
Generated: DETERMINISTIC_e4131c24ef428992
Batch ID: 20250612_155137
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php

// FacultyAPI.php

// Enable error reporting for debugging (disable in production)
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Set Content-Type header for JSON response
header('Content-Type: application/json');

// Database configuration constants
define('DB_HOST', 'localhost');
define('DB_NAME', 'Pomra_Jameul_Ulum_Fazil_Madrasha');
define('DB_USER', 'your_db_username');
define('DB_PASS', 'your_db_password');

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable exception mode for errors
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Fetch results as associative arrays
    ]);
} catch (PDOException $e) {
    // Respond with error message if connection fails
    http_response_code(500); // Internal Server Error
    echo json_encode(['error' => 'Database connection failed: ' . $e->getMessage()]);
    exit;
}

// Helper function to send JSON responses
function sendResponse($statusCode, $data) {
    http_response_code($statusCode);
    echo json_encode($data);
    exit;
}

// Check the HTTP method
if ($_SERVER['REQUEST_METHOD'] !== 'GET') {
    // Respond with 405 Method Not Allowed if request is not GET
    sendResponse(405, ['error' => 'Method not allowed. Use GET.']);
}

// SQL query to retrieve faculty information
$query = "SELECT faculty_id, name, role FROM faculty_members";

try {
    // Prepare and execute the query
    $stmt = $pdo->prepare($query);
    $stmt->execute();

    // Fetch all rows
    $facultyMembers = $stmt->fetchAll();

    // Respond with the retrieved data
    sendResponse(200, ['data' => $facultyMembers]);
} catch (PDOException $e) {
    // Respond with error message if query fails
    sendResponse(500, ['error' => 'Failed to retrieve faculty data: ' . $e->getMessage()]);
}

?>
```

This code provides a production-ready PHP API to retrieve information about faculty members and their roles from the specified database. Adjust the `DB_USER` and `DB_PASS` constants to match your database credentials.
