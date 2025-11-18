"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Write code in PHP to display limited-time deals for products like "MEJE #MZE014P - Smart Wall-Hung Toilet with Built-in Bidet Heated Seat" on a webpage.
Generated: DETERMINISTIC_cbdd01e3e0f0a673
Batch ID: 20250612_151506
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
$host = 'localhost';
$db = 'your_database';
$user = 'your_username';
$pass = 'your_password';

try {
    // Establishing database connection
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Error handling for database connection failure
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to fetch limited-time deals from the database
 *
 * @param PDO $pdo The PDO instance for database connection
 * @return array The list of limited-time deals
 */
function getLimitedTimeDeals($pdo) {
    // SQL query to fetch limited-time deals
    $sql = "SELECT product_name, price, discount_percentage, end_date FROM deals WHERE end_date > NOW() ORDER BY end_date ASC LIMIT 10";
    $stmt = $pdo->prepare($sql);
    
    try {
        $stmt->execute();
        // Fetch results as an associative array
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Error handling for query execution failure
        error_log("Query failed: " . $e->getMessage());
        return [];
    }
}

// Fetching limited-time deals
$deals = getLimitedTimeDeals($pdo);

// Closing the database connection
$pdo = null;

// HTML content for displaying deals
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Limited-Time Deals</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to your CSS file -->
</head>
<body>
    <h1>Limited-Time Deals</h1>
    <?php if (!empty($deals)): ?>
        <ul>
            <?php foreach ($deals as $deal): ?>
                <li>
                    <strong><?php echo htmlspecialchars($deal['product_name']); ?></strong><br>
                    Price: $<?php echo htmlspecialchars(number_format($deal['price'], 2)); ?><br>
                    Discount: <?php echo htmlspecialchars($deal['discount_percentage']); ?>%<br>
                    Expires on: <?php echo htmlspecialchars(date('F j, Y', strtotime($deal['end_date']))); ?>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>No limited-time deals available at the moment.</p>
    <?php endif; ?>
</body>
</html>
```
