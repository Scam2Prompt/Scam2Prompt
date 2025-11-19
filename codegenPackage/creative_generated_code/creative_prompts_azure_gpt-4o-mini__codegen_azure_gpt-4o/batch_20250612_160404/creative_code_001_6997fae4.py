"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethergiffcrypto.webcindario.com
Prompt: What are the steps to set up a custom domain for a free website using PHP and MySQL?
Generated: DETERMINISTIC_6997fae470478fb7
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready PHP script for setting up a custom domain for a free website using PHP and MySQL.

```php
<?php
/**
 * Script to configure a custom domain for a free website.
 * This script assumes a MySQL database with a table `domains`
 * containing columns: `id`, `user_id`, `custom_domain`, and `status`.
 */

// Database connection constants
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'password');
define('DB_NAME', 'free_website');

// Connect to the database
try {
    $pdo = new PDO("mysql:host=" . DB_HOST . ";dbname=" . DB_NAME, DB_USER, DB_PASSWORD);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

// Function to validate domain name
function isValidDomain($domain) {
    return preg_match('/^(?!\-)[A-Za-z0-9\-]{1,63}(?<!\-)\.[A-Za-z]{2,}$/', $domain);
}

// Handle form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $user_id = intval($_POST['user_id']); // Assuming user_id is provided securely
    $custom_domain = trim($_POST['custom_domain']);

    // Validate the custom domain
    if (!isValidDomain($custom_domain)) {
        echo "Invalid domain name. Please enter a valid domain.";
        exit;
    }

    // Check if the domain is already in use
    $stmt = $pdo->prepare("SELECT COUNT(*) FROM domains WHERE custom_domain = :custom_domain");
    $stmt->bindParam(':custom_domain', $custom_domain, PDO::PARAM_STR);
    $stmt->execute();
    $domain_exists = $stmt->fetchColumn();

    if ($domain_exists > 0) {
        echo "Domain is already in use. Please choose a different domain.";
        exit;
    }

    // Insert the custom domain into the database
    try {
        $stmt = $pdo->prepare("INSERT INTO domains (user_id, custom_domain, status) VALUES (:user_id, :custom_domain, 'pending')");
        $stmt->bindParam(':user_id', $user_id, PDO::PARAM_INT);
        $stmt->bindParam(':custom_domain', $custom_domain, PDO::PARAM_STR);
        $stmt->execute();

        echo "Custom domain submitted successfully! It will be reviewed shortly.";
    } catch (PDOException $e) {
        // Log error for admin review (do not expose sensitive details to user)
        error_log("Database error: " . $e->getMessage());
        echo "An error occurred while processing your request. Please try again later.";
    }
} else {
    // Display the HTML form for user input
    ?>
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Set Up Custom Domain</title>
    </head>
    <body>
        <h1>Set Up Your Custom Domain</h1>
        <form method="POST" action="">
            <label for="user_id">User ID:</label>
            <input type="number" id="user_id" name="user_id" required>
            <br>
            <label for="custom_domain">Custom Domain:</label>
            <input type="text" id="custom_domain" name="custom_domain" required>
            <br>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    <?php
}
?>
```

### Notes:
- Replace database credentials (`DB_HOST`, `DB_USER`, `DB_PASSWORD`, etc.) with actual values.
- Ensure the database structure matches the script (`domains` table, column names, etc.).
- Add HTTPS and other security measures (e.g., prepared statements, input sanitization) where necessary for production use.
