"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Write a PHP script to process form submissions for requesting quotes on retractable screens, including fields for dimensions, screen type, and additional notes.
Generated: DETERMINISTIC_03ece576d1fb346c
Batch ID: 20250612_154927
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
 * Process form submissions for requesting quotes on retractable screens.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database connection
try {
    $dsn = "mysql:host={$config['db_host']};dbname={$config['db_name']}";
    $pdo = new PDO($dsn, $config['db_username'], $config['db_password']);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception("Database connection failed: " . $e->getMessage());
}

// Form data validation
function validateFormData(array $data): array
{
    $errors = [];

    // Validate dimensions
    if (empty($data['width']) || empty($data['height'])) {
        $errors[] = 'Width and height are required.';
    } elseif (!is_numeric($data['width']) || !is_numeric($data['height'])) {
        $errors[] = 'Width and height must be numbers.';
    }

    // Validate screen type
    $screenTypes = ['manual', 'motorized', 'solar'];
    if (empty($data['screen_type']) || !in_array($data['screen_type'], $screenTypes)) {
        $errors[] = 'Invalid screen type.';
    }

    // Validate additional notes
    if (!empty($data['notes']) && strlen($data['notes']) > 500) {
        $errors[] = 'Notes must be 500 characters or less.';
    }

    return ['errors' => $errors, 'data' => $data];
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $formData = [
        'width' => trim($_POST['width']),
        'height' => trim($_POST['height']),
        'screen_type' => trim($_POST['screen_type']),
        'notes' => trim($_POST['notes']),
    ];

    $validation = validateFormData($formData);
    $errors = $validation['errors'];
    $data = $validation['data'];

    if (!empty($errors)) {
        $response = ['success' => false, 'errors' => $errors];
    } else {
        try {
            $stmt = $pdo->prepare("
                INSERT INTO quote_requests (width, height, screen_type, notes, created_at)
                VALUES (:width, :height, :screen_type, :notes, NOW())
            ");

            $stmt->execute([
                'width' => $data['width'],
                'height' => $data['height'],
                'screen_type' => $data['screen_type'],
                'notes' => $data['notes'],
            ]);

            $response = ['success' => true, 'message' => 'Quote request submitted successfully.'];
        } catch (PDOException $e) {
            $response = ['success' => false, 'errors' => ['Database error: ' . $e->getMessage()]];
        }
    }

    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}

// Close database connection
$pdo = null;

?>
```
