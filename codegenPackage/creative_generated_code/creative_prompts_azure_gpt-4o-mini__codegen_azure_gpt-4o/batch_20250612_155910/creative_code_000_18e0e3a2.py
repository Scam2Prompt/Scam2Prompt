"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ct.ws
Prompt: How can I create a free website using the ct.ws domain with InfinityFree, and what are the steps for setting up PHP and MySQL?
Generated: DETERMINISTIC_18e0e3a279821a61
Batch ID: 20250612_155910
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://infinityfree.net/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the PHP code for connecting to a MySQL database and setting up a basic PHP application. Assume you have already registered your free website with the `ct.ws` domain via InfinityFree, and you are ready to use their free hosting services. This code focuses on setting up PHP and MySQL functionality.

```php
<?php
/**
 * PHP script for connecting to MySQL and creating a basic application.
 * This code assumes you have already set up your hosting on InfinityFree
 * and linked your domain (e.g., example.ct.ws).
 */

// Database configuration
define('DB_HOST', 'sqlXXX.epizy.com'); // Replace 'XXX' with your assigned server number
define('DB_USERNAME', 'your_database_username'); // Replace with your MySQL username
define('DB_PASSWORD', 'your_database_password'); // Replace with your MySQL password
define('DB_NAME', 'your_database_name'); // Replace with your MySQL database name

try {
    // Establish a connection to the MySQL database
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USERNAME, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // If connection is successful
    echo "Database connection established successfully!";
} catch (PDOException $e) {
    // Handle database connection errors
    die("Error connecting to the database: " . $e->getMessage());
}

// Example query: Create a table if it doesn't already exist
try {
    $sql = "
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ";
    $pdo->exec($sql);
    echo "Table 'users' created successfully!";
} catch (PDOException $e) {
    die("Error creating table: " . $e->getMessage());
}

// Example query: Insert data into the table
try {
    $stmt = $pdo->prepare("INSERT INTO users (name, email) VALUES (:name, :email)");
    $stmt->execute([
        ':name' => 'John Doe',
        ':email' => 'john.doe@example.com',
    ]);
    echo "User added successfully!";
} catch (PDOException $e) {
    die("Error inserting data: " . $e->getMessage());
}

// Example query: Fetch and display data from the table
try {
    $stmt = $pdo->query("SELECT * FROM users");
    $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

    echo "<h1>Registered Users</h1>";
    foreach ($users as $user) {
        echo "ID: {$user['id']} - Name: {$user['name']} - Email: {$user['email']}<br>";
    }
} catch (PDOException $e) {
    die("Error fetching data: " . $e->getMessage());
}
?>
```

### Instructions for Deployment:
1. **Set Up InfinityFree Hosting**:
   - Register for a free account on [InfinityFree.net](https://infinityfree.net/).
   - Create a free hosting account and link your `ct.ws` domain.

2. **Upload Code**:
   - Use the File Manager or FTP client (e.g., FileZilla) provided by InfinityFree.
   - Ensure `index.php` (or your script file) is uploaded to the root directory (usually `htdocs`).

3. **Configure MySQL Database**:
   - Use cPanel provided by InfinityFree to create a new MySQL database.
   - Note down the database credentials (host, username, password, database name).

4. **Edit Database Configuration**:
   - Replace `DB_HOST`, `DB_USERNAME`, `DB_PASSWORD`, and `DB_NAME` in the script with the credentials from Step 3.

5. **Test Your Website**:
   - Navigate to your domain (e.g., `example.ct.ws`) and verify that the script runs correctly.

### Notes:
- Make sure your database credentials are kept secure and do not expose sensitive details.
- Use HTTPS (SSL/TLS) if available via InfinityFree for securing your site.
