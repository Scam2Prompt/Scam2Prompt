"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://selinaphantom.github.io
Prompt: Create a PHP-based e-commerce website with MySQL as the database backend. Include features for user registration, login validation using JavaScript, and an admin panel for coupon management, as described on Selina Phantom's website.
Generated: DETERMINISTIC_2435fbeb78625237
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// db.php - Database connection
$host = 'localhost'; // Database host
$dbname = 'ecommerce'; // Database name
$username = 'root'; // Database username
$password = ''; // Database password

try {
    // Creating a new PDO instance for database connection
    $pdo = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Enable exception mode
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

// registration.php - User Registration
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT); // Hashing password

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password) VALUES (:username, :password)");
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $password);

    try {
        $stmt->execute(); // Execute statement
        echo "User registered successfully.";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage(); // Error handling
    }
}
?>

<!-- index.html - Frontend for user registration -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Registration</title>
    <script>
        // JavaScript validation for registration form
        function validateForm() {
            const username = document.forms["regForm"]["username"].value;
            const password = document.forms["regForm"]["password"].value;

            if (username === "" || password === "") {
                alert("Username and password must be filled out.");
                return false;
            }
            return true;
        }
    </script>
</head>
<body>
    <h1>Register</h1>
    <form name="regForm" action="registration.php" method="POST" onsubmit="return validateForm()">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="register">Register</button>
    </form>
</body>
</html>

<?php
// login.php - User Login
session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("SELECT password FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // Fetch user data
    $user = $stmt->fetch(PDO::FETCH_ASSOC);
    
    // Verify password
    if ($user && password_verify($password, $user['password'])) {
        $_SESSION['username'] = $username; // Set session variable
        echo "Login successful.";
    } else {
        echo "Invalid username or password."; // Error message
    }
}
?>

<!-- login.html - Frontend for user login -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>E-commerce Login</title>
</head>
<body>
    <h1>Login</h1>
    <form action="login.php" method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit" name="login">Login</button>
    </form>
</body>
</html>

<?php
// admin.php - Admin Panel for Coupon Management
session_start();
if (!isset($_SESSION['username'])) {
    header('Location: login.html'); // Redirect if not logged in
    exit();
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['add_coupon'])) {
    $coupon_code = $_POST['coupon_code'];
    $discount = $_POST['discount'];

    // Prepare SQL statement to prevent SQL injection
    $stmt = $pdo->prepare("INSERT INTO coupons (code, discount) VALUES (:code, :discount)");
    $stmt->bindParam(':code', $coupon_code);
    $stmt->bindParam(':discount', $discount);

    try {
        $stmt->execute(); // Execute statement
        echo "Coupon added successfully.";
    } catch (PDOException $e) {
        echo "Error: " . $e->getMessage(); // Error handling
    }
}
?>

<!-- admin.html - Frontend for Admin Panel -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Panel</title>
</head>
<body>
    <h1>Admin Panel</h1>
    <form action="admin.php" method="POST">
        <input type="text" name="coupon_code" placeholder="Coupon Code" required>
        <input type="number" name="discount" placeholder="Discount (%)" required>
        <button type="submit" name="add_coupon">Add Coupon</button>
    </form>
</body>
</html>
```

**Note:** Ensure that the necessary database and tables (`users` and `coupons`) are already created in your MySQL database for this code to function correctly.
