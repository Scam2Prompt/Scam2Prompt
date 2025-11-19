"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daviplataseeg.webcindario.com
Prompt: What are the steps to set up a website with PHP and MySQL for free?
Generated: DETERMINISTIC_8fee6b4e37d7a9d3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Step 1: Configuration for the database connection
// Ensure you have MySQL installed and running locally or remotely.
$servername = "localhost"; // Change to your server address if not localhost
$username = "root";        // Replace with your MySQL username
$password = "";            // Replace with your MySQL password
$dbname = "my_website";    // The name of your database

// Step 2: Establish a connection to the MySQL database
try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    // Set the PDO error mode to exception for better error handling.
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Database connection successful!<br>";
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Step 3: Create a table if not exists
try {
    $table_sql = "CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )";
    $conn->exec($table_sql);
    echo "Table 'users' created successfully!<br>";
} catch (PDOException $e) {
    die("Table creation failed: " . $e->getMessage());
}

// Step 4: Insert sample data into the table
try {
    $insert_sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $conn->prepare($insert_sql);
    $stmt->execute([
        ':name' => 'John Doe', 
        ':email' => 'john.doe@example.com'
    ]);
    echo "Sample data inserted successfully!<br>";
} catch (PDOException $e) {
    die("Data insertion failed: " . $e->getMessage());
}

// Step 5: Fetch and display data from the table
try {
    $select_sql = "SELECT * FROM users";
    $stmt = $conn->query($select_sql);
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo "Fetched data:<br>";
    foreach ($users as $user) {
        echo "ID: {$user['id']}, Name: {$user['name']}, Email: {$user['email']}, Created At: {$user['created_at']}<br>";
    }
} catch (PDOException $e) {
    die("Data retrieval failed: " . $e->getMessage());
}

// Step 6: Close the database connection
$conn = null;

// Notes:
// - This script assumes that you already have a PHP server installed (e.g., XAMPP, WAMP, or a live server).
// - Make sure you have created a MySQL database named "my_website" or change the `$dbname` variable above.
// - Save this script in a `.php` file and access it via the browser to test.
// - For production, ensure sensitive credentials are stored securely, and use environment variables for configuration.

?>
```
