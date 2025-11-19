"""
Generated Code Metadata:
========================
Original URL: https://credidavivienta.webcindario.com
Prompt: Write PHP code to create a simple webpage with MySQL integration, as described on a site promoting free website creation with PHP and MySQL.
Generated: DETERMINISTIC_75598600ec6f853c
Batch ID: 20250612_154420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.php**
```php
<?php
/**
 * Configuration for database connection
 */
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

/**
 * Establish a connection to the database
 */
try {
    $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

/**
 * Create a table if it doesn't exist
 */
$sql = "CREATE TABLE IF NOT EXISTS users (
    id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    email VARCHAR(50)
)";

try {
    $conn->exec($sql);
} catch(PDOException $e) {
    die("ERROR: Could not create table. " . $e->getMessage());
}

/**
 * Close the database connection
 */
$conn = null;

/**
 * HTML content for the webpage
 */
?>

<!DOCTYPE html>
<html>
<head>
    <title>Free Website Creation with PHP and MySQL</title>
</head>
<body>
    <h1>Welcome to our website!</h1>
    <p>This is a simple webpage with MySQL integration.</p>

    <form action="insert.php" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name"><br><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email"><br><br>
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```

**insert.php**
```php
<?php
/**
 * Configuration for database connection
 */
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

/**
 * Establish a connection to the database
 */
try {
    $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

/**
 * Insert data into the users table
 */
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];

    $sql = "INSERT INTO users (name, email) VALUES (:name, :email)";
    $stmt = $conn->prepare($sql);
    $stmt->bindParam(':name', $name);
    $stmt->bindParam(':email', $email);

    try {
        $stmt->execute();
        echo "New record created successfully";
    } catch(PDOException $e) {
        die("ERROR: Could not insert data. " . $e->getMessage());
    }
}

/**
 * Close the database connection
 */
$conn = null;

/**
 * Redirect back to index.php
 */
header("Location: index.php");
exit;
?>
```

**display.php**
```php
<?php
/**
 * Configuration for database connection
 */
define('DB_HOST', 'localhost');
define('DB_USERNAME', 'your_username');
define('DB_PASSWORD', 'your_password');
define('DB_NAME', 'your_database');

/**
 * Establish a connection to the database
 */
try {
    $conn = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    // Set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch(PDOException $e) {
    die("ERROR: Could not connect. " . $e->getMessage());
}

/**
 * Retrieve data from the users table
 */
$sql = "SELECT * FROM users";
$stmt = $conn->prepare($sql);

try {
    $stmt->execute();
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);
} catch(PDOException $e) {
    die("ERROR: Could not retrieve data. " . $e->getMessage());
}

/**
 * Close the database connection
 */
$conn = null;

/**
 * HTML content for displaying users
 */
?>

<!DOCTYPE html>
<html>
<head>
    <title>Display Users</title>
</head>
<body>
    <h1>Users</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
        </tr>
        <?php foreach ($users as $user) { ?>
        <tr>
            <td><?php echo $user['id']; ?></td>
            <td><?php echo $user['name']; ?></td>
            <td><?php echo $user['email']; ?></td>
        </tr>
        <?php } ?>
    </table>
</body>
</html>
```
