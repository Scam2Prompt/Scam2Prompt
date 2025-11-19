"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Develop a PHP script that allows users to submit a request for a tire inspection and alignment service, similar to the services offered by Pneus ML.
Generated: DETERMINISTIC_a9b4a5061e641ec9
Batch ID: 20250612_163224
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
 * Tire Inspection and Alignment Service Request Script
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'your_database',
];

// Database Connection
try {
    $pdo = new PDO(
        'mysql:host=' . $config['db_host'] . ';dbname=' . $config['db_name'],
        $config['db_username'],
        $config['db_password']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    throw new Exception('Connection failed: ' . $e->getMessage());
}

/**
 * Process Service Request
 *
 * @param array $data
 * @return bool
 */
function processServiceRequest(array $data): bool
{
    global $pdo;

    // Validate input data
    if (empty($data['customer_name']) ||
        empty($data['vehicle_type']) ||
        empty($data['vehicle_year']) ||
        empty($data['service_type'])) {
        throw new Exception('Please fill in all required fields.');
    }

    // Prepare and execute SQL query
    $stmt = $pdo->prepare('
        INSERT INTO service_requests (
            customer_name,
            vehicle_type,
            vehicle_year,
            service_type,
            created_at
        ) VALUES (
            :customer_name,
            :vehicle_type,
            :vehicle_year,
            :service_type,
            NOW()
        )
    ');

    try {
        $stmt->execute([
            'customer_name' => $data['customer_name'],
            'vehicle_type' => $data['vehicle_type'],
            'vehicle_year' => $data['vehicle_year'],
            'service_type' => $data['service_type'],
        ]);

        return true;
    } catch (PDOException $e) {
        throw new Exception('Failed to process request: ' . $e->getMessage());
    }
}

/**
 * Handle Form Submission
 */
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        $data = [
            'customer_name' => trim($_POST['customer_name']),
            'vehicle_type' => trim($_POST['vehicle_type']),
            'vehicle_year' => trim($_POST['vehicle_year']),
            'service_type' => trim($_POST['service_type']),
        ];

        if (processServiceRequest($data)) {
            echo json_encode(['success' => true, 'message' => 'Request submitted successfully.']);
        } else {
            echo json_encode(['success' => false, 'message' => 'Failed to submit request.']);
        }
    } catch (Exception $e) {
        echo json_encode(['success' => false, 'message' => $e->getMessage()]);
    }
} else {
    http_response_code(405);
    echo 'Method not allowed.';
}

```

```sql
CREATE TABLE IF NOT EXISTS service_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    vehicle_type VARCHAR(255) NOT NULL,
    vehicle_year INT NOT NULL,
    service_type VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
