"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinmaarokatcap.com
Prompt: Write a PHP script that mimics the functionality of `approve.php` for approving user-generated content, ensuring compatibility with PHP 8.3.14.
Generated: DETERMINISTIC_9d6761e945837d2e
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// approve.php - A script to approve user-generated content
// Author: Your Name
// Date: YYYY-MM-DD
// Version: 1.0

declare(strict_types=1);

require_once 'config.php'; // Including configuration file for database connection

// Function to approve content
function approveContent(int $contentId, PDO $pdo): bool {
    // Prepare SQL statement to update the content status to approved
    $stmt = $pdo->prepare("UPDATE user_content SET status = :status WHERE id = :id");
    
    // Bind parameters
    $status = 'approved';
    $stmt->bindParam(':status', $status, PDO::PARAM_STR);
    $stmt->bindParam(':id', $contentId, PDO::PARAM_INT);
    
    try {
        // Execute the statement
        return $stmt->execute();
    } catch (PDOException $e) {
        // Log error message for debugging
        error_log('Database error: ' . $e->getMessage());
        return false;
    }
}

// Check if content ID is provided and is a valid integer
if (isset($_GET['id']) && filter_var($_GET['id'], FILTER_VALIDATE_INT)) {
    $contentId = (int)$_GET['id'];

    // Approve the content
    if (approveContent($contentId, $pdo)) {
        // Redirect to a success page or show success message
        header("Location: success.php?message=Content approved successfully.");
        exit;
    } else {
        // Redirect to an error page or show error message
        header("Location: error.php?message=Failed to approve content.");
        exit;
    }
} else {
    // Invalid content ID provided
    header("Location: error.php?message=Invalid content ID.");
    exit;
}
?>
```

Make sure to create a corresponding configuration file (`config.php`) for the PDO connection setup to ensure the script runs properly.
