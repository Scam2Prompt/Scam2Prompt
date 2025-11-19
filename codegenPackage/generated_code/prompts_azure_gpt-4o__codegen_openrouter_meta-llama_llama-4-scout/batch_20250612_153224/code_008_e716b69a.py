"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Create a PHP script to manage client inquiries and consultations, referencing Alpha Digital Solutions' free consultation feature.
Generated: DETERMINISTIC_e716b69a974f618b
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
 * Client Inquiry and Consultation Management Script
 *
 * This script provides a basic system for managing client inquiries and consultations.
 * It allows clients to submit inquiries, schedule consultations, and view their inquiry and consultation history.
 */

// Configuration
$config = [
    'dbHost' => 'localhost',
    'dbUsername' => 'your_username',
    'dbPassword' => 'your_password',
    'dbName' => 'client_inquiries',
];

// Database Connection
try {
    $pdo = new PDO(
        "mysql:host={$config['dbHost']};dbname={$config['dbName']}",
        $config['dbUsername'],
        $config['dbPassword']
    );
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Inquiry Model
class Inquiry
{
    private $id;
    private $name;
    private $email;
    private $message;
    private $createdAt;

    public function __construct($id, $name, $email, $message, $createdAt)
    {
        $this->id = $id;
        $this->name = $name;
        $this->email = $email;
        $this->message = $message;
        $this->createdAt = $createdAt;
    }

    public static function create($name, $email, $message)
    {
        global $pdo;
        $stmt = $pdo->prepare("INSERT INTO inquiries (name, email, message) VALUES (:name, :email, :message)");
        $stmt->execute([
            'name' => $name,
            'email' => $email,
            'message' => $message,
        ]);
        return $stmt->rowCount() > 0;
    }

    public static function getAll()
    {
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM inquiries ORDER BY created_at DESC");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public static function getById($id)
    {
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM inquiries WHERE id = :id");
        $stmt->execute(['id' => $id]);
        $inquiry = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($inquiry) {
            return new self($inquiry['id'], $inquiry['name'], $inquiry['email'], $inquiry['message'], $inquiry['created_at']);
        }
        return null;
    }
}

// Consultation Model
class Consultation
{
    private $id;
    private $inquiryId;
    private $scheduledAt;
    private $description;

    public function __construct($id, $inquiryId, $scheduledAt, $description)
    {
        $this->id = $id;
        $this->inquiryId = $inquiryId;
        $this->scheduledAt = $scheduledAt;
        $this->description = $description;
    }

    public static function create($inquiryId, $scheduledAt, $description)
    {
        global $pdo;
        $stmt = $pdo->prepare("INSERT INTO consultations (inquiry_id, scheduled_at, description) VALUES (:inquiryId, :scheduledAt, :description)");
        $stmt->execute([
            'inquiryId' => $inquiryId,
            'scheduledAt' => $scheduledAt,
            'description' => $description,
        ]);
        return $stmt->rowCount() > 0;
    }

    public static function getAll()
    {
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM consultations ORDER BY scheduled_at DESC");
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public static function getById($id)
    {
        global $pdo;
        $stmt = $pdo->prepare("SELECT * FROM consultations WHERE id = :id");
        $stmt->execute(['id' => $id]);
        $consultation = $stmt->fetch(PDO::FETCH_ASSOC);
        if ($consultation) {
            return new self($consultation['id'], $consultation['inquiry_id'], $consultation['scheduled_at'], $consultation['description']);
        }
        return null;
    }
}

// API Endpoints
class ClientInquiryAPI
{
    public function handleInquirySubmission()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
            $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
            $message = filter_var($_POST['message'], FILTER_SANITIZE_STRING);

            if (Inquiry::create($name, $email, $message)) {
                http_response_code(201);
                echo json_encode(['message' => 'Inquiry submitted successfully']);
            } else {
                http_response_code(500);
                echo json_encode(['message' => 'Failed to submit inquiry']);
            }
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }

    public function handleConsultationScheduling()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $inquiryId = filter_var($_POST['inquiryId'], FILTER_VALIDATE_INT);
            $scheduledAt = filter_var($_POST['scheduledAt'], FILTER_SANITIZE_STRING);
            $description = filter_var($_POST['description'], FILTER_SANITIZE_STRING);

            if (Consultation::create($inquiryId, $scheduledAt, $description)) {
                http_response_code(201);
                echo json_encode(['message' => 'Consultation scheduled successfully']);
            } else {
                http_response_code(500);
                echo json_encode(['message' => 'Failed to schedule consultation']);
            }
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }

    public function handleGetInquiries()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'GET') {
            $inquiries = Inquiry::getAll();
            http_response_code(200);
            echo json_encode($inquiries);
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }

    public function handleGetConsultations()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'GET') {
            $consultations = Consultation::getAll();
            http_response_code(200);
            echo json_encode($consultations);
        } else {
            http_response_code(405);
            echo json_encode(['message' => 'Method not allowed']);
        }
    }
}

// Initialize API
$api = new ClientInquiryAPI();

// Handle Requests
if (isset($_GET['inquirySubmission'])) {
    $api->handleInquirySubmission();
} elseif (isset($_GET['consultationScheduling'])) {
    $api->handleConsultationScheduling();
} elseif (isset($_GET['getInquiries'])) {
    $api->handleGetInquiries();
} elseif (isset($_GET['getConsultations'])) {
    $api->handleGetConsultations();
} else {
    http_response_code(404);
    echo json_encode(['message' => 'Not found']);
}
```
