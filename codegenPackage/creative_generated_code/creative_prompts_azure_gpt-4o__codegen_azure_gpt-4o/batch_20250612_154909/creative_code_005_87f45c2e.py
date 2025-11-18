"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getinge-torin.com
Prompt: Develop a PHP script to implement a login system with username and password validation, including a feature to toggle password visibility, inspired by the Torin portal.
Generated: DETERMINISTIC_87f45c2e5e7859c8
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to manage user login state and store error messages.
session_start();

// Database connection variables
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "torin_portal";

// Establish a connection to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check if the database connection is successful
if ($conn->connect_error) {
    die("Database connection failed: " . $conn->connect_error);
}

// Function to sanitize user input to prevent SQL injection and XSS
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $user = sanitizeInput($_POST['username']);
    $pass = sanitizeInput($_POST['password']);

    // Check if both fields are filled
    if (empty($user) || empty($pass)) {
        $_SESSION['error'] = "Username and password are required.";
    } else {
        // Prepare a secure SQL statement
        $stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
        $stmt->bind_param("s", $user);
        $stmt->execute();
        $stmt->store_result();

        // Check if the user exists
        if ($stmt->num_rows > 0) {
            $stmt->bind_result($hashedPassword);
            $stmt->fetch();

            // Validate the password
            if (password_verify($pass, $hashedPassword)) {
                $_SESSION['username'] = $user; // Set session variable to log in user
                header("Location: dashboard.php"); // Redirect to the dashboard
                exit();
            } else {
                $_SESSION['error'] = "Invalid password.";
            }
        } else {
            $_SESSION['error'] = "Username not found.";
        }

        $stmt->close();
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Torin Portal</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            width: 300px;
        }
        .login-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #333333;
        }
        .login-container label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        .login-container input {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #cccccc;
            border-radius: 4px;
            font-size: 16px;
        }
        .login-container button {
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #ffffff;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            cursor: pointer;
        }
        .login-container button:hover {
            background-color: #0056b3;
        }
        .toggle-password {
            cursor: pointer;
            position: absolute;
            right: 15px;
            top: 45px;
            font-size: 14px;
            color: #007bff;
        }
        .error-message {
            color: red;
            font-size: 14px;
            margin-bottom: 15px;
        }
    </style>
    <script>
        // Function to toggle password visibility
        function togglePassword() {
            const passwordInput = document.getElementById('password');
            const toggleText = document.getElementById('toggle-password');
            if (passwordInput.type === 'password') {
                passwordInput.type = 'text';
                toggleText.textContent = 'Hide';
            } else {
                passwordInput.type = 'password';
                toggleText.textContent = 'Show';
            }
        }
    </script>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <!-- Display error messages if any -->
        <?php if (isset($_SESSION['error'])): ?>
            <p class="error-message"><?php echo $_SESSION['error']; unset($_SESSION['error']); ?></p>
        <?php endif; ?>
        <form method="POST" action="">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password</label>
            <div style="position: relative;">
                <input type="password" id="password" name="password" required>
                <span id="toggle-password" class="toggle-password" onclick="togglePassword()">Show</span>
            </div>
            <button type="submit">Login</button>
        </form>
    </div>
</body>
</html>
```
