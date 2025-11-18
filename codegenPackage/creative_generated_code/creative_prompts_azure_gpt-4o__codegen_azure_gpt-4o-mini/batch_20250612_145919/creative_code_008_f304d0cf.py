"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatangame.games
Prompt: Write a code snippet in PHP for securely handling user registration and login processes, including bonus allocation upon signup, as described on BaxBet.
Generated: DETERMINISTIC_f304d0cf3ddbde09
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Database connection settings
$host = 'localhost'; // Database host
$db = 'your_database'; // Database name
$user = 'your_username'; // Database username
$pass = 'your_password'; // Database password

// Create a new PDO instance for database connection
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to handle user registration
 * 
 * @param string $username The username of the user
 * @param string $password The password of the user
 * @return bool True on success, false on failure
 */
function registerUser($username, $password) {
    global $pdo;

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare SQL query to insert the new user
    $sql = "INSERT INTO users (username, password, bonus) VALUES (:username, :password, :bonus)";
    $bonusAllocation = 100; // Example bonus amount for new signup

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['username' => $username, 'password' => $hashedPassword, 'bonus' => $bonusAllocation]);
        return true; // User registered successfully
    } catch (PDOException $e) {
        // Handle registration error
        echo "Registration failed: " . $e->getMessage();
        return false;
    }
}

/**
 * Function to handle user login
 * 
 * @param string $username The username of the user
 * @param string $password The password of the user
 * @return bool True if login is successful, false otherwise
 */
function loginUser($username, $password) {
    global $pdo;

    // Prepare SQL query to fetch the user
    $sql = "SELECT password FROM users WHERE username = :username";

    try {
        $stmt = $pdo->prepare($sql);
        $stmt->execute(['username' => $username]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        // Verify the password against the hashed password
        if ($user && password_verify($password, $user['password'])) {
            return true; // Login successful
        } else {
            return false; // Invalid username or password
        }
    } catch (PDOException $e) {
        // Handle login error
        echo "Login failed: " . $e->getMessage();
        return false;
    }
}

// Example usage:
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        $username = $_POST['username'] ?? '';
        $password = $_POST['password'] ?? '';
        registerUser($username, $password);
    } elseif (isset($_POST['login'])) {
        $username = $_POST['username'] ?? '';
        $password = $_POST['password'] ?? '';
        if (loginUser($username, $password)) {
            echo "Login successful!";
        } else {
            echo "Invalid username or password.";
        }
    }
}
?>
```
