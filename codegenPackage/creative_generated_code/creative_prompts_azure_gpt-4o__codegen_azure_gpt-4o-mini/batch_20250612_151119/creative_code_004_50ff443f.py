"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nkbihfbeogaeaobhlefnkodbefgpgknn.com
Prompt: Write a PHP script to implement a user registration system for UFABET's boxing betting platform, including features like mobile number verification.
Generated: DETERMINISTIC_50ff443fbaae7af3
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// User Registration System for UFABET Boxing Betting Platform

// Database Configuration
$host = 'localhost'; // Database host
$db = 'ufabet';      // Database name
$user = 'root';      // Database username
$pass = '';          // Database password

// Create a database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to send verification SMS (stubbed for simplicity)
function sendVerificationSms($mobileNumber, $verificationCode) {
    // Implement SMS sending logic here (using an SMS gateway API)
    // This function should return true if SMS is sent successfully, false otherwise
    return true;
}

// Function to register a new user
function registerUser($mobileNumber, $verificationCode) {
    global $pdo;

    // Check if the mobile number is already registered
    $stmt = $pdo->prepare("SELECT * FROM users WHERE mobile_number = :mobile_number");
    $stmt->execute(['mobile_number' => $mobileNumber]);
    
    if ($stmt->rowCount() > 0) {
        return "This mobile number is already registered.";
    }

    // Insert new user into the database
    $stmt = $pdo->prepare("INSERT INTO users (mobile_number, verification_code) VALUES (:mobile_number, :verification_code)");
    
    if ($stmt->execute(['mobile_number' => $mobileNumber, 'verification_code' => $verificationCode])) {
        // Send verification SMS
        if (sendVerificationSms($mobileNumber, $verificationCode)) {
            return "Registration successful! A verification code has been sent to your mobile number.";
        } else {
            return "Registration successful, but failed to send verification SMS.";
        }
    } else {
        return "Registration failed, please try again.";
    }
}

// Function to verify the user's mobile number
function verifyUser($mobileNumber, $verificationCode) {
    global $pdo;

    // Check if the verification code matches
    $stmt = $pdo->prepare("SELECT * FROM users WHERE mobile_number = :mobile_number AND verification_code = :verification_code");
    $stmt->execute(['mobile_number' => $mobileNumber, 'verification_code' => $verificationCode]);

    if ($stmt->rowCount() > 0) {
        // Update user status to verified
        $stmt = $pdo->prepare("UPDATE users SET is_verified = 1 WHERE mobile_number = :mobile_number");
        if ($stmt->execute(['mobile_number' => $mobileNumber])) {
            return "Mobile number verified successfully!";
        } else {
            return "Failed to update verification status.";
        }
    } else {
        return "Verification failed. Invalid mobile number or verification code.";
    }
}

// Example usage
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate input
    if (isset($_POST['action'])) {
        $action = $_POST['action'];
        $mobileNumber = $_POST['mobile_number'];
        
        // Generate a random verification code
        $verificationCode = rand(100000, 999999);
        
        if ($action === 'register') {
            // Register user
            $message = registerUser($mobileNumber, $verificationCode);
            echo $message;
        } elseif ($action === 'verify') {
            $code = $_POST['verification_code'];
            // Verify user
            $message = verifyUser($mobileNumber, $code);
            echo $message;
        }
    }
}

?>

<!-- HTML Form for User Registration and Verification -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Registration</title>
</head>
<body>
    <h2>User Registration</h2>
    <form method="POST">
        <input type="text" name="mobile_number" placeholder="Mobile Number" required>
        <input type="hidden" name="action" value="register">
        <button type="submit">Register</button>
    </form>

    <h2>Verify Mobile Number</h2>
    <form method="POST">
        <input type="text" name="mobile_number" placeholder="Mobile Number" required>
        <input type="text" name="verification_code" placeholder="Verification Code" required>
        <input type="hidden" name="action" value="verify">
        <button type="submit">Verify</button>
    </form>
</body>
</html>
```
