"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergiffcrypto.webcindario.com
Prompt: Write PHP code to display data from a MySQL database in an HTML table.
Generated: DETERMINISTIC_973861b55f5d4b14
Batch ID: 20250612_151912
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
$dbname = 'your_database'; // Database name
$username = 'your_username'; // Database username
$password = 'your_password'; // Database password

try {
    // Create a new PDO instance
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Prepare and execute the SQL query
    $stmt = $pdo->prepare("SELECT * FROM your_table"); // Replace 'your_table' with your actual table name
    $stmt->execute();

    // Fetch all rows
    $data = $stmt->fetchAll(PDO::FETCH_ASSOC);
    
    // Check if there are any results
    if (count($data) > 0) {
        // Start HTML table
        echo "<table border='1'>";
        echo "<tr>";
        
        // Display table headers
        foreach (array_keys($data[0]) as $header) {
            echo "<th>" . htmlspecialchars($header) . "</th>";
        }
        echo "</tr>";

        // Display table rows
        foreach ($data as $row) {
            echo "<tr>";
            foreach ($row as $cell) {
                echo "<td>" . htmlspecialchars($cell) . "</td>";
            }
            echo "</tr>";
        }
        
        // End HTML table
        echo "</table>";
    } else {
        // Message when no data is found
        echo "No data found.";
    }
} catch (PDOException $e) {
    // Handle database connection errors
    echo "Database error: " . htmlspecialchars($e->getMessage());
} catch (Exception $e) {
    // Handle any other errors
    echo "An error occurred: " . htmlspecialchars($e->getMessage());
} finally {
    // Close the database connection
    $pdo = null;
}
?>
```
