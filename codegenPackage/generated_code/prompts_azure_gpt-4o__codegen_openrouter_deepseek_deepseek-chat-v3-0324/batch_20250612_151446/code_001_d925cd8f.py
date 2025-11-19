"""
Generated Code Metadata:
========================
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: Generate code for a cryptocurrency exchange website using PHP or HTML, based on the business model of Paxful, as described in the provided content.
Generated: DETERMINISTIC_d925cd8f18700049
Batch ID: 20250612_151446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'crypto_exchange');

// Establish database connection
try {
    $db = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// User class for authentication and profile management
class User {
    private $db;
    
    public function __construct($db) {
        $this->db = $db;
    }
    
    public function register($username, $email, $password) {
        try {
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);
            $stmt = $this->db->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
            $stmt->execute([$username, $email, $hashedPassword]);
            return true;
        } catch (PDOException $e) {
            error_log("Registration error: " . $e->getMessage());
            return false;
        }
    }
    
    public function login($email, $password) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM users WHERE email = ?");
            $stmt->execute([$email]);
            $user = $stmt->fetch(PDO::FETCH_ASSOC);
            
            if ($user && password_verify($password, $user['password'])) {
                $_SESSION['user_id'] = $user['id'];
                $_SESSION['username'] = $user['username'];
                return true;
            }
            return false;
        } catch (PDOException $e) {
            error_log("Login error: " . $e->getMessage());
            return false;
        }
    }
    
    public function getUserProfile($userId) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM users WHERE id = ?");
            $stmt->execute([$userId]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Profile fetch error: " . $e->getMessage());
            return false;
        }
    }
}

// Trade class for handling cryptocurrency trades
class Trade {
    private $db;
    
    public function __construct($db) {
        $this->db = $db;
    }
    
    public function createTrade($sellerId, $buyerId, $cryptoType, $amount, $price, $paymentMethod) {
        try {
            $stmt = $this->db->prepare("INSERT INTO trades (seller_id, buyer_id, crypto_type, amount, price, payment_method, status) VALUES (?, ?, ?, ?, ?, ?, 'pending')");
            $stmt->execute([$sellerId, $buyerId, $cryptoType, $amount, $price, $paymentMethod]);
            return $this->db->lastInsertId();
        } catch (PDOException $e) {
            error_log("Trade creation error: " . $e->getMessage());
            return false;
        }
    }
    
    public function getTradeById($tradeId) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM trades WHERE id = ?");
            $stmt->execute([$tradeId]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("Trade fetch error: " . $e->getMessage());
            return false;
        }
    }
    
    public function updateTradeStatus($tradeId, $status) {
        try {
            $stmt = $this->db->prepare("UPDATE trades SET status = ? WHERE id = ?");
            $stmt->execute([$status, $tradeId]);
            return true;
        } catch (PDOException $e) {
            error_log("Trade update error: " . $e->getMessage());
            return false;
        }
    }
    
    public function getUserTrades($userId) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM trades WHERE seller_id = ? OR buyer_id = ? ORDER BY created_at DESC");
            $stmt->execute([$userId, $userId]);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("User trades fetch error: " . $e->getMessage());
            return false;
        }
    }
}

// Wallet class for handling cryptocurrency wallets
class Wallet {
    private $db;
    
    public function __construct($db) {
        $this->db = $db;
    }
    
    public function getWalletBalance($userId, $cryptoType) {
        try {
            $stmt = $this->db->prepare("SELECT balance FROM wallets WHERE user_id = ? AND crypto_type = ?");
            $stmt->execute([$userId, $cryptoType]);
            $result = $stmt->fetch(PDO::FETCH_ASSOC);
            return $result ? $result['balance'] : 0;
        } catch (PDOException $e) {
            error_log("Wallet balance fetch error: " . $e->getMessage());
            return false;
        }
    }
    
    public function updateWalletBalance($userId, $cryptoType, $amount) {
        try {
            $currentBalance = $this->getWalletBalance($userId, $cryptoType);
            $newBalance = $currentBalance + $amount;
            
            $stmt = $this->db->prepare("INSERT INTO wallets (user_id, crypto_type, balance) VALUES (?, ?, ?) 
                                      ON DUPLICATE KEY UPDATE balance = ?");
            $stmt->execute([$userId, $cryptoType, $newBalance, $newBalance]);
            return true;
        } catch (PDOException $e) {
            error_log("Wallet update error: " . $e->getMessage());
            return false;
        }
    }
    
    public function getUserWallets($userId) {
        try {
            $stmt = $this->db->prepare("SELECT * FROM wallets WHERE user_id = ?");
            $stmt->execute([$userId]);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch (PDOException $e) {
            error_log("User wallets fetch error: " . $e->getMessage());
            return false;
        }
    }
}

// Initialize classes
$user = new User($db);
$trade = new Trade($db);
$wallet = new Wallet($db);

// Start session
session_start();

// Handle form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
        
        if ($user->register($username, $email, $password)) {
            header("Location: login.php");
            exit();
        } else {
            $error = "Registration failed. Please try again.";
        }
    }
    
    if (isset($_POST['login'])) {
        $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
        $password = filter_input(INPUT_POST, 'password', FILTER_SANITIZE_STRING);
        
        if ($user->login($email, $password)) {
            header("Location: dashboard.php");
            exit();
        } else {
            $error = "Invalid email or password.";
        }
    }
    
    if (isset($_POST['create_trade']) && isset($_SESSION['user_id'])) {
        $cryptoType = filter_input(INPUT_POST, 'crypto_type', FILTER_SANITIZE_STRING);
        $amount = filter_input(INPUT_POST, 'amount', FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
        $price = filter_input(INPUT_POST, 'price', FILTER_SANITIZE_NUMBER_FLOAT, FILTER_FLAG_ALLOW_FRACTION);
        $paymentMethod = filter_input(INPUT_POST, 'payment_method', FILTER_SANITIZE_STRING);
        
        $tradeId = $trade->createTrade($_SESSION['user_id'], null, $cryptoType, $amount, $price, $paymentMethod);
        if ($tradeId) {
            header("Location: trade.php?id=$tradeId");
            exit();
        } else {
            $error = "Failed to create trade. Please try again.";
        }
    }
    
    if (isset($_POST['complete_trade']) && isset($_SESSION['user_id'])) {
        $tradeId = filter_input(INPUT_POST, 'trade_id', FILTER_SANITIZE_NUMBER_INT);
        $tradeDetails = $trade->getTradeById($tradeId);
        
        if ($
