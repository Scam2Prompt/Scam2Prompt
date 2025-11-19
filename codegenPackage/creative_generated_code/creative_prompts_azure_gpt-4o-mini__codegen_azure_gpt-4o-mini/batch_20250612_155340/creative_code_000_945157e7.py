"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davihncas230.webcindario.com
Prompt: How can I create a free website using PHP and MySQL as mentioned on the site?
Generated: DETERMINISTIC_945157e7745a10be
Batch ID: 20250612_155340
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Handles database connection
class Database {
    private $host = 'localhost'; // Database host
    private $db_name = 'your_database_name'; // Database name
    private $username = 'your_username'; // Database username
    private $password = 'your_password'; // Database password
    public $connection;

    // Method to get database connection
    public function getConnection() {
        $this->connection = null;
        try {
            // Create a new PDO instance
            $this->connection = new PDO("mysql:host={$this->host};dbname={$this->db_name}", $this->username, $this->password);
            // Set the PDO error mode to exception
            $this->connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            // Handle connection error
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->connection;
    }
}

// user.php - User handling class
class User {
    private $connection;
    private $table_name = 'users'; // Table name

    // Constructor receives the database connection
    public function __construct($db) {
        $this->connection = $db;
    }

    // Method to create a new user
    public function create($username, $password) {
        // Prepare the SQL statement
        $query = "INSERT INTO " . $this->table_name . " (username, password) VALUES (:username, :password)";

        // Prepare the statement
        $stmt = $this->connection->prepare($query);

        // Sanitize inputs
        $username = htmlspecialchars(strip_tags($username));
        $password = password_hash($password, PASSWORD_BCRYPT); // Hash the password

        // Bind the parameters
        $stmt->bindParam(':username', $username);
        $stmt->bindParam(':password', $password);

        // Execute the statement
        if ($stmt->execute()) {
            return true;
        }
        
        return false; // Return false if unable to create user
    }
}

// index.php - Main entry point
require_once 'database.php';
require_once 'user.php';

// Create a database connection
$database = new Database();
$db = $database->getConnection();

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // Create a new user object
    $user = new User($db);

    // Attempt to create the user
    if ($user->create($username, $password)) {
        echo "User created successfully.";
    } else {
        echo "Unable to create user. Please try again.";
    }
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create User</title>
</head>
<body>
    <h2>Create a Free Account</h2>
    <form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
        <label for="username">Username:</label>
        <input type="text" name="username" required>
        <br>
        <label for="password">Password:</label>
        <input type="password" name="password" required>
        <br>
        <input type="submit" value="Create Account">
    </form>
</body>
</html>
```

### Note:
- Replace `your_database_name`, `your_username`, and `your_password` with actual database credentials.
- Ensure that the MySQL database has a users table with appropriate columns (`username` and `password`) created before using this code.
