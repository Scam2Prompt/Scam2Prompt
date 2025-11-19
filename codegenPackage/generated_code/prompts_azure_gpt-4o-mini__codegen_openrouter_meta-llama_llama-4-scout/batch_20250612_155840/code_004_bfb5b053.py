"""
Generated Code Metadata:
========================
Original URL: https://amarhospital.com
Prompt: Design a PHP script that manages 24/7 emergency service requests, taking inspiration from the emergency services offered at Amar Hospital in Patiala.
Generated: DETERMINISTIC_bfb5b0539013caee
Batch ID: 20250612_155840
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
 * Emergency Service Request Manager
 *
 * This script manages 24/7 emergency service requests.
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'root',
    'db_password' => '',
    'db_name' => 'emergency_services',
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
    echo 'Connection failed: ' . $e->getMessage();
    exit();
}

/**
 * Emergency Request Class
 */
class EmergencyRequest
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    /**
     * Create a new emergency request
     *
     * @param string $name
     * @param string $contact_number
     * @param string $location
     * @param string $description
     *
     * @return bool
     */
    public function createRequest($name, $contact_number, $location, $description)
    {
        try {
            $stmt = $this->pdo->prepare('
                INSERT INTO emergency_requests (name, contact_number, location, description, created_at)
                VALUES (:name, :contact_number, :location, :description, NOW())
            ');
            $stmt->execute([
                'name' => $name,
                'contact_number' => $contact_number,
                'location' => $location,
                'description' => $description,
            ]);
            return true;
        } catch (PDOException $e) {
            echo 'Error creating request: ' . $e->getMessage();
            return false;
        }
    }

    /**
     * Get all emergency requests
     *
     * @return array
     */
    public function getRequests()
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM emergency_requests ORDER BY created_at DESC');
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            echo 'Error fetching requests: ' . $e->getMessage();
            return [];
        }
    }

    /**
     * Update emergency request status
     *
     * @param int $id
     * @param string $status
     *
     * @return bool
     */
    public function updateRequestStatus($id, $status)
    {
        try {
            $stmt = $this->pdo->prepare('
                UPDATE emergency_requests
                SET status = :status, updated_at = NOW()
                WHERE id = :id
            ');
            $stmt->execute([
                'id' => $id,
                'status' => $status,
            ]);
            return true;
        } catch (PDOException $e) {
            echo 'Error updating request status: ' . $e->getMessage();
            return false;
        }
    }
}

// Create emergency request instance
$emergencyRequest = new EmergencyRequest($pdo);

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $name = trim($_POST['name']);
    $contact_number = trim($_POST['contact_number']);
    $location = trim($_POST['location']);
    $description = trim($_POST['description']);

    // Validate input
    if (empty($name) || empty($contact_number) || empty($location) || empty($description)) {
        echo 'Please fill in all fields.';
        exit();
    }

    // Create emergency request
    if ($emergencyRequest->createRequest($name, $contact_number, $location, $description)) {
        echo 'Emergency request created successfully!';
    } else {
        echo 'Failed to create emergency request.';
    }
}

// Display emergency requests
$requests = $emergencyRequest->getRequests();

// Create table if it doesn't exist
try {
    $pdo->exec('
        CREATE TABLE IF NOT EXISTS emergency_requests (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            contact_number VARCHAR(20) NOT NULL,
            location VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            status VARCHAR(50) DEFAULT "pending",
            created_at DATETIME NOT NULL,
            updated_at DATETIME
        );
    ');
} catch (PDOException $e) {
    echo 'Error creating table: ' . $e->getMessage();
    exit();
}

// Display form and requests
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Emergency Service Requests</title>
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 10px;
        }
    </style>
</head>
<body>
    <h1>Emergency Service Requests</h1>
    <form action="" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="contact_number">Contact Number:</label>
        <input type="text" id="contact_number" name="contact_number"><br><br>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location"><br><br>
        <label for="description">Description:</label>
        <textarea id="description" name="description"></textarea><br><br>
        <input type="submit" value="Submit Request">
    </form>
    <h2>Emergency Requests:</h2>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Contact Number</th>
            <th>Location</th>
            <th>Description</th>
            <th>Status</th>
            <th>Actions</th>
        </tr>
        <?php foreach ($requests as $request) : ?>
        <tr>
            <td><?= $request['id'] ?></td>
            <td><?= $request['name'] ?></td>
            <td><?= $request['contact_number'] ?></td>
            <td><?= $request['location'] ?></td>
            <td><?= $request['description'] ?></td>
            <td><?= $request['status'] ?></td>
            <td>
                <a href="?id=<?= $request['id'] ?>&status=accepted">Accept</a>
                <a href="?id=<?= $request['id'] ?>&status=rejected">Reject</a>
            </td>
        </tr>
        <?php endforeach; ?>
    </table>

    <?php
    // Update request status
    if (isset($_GET['id']) && isset($_GET['status'])) {
        $id = (int) $_GET['id'];
        $status = $_GET['status'];
        $emergencyRequest->updateRequestStatus($id, $status);
    }
    ?>
</body>
</html>
```
