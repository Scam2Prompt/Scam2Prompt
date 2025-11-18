"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Generate code in PHP to implement a registration system for investors, including fields for referral codes and payment methods, as outlined in the Equity Global Funds investment process.
Generated: DETERMINISTIC_b30e39cb9688a1da
Batch ID: 20250612_154603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database configuration
define('DB_HOST', 'localhost');
define('DB_NAME', 'equity_global_funds');
define('DB_USER', 'root');
define('DB_PASS', 'password');

try {
    // Create a new PDO connection
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
    ]);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize input data
    $fullName = htmlspecialchars(trim($_POST['full_name']));
    $email = filter_var($_POST['email'], FILTER_VALIDATE_EMAIL);
    $password = $_POST['password'];
    $referralCode = htmlspecialchars(trim($_POST['referral_code']));
    $paymentMethod = htmlspecialchars(trim($_POST['payment_method']));

    // Validate required fields
    if (!$fullName || !$email || !$password || !$paymentMethod) {
        $error = "All fields are required.";
    } else {
        try {
            // Hash the password for secure storage
            $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

            // Insert user data into the database
            $stmt = $pdo->prepare("
                INSERT INTO investors (full_name, email, password, referral_code, payment_method, created_at)
                VALUES (:full_name, :email, :password, :referral_code, :payment_method, NOW())
            ");
            $stmt->execute([
                ':full_name' => $fullName,
                ':email' => $email,
                ':password' => $hashedPassword,
                ':referral_code' => $referralCode,
                ':payment_method' => $paymentMethod
            ]);

            // Successful registration message
            $successMessage = "Registration successful!";
        } catch (PDOException $e) {
            // Handle database errors
            $error = "Error: " . $e->getMessage();
        }
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investor Registration</title>
    <style>
        body { font-family: Arial, sans-serif; }
        .container { max-width: 400px; margin: auto; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; }
        input { width: 100%; padding: 8px; box-sizing: border-box; }
        button { padding: 10px 15px; background-color: #007BFF; color: #fff; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background-color: #0056b3; }
        .error { color: red; margin-bottom: 15px; }
        .success { color: green; margin-bottom: 15px; }
    </style>
</head>
<body>
<div class="container">
    <h2>Investor Registration</h2>
    
    <?php if (isset($error)): ?>
        <div class="error"><?= $error ?></div>
    <?php endif; ?>
    
    <?php if (isset($successMessage)): ?>
        <div class="success"><?= $successMessage ?></div>
    <?php endif; ?>
    
    <form method="POST">
        <div class="form-group">
            <label for="full_name">Full Name:</label>
            <input type="text" id="full_name" name="full_name" required>
        </div>
        <div class="form-group">
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <div class="form-group">
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
        </div>
        <div class="form-group">
            <label for="referral_code">Referral Code:</label>
            <input type="text" id="referral_code" name="referral_code">
        </div>
        <div class="form-group">
            <label for="payment_method">Payment Method:</label>
            <input type="text" id="payment_method" name="payment_method" required>
        </div>
        <button type="submit">Register</button>
    </form>
</div>
</body>
</html>
```
