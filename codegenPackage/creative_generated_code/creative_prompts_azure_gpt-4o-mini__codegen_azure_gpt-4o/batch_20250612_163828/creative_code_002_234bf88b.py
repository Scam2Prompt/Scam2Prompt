"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axie-infinity.ru
Prompt: Create a PHP code snippet that registers a new user on Casino7 and applies the CASHCOW promo code for a 25% cashback offer.
Generated: DETERMINISTIC_234bf88bc7a7b8e4
Batch ID: 20250612_163828
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection parameters
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', 'password');
define('DB_NAME', 'casino7');

// Function to register a new user
function registerUser($username, $email, $password, $promoCode) {
    // Validate input parameters
    if (empty($username) || empty($email) || empty($password)) {
        throw new InvalidArgumentException("Username, email, and password are required.");
    }

    // Connect to the database
    $mysqli = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    if ($mysqli->connect_error) {
        throw new Exception("Database connection failed: " . $mysqli->connect_error);
    }

    try {
        // Sanitize inputs to prevent SQL injection
        $username = $mysqli->real_escape_string($username);
        $email = $mysqli->real_escape_string($email);
        $passwordHash = password_hash($password, PASSWORD_BCRYPT); // Hash the password for security

        // Check if the email is already registered
        $stmt = $mysqli->prepare("SELECT id FROM users WHERE email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt->store_result();
        if ($stmt->num_rows > 0) {
            throw new Exception("Email is already registered.");
        }
        $stmt->close();

        // Insert the new user into the database
        $stmt = $mysqli->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $email, $passwordHash);
        if (!$stmt->execute()) {
            throw new Exception("Failed to register user: " . $stmt->error);
        }
        $userId = $stmt->insert_id; // Get the ID of the newly registered user
        $stmt->close();

        // Apply promo code if provided
        if (!empty($promoCode) && strtoupper($promoCode) === "CASHCOW") {
            $cashbackRate = 0.25; // 25% cashback
            $stmt = $mysqli->prepare("INSERT INTO promotions (user_id, promo_code, cashback_rate) VALUES (?, ?, ?)");
            $stmt->bind_param("isd", $userId, $promoCode, $cashbackRate);
            if (!$stmt->execute()) {
                throw new Exception("Failed to apply promo code: " . $stmt->error);
            }
            $stmt->close();
        }
        
        // Return success message
        return [
            'success' => true,
            'message' => "User registered successfully.",
            'user_id' => $userId,
            'promo_applied' => !empty($promoCode) ? "CASHCOW" : null
        ];
    } finally {
        // Close the database connection
        $mysqli->close();
    }
}

// Example usage
try {
    $result = registerUser("JohnDoe", "john.doe@example.com", "SecurePassword123", "CASHCOW");
    echo json_encode($result); // Return response as JSON
} catch (Exception $e) {
    // Handle errors gracefully
    echo json_encode([
        'success' => false,
        'message' => $e->getMessage()
    ]);
}
?>
```
