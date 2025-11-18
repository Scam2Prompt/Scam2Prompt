"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nequipsee.webcindario.com
Prompt: Create a PHP script to handle form submissions and store the data in a MySQL database.
Generated: DETERMINISTIC_0eaa910caf26238f
Batch ID: 20250612_151047
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// database.php - Database connection script
class Database {
    private $host = 'localhost';
    private $db_name = 'your_database_name';
    private $username = 'your_username';
    private $password = 'your_password';
    public $conn;

    // Function to establish a database connection
    public function getConnection() {
        $this->conn = null;
        try {
            $this->conn = new PDO("mysql:host={$this->host};dbname={$this->db_name}", $this->username, $this->password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        } catch (PDOException $exception) {
            echo "Connection error: " . $exception->getMessage();
        }
        return $this->conn;
    }
}

// form_handler.php - Form submission handling script
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate the input data
    if (empty($name) || empty($email) || empty($message)) {
        die('Error: Please fill in all fields.');
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die('Error: Invalid email format.');
    }

    // Include database connection
    include_once 'database.php';
    $database = new Database();
    $db = $database->getConnection();

    // Prepare the SQL statement
    $query = "INSERT INTO submissions (name, email, message) VALUES (:name, :email, :message)";
    $stmt = $db->prepare($query);

    // Bind parameters
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);
    $stmt->bindParam(':message', $message);

    // Execute the query and check for success
    try {
        if ($stmt->execute()) {
            echo "Form submission successful!";
        } else {
            echo "Error: Unable to submit the form.";
        }
    } catch (PDOException $exception) {
        echo "Error: " . $exception->getMessage();
    }
} else {
    // Handle invalid requests
    die('Error: Invalid request method.');
}
```

### Database Table Structure
```sql
CREATE TABLE `submissions` (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    `email` VARCHAR(255) NOT NULL,
    `message` TEXT NOT NULL,
    PRIMARY KEY (`id`)
);
```

### Usage
- Save the PHP code in `form_handler.php` and `database.php`.
- Update database credentials in `database.php`.
- Create the `submissions` table in your MySQL database using the provided SQL script.
- POST data to `form_handler.php` through a form with `name`, `email`, and `message` fields.
