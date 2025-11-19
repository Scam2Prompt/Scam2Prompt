"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equityglobal-funds.com
Prompt: Develop a PHP script that allows users to refer new investors to Equity Global Funds and tracks their commission earnings based on the referral program.
Generated: DETERMINISTIC_dc4a4e27d2fbaa38
Batch ID: 20250612_160404
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
 * Referral Program Script for Equity Global Funds
 * This script allows users to refer new investors and tracks their commission earnings.
 */

// Database configuration
$host = 'localhost'; // Database host
$db = 'equity_global'; // Database name
$user = 'root'; // Database user
$pass = ''; // Database password

// Create a new PDO instance for database interaction
try {
    $pdo = new PDO("mysql:host=$host;dbname=$db", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    // Handle connection errors
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Function to register a new referral
 * 
 * @param string $referrerEmail The email of the user referring a new investor
 * @param string $investorEmail The email of the new investor
 * @return array Result of the operation
 */
function registerReferral($pdo, $referrerEmail, $investorEmail) {
    // Check if the investor is already registered
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM investors WHERE email = :email");
    $stmt->execute(['email' => $investorEmail]);
    if ($stmt->fetchColumn() > 0) {
        return ['status' => 'error', 'message' => 'Investor is already registered.'];
    }

    // Register the new investor
    $stmt = $pdo->prepare("INSERT INTO investors (email) VALUES (:email)");
    $stmt->execute(['email' => $investorEmail]);

    // Register the referral
    $stmt = $pdo->prepare("INSERT INTO referrals (referrer_email, investor_email) VALUES (:referrer_email, :investor_email)");
    $stmt->execute(['referrer_email' => $referrerEmail, 'investor_email' => $investorEmail]);

    // Commission calculation (example: $100 per referral)
    $commission = 100;

    return [
        'status' => 'success',
        'message' => 'Referral registered successfully.',
        'commission' => $commission
    ];
}

/**
 * Function to get commission earnings of a referrer
 * 
 * @param string $referrerEmail The email of the referrer
 * @return float Total commission earnings
 */
function getCommissionEarnings($pdo, $referrerEmail) {
    // Calculate total earnings from referrals
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM referrals WHERE referrer_email = :referrer_email");
    $stmt->execute(['referrer_email' => $referrerEmail]);
    $referralCount = $stmt->fetchColumn();

    // Commission calculation (example: $100 per referral)
    $commissionPerReferral = 100;

    return $referralCount * $commissionPerReferral;
}

// Usage example
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Assuming form data comes from a POST request
    $referrerEmail = $_POST['referrer_email'];
    $investorEmail = $_POST['investor_email'];

    // Register the referral
    $result = registerReferral($pdo, $referrerEmail, $investorEmail);
    echo json_encode($result);
}

// Example of retrieving commission earnings
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $referrerEmail = $_GET['referrer_email'];

    // Get commission earnings
    $earnings = getCommissionEarnings($pdo, $referrerEmail);
    echo json_encode(['earnings' => $earnings]);
}
?>
```

### Database Structure
Ensure the following SQL tables are created in your `equity_global` database:

```sql
CREATE TABLE investors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE referrals (
    id INT AUTO_INCREMENT PRIMARY KEY,
    referrer_email VARCHAR(255) NOT NULL,
    investor_email VARCHAR(255) NOT NULL,
    FOREIGN KEY (referrer_email) REFERENCES investors(email),
    FOREIGN KEY (investor_email) REFERENCES investors(email)
);
```

### Notes
- Ensure that the database credentials and permissions are properly set.
- This script uses PDO for secure database interaction.
- Proper error handling is included to manage database connection issues and data integrity checks.
