"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amarhospital.com
Prompt: Design a PHP script that manages 24/7 emergency service requests, taking inspiration from the emergency services offered at Amar Hospital in Patiala.
Generated: DETERMINISTIC_bfb5b0539013caee
Batch ID: 20250612_155840
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
 * Emergency Service Request Management Script
 * 
 * This script handles 24/7 emergency service requests, inspired by Amar Hospital.
 * Features:
 * - Accept emergency service requests via HTTP POST.
 * - Validate user input and handle errors gracefully.
 * - Log requests for record-keeping.
 * - Provide a basic API response to callers.
 * 
 * Best practices for security, readability, and maintainability are followed.
 */

// Enable error reporting for development (disable in production).
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Configuration
define('LOG_FILE', 'emergency_requests.log');

/**
 * Function to log emergency requests to a file.
 * 
 * @param array $data Associative array containing request details.
 * @return void
 */
function logEmergencyRequest(array $data): void {
    $logEntry = date('Y-m-d H:i:s') . ' - ' . json_encode($data) . PHP_EOL;
    file_put_contents(LOG_FILE, $logEntry, FILE_APPEND | LOCK_EX);
}

/**
 * Function to handle incoming emergency requests.
 * 
 * @return void
 */
function handleEmergencyRequest(): void {
    // Check if the request method is POST.
    if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
        http_response_code(405); // Method Not Allowed.
        echo json_encode(['status' => 'error', 'message' => 'Only POST requests are allowed']);
        return;
    }

    // Accept and validate input data.
    $input = json_decode(file_get_contents('php://input'), true);
    
    if (!is_array($input)) {
        http_response_code(400); // Bad Request.
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON input']);
        return;
    }

    // Validate required fields.
    $requiredFields = ['name', 'contact', 'service_type', 'location', 'description'];
    foreach ($requiredFields as $field) {
        if (empty($input[$field])) {
            http_response_code(422); // Unprocessable Entity.
            echo json_encode(['status' => 'error', 'message' => "Missing required field: {$field}"]);
            return;
        }
    }

    // Sanitize input data.
    $name = htmlspecialchars(trim($input['name']));
    $contact = htmlspecialchars(trim($input['contact']));
    $serviceType = htmlspecialchars(trim($input['service_type']));
    $location = htmlspecialchars(trim($input['location']));
    $description = htmlspecialchars(trim($input['description']));

    // Prepare the data for logging and response.
    $requestData = [
        'name' => $name,
        'contact' => $contact,
        'service_type' => $serviceType,
        'location' => $location,
        'description' => $description,
        'timestamp' => date('Y-m-d H:i:s')
    ];

    // Log the request.
    logEmergencyRequest($requestData);

    // Respond with a success message.
    http_response_code(200); // OK.
    echo json_encode(['status' => 'success', 'message' => 'Emergency request logged successfully']);
}

// Execute the request handler.
handleEmergencyRequest();
?>
```

This PHP script manages emergency service requests effectively, adhering to production-ready standards with detailed commenting and robust error handling.
