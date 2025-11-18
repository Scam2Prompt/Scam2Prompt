"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Develop a registration form in HTML and PHP for a gaming platform, ensuring ease of use and security, similar to MESIN128's registration process.
Generated: DETERMINISTIC_05e6f2708a251bed
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### `registration_form.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gaming Platform Registration</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="registration-container">
        <h1>Register for Gaming Platform</h1>
        <form action="register.php" method="POST">
            <!-- Username Field -->
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required maxlength="20" autocomplete="off">

            <!-- Email Field -->
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required autocomplete="off">

            <!-- Password Field -->
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required minlength="8">

            <!-- Confirm Password Field -->
            <label for="confirm_password">Confirm Password:</label>
            <input type="password" id="confirm_password" name="confirm_password" required minlength="8">

            <!-- Submit Button -->
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>
```

### `register.php`
```php
<?php
// Start the session to handle flash messages or session data
session_start();

// Utility function for sanitizing user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Database connection parameters
$db_host = "localhost";
$db_user = "root";
$db_pass = "password";
$db_name = "gaming_platform";

try {
    // Establish a secure connection to the database using PDO
    $pdo = new PDO("mysql:host=$db_host;dbname=$db_name;charset=utf8", $db_user, $db_pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Sanitize and validate input fields
    $username = sanitizeInput($_POST["username"]);
    $email = sanitizeInput($_POST["email"]);
    $password = sanitizeInput($_POST["password"]);
    $confirm_password = sanitizeInput($_POST["confirm_password"]);

    // Validate password match
    if ($password !== $confirm_password) {
        die("Passwords do not match. Please try again.");
    }

    // Hash the password for secure storage
    $hashed_password = password_hash($password, PASSWORD_BCRYPT);

    try {
        // Check if the username or email already exists
        $stmt = $pdo->prepare("SELECT COUNT(*) FROM users WHERE username = :username OR email = :email");
        $stmt->execute(["username" => $username, "email" => $email]);
        $user_exists = $stmt->fetchColumn();

        if ($user_exists) {
            die("Username or Email already exists. Please try a different one.");
        }

        // Insert the new user into the database
        $stmt = $pdo->prepare("INSERT INTO users (username, email, password) VALUES (:username, :email, :password)");
        $stmt->execute([
            "username" => $username,
            "email" => $email,
            "password" => $hashed_password
        ]);

        echo "Registration successful! You can now log in.";
    } catch (PDOException $e) {
        // Handle database interaction errors
        die("An error occurred while processing your request. Please try again later.");
    }
}
?>
```

### `styles.css`
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.registration-container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

h1 {
    text-align: center;
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 5px;
    font-weight: bold;
}

input {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```
