"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-miner.shop
Prompt: Create a PHP code snippet that submits a new business listing to a directory similar to the one found on bitcoin-miner.shop.
Generated: DETERMINISTIC_1a8fccd3cc9596c6
Batch ID: 20250612_160526
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
 * Business Listing Submission Script
 *
 * This script handles the submission of a new business listing 
 * to the directory. It performs necessary validation, sanitizes 
 * inputs, and handles database insertion with appropriate error handling.
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'your_username');
define('DB_PASS', 'your_password');
define('DB_NAME', 'your_database');

/**
 * Connect to the database.
 * 
 * @return mysqli
 * @throws Exception if connection fails
 */
function connectDatabase() {
    $connection = new mysqli(DB_HOST, DB_USER, DB_PASS, DB_NAME);
    
    // Check connection
    if ($connection->connect_error) {
        throw new Exception('Database connection error: ' . $connection->connect_error);
    }

    return $connection;
}

/**
 * Sanitize input data.
 * 
 * @param string $data
 * @return string
 */
function sanitizeInput($data) {
    return htmlspecialchars(trim($data));
}

/**
 * Submit a new business listing.
 * 
 * @param string $name
 * @param string $description
 * @param string $website
 * @return bool
 * @throws Exception on failure to insert
 */
function submitListing($name, $description, $website) {
    $connection = connectDatabase();

    // Prepare and bind
    $stmt = $connection->prepare("INSERT INTO business_listings (name, description, website) VALUES (?, ?, ?)");
    if (!$stmt) {
        throw new Exception('Prepare statement error: ' . $connection->error);
    }

    $stmt->bind_param("sss", $name, $description, $website);

    // Execute and check for errors
    if (!$stmt->execute()) {
        throw new Exception('Execution error: ' . $stmt->error);
    }

    $stmt->close();
    $connection->close();

    return true;
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    try {
        // Validate and sanitize inputs
        if (!isset($_POST['name'], $_POST['description'], $_POST['website'])) {
            throw new Exception('All fields are required.');
        }

        $name = sanitizeInput($_POST['name']);
        $description = sanitizeInput($_POST['description']);
        $website = sanitizeInput($_POST['website']);

        // Submit the listing
        submitListing($name, $description, $website);
        echo "Business listing submitted successfully!";
    } catch (Exception $e) {
        // Handle exceptions and display error message
        echo 'Error: ' . $e->getMessage();
    }
}

?>

<!-- HTML Form for business listing submission -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Submit Business Listing</title>
</head>
<body>
    <h1>Submit Your Business Listing</h1>
    <form action="" method="post">
        <label for="name">Business Name:</label>
        <input type="text" id="name" name="name" required><br>

        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea><br>

        <label for="website">Website URL:</label>
        <input type="url" id="website" name="website" required><br>

        <button type="submit">Submit Listing</button>
    </form>
</body>
</html>
```
