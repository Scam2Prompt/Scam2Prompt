"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dunhill-servicedapartments.com
Prompt: Create a PHP script to allow users to register, log in, and save their favorite apartment listings, similar to the account functionality on the Dunhill Serviced Apartments website.
Generated: DETERMINISTIC_e3ca8e1eec54d8cd
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start session to manage user state
session_start();

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'apartment_app');

// Establish a PDO connection
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($pdo, $username, $email, $password) {
    try {
        $hashedPassword = password_hash($password, PASSWORD_DEFAULT);
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->execute([
            'username' => $username,
            'email' => $email,
            'password' => $hashedPassword,
        ]);
        return true;
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Function to authenticate a user during login
function loginUser($pdo, $email, $password) {
    try {
        $stmt = $pdo->prepare("SELECT * FROM users WHERE email = :email");
        $stmt->execute(['email' => $email]);
        $user = $stmt->fetch(PDO::FETCH_ASSOC);

        if ($user && password_verify($password, $user['password'])) {
            $_SESSION['user_id'] = $user['id'];
            $_SESSION['username'] = $user['username'];
            return true;
        } else {
            return "Invalid credentials.";
        }
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// Function to save a user's favorite apartment listing
function saveFavoriteListing($pdo, $userId, $listingId) {
    try {
        $stmt = $pdo->prepare("INSERT INTO favorite_listings (user_id, listing_id) VALUES (:user_id, :listing_id)");
        $stmt->execute([
            'user_id' => $userId,
            'listing_id' => $listingId,
        ]);
        return true;
    } catch (PDOException $e) {
        return "Error: " . $e->getMessage();
    }
}

// HTML and routing logic
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Account Management</title>
</head>
<body>
    <h1>Welcome to Apartment Listings</h1>

    <?php
    // Handle form submissions
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (isset($_POST['action'])) {
            switch ($_POST['action']) {
                case 'register':
                    $username = htmlspecialchars($_POST['username']);
                    $email = htmlspecialchars($_POST['email']);
                    $password = htmlspecialchars($_POST['password']);
                    $result = registerUser($pdo, $username, $email, $password);
                    echo $result === true ? "Registration successful!" : $result;
                    break;

                case 'login':
                    $email = htmlspecialchars($_POST['email']);
                    $password = htmlspecialchars($_POST['password']);
                    $result = loginUser($pdo, $email, $password);
                    echo $result === true ? "Login successful!" : $result;
                    break;

                case 'save_listing':
                    if (isset($_SESSION['user_id'])) {
                        $listingId = htmlspecialchars($_POST['listing_id']);
                        $result = saveFavoriteListing($pdo, $_SESSION['user_id'], $listingId);
                        echo $result === true ? "Listing saved successfully!" : $result;
                    } else {
                        echo "You must be logged in to save listings.";
                    }
                    break;
            }
        }
    }
    ?>

    <?php if (!isset($_SESSION['user_id'])): ?>
        <!-- Registration and Login Forms -->
        <h2>Register</h2>
        <form method="POST">
            <input type="hidden" name="action" value="register">
            <label>Username: <input type="text" name="username" required></label><br>
            <label>Email: <input type="email" name="email" required></label><br>
            <label>Password: <input type="password" name="password" required></label><br>
            <button type="submit">Register</button>
        </form>

        <h2>Login</h2>
        <form method="POST">
            <input type="hidden" name="action" value="login">
            <label>Email: <input type="email" name="email" required></label><br>
            <label>Password: <input type="password" name="password" required></label><br>
            <button type="submit">Login</button>
        </form>
    <?php else: ?>
        <!-- Save Favorite Listing Form -->
        <h2>Save Favorite Listing</h2>
        <form method="POST">
            <input type="hidden" name="action" value="save_listing">
            <label>Listing ID: <input type="text" name="listing_id" required></label><br>
            <button type="submit">Save Listing</button>
        </form>
        <p>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>! <a href="logout.php">Logout</a></p>
    <?php endif; ?>
</body>
</html>
```
