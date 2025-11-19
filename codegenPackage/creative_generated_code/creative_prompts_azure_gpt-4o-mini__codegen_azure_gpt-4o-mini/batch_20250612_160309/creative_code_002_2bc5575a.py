"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megapromining.live
Prompt: Create a PHP code snippet that allows users to register for an account on Megapromining and handle user input securely.
Generated: DETERMINISTIC_2bc5575a9c2a432e
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Secure Database Connection
$host = 'localhost'; // Database host
$db = 'megapromining'; // Database name
$user = 'root'; // Database username
$pass = ''; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

// Function to register a new user
function registerUser($username, $password, $email) {
    global $pdo;

    // Validate input data
    if (empty($username) || empty($password) || empty($email)) {
        throw new InvalidArgumentException("All fields are required.");
    }

    // Hash the password for security
    $hashedPassword = password_hash($password, PASSWORD_BCRYPT);

    // Prepare SQL statement to avoid SQL injection
    $stmt = $pdo->prepare("INSERT INTO users (username, password, email) VALUES (:username, :password, :email)");

    // Bind parameters
    $stmt->bindParam(':username', $username);
    $stmt->bindParam(':password', $hashedPassword);
    $stmt->bindParam(':email', $email);

    // Execute the statement and handle potential errors
    try {
        $stmt->execute();
        return "User registered successfully!";
    } catch (PDOException $e) {
        if ($e->getCode() === 23000) {
            // Handle unique constraint violation (e.g., duplicate username/email)
            throw new Exception("Username or email already exists.");
        } else {
            // Handle any other database errors
            throw new Exception("Error registering user: " . $e->getMessage());
        }
    }
}

// Example usage
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    try {
        // Sanitize user input to prevent XSS attacks
        $username = htmlspecialchars(trim($_POST['username']));
        $password = htmlspecialchars(trim($_POST['password']));
        $email = htmlspecialchars(trim($_POST['email']));

        // Register the user and echo the result
        echo registerUser($username, $password, $email);
    } catch (Exception $e) {
        // Display error message
        echo "Registration failed: " . $e->getMessage();
    } catch (InvalidArgumentException $e) {
        // Handle validation errors
        echo "Validation error: " . $e->getMessage();
    }
}
?>
```

**Note:** This code assumes you have a database named `megapromining` and a `users` table with columns `username`, `password`, and `email`. You should also ensure that error messages do not expose sensitive information in a production environment.
