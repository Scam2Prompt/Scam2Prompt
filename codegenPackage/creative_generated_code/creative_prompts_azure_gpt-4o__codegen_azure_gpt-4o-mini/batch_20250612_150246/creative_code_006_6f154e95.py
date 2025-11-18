"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a PHP script to fetch and display user data (username, balance, total earnings, task statistics) in a Bootstrap-styled dashboard, as outlined in the webpage content.
Generated: DETERMINISTIC_6f154e95b1e7deb4
Batch ID: 20250612_150246
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.5.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```php
<?php
// Start the session to use session variables
session_start();

// Include database configuration file
require_once 'db_config.php';

// Function to fetch user data
function fetchUserData($userId) {
    // Create a new PDO instance for the database connection
    try {
        $pdo = new PDO(DB_DSN, DB_USER, DB_PASS);
        $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Prepare the SQL statement to fetch user data
        $stmt = $pdo->prepare("SELECT username, balance, total_earnings, task_statistics FROM users WHERE id = :userId");
        $stmt->bindParam(':userId', $userId, PDO::PARAM_INT);
        $stmt->execute();
        
        // Fetch the user data
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Handle database errors
        die("Database error: " . $e->getMessage());
    }
}

// Check if user is logged in
if (!isset($_SESSION['user_id'])) {
    die("Access denied. Please log in.");
}

// Fetch user data for the logged-in user
$userId = $_SESSION['user_id'];
$userData = fetchUserData($userId);

// Check if user data was retrieved
if (!$userData) {
    die("User data not found.");
}

// HTML Structure with Bootstrap styling
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-4">User Dashboard</h1>
        <div class="card">
            <div class="card-header">
                <h2><?= htmlspecialchars($userData['username']) ?>'s Profile</h2>
            </div>
            <div class="card-body">
                <h5>Balance: $<?= number_format($userData['balance'], 2) ?></h5>
                <h5>Total Earnings: $<?= number_format($userData['total_earnings'], 2) ?></h5>
                <h5>Task Statistics: <?= htmlspecialchars($userData['task_statistics']) ?></h5>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

**Note**: Make sure to replace `db_config.php` with your actual database configuration file containing the `DB_DSN`, `DB_USER`, and `DB_PASS` constants. Also, ensure your database and users table structure matches the SQL query in the `fetchUserData` function.
