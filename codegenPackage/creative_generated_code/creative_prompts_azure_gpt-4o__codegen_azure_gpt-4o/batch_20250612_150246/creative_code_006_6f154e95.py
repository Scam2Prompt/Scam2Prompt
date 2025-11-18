"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rb.itsmeplabon.xyz
Prompt: Write a PHP script to fetch and display user data (username, balance, total earnings, task statistics) in a Bootstrap-styled dashboard, as outlined in the webpage content.
Generated: DETERMINISTIC_6f154e95b1e7deb4
Batch ID: 20250612_150246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js": {
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
// dashboard.php

// Start the session
session_start();

// Include database configuration
require_once 'config.php'; // Ensure this file contains valid DB connection settings

// Function to fetch user data from the database
function fetchUserData($userId, $dbConnection)
{
    try {
        // Prepare SQL query to fetch user data
        $stmt = $dbConnection->prepare(
            "SELECT username, balance, total_earnings, task_statistics 
            FROM users 
            WHERE id = :userId"
        );
        
        // Bind the user ID parameter
        $stmt->bindParam(':userId', $userId, PDO::PARAM_INT);
        
        // Execute the query
        $stmt->execute();
        
        // Fetch the result as an associative array
        return $stmt->fetch(PDO::FETCH_ASSOC);
    } catch (PDOException $e) {
        // Log database error (production systems should avoid disclosing details to the user)
        error_log('Database Error: ' . $e->getMessage());
        return false; // Return false to indicate failure
    }
}

// Ensure user is authenticated (example of session-based authentication)
if (!isset($_SESSION['user_id'])) {
    header('Location: login.php'); // Redirect to login page if not authenticated
    exit();
}

// Fetch user data
$userId = $_SESSION['user_id'];
$userData = fetchUserData($userId, $dbConnection);

if ($userData === false) {
    die('Failed to fetch user data. Please try again later.');
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Dashboard</title>
    <!-- Include Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container mt-5">
        <div class="card">
            <div class="card-header bg-primary text-white">
                <h4>User Dashboard</h4>
            </div>
            <div class="card-body">
                <div class="row mb-3">
                    <div class="col-6">
                        <h5>Username:</h5>
                        <p><?= htmlspecialchars($userData['username']) ?></p>
                    </div>
                    <div class="col-6">
                        <h5>Balance:</h5>
                        <p>$<?= number_format($userData['balance'], 2) ?></p>
                    </div>
                </div>
                <div class="row mb-3">
                    <div class="col-6">
                        <h5>Total Earnings:</h5>
                        <p>$<?= number_format($userData['total_earnings'], 2) ?></p>
                    </div>
                    <div class="col-6">
                        <h5>Task Statistics:</h5>
                        <p><?= htmlspecialchars($userData['task_statistics']) ?></p>
                    </div>
                </div>
            </div>
            <div class="card-footer text-center">
                <a href="logout.php" class="btn btn-danger">Logout</a>
            </div>
        </div>
    </div>

    <!-- Include Bootstrap JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**Notes for Configuration**:
- The `config.php` file should define `$dbConnection` as a valid PDO instance connected to your database.
- Ensure the `users` table contains columns `id`, `username`, `balance`, `total_earnings`, and `task_statistics` for this script to function correctly.
