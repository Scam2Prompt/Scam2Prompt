"""
Generated Code Metadata:
========================
Original URL: https://freeproxy.me
Prompt: Generate a PHP script to create a proxy partner network similar to FreeProxy.me's Free Web Proxy Partners feature.
Generated: DETERMINISTIC_41cdc94e38e6180f
Batch ID: 20250612_150327
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
 * Proxy Partner Network Script
 * 
 * This script allows users to register as proxy partners, manage their proxy servers,
 * and provides an API for proxy rotation.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'proxy_partner_network');
define('API_KEY_LENGTH', 32);

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 0);
ini_set('log_errors', 1);
ini_set('error_log', __DIR__ . '/error.log');

// Create database connection
function db_connect() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    if ($conn->connect_error) {
        error_log("Database connection failed: " . $conn->connect_error);
        die("Database connection failed. Please try again later.");
    }
    
    return $conn;
}

// Initialize database tables
function init_db() {
    $conn = db_connect();
    
    $queries = [
        "CREATE TABLE IF NOT EXISTS partners (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            api_key VARCHAR(32) NOT NULL UNIQUE,
            status ENUM('active', 'suspended', 'pending') DEFAULT 'pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )",
        
        "CREATE TABLE IF NOT EXISTS proxy_servers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            partner_id INT NOT NULL,
            ip_address VARCHAR(45) NOT NULL,
            port INT NOT NULL,
            protocol ENUM('http', 'https', 'socks4', 'socks5') NOT NULL,
            country VARCHAR(2) NOT NULL,
            is_active BOOLEAN DEFAULT TRUE,
            last_checked TIMESTAMP NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (partner_id) REFERENCES partners(id) ON DELETE CASCADE
        )",
        
        "CREATE TABLE IF NOT EXISTS proxy_stats (
            id INT AUTO_INCREMENT PRIMARY KEY,
            proxy_id INT NOT NULL,
            requests INT DEFAULT 0,
            success INT DEFAULT 0,
            failed INT DEFAULT 0,
            last_used TIMESTAMP NULL,
            FOREIGN KEY (proxy_id) REFERENCES proxy_servers(id) ON DELETE CASCADE
        )"
    ];
    
    foreach ($queries as $query) {
        if (!$conn->query($query)) {
            error_log("Database initialization failed: " . $conn->error);
            return false;
        }
    }
    
    $conn->close();
    return true;
}

// Generate random API key
function generate_api_key() {
    return bin2hex(random_bytes(API_KEY_LENGTH / 2));
}

// Register new partner
function register_partner($name, $email) {
    $conn = db_connect();
    
    // Validate input
    if (empty($name) || empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        return ['success' => false, 'message' => 'Invalid input data'];
    }
    
    // Check if email exists
    $stmt = $conn->prepare("SELECT id FROM partners WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $stmt->store_result();
    
    if ($stmt->num_rows > 0) {
        $stmt->close();
        $conn->close();
        return ['success' => false, 'message' => 'Email already registered'];
    }
    $stmt->close();
    
    // Insert new partner
    $api_key = generate_api_key();
    $stmt = $conn->prepare("INSERT INTO partners (name, email, api_key) VALUES (?, ?, ?)");
    $stmt->bind_param("sss", $name, $email, $api_key);
    
    if ($stmt->execute()) {
        $partner_id = $stmt->insert_id;
        $stmt->close();
        $conn->close();
        return [
            'success' => true,
            'message' => 'Partner registered successfully',
            'partner_id' => $partner_id,
            'api_key' => $api_key
        ];
    } else {
        error_log("Partner registration failed: " . $stmt->error);
        $stmt->close();
        $conn->close();
        return ['success' => false, 'message' => 'Registration failed'];
    }
}

// Add proxy server
function add_proxy_server($partner_id, $api_key, $ip, $port, $protocol, $country) {
    $conn = db_connect();
    
    // Validate partner
    $stmt = $conn->prepare("SELECT id FROM partners WHERE id = ? AND api_key = ? AND status = 'active'");
    $stmt->bind_param("is", $partner_id, $api_key);
    $stmt->execute();
    $stmt->store_result();
    
    if ($stmt->num_rows === 0) {
        $stmt->close();
        $conn->close();
        return ['success' => false, 'message' => 'Invalid partner or API key'];
    }
    $stmt->close();
    
    // Validate proxy data
    if (!filter_var($ip, FILTER_VALIDATE_IP) || 
        !is_numeric($port) || $port < 1 || $port > 65535 ||
        !in_array(strtolower($protocol), ['http', 'https', 'socks4', 'socks5']) ||
        strlen($country) !== 2) {
        $conn->close();
        return ['success' => false, 'message' => 'Invalid proxy data'];
    }
    
    // Insert proxy
    $stmt = $conn->prepare("INSERT INTO proxy_servers (partner_id, ip_address, port, protocol, country) VALUES (?, ?, ?, ?, ?)");
    $stmt->bind_param("isiss", $partner_id, $ip, $port, $protocol, $country);
    
    if ($stmt->execute()) {
        $proxy_id = $stmt->insert_id;
        
        // Initialize stats
        $stmt2 = $conn->prepare("INSERT INTO proxy_stats (proxy_id) VALUES (?)");
        $stmt2->bind_param("i", $proxy_id);
        $stmt2->execute();
        $stmt2->close();
        
        $stmt->close();
        $conn->close();
        return [
            'success' => true,
            'message' => 'Proxy server added successfully',
            'proxy_id' => $proxy_id
        ];
    } else {
        error_log("Proxy addition failed: " . $stmt->error);
        $stmt->close();
        $conn->close();
        return ['success' => false, 'message' => 'Failed to add proxy server'];
    }
}

// Get random proxy
function get_random_proxy($country = null, $protocol = null) {
    $conn = db_connect();
    
    $query = "SELECT ps.id, ps.ip_address, ps.port, ps.protocol, ps.country 
              FROM proxy_servers ps 
              WHERE ps.is_active = TRUE";
    
    $params = [];
    $types = '';
    
    if ($country) {
        $query .= " AND ps.country = ?";
        $params[] = strtoupper($country);
        $types .= 's';
    }
    
    if ($protocol) {
        $query .= " AND ps.protocol = ?";
        $params[] = strtolower($protocol);
        $types .= 's';
    }
    
    $query .= " ORDER BY RAND() LIMIT 1";
    
    $stmt = $conn->prepare($query);
    
    if (!empty($params)) {
        $stmt->bind_param($types, ...$params);
    }
    
    $stmt->execute();
    $result = $stmt->get_result();
    
    if ($result->num_rows > 0) {
        $proxy = $result->fetch_assoc();
        
        // Update stats
        $update = $conn->prepare("UPDATE proxy_stats SET requests = requests + 1, last_used = NOW() WHERE proxy_id = ?");
        $update->bind_param("i", $proxy['id']);
        $update->execute();
        $update->close();
        
        $stmt->close();
        $conn->close();
        return ['success' => true, 'proxy' => $proxy];
    } else {
        $stmt->close();
        $conn->close();
        return ['success' => false, 'message' => 'No available proxies matching criteria'];
    }
}

// API endpoint handler
function handle_api_request() {
    header('Content-Type: application/json');
    
    $action = $_GET['action'] ?? '';
    $api_key = $_GET['api_key'] ?? '';
    
    try {
        switch ($action) {
            case 'register':
                $name = $_POST['name'] ?? '';
                $email = $_POST['email'] ?? '';
                $response = register_partner($name, $email);
                break;
                
            case 'add_proxy':
                $partner_id = $_POST['partner_id'] ??
