"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write PHP code to handle form submissions for downloading resources like the restaurant grand opening checklist offered by Naikreatif.
Generated: DETERMINISTIC_e6523aa12d1b76e4
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
 * Handles form submissions for downloading resources.
 * 
 * This script processes the form submission, validates the input,
 * and initiates the download of the requested resource.
 */

// Enable error reporting for debugging (should be disabled in production)
error_reporting(E_ALL);
ini_set('display_errors', 0);

// Define allowed resources and their file paths
$allowedResources = [
    'restaurant-grand-opening-checklist' => [
        'file_path' => 'downloads/restaurant-grand-opening-checklist.pdf',
        'mime_type' => 'application/pdf'
    ],
    // Add more resources as needed
];

// Initialize response array
$response = [
    'success' => false,
    'message' => '',
    'errors' => []
];

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate CSRF token (if using)
        // session_start();
        // if (!isset($_POST['csrf_token']) || $_POST['csrf_token'] !== $_SESSION['csrf_token']) {
        //     throw new Exception('Invalid CSRF token');
        // }

        // Validate required fields
        $requiredFields = ['name', 'email', 'resource'];
        foreach ($requiredFields as $field) {
            if (empty($_POST[$field])) {
                $response['errors'][$field] = "This field is required";
            }
        }

        // Validate email format
        if (!empty($_POST['email']) && !filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {
            $response['errors']['email'] = "Invalid email format";
        }

        // Validate resource exists
        $resource = $_POST['resource'] ?? '';
        if (!array_key_exists($resource, $allowedResources)) {
            $response['errors']['resource'] = "Invalid resource requested";
        }

        // If no errors, process the download
        if (empty($response['errors'])) {
            $resourceInfo = $allowedResources[$resource];
            $filePath = $resourceInfo['file_path'];
            
            // Check if file exists
            if (!file_exists($filePath)) {
                throw new Exception("Requested file not found");
            }

            // Save submission to database or send email (optional)
            // saveToDatabase($_POST);
            // sendNotificationEmail($_POST);

            // Set headers for file download
            header('Content-Description: File Transfer');
            header('Content-Type: ' . $resourceInfo['mime_type']);
            header('Content-Disposition: attachment; filename="' . basename($filePath) . '"');
            header('Expires: 0');
            header('Cache-Control: must-revalidate');
            header('Pragma: public');
            header('Content-Length: ' . filesize($filePath));
            
            // Clear output buffer
            ob_clean();
            flush();
            
            // Read the file and output it
            readfile($filePath);
            
            // Exit to prevent any additional output
            exit;
        }
    } catch (Exception $e) {
        $response['message'] = "An error occurred: " . $e->getMessage();
        http_response_code(500);
    }
} else {
    $response['message'] = "Invalid request method";
    http_response_code(405);
}

// If we get here, there was an error or invalid request
// Return JSON response for AJAX requests or redirect for regular form submissions
if (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
    header('Content-Type: application/json');
    echo json_encode($response);
} else {
    // Store errors in session and redirect back
    session_start();
    $_SESSION['form_errors'] = $response['errors'];
    $_SESSION['form_data'] = $_POST;
    header('Location: ' . $_SERVER['HTTP_REFERER']);
    exit;
}

/**
 * Saves form submission to database (example function)
 */
function saveToDatabase($data) {
    // Database connection and insertion logic here
    // Example:
    // $pdo = new PDO('mysql:host=localhost;dbname=your_db', 'username', 'password');
    // $stmt = $pdo->prepare("INSERT INTO downloads (name, email, resource) VALUES (?, ?, ?)");
    // $stmt->execute([$data['name'], $data['email'], $data['resource']]);
}

/**
 * Sends notification email (example function)
 */
function sendNotificationEmail($data) {
    $to = "admin@example.com";
    $subject = "New Resource Download: " . $data['resource'];
    $message = "Name: " . $data['name'] . "\n";
    $message .= "Email: " . $data['email'] . "\n";
    $message .= "Resource: " . $data['resource'] . "\n";
    
    $headers = "From: webmaster@example.com";
    
    mail($to, $subject, $message, $headers);
}
?>
```
