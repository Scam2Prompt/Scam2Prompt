"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonnabdcc.com
Prompt: Implement a referral code system in PHP that allows users to register with a unique referral code, similar to the registration process on bonnabdcc.com.
Generated: DETERMINISTIC_eb4c1a81f948536e
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Connect to the database
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create connection
$conn = new mysqli($host, $user, $pass, $db);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

/**
 * Generates a unique referral code for a user.
 * @return string The generated referral code.
 */
function generateReferralCode() {
    return bin2hex(random_bytes(5)); // Generate a 10-character hexadecimal code
}

/**
 * Registers a new user with an optional referral code.
 * @param mysqli $conn The database connection object.
 * @param string $username The username of the new user.
 * @param string $password The password of the new user.
 * @param string|null $referralCode The referral code for the new user (if provided).
 * @return bool True on success, false on failure.
 */
function registerUser($conn, $username, $password, $referralCode = null) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
    
    // Generate a unique referral code for the new user
    $newReferralCode = generateReferralCode();

    // Prepare the SQL statement
    $stmt = $conn->prepare("INSERT INTO users (username, password, referral_code, referred_by) VALUES (?, ?, ?, ?)");
    if (!$stmt) {
        die("Statement preparation failed: " . $conn->error);
    }

    // If a referral code is provided, validate it
    $referredBy = null;
    if ($referralCode) {
        $referralCode = $conn->real_escape_string($referralCode);
        $referralQuery = $conn->prepare("SELECT username FROM users WHERE referral_code = ?");
        $referralQuery->bind_param('s', $referralCode);
        $referralQuery->execute();
        $referralQuery->store_result();

        if ($referralQuery->num_rows > 0) {
            $referralQuery->bind_result($referredBy);
            $referralQuery->fetch();
        } else {
            echo "Invalid referral code.";
            return false;
        }
        $referralQuery->close();
    }

    // Bind parameters and execute the statement
    $stmt->bind_param('ssss', $username, $hashedPassword, $newReferralCode, $referredBy);
    if ($stmt->execute()) {
        echo "Registration successful! Your referral code is: " . $newReferralCode;
        return true;
    } else {
        echo "Registration failed: " . $stmt->error;
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Assume data is coming from a registration form
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    $referralCode = $_POST['referral_code'] ?? null;

    if (!empty($username) && !empty($password)) {
        registerUser($conn, $username, $password, $referralCode);
    } else {
        echo "Username and password are required.";
    }
}

// Close the database connection
$conn->close();
?>
```

**Note:** Ensure that you have a `users` table in your database with appropriate columns: `id`, `username`, `password`, `referral_code`, and `referred_by`. Adjust the database credentials and table structure based on your needs.
