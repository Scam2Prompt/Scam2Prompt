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
 * Emergency Service Request Management System
 * This script handles emergency service requests for Amar Hospital, Patiala.
 * It allows users to submit service requests and view current requests.
 */

// Database connection settings
$host = 'localhost';
$db   = 'emergency_service_db';
$user = 'root';
$pass = '';
$charset = 'utf8mb4';

// Set up the connection using PDO
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

/**
 * Function to submit a new emergency service request
 *
 * @param string $name
 * @param string $phone
 * @param string $service
 * @return bool
 */
function submitRequest($name, $phone, $service) {
    global $pdo;

    // Validate input
    if (empty($name) || empty($phone) || empty($service)) {
        throw new InvalidArgumentException('All fields are required.');
    }

    // Prepare and execute the SQL statement
    $sql = "INSERT INTO service_requests (name, phone, service, request_time) VALUES (?, ?, ?, NOW())";
    $stmt = $pdo->prepare($sql);
    return $stmt->execute([$name, $phone, $service]);
}

/**
 * Function to retrieve all emergency service requests
 *
 * @return array
 */
function getRequests() {
    global $pdo;

    // Prepare the SQL statement
    $sql = "SELECT * FROM service_requests ORDER BY request_time DESC";
    $stmt = $pdo->prepare($sql);
    $stmt->execute();
    
    return $stmt->fetchAll();
}

// Handling form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Collect and sanitize input
        $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
        $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
        $service = filter_input(INPUT_POST, 'service', FILTER_SANITIZE_STRING);
        
        // Submit the request
        submitRequest($name, $phone, $service);
        $message = "Request submitted successfully!";
    } catch (Exception $e) {
        $error = "Error: " . $e->getMessage();
    }
}

// Retrieve existing requests
$requests = getRequests();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emergency Service Requests</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Emergency Service Request Form</h1>

    <?php if (isset($error)): ?>
        <div class="error"><?php echo htmlspecialchars($error); ?></div>
    <?php endif; ?>

    <?php if (isset($message)): ?>
        <div class="success"><?php echo htmlspecialchars($message); ?></div>
    <?php endif; ?>

    <form method="POST" action="">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        
        <label for="service">Service Required:</label>
        <select id="service" name="service" required>
            <option value="Ambulance">Ambulance</option>
            <option value="Medical Advice">Medical Advice</option>
            <option value="Fire Service">Fire Service</option>
            <option value="Police Assistance">Police Assistance</option>
        </select>
        
        <button type="submit">Submit Request</button>
    </form>

    <h2>Current Service Requests</h2>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Phone</th>
                <th>Service</th>
                <th>Request Time</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($requests as $request): ?>
                <tr>
                    <td><?php echo htmlspecialchars($request['name']); ?></td>
                    <td><?php echo htmlspecialchars($request['phone']); ?></td>
                    <td><?php echo htmlspecialchars($request['service']); ?></td>
                    <td><?php echo htmlspecialchars($request['request_time']); ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>
</html>
```

Make sure to create a corresponding database and table named `service_requests` with the necessary fields (`id`, `name`, `phone`, `service`, `request_time`) to execute this code properly. Additionally, you may want to add more error handling as necessary and consider security aspects such as SQL injection prevention in real-world applications.
