"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://squid.wtf
Prompt: Develop a donation tracking system in PHP that integrates with SQUID.WTF's donation request for server maintenance, specifically for the North American server.
Generated: DETERMINISTIC_cb8392b823c6e46f
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Donation Tracking System for SQUID.WTF's North American Server Maintenance

// Define database connection constants
define('DB_HOST', 'localhost'); // Replace with your database host
define('DB_NAME', 'donation_tracker'); // Replace with your database name
define('DB_USER', 'root'); // Replace with your database username
define('DB_PASS', 'password'); // Replace with your database password

try {
    // Establish a connection to the database using PDO
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASS, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // Enable error reporting
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // Set default fetch mode
    ]);
} catch (PDOException $e) {
    // Handle database connection failure
    die("Database connection failed: " . $e->getMessage());
}

// Function to add a new donation entry
function addDonation($name, $amount, $message) {
    global $pdo;

    try {
        // Prepare SQL statement to insert donation data
        $sql = "INSERT INTO donations (name, amount, message, timestamp) VALUES (:name, :amount, :message, :timestamp)";
        $stmt = $pdo->prepare($sql);

        // Bind parameters and execute the query
        $stmt->execute([
            ':name' => $name,
            ':amount' => $amount,
            ':message' => $message,
            ':timestamp' => date('Y-m-d H:i:s'), // Current timestamp
        ]);
    } catch (PDOException $e) {
        // Handle SQL execution failure
        return "Error adding donation: " . $e->getMessage();
    }

    return "Donation added successfully!";
}

// Function to fetch all donation entries
function fetchDonations() {
    global $pdo;

    try {
        // Prepare and execute SQL query to fetch all donations
        $sql = "SELECT * FROM donations ORDER BY timestamp DESC";
        $stmt = $pdo->query($sql);

        // Retrieve results
        return $stmt->fetchAll();
    } catch (PDOException $e) {
        // Handle SQL execution failure
        return "Error fetching donations: " . $e->getMessage();
    }
}

// Example usage of the donation tracking system
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Ensure all required fields are provided
    if (!empty($_POST['name']) && !empty($_POST['amount']) && is_numeric($_POST['amount'])) {
        // Add the donation
        $result = addDonation($_POST['name'], $_POST['amount'], $_POST['message'] ?? '');
        echo $result;
    } else {
        echo "Error: Name and valid amount are required.";
    }
} else {
    // Fetch and display all donations (for testing purposes)
    $donations = fetchDonations();

    echo "<h1>Donation Tracker</h1><ul>";
    foreach ($donations as $donation) {
        echo "<li>" . htmlspecialchars($donation['name']) . " donated $" . htmlspecialchars($donation['amount']) . " - " . htmlspecialchars($donation['message']) . " on " . $donation['timestamp'] . "</li>";
    }
    echo "</ul>";
}
?>
```

### Additional Notes:
1. **SQL Schema Example**: Ensure your database table `donations` is set up as follows:
   ```sql
   CREATE TABLE donations (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       amount DECIMAL(10, 2) NOT NULL,
       message TEXT,
       timestamp DATETIME NOT NULL
   );
   ```
2. Replace the database connection parameters (`DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS`) with actual values.
