"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Create a PHP script that interacts with a MySQL database using PEAR libraries.
Generated: DETERMINISTIC_2fbef771f7193172
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Include the PEAR DB library
require_once 'DB.php';

// Database connection parameters
$dsn = 'mysql://username:password@localhost/database_name'; // Update with your DB credentials
$options = array(
    'debug' => 2, // Set to 0 for production
    'portability' => DB_PORTABILITY_ALL,
);

// Establish a database connection
$db = DB::connect($dsn, $options);

// Check for a successful connection
if (PEAR::isError($db)) {
    die('Database connection failed: ' . $db->getMessage());
}

// Function to fetch all users from the database
function fetchAllUsers($db) {
    // Prepare the SQL query
    $query = 'SELECT * FROM users'; // Update with your table name

    // Execute the query
    $result = $db->query($query);

    // Check for query execution errors
    if (PEAR::isError($result)) {
        die('Query failed: ' . $result->getMessage());
    }

    // Fetch all results
    $users = array();
    while ($row = $result->fetchRow(DB_FETCHMODE_ASSOC)) {
        $users[] = $row;
    }

    return $users;
}

// Function to insert a new user into the database
function insertUser($db, $username, $email) {
    // Prepare the SQL query
    $query = 'INSERT INTO users (username, email) VALUES (?, ?)'; // Update with your table name

    // Prepare the statement
    $stmt = $db->prepare($query);

    // Check for statement preparation errors
    if (PEAR::isError($stmt)) {
        die('Statement preparation failed: ' . $stmt->getMessage());
    }

    // Execute the statement with parameters
    $result = $stmt->execute(array($username, $email));

    // Check for execution errors
    if (PEAR::isError($result)) {
        die('Insert failed: ' . $result->getMessage());
    }

    return $db->getLastInsertID(); // Return the ID of the newly inserted user
}

// Example usage
try {
    // Fetch all users
    $users = fetchAllUsers($db);
    echo "Users fetched successfully:\n";
    print_r($users);

    // Insert a new user
    $newUserId = insertUser($db, 'newuser', 'newuser@example.com');
    echo "New user inserted with ID: $newUserId\n";

} catch (Exception $e) {
    // Handle any exceptions
    echo 'An error occurred: ' . $e->getMessage();
}

// Close the database connection
$db->disconnect();
?>
```
