"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metlifeinvests.com
Prompt: Write a PHP script to handle user account creation and investment plan purchases, as outlined in MET LIFE INVESTS' "How to Get Started" section.
Generated: DETERMINISTIC_dc9b3be69fed6734
Batch ID: 20250612_151506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// UserAccountManager.php

class UserAccountManager
{
    private $dbConnection;

    // Constructor to initialize the database connection
    public function __construct($dbHost, $dbUser, $dbPass, $dbName)
    {
        // Create a new database connection using mysqli
        $this->dbConnection = new mysqli($dbHost, $dbUser, $dbPass, $dbName);

        // Check for connection errors
        if ($this->dbConnection->connect_error) {
            die("Connection failed: " . $this->dbConnection->connect_error);
        }
    }

    // Method to create a new user account
    public function createUser($username, $password, $email)
    {
        // Sanitize user input to prevent SQL injection
        $username = $this->dbConnection->real_escape_string($username);
        $password = password_hash($password, PASSWORD_BCRYPT); // Hash the password for security
        $email = $this->dbConnection->real_escape_string($email);

        // Prepare SQL statement
        $sql = "INSERT INTO users (username, password, email) VALUES ('$username', '$password', '$email')";

        // Execute the query and handle errors
        if ($this->dbConnection->query($sql) === TRUE) {
            return "User account created successfully.";
        } else {
            return "Error: " . $this->dbConnection->error;
        }
    }

    // Method to purchase an investment plan
    public function purchaseInvestmentPlan($username, $planId)
    {
        // Sanitize user input
        $username = $this->dbConnection->real_escape_string($username);
        $planId = (int)$planId; // Cast to integer for security

        // Prepare SQL statement
        $sql = "INSERT INTO investments (username, plan_id) VALUES ('$username', '$planId')";

        // Execute the query and handle errors
        if ($this->dbConnection->query($sql) === TRUE) {
            return "Investment plan purchased successfully.";
        } else {
            return "Error: " . $this->dbConnection->error;
        }
    }

    // Destructor to close the database connection
    public function __destruct()
    {
        $this->dbConnection->close();
    }
}

// Example usage
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    // Database connection parameters
    $dbHost = 'localhost';
    $dbUser = 'root';
    $dbPass = '';
    $dbName = 'metlife_invests';

    // Create an instance of UserAccountManager
    $userManager = new UserAccountManager($dbHost, $dbUser, $dbPass, $dbName);

    // Handle user account creation
    if (isset($_POST['action']) && $_POST['action'] === 'create_user') {
        $username = $_POST['username'];
        $password = $_POST['password'];
        $email = $_POST['email'];

        // Create user account
        $response = $userManager->createUser($username, $password, $email);
        echo $response;
    }

    // Handle investment plan purchase
    elseif (isset($_POST['action']) && $_POST['action'] === 'purchase_plan') {
        $username = $_POST['username'];
        $planId = $_POST['plan_id'];

        // Purchase investment plan
        $response = $userManager->purchaseInvestmentPlan($username, $planId);
        echo $response;
    }
}
?>
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Account Creation and Investment Plans</title>
</head>
<body>
    <h1>User Account Creation</h1>
    <form method="POST" action="UserAccountManager.php">
        <input type="hidden" name="action" value="create_user">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" required>
        <br>
        <button type="submit">Create Account</button>
    </form>

    <h1>Purchase Investment Plan</h1>
    <form method="POST" action="UserAccountManager.php">
        <input type="hidden" name="action" value="purchase_plan">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="plan_id">Investment Plan ID:</label>
        <input type="number" name="plan_id" required>
        <br>
        <button type="submit">Purchase Plan</button>
    </form>
</body>
</html>
```
