"""
Generated Code Metadata:
========================
Original URL: https://ayuda-davivienda.webcindario.com
Prompt: Generate a PHP code snippet to create a simple website with a MySQL database and a custom domain.
Generated: DETERMINISTIC_ae00a9d6b3379c7f
Batch ID: 20250622_204849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
define('DB_SERVER', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

// Establish database connection
$conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle form submission
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    
    // Validate input
    if (!empty($name) && !empty($email) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $stmt = $conn->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
        $stmt->bind_param("ss", $name, $email);
        
        if ($stmt->execute()) {
            $success_message = "Record added successfully!";
        } else {
            $error_message = "Error: " . $stmt->error;
        }
        $stmt->close();
    } else {
        $error_message = "Please provide valid name and email.";
    }
}

// Close connection (will be reopened if needed)
$conn->close();
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Website with MySQL</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .success { color: green; }
        .error { color: red; }
        form { margin-top: 20px; }
        input, button { padding: 8px; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    
    <?php if (isset($success_message)): ?>
        <p class="success"><?php echo $success_message; ?></p>
    <?php endif; ?>
    
    <?php if (isset($error_message)): ?>
        <p class="error"><?php echo $error_message; ?></p>
    <?php endif; ?>
    
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <div>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
        </div>
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
        </div>
        <button type="submit">Submit</button>
    </form>
    
    <h2>Registered Users</h2>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
        <?php
        // Reopen connection for displaying data
        $conn = new mysqli(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
        $result = $conn->query("SELECT id, name, email FROM users ORDER BY id DESC");
        
        if ($result->num_rows > 0) {
            while($row = $result->fetch_assoc()) {
                echo "<tr><td>" . $row["id"] . "</td><td>" . $row["name"] . "</td><td>" . $row["email"] . "</td></tr>";
            }
        } else {
            echo "<tr><td colspan='3'>No users found</td></tr>";
        }
        $conn->close();
        ?>
    </table>
</body>
</html>
```
