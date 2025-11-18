"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://davivihnasd1.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display a "Web Disponible" message, similar to the example on davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_04a93d59766ff781
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// Configuration settings
$host = 'localhost';           // Database host
$dbname = 'your_database';     // Database name
$username = 'your_username';   // Database username
$password = 'your_password';   // Database password

try {
    // Establish a connection to the MySQL database using PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $username, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // Set error mode to exception

    // If the connection is successful, display the message
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '    <meta charset="UTF-8">';
    echo '    <meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '    <title>Web Disponible</title>';
    echo '    <style>';
    echo '        body { font-family: Arial, sans-serif; text-align: center; padding-top: 20%; }';
    echo '        h1 { color: green; }';
    echo '    </style>';
    echo '</head>';
    echo '<body>';
    echo '    <h1>Web Disponible</h1>';
    echo '</body>';
    echo '</html>';
} catch (PDOException $e) {
    // If there is a connection error, log it and display an error message
    error_log("Database connection error: " . $e->getMessage());
    http_response_code(500); // Set HTTP response code to 500 (Internal Server Error)
    echo '<!DOCTYPE html>';
    echo '<html lang="en">';
    echo '<head>';
    echo '    <meta charset="UTF-8">';
    echo '    <meta name="viewport" content="width=device-width, initial-scale=1.0">';
    echo '    <title>Error</title>';
    echo '    <style>';
    echo '        body { font-family: Arial, sans-serif; text-align: center; padding-top: 20%; }';
    echo '        h1 { color: red; }';
    echo '    </style>';
    echo '</head>';
    echo '<body>';
    echo '    <h1>Service Unavailable</h1>';
    echo '</body>';
    echo '</html>';
    exit; // Exit the script
}
?>
```
