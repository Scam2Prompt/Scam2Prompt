"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mstoolsnetshop.com
Prompt: Develop a PHP script for an investment platform with cron job functionality, modeled after the "Zilnex Investment Script With Cron Jobs" showcased on mstoolsnetshop.com.
Generated: DETERMINISTIC_db2cfbb3b4a67bb6
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// investment_script.php

// Database connection settings
$host = 'localhost';
$db = 'investment_db';
$user = 'root';
$pass = 'password';

// Create a new PDO instance for database interactions
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    // Set the PDO error mode to exception
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection error
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to process investments
 */
function processInvestments($pdo) {
    // Define the query to fetch active investments
    $query = "SELECT * FROM investments WHERE status = 'active'";
    
    try {
        $stmt = $pdo->query($query);
        $investments = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Loop through each investment and calculate returns
        foreach ($investments as $investment) {
            $returnAmount = calculateReturn($investment['amount'], $investment['interest_rate'], $investment['duration']);

            // Update the investment record with the new return amount
            $updateQuery = "UPDATE investments SET return_amount = :returnAmount WHERE id = :id";
            $updateStmt = $pdo->prepare($updateQuery);
            $updateStmt->execute([
                ':returnAmount' => $returnAmount,
                ':id' => $investment['id'],
            ]);
        }
    } catch (PDOException $e) {
        // Handle query error
        error_log("Error processing investments: " . $e->getMessage());
    }
}

/**
 * Function to calculate the investment return
 *
 * @param float $amount The initial investment amount
 * @param float $interestRate The annual interest rate
 * @param int $duration The duration of the investment in years
 * @return float The calculated return amount
 */
function calculateReturn($amount, $interestRate, $duration) {
    // Simple interest calculation
    return $amount * (1 + ($interestRate / 100) * $duration);
}

// Execute the investment processing function
processInvestments($pdo);

// Close the database connection
$pdo = null;

// cron.php

// This file can be called as a cron job to run the investment script periodically
require 'investment_script.php';
```

**Cron Job Setup:**
To set up the cron job, you can edit your crontab by running `crontab -e` and adding the following line to execute the script every hour:

```
0 * * * * /usr/bin/php /path/to/your/investment_script.php
```

Make sure to replace `/path/to/your/investment_script.php` with the actual path to your PHP script.
