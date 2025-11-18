"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://seguritydecuenta.webcindario.com
Prompt: Write PHP code to set up a basic website with MySQL integration, including steps to configure a custom domain.
Generated: DETERMINISTIC_a6c3dd361e4a3f11
Batch ID: 20250612_151247
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the PHP code to set up a basic website with MySQL integration. The code includes comments for clarity and follows best practices:

```php
<?php
// config.php - Configuration file for database connection
// Always keep sensitive information like database credentials outside the web root directory in production.

// Database connection settings
define('DB_HOST', 'localhost'); // Change to your database host
define('DB_USER', 'root');      // Change to your database username
define('DB_PASS', 'password');  // Change to your database password
define('DB_NAME', 'my_website'); // Change to your database name

/**
 * Establish a connection to the MySQL database.
 * Returns the connection object on success or exits the script with an error message on failure.
 */
function getDbConnection() {
    $conn = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($conn->connect_error) {
        die("Database connection failed: " . $conn->connect_error);
    }

    return $conn;
}
?>

<?php
// index.php - Main file for handling requests

require_once 'config.php'; // Load the database configuration

// Connect to the database
$conn = getDbConnection();

// Create a simple table if it doesn't exist
$tableCreationQuery = "
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        email VARCHAR(100) NOT NULL UNIQUE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
";

if ($conn->query($tableCreationQuery) !== TRUE) {
    die("Error creating table: " . $conn->error);
}

// Insert sample data into the table
$insertQuery = "
    INSERT INTO users (username, email)
    VALUES ('testuser', 'testuser@example.com')
    ON DUPLICATE KEY UPDATE username=username
";

if ($conn->query($insertQuery) !== TRUE) {
    die("Error inserting sample data: " . $conn->error);
}

// Retrieve data from the table
$result = $conn->query("SELECT * FROM users");

if ($result->num_rows > 0) {
    // Display user data in a basic HTML table
    echo "<h1>User List</h1>";
    echo "<table border='1'>";
    echo "<tr><th>ID</th><th>Username</th><th>Email</th><th>Created At</th></tr>";

    while ($row = $result->fetch_assoc()) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['id']) . "</td>";
        echo "<td>" . htmlspecialchars($row['username']) . "</td>";
        echo "<td>" . htmlspecialchars($row['email']) . "</td>";
        echo "<td>" . htmlspecialchars($row['created_at']) . "</td>";
        echo "</tr>";
    }

    echo "</table>";
} else {
    echo "No users found.";
}

// Close the database connection
$conn->close();
?>

<!-- basic HTML template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Basic Website</title>
</head>
<body>
    <h1>Welcome to Our Website</h1>
    <p>This is a basic PHP website with MySQL integration.</p>
</body>
</html>
```

### Steps to Configure a Custom Domain
1. **Purchase a Domain Name:** Buy a domain from a registrar like GoDaddy or Namecheap.
2. **Point Domain to Your Server:** Update the domain's DNS settings to point to your server's IP address.
3. **Set Up a Virtual Host in Apache or Nginx:** Configure your web server to handle requests for your custom domain.
   - Example for Apache: In `/etc/apache2/sites-available/yourdomain.conf`:
     ```
     <VirtualHost *:80>
         ServerName yourdomain.com
         DocumentRoot /path/to/your/project
         <Directory /path/to/your/project>
             AllowOverride All
         </Directory>
     </VirtualHost>
     ```
   - Enable the configuration: `sudo a2ensite yourdomain.conf` and restart Apache: `sudo systemctl restart apache2`.
4. **Install SSL Certificate:** Use Let's Encrypt or another provider to secure your site with HTTPS. For Let's Encrypt:
   ```
   sudo certbot --apache -d yourdomain.com
   ```
5. **Test Your Site:** Visit your custom domain in a web browser.

This completes the requested PHP code and configuration steps for a basic website.
