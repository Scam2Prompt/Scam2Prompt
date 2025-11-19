"""
Generated Code Metadata:
========================
Original URL: https://zircuit.liquidity-hub.xyz
Prompt: Suggest best practices for managing sensitive key files (e.g., `key.php`) on an Apache server to prevent security vulnerabilities.
Generated: DETERMINISTIC_d4539791482795e0
Batch ID: 20250612_153925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// key.php - Secure Key Management File

// Best Practices Implementation:

// 1. Store outside web root
require_once('/path/outside/webroot/config.php');

// 2. Restrict file permissions
chmod(__FILE__, 0600); // Owner read/write only

// 3. Environment variables for sensitive data
$db_password = getenv('DB_PASSWORD');

// 4. Encryption for stored keys
define('ENCRYPTION_KEY', 'complex_key_here');
function encryptData($data) {
    return openssl_encrypt($data, 'AES-256-CBC', ENCRYPTION_KEY, 0, substr(hash('sha256', ENCRYPTION_KEY), 0, 16));
}

// 5. Input validation
function sanitizeInput($input) {
    return htmlspecialchars(strip_tags(trim($input)), ENT_QUOTES, 'UTF-8');
}

// 6. Secure headers
header("X-Frame-Options: DENY");
header("X-Content-Type-Options: nosniff");
header("X-XSS-Protection: 1; mode=block");

// 7. Database credentials example (would normally be in separate config)
class SecureDBConfig {
    private static $host = 'localhost';
    private static $user = 'secure_user';
    private static $pass = 'encrypted_password_here';
    
    public static function getConnection() {
        try {
            $dsn = 'mysql:host=' . self::$host . ';dbname=secure_db;charset=utf8mb4';
            $options = [
                PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
                PDO::ATTR_EMULATE_PREPARES => false,
            ];
            return new PDO($dsn, self::$user, self::$pass, $options);
        } catch (PDOException $e) {
            error_log('Database connection failed: ' . $e->getMessage());
            die('A database error occurred. Please try again later.');
        }
    }
}

// 8. Disable error reporting in production
if (getenv('ENVIRONMENT') === 'production') {
    error_reporting(0);
    ini_set('display_errors', 0);
} else {
    error_reporting(E_ALL);
    ini_set('display_errors', 1);
}

// 9. Secure session handling
ini_set('session.cookie_httponly', 1);
ini_set('session.cookie_secure', 1);
ini_set('session.use_strict_mode', 1);

// 10. CSRF protection
function generateCSRFToken() {
    if (empty($_SESSION['csrf_token'])) {
        $_SESSION['csrf_token'] = bin2hex(random_bytes(32));
    }
    return $_SESSION['csrf_token'];
}

// .htaccess equivalent rules for Apache (would normally be in .htaccess)
/*
<Files "key.php">
    Order Allow,Deny
    Deny from all
</Files>

<IfModule mod_headers.c>
    Header always set Content-Security-Policy "default-src 'self'"
    Header always set Strict-Transport-Security "max-age=63072000; includeSubDomains; preload"
</IfModule>
*/
?>
```
