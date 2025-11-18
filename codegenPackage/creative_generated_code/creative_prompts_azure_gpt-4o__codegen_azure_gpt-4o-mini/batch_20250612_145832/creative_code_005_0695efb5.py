"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status-ehaat.life
Prompt: Write a PHP script to fetch and display lottery results using the database schema outlined in the "查询信息" section of the webpage.
Generated: DETERMINISTIC_0695efb5dab7c8e1
Batch ID: 20250612_145832
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
$db = 'lottery_db'; // Database name
$user = 'db_user'; // Database username
$pass = 'db_password'; // Database password
$charset = 'utf8mb4'; // Character set

// Set up the Data Source Name (DSN)
$dsn = "mysql:host=$host;dbname=$db;charset=$charset";

// Set up options for PDO
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION, // Enable exceptions for errors
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,       // Fetch as associative array
    PDO::ATTR_EMULATE_PREPARES   => false,                  // Disable emulation of prepared statements
];

try {
    // Create a new PDO instance
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Handle database connection error
    throw new \PDOException($e->getMessage(), (int)$e->getCode());
}

// Function to fetch lottery results
function fetchLotteryResults($pdo) {
    $sql = "SELECT draw_date, winning_numbers, prize_amount FROM lottery_results ORDER BY draw_date DESC"; // SQL query

    try {
        $stmt = $pdo->query($sql); // Execute the query
        return $stmt->fetchAll(); // Fetch all results
    } catch (\PDOException $e) {
        // Handle query execution error
        echo "Query failed: " . $e->getMessage();
        return [];
    }
}

// Fetch the lottery results
$results = fetchLotteryResults($pdo);

// Display the lottery results
if (!empty($results)) {
    echo "<h1>Lottery Results</h1>";
    echo "<table border='1'>
            <tr>
                <th>Draw Date</th>
                <th>Winning Numbers</th>
                <th>Prize Amount</th>
            </tr>";

    foreach ($results as $row) {
        echo "<tr>
                <td>" . htmlspecialchars($row['draw_date']) . "</td>
                <td>" . htmlspecialchars($row['winning_numbers']) . "</td>
                <td>" . htmlspecialchars($row['prize_amount']) . "</td>
              </tr>";
    }

    echo "</table>";
} else {
    echo "<h1>No results found.</h1>";
}
?>
```
