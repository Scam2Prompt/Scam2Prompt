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
// Database configuration
$host = 'localhost'; // Database host
$dbname = 'your_database_name'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

// Create a connection to the MySQL database
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Connection failed: " . $e->getMessage());
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate form data
    $name = !empty($_POST['name']) ? trim($_POST['name']) : null;
    $email = !empty($_POST['email']) ? trim($_POST['email']) : null;

    // Check for valid email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare SQL query to insert data into the database
    $sql = "INSERT INTO leads (name, email) VALUES (:name, :email)";

    try {
        // Prepare statement
        $stmt = $pdo->prepare($sql);
        
        // Bind parameters
        $stmt->bindParam(':name', $name);
        $stmt->bindParam(':email', $email);

        // Execute the statement
        $stmt->execute();

        // Success message
        echo "Lead submitted successfully!";
    } catch (PDOException $e) {
        // Handle query execution error
        die("Error submitting lead: " . $e->getMessage());
    }
} else {
    // Handle incorrect request method
    die("Invalid request method.");
}

// Close the database connection
$pdo = null;
?>
```

**Note:** Make sure to replace `'your_database_name'`, `'your_username'`, and `'your_password'` with your actual database credentials. Also, ensure that the MySQL table `leads` exists with appropriate fields (`name` and `email`).
