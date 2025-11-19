"""
Generated Code Metadata:
========================
Original URL: https://fxbinaryinvestpro.com
Prompt: Develop a PHP script that implements a referral program similar to the one described on Fxbinaryinvestpro, allowing users to track their referrals and earnings.
Generated: DETERMINISTIC_52a0d0044baeb2cd
Batch ID: 20250612_160245
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
 * Referral Program Implementation in PHP
 */

// Configuration
$config = [
    'db_host' => 'localhost',
    'db_username' => 'your_username',
    'db_password' => 'your_password',
    'db_name' => 'referral_program',
    'referral_commission' => 10, // percentage
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

// Create tables if not exist
$pdo->exec('
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        referral_code VARCHAR(255) NOT NULL,
        balance DECIMAL(10, 2) DEFAULT 0.00
    );
');

$pdo->exec('
    CREATE TABLE IF NOT EXISTS referrals (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        referred_user_id INT NOT NULL,
        commission DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (referred_user_id) REFERENCES users(id)
    );
');

// Referral Program Class
class ReferralProgram
{
    private $pdo;
    private $config;

    public function __construct($pdo, $config)
    {
        $this->pdo = $pdo;
        $this->config = $config;
    }

    public function createUser($username, $email, $referralCode = null)
    {
        $stmt = $this->pdo->prepare('
            INSERT INTO users (username, email, referral_code, balance)
            VALUES (:username, :email, :referral_code, 0.00);
        ');
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':referral_code', $referralCode);
        $stmt->execute();

        $userId = $this->pdo->lastInsertId();

        if ($referralCode) {
            $this->processReferral($referralCode, $userId);
        }

        return $userId;
    }

    private function processReferral($referralCode, $userId)
    {
        $stmt = $this->pdo->prepare('
            SELECT id, balance FROM users
            WHERE referral_code = :referral_code;
        ');
        $stmt->bindParam(':referral_code', $referralCode);
        $stmt->execute();

        $referrerUser = $stmt->fetch();

        if ($referrerUser) {
            $commission = $this->config['referral_commission'] / 100;
            $stmt = $this->pdo->prepare('
                INSERT INTO referrals (user_id, referred_user_id, commission)
                VALUES (:user_id, :referred_user_id, :commission);
            ');
            $stmt->bindParam(':user_id', $referrerUser['id']);
            $stmt->bindParam(':referred_user_id', $userId);
            $stmt->bindParam(':commission', $commission);
            $stmt->execute();

            // Update referrer balance
            $newBalance = $referrerUser['balance'] + $commission;
            $stmt = $this->pdo->prepare('
                UPDATE users SET balance = :balance
                WHERE id = :id;
            ');
            $stmt->bindParam(':balance', $newBalance);
            $stmt->bindParam(':id', $referrerUser['id']);
            $stmt->execute();
        }
    }

    public function getUserBalance($userId)
    {
        $stmt = $this->pdo->prepare('
            SELECT balance FROM users
            WHERE id = :id;
        ');
        $stmt->bindParam(':id', $userId);
        $stmt->execute();

        $user = $stmt->fetch();

        return $user['balance'] ?? 0.00;
    }

    public function getReferrals($userId)
    {
        $stmt = $this->pdo->prepare('
            SELECT * FROM referrals
            WHERE user_id = :user_id;
        ');
        $stmt->bindParam(':user_id', $userId);
        $stmt->execute();

        return $stmt->fetchAll();
    }
}

// Example usage
$referralProgram = new ReferralProgram($pdo, $config);

// Create users
$user1Id = $referralProgram->createUser('user1', 'user1@example.com');
$user2Id = $referralProgram->createUser('user2', 'user2@example.com', 'REF' . $user1Id);

// Get user balance
echo "User 1 balance: " . $referralProgram->getUserBalance($user1Id) . PHP_EOL;
echo "User 2 balance: " . $referralProgram->getUserBalance($user2Id) . PHP_EOL;

// Get referrals
echo "User 1 referrals:" . PHP_EOL;
print_r($referralProgram->getReferrals($user1Id));

$pdo = null;
```
