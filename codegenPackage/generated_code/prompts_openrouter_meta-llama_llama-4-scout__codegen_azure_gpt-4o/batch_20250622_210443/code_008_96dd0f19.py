"""
Generated Code Metadata:
========================
Original URL: https://dadkhahhadi.ir
Prompt: Design a database schema and API for a patient assistant media application using PHP and MySQL.
Generated: DETERMINISTIC_96dd0f1903044896
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database Schema (MySQL)
/*
CREATE DATABASE PatientAssistant;

USE PatientAssistant;

CREATE TABLE Patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(15),
    date_of_birth DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    patient_id INT NOT NULL,
    media_type ENUM('image', 'video', 'audio') NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE
);
*/

// API Code (PHP)

header('Content-Type: application/json');

// Database connection
function getDbConnection() {
    $host = 'localhost';
    $db = 'PatientAssistant';
    $user = 'root';
    $pass = '';
    $charset = 'utf8mb4';

    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $options = [
        PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
        PDO::ATTR_EMULATE_PREPARES   => false,
    ];

    try {
        return new PDO($dsn, $user, $pass, $options);
    } catch (PDOException $e) {
        http_response_code(500);
        echo json_encode(['error' => 'Database connection failed']);
        exit;
    }
}

// Helper function to send JSON responses
function sendResponse($data, $statusCode = 200) {
    http_response_code($statusCode);
    echo json_encode($data);
    exit;
}

// Route handling
$requestMethod = $_SERVER['REQUEST_METHOD'];
$endpoint = $_GET['endpoint'] ?? '';

$db = getDbConnection();

switch ($endpoint) {
    case 'addPatient':
        if ($requestMethod === 'POST') {
            $input = json_decode(file_get_contents('php://input'), true);

            if (!isset($input['name'], $input['email'], $input['date_of_birth'])) {
                sendResponse(['error' => 'Missing required fields'], 400);
            }

            try {
                $stmt = $db->prepare("INSERT INTO Patients (name, email, phone, date_of_birth) VALUES (?, ?, ?, ?)");
                $stmt->execute([
                    $input['name'],
                    $input['email'],
                    $input['phone'] ?? null,
                    $input['date_of_birth']
                ]);
                sendResponse(['message' => 'Patient added successfully']);
            } catch (PDOException $e) {
                sendResponse(['error' => 'Failed to add patient'], 500);
            }
        } else {
            sendResponse(['error' => 'Invalid request method'], 405);
        }
        break;

    case 'uploadMedia':
        if ($requestMethod === 'POST') {
            $input = json_decode(file_get_contents('php://input'), true);

            if (!isset($input['patient_id'], $input['media_type'], $input['file_path'])) {
                sendResponse(['error' => 'Missing required fields'], 400);
            }

            try {
                $stmt = $db->prepare("INSERT INTO Media (patient_id, media_type, file_path) VALUES (?, ?, ?)");
                $stmt->execute([
                    $input['patient_id'],
                    $input['media_type'],
                    $input['file_path']
                ]);
                sendResponse(['message' => 'Media uploaded successfully']);
            } catch (PDOException $e) {
                sendResponse(['error' => 'Failed to upload media'], 500);
            }
        } else {
            sendResponse(['error' => 'Invalid request method'], 405);
        }
        break;

    case 'getPatientMedia':
        if ($requestMethod === 'GET') {
            $patientId = $_GET['patient_id'] ?? null;

            if (!$patientId) {
                sendResponse(['error' => 'Missing patient_id'], 400);
            }

            try {
                $stmt = $db->prepare("SELECT * FROM Media WHERE patient_id = ?");
                $stmt->execute([$patientId]);
                $media = $stmt->fetchAll();
                sendResponse($media);
            } catch (PDOException $e) {
                sendResponse(['error' => 'Failed to fetch media'], 500);
            }
        } else {
            sendResponse(['error' => 'Invalid request method'], 405);
        }
        break;

    default:
        sendResponse(['error' => 'Endpoint not found'], 404);
        break;
}
?>
```
