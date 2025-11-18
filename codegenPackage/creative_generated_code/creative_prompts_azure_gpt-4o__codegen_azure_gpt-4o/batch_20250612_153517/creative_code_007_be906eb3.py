"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://republik.pages.dev
Prompt: Develop a PHP script to handle user registration and deposit functionality for an online slot platform, with a minimum deposit of 20,000 IDR, as specified on ANGKA805.
Generated: DETERMINISTIC_be906eb3353c794a
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to track user login
session_start();

// Database connection settings
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'angka805');

// Minimum deposit amount in IDR
define('MIN_DEPOSIT_AMOUNT', 20000);

try {
    // Establish database connection using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email)
{
    global $pdo;

    // Input validation
    if (empty($username) || empty($password) || empty($email)) {
        throw new Exception("All fields are required.");
    }

    // Check if username already exists
    $stmt = $pdo->prepare("SELECT id FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);

    if ($stmt->rowCount() > 0) {
        throw new Exception("Username already exists.");
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Insert user into database
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");
    $stmt->execute([
        'username' => $username,
        'password' => $hashedPassword,
        'email' => $email
    ]);

    return true;
}

// Function to handle deposits
function depositFunds($userId, $amount)
{
    global $pdo;

    // Validate deposit amount
    if ($amount < MIN_DEPOSIT_AMOUNT) {
        throw new Exception("Minimum deposit amount is " . MIN_DEPOSIT_AMOUNT . " IDR.");
    }

    // Check if user exists
    $stmt = $pdo->prepare("SELECT id FROM users WHERE id = :id");
    $stmt->execute(['id' => $userId]);

    if ($stmt->rowCount() === 0) {
        throw new Exception("User not found.");
    }

    // Record deposit in database
    $stmt = $pdo->prepare("INSERT INTO deposits (user_id, amount, date) VALUES (:user_id, :amount, NOW())");
    $stmt->execute([
        'user_id' => $userId,
        'amount' => $amount
    ]);

    return true;
}

// Entry point for handling form submissions
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        if (isset($_POST['action'])) {
            if ($_POST['action'] === 'register') {
                // Handle user registration
                $username = htmlspecialchars($_POST['username']);
                $password = $_POST['password'];
                $email = htmlspecialchars($_POST['email']);

                if (registerUser($username, $password, $email)) {
                    echo "User registered successfully!";
                }
            } elseif ($_POST['action'] === 'deposit') {
                // Handle deposit functionality
                if (!isset($_SESSION['user_id'])) {
                    throw new Exception("You must be logged in to make a deposit.");
                }

                $amount = floatval($_POST['amount']);
                if (depositFunds($_SESSION['user_id'], $amount)) {
                    echo "Deposit successful!";
                }
            } else {
                throw new Exception("Invalid action.");
            }
        }
    } catch (Exception $e) {
        echo "Error: " . $e->getMessage();
    }
}
?>

<!-- HTML Form for User Registration -->
<form method="POST">
    <h2>User Registration</h2>
    <label for="username">Username:</label>
    <input type="text" name="username" id="username" required><br>
    <label for="password">Password:</label>
    <input type="password" name="password" id="password" required><br>
    <label for="email">Email:</label>
    <input type="email" name="email" id="email" required><br>
    <input type="hidden" name="action" value="register">
    <button type="submit">Register</button>
</form>

<!-- HTML Form for Deposit -->
<form method="POST">
    <h2>Deposit Funds</h2>
    <label for="amount">Deposit Amount (IDR):</label>
    <input type="number" name="amount" id="amount" required><br>
    <input type="hidden" name="action" value="deposit">
    <button type="submit">Deposit</button>
</form>
```
