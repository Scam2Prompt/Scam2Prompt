"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acess-sushi-swap.blogspot.com
Prompt: Create a PHP code snippet that retrieves and displays a list of educational toys available in a stationery store's inventory.
Generated: DETERMINISTIC_4ba3e4322c01415f
Batch ID: 20250612_160507
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
/**
 * Retrieves and displays a list of educational toys from the stationery store's inventory.
 *
 * This script connects to the database, fetches the educational toys,
 * and displays them in a structured format.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'stationery_store');

// Function to create a database connection
function createConnection() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);

    // Check connection
    if ($connection->connect_error) {
        die("Connection failed: " . $connection->connect_error);
    }
    
    return $connection;
}

// Function to fetch educational toys from the inventory
function fetchEducationalToys($connection) {
    $sql = "SELECT name, description, price FROM products WHERE category = 'educational_toys'";
    $result = $connection->query($sql);

    // Check for query errors
    if ($result === false) {
        die("Error fetching data: " . $connection->error);
    }

    // Fetch all educational toys
    $toys = [];
    while ($row = $result->fetch_assoc()) {
        $toys[] = $row;
    }

    return $toys;
}

// Function to display the list of educational toys
function displayToys($toys) {
    if (empty($toys)) {
        echo "No educational toys available.";
        return;
    }

    echo "<h2>Available Educational Toys</h2>";
    echo "<ul>";
    foreach ($toys as $toy) {
        echo "<li>";
        echo "<strong>Name:</strong> " . htmlspecialchars($toy['name']) . "<br>";
        echo "<strong>Description:</strong> " . htmlspecialchars($toy['description']) . "<br>";
        echo "<strong>Price:</strong> $" . number_format($toy['price'], 2);
        echo "</li>";
    }
    echo "</ul>";
}

// Main execution
$connection = createConnection();
$educationalToys = fetchEducationalToys($connection);
displayToys($educationalToys);

// Close the database connection
$connection->close();
?>
```
