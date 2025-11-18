"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://verified.myclickfunnels.com
Prompt: Generate PHP code to process form submissions from a ClickFunnels lead magnet and store the data in a MySQL database.
Generated: DETERMINISTIC_5af19e75a4ca350e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration for database connection
define('DB_HOST', 'localhost'); // Database host
define('DB_NAME', 'your_database_name'); // Database name
define('DB_USER', 'your_database_user'); // Database user
define('DB_PASS', 'your_database_password'); // Database password

/**
 * Establishes a connection to the MySQL database.
 *
 * @return PDO The database connection object.
 */
function getDatabaseConnection() {
    try {
        $dsn = "mysql:host=" . DB_HOST . ";dbname=" . DB_NAME . ";charset=utf8mb4";
        $options = [
            PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES   => false,
        ];
        return new PDO($dsn, DB_USER, DB_PASS, $options);
    } catch (PDOException $e) {
        // Log the error and exit
        error_log("Database connection failed: " . $e->getMessage());
        die("Database connection error. Please try again later.");
    }
}

// Check if the form is submitted via POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);

    // Ensure required fields are provided
    if (empty($name) || empty($email)) {
        die("Invalid form submission. Name and email are required.");
    }

    // Prepare SQL query to insert data into the database
    $query = "INSERT INTO leads (name, email, created_at) VALUES (:name, :email, NOW())";

    try {
        // Get database connection
        $pdo = getDatabaseConnection();

        // Use prepared statements to protect against SQL injection
        $stmt = $pdo->prepare($query);
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);

        // Execute the query
        $stmt->execute();

        // Provide user feedback
        echo "Lead successfully submitted!";
    } catch (PDOException $e) {
        // Log the error and notify the user
        error_log("Database query failed: " . $e->getMessage());
        die("An error occurred while processing your submission. Please try again later.");
    }
} else {
    // Handle invalid request methods
    die("Invalid request method. Please submit the form via POST.");
}
?>
```

### Notes:
1. Ensure that the database table `leads` exists in the database with columns `id`, `name`, `email`, and `created_at`.
2. Replace `your_database_name`, `your_database_user`, and `your_database_password` with appropriate credentials.
3. This code assumes the form fields are named `name` and `email`. Adjust as needed for your specific form setup.
