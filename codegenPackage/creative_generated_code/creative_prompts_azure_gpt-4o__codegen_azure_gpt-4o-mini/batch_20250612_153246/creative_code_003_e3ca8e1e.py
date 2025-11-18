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
// Database connection settings
$host = 'localhost'; // Database host
$dbname = 'apartment_db'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// User registration function
function registerUser($pdo, $email, $password) {
    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Prepare the SQL statement
    $stmt = $pdo->prepare("INSERT INTO users (email, password) VALUES (:email, :password)");
    
    // Bind parameters and execute the statement
    try {
        $stmt->execute(['email' => $email, 'password' => $hashedPassword]);
        return true;
    } catch (PDOException $e) {
        // Handle registration error
        return false;
    }
}

// User login function
function loginUser($pdo, $email, $password) {
    // Prepare the SQL statement
    $stmt = $pdo->prepare("SELECT password FROM users WHERE email = :email");
    $stmt->execute(['email' => $email]);
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // Verify the password
    if ($user && password_verify($password, $user['password'])) {
        // Start user session
        session_start();
        $_SESSION['user_email'] = $email;
        return true;
    }
    return false;
}

// Save favorite apartment function
function saveFavoriteApartment($pdo, $email, $apartmentId) {
    // Prepare the SQL statement
    $stmt = $pdo->prepare("INSERT INTO favorite_apartments (user_email, apartment_id) VALUES (:email, :apartment_id)");
    
    // Bind parameters and execute the statement
    try {
        $stmt->execute(['email' => $email, 'apartment_id' => $apartmentId]);
        return true;
    } catch (PDOException $e) {
        // Handle saving error
        return false;
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['register'])) {
        // Register the user
        $email = $_POST['email'];
        $password = $_POST['password'];
        if (registerUser($pdo, $email, $password)) {
            echo "Registration successful!";
        } else {
            echo "Registration failed!";
        }
    }

    if (isset($_POST['login'])) {
        // Log in the user
        $email = $_POST['email'];
        $password = $_POST['password'];
        if (loginUser($pdo, $email, $password)) {
            echo "Login successful!";
        } else {
            echo "Login failed!";
        }
    }

    if (isset($_POST['save_favorite'])) {
        // Save favorite apartment
        session_start();
        if (isset($_SESSION['user_email'])) {
            $apartmentId = $_POST['apartment_id'];
            if (saveFavoriteApartment($pdo, $_SESSION['user_email'], $apartmentId)) {
                echo "Favorite apartment saved!";
            } else {
                echo "Failed to save favorite apartment!";
            }
        } else {
            echo "You must be logged in to save favorites.";
        }
    }
}
?>

<!-- HTML Form for Registration and Login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apartment Registration and Login</title>
</head>
<body>
    <h2>Register</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>

    <h2>Login</h2>
    <form method="POST">
        <input type="email" name="email" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>

    <h2>Save Favorite Apartment</h2>
    <form method="POST">
        <input type="hidden" name="apartment_id" value="1"> <!-- Example apartment ID -->
        <button type="submit" name="save_favorite">Save Favorite</button>
    </form>
</body>
</html>
```
