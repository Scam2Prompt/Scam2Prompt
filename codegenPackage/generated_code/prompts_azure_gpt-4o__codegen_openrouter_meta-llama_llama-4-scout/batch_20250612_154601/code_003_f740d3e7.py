"""
Generated Code Metadata:
========================
Original URL: https://solutechsystem.com.ng
Prompt: Write a PHP script to manage donations for an NGO website, incorporating user-friendly features inspired by Solutech System's NGO website design offerings.
Generated: DETERMINISTIC_f740d3e788372dcf
Batch ID: 20250612_154601
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
 * Donation Management System for NGO Website
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'ngo_donations',
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
    throw new Exception('Database connection failed: ' . $e->getMessage());
}

/**
 * Donation Class
 */
class Donation
{
    private $pdo;

    public function __construct($pdo)
    {
        $this->pdo = $pdo;
    }

    /**
     * Create a new donation
     *
     * @param string $name
     * @param string $email
     * @param float $amount
     * @param string $currency
     * @return bool
     */
    public function createDonation($name, $email, $amount, $currency)
    {
        try {
            $stmt = $this->pdo->prepare('
                INSERT INTO donations (name, email, amount, currency)
                VALUES (:name, :email, :amount, :currency)
            ');
            $stmt->execute([
                'name' => $name,
                'email' => $email,
                'amount' => $amount,
                'currency' => $currency,
            ]);
            return true;
        } catch (PDOException $e) {
            error_log('Error creating donation: ' . $e->getMessage());
            return false;
        }
    }

    /**
     * Get all donations
     *
     * @return array
     */
    public function getDonations()
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM donations');
            $stmt->execute();
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log('Error fetching donations: ' . $e->getMessage());
            return [];
        }
    }

    /**
     * Get donation by ID
     *
     * @param int $id
     * @return array
     */
    public function getDonationById($id)
    {
        try {
            $stmt = $this->pdo->prepare('SELECT * FROM donations WHERE id = :id');
            $stmt->execute(['id' => $id]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log('Error fetching donation: ' . $e->getMessage());
            return [];
        }
    }
}

// Initialize Donation class
$donation = new Donation($pdo);

// API Endpoints
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['donate'])) {
        $name = filter_var($_POST['name'], FILTER_SANITIZE_STRING);
        $email = filter_var($_POST['email'], FILTER_SANITIZE_EMAIL);
        $amount = filter_var($_POST['amount'], FILTER_VALIDATE_FLOAT);
        $currency = filter_var($_POST['currency'], FILTER_SANITIZE_STRING);

        if ($donation->createDonation($name, $email, $amount, $currency)) {
            http_response_code(201);
            echo json_encode(['message' => 'Donation created successfully']);
        } else {
            http_response_code(500);
            echo json_encode(['message' => 'Error creating donation']);
        }
    }
} elseif ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (isset($_GET['id'])) {
        $id = filter_var($_GET['id'], FILTER_VALIDATE_INT);
        $donationData = $donation->getDonationById($id);
        if ($donationData) {
            http_response_code(200);
            echo json_encode($donationData);
        } else {
            http_response_code(404);
            echo json_encode(['message' => 'Donation not found']);
        }
    } else {
        $donations = $donation->getDonations();
        http_response_code(200);
        echo json_encode($donations);
    }
}

// Database Schema
$sql = '
    CREATE TABLE IF NOT EXISTS donations (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        amount FLOAT NOT NULL,
        currency VARCHAR(10) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
';

try {
    $pdo->exec($sql);
} catch (PDOException $e) {
    error_log('Error creating database schema: ' . $e->getMessage());
}

$pdo = null;
```
