"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://capcutpro.ofertatcdigital.shop
Prompt: Provide a step-by-step guide in PHP to create an API for managing CapCut Pro account purchases, including features like account registration and email-based activation.
Generated: DETERMINISTIC_3a524877cca00a00
Batch ID: 20250612_150345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Load required libraries
require 'vendor/autoload.php'; // Assuming you're using Composer for dependency management

use Slim\Factory\AppFactory;
use Psr\Http\Message\ResponseInterface;
use Psr\Http\Message\ServerRequestInterface;

// Initialize Slim App
$app = AppFactory::create();
$app->setBasePath('/api'); // Set base path for API

// Database connection (using PDO for example)
function getDBConnection() {
    $host = '127.0.0.1';
    $db = 'capcut_accounts';
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
    } catch (\PDOException $e) {
        throw new \PDOException($e->getMessage(), (int)$e->getCode());
    }
}

// Account Registration Route
$app->post('/register', function (ServerRequestInterface $request, ResponseInterface $response) {
    $data = json_decode($request->getBody()->getContents(), true);
    
    // Validate input
    if (!isset($data['email']) || !filter_var($data['email'], FILTER_VALIDATE_EMAIL)) {
        return $response->withStatus(400)->withJson(['error' => 'Invalid email format']);
    }

    if (!isset($data['password']) || strlen($data['password']) < 6) {
        return $response->withStatus(400)->withJson(['error' => 'Password must be at least 6 characters']);
    }

    // Create database connection
    $pdo = getDBConnection();

    // Insert user into database
    try {
        $stmt = $pdo->prepare('INSERT INTO users (email, password, activated) VALUES (?, ?, ?)');
        $stmt->execute([$data['email'], password_hash($data['password'], PASSWORD_DEFAULT), 0]);

        // Send activation email (pseudo-code, requires mailer setup)
        // sendActivationEmail($data['email']);

        return $response->withStatus(201)->withJson(['message' => 'Registration successful, please check your email to activate your account.']);
    } catch (PDOException $e) {
        return $response->withStatus(500)->withJson(['error' => 'Database error: ' . $e->getMessage()]);
    }
});

// Account Activation Route
$app->get('/activate/{token}', function (ServerRequestInterface $request, ResponseInterface $response, array $args) {
    $token = $args['token'];

    // Validate token (implement token validation logic)
    // Example: $user = validateActivationToken($token);

    // If valid token, activate user account
    if ($user) {
        $pdo = getDBConnection();
        
        try {
            $stmt = $pdo->prepare('UPDATE users SET activated = ? WHERE email = ?');
            $stmt->execute([1, $user['email']]);

            return $response->withStatus(200)->withJson(['message' => 'Account activated successfully']);
        } catch (PDOException $e) {
            return $response->withStatus(500)->withJson(['error' => 'Database error: ' . $e->getMessage()]);
        }
    } else {
        return $response->withStatus(400)->withJson(['error' => 'Invalid activation token']);
    }
});

// Run the application
$app->run();
```

### Database Setup
To use this code, ensure you have a MySQL database set up with the following table structure:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    activated TINYINT(1) DEFAULT 0
);
```

### Notes
- You'll need to implement the actual email sending logic in the `sendActivationEmail` function and token generation/validation logic for account activation.
- Use environment variables or a configuration file to manage sensitive data (like database credentials) in a production environment.
- Ensure proper access control and security measures are in place for production deployment.
