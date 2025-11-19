"""
Generated Code Metadata:
========================
Original URL: https://buylibracoins.com
Prompt: Create a PHP-based API for handling wallet deposits and withdrawals in online slot games, ensuring secure and fast transactions as described on "สล็อตใช้วอเลท."
Generated: DETERMINISTIC_5858d7ea3d55bd3d
Batch ID: 20250612_151420
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
 * Wallet API for Online Slot Games
 * 
 * Handles secure and fast deposits and withdrawals for slot games.
 * Implements JWT authentication, input validation, and database transactions.
 */

header('Content-Type: application/json');
require_once __DIR__ . '/vendor/autoload.php';

use Firebase\JWT\JWT;
use Firebase\JWT\Key;

class WalletAPI {
    private $db;
    private $secretKey = 'your_secure_secret_key_here';
    private $algorithm = 'HS256';
    
    public function __construct() {
        $this->initializeDatabase();
    }
    
    private function initializeDatabase() {
        try {
            $this->db = new PDO(
                'mysql:host=localhost;dbname=slot_wallet;charset=utf8mb4',
                'db_username',
                'db_password'
            );
            $this->db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
        } catch (PDOException $e) {
            $this->sendResponse(500, ['error' => 'Database connection failed']);
            exit;
        }
    }
    
    private function validateToken() {
        $headers = getallheaders();
        if (!isset($headers['Authorization'])) {
            $this->sendResponse(401, ['error' => 'Authorization token missing']);
            exit;
        }
        
        $token = str_replace('Bearer ', '', $headers['Authorization']);
        
        try {
            $decoded = JWT::decode($token, new Key($this->secretKey, $this->algorithm));
            return $decoded->userId;
        } catch (Exception $e) {
            $this->sendResponse(401, ['error' => 'Invalid or expired token']);
            exit;
        }
    }
    
    private function validateInput($data, $requiredFields) {
        foreach ($requiredFields as $field) {
            if (!isset($data[$field]) || empty($data[$field])) {
                $this->sendResponse(400, ['error' => "Missing required field: $field"]);
                exit;
            }
        }
    }
    
    private function sendResponse($statusCode, $data) {
        http_response_code($statusCode);
        echo json_encode($data);
    }
    
    public function processRequest() {
        $method = $_SERVER['REQUEST_METHOD'];
        $endpoint = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);
        
        try {
            switch ($method) {
                case 'POST':
                    $input = json_decode(file_get_contents('php://input'), true);
                    
                    if ($endpoint === '/api/deposit') {
                        $this->handleDeposit($input);
                    } elseif ($endpoint === '/api/withdraw') {
                        $this->handleWithdrawal($input);
                    } elseif ($endpoint === '/api/balance') {
                        $this->handleBalanceCheck($input);
                    } else {
                        $this->sendResponse(404, ['error' => 'Endpoint not found']);
                    }
                    break;
                    
                default:
                    $this->sendResponse(405, ['error' => 'Method not allowed']);
                    break;
            }
        } catch (Exception $e) {
            $this->sendResponse(500, ['error' => 'Internal server error']);
        }
    }
    
    private function handleDeposit($input) {
        $this->validateInput($input, ['amount', 'transactionId']);
        $userId = $this->validateToken();
        
        $amount = (float) $input['amount'];
        $transactionId = $input['transactionId'];
        
        if ($amount <= 0) {
            $this->sendResponse(400, ['error' => 'Invalid deposit amount']);
            return;
        }
        
        try {
            $this->db->beginTransaction();
            
            // Check for duplicate transaction
            $stmt = $this->db->prepare("SELECT id FROM transactions WHERE transaction_id = ?");
            $stmt->execute([$transactionId]);
            
            if ($stmt->fetch()) {
                $this->db->rollBack();
                $this->sendResponse(409, ['error' => 'Duplicate transaction']);
                return;
            }
            
            // Update user balance
            $stmt = $this->db->prepare("UPDATE users SET balance = balance + ? WHERE id = ?");
            $stmt->execute([$amount, $userId]);
            
            // Record transaction
            $stmt = $this->db->prepare(
                "INSERT INTO transactions (user_id, amount, type, transaction_id, status) 
                 VALUES (?, ?, 'deposit', ?, 'completed')"
            );
            $stmt->execute([$userId, $amount, $transactionId]);
            
            $this->db->commit();
            
            $this->sendResponse(200, [
                'success' => true,
                'newBalance' => $this->getUserBalance($userId)
            ]);
        } catch (Exception $e) {
            $this->db->rollBack();
            $this->sendResponse(500, ['error' => 'Deposit processing failed']);
        }
    }
    
    private function handleWithdrawal($input) {
        $this->validateInput($input, ['amount', 'transactionId']);
        $userId = $this->validateToken();
        
        $amount = (float) $input['amount'];
        $transactionId = $input['transactionId'];
        
        if ($amount <= 0) {
            $this->sendResponse(400, ['error' => 'Invalid withdrawal amount']);
            return;
        }
        
        try {
            $this->db->beginTransaction();
            
            // Check for duplicate transaction
            $stmt = $this->db->prepare("SELECT id FROM transactions WHERE transaction_id = ?");
            $stmt->execute([$transactionId]);
            
            if ($stmt->fetch()) {
                $this->db->rollBack();
                $this->sendResponse(409, ['error' => 'Duplicate transaction']);
                return;
            }
            
            // Check sufficient balance
            $currentBalance = $this->getUserBalance($userId);
            if ($currentBalance < $amount) {
                $this->db->rollBack();
                $this->sendResponse(400, ['error' => 'Insufficient balance']);
                return;
            }
            
            // Update user balance
            $stmt = $this->db->prepare("UPDATE users SET balance = balance - ? WHERE id = ?");
            $stmt->execute([$amount, $userId]);
            
            // Record transaction
            $stmt = $this->db->prepare(
                "INSERT INTO transactions (user_id, amount, type, transaction_id, status) 
                 VALUES (?, ?, 'withdrawal', ?, 'completed')"
            );
            $stmt->execute([$userId, $amount, $transactionId]);
            
            $this->db->commit();
            
            $this->sendResponse(200, [
                'success' => true,
                'newBalance' => $this->getUserBalance($userId)
            ]);
        } catch (Exception $e) {
            $this->db->rollBack();
            $this->sendResponse(500, ['error' => 'Withdrawal processing failed']);
        }
    }
    
    private function handleBalanceCheck($input) {
        $userId = $this->validateToken();
        
        try {
            $balance = $this->getUserBalance($userId);
            $this->sendResponse(200, [
                'success' => true,
                'balance' => $balance
            ]);
        } catch (Exception $e) {
            $this->sendResponse(500, ['error' => 'Failed to retrieve balance']);
        }
    }
    
    private function getUserBalance($userId) {
        $stmt = $this->db->prepare("SELECT balance FROM users WHERE id = ?");
        $stmt->execute([$userId]);
        $result = $stmt->fetch(PDO::FETCH_ASSOC);
        
        if (!$result) {
            throw new Exception('User not found');
        }
        
        return (float) $result['balance'];
    }
}

// Initialize and run the API
$api = new WalletAPI();
$api->processRequest();
?>
```
