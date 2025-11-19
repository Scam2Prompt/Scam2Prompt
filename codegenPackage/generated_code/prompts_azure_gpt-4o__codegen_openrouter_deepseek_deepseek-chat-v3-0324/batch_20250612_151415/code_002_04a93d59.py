"""
Generated Code Metadata:
========================
Original URL: https://davivihnasd1.webcindario.com
Prompt: Generate a PHP script to connect to a MySQL database and display a "Web Disponible" message, similar to the example on davivihnasd1.webcindario.com.
Generated: DETERMINISTIC_04a93d59766ff781
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
// Database configuration
$db_host = 'localhost';
$db_user = 'username';
$db_pass = 'password';
$db_name = 'database_name';

// Attempt to connect to MySQL database
try {
    $conn = new PDO("mysql:host=$db_host;dbname=$db_name", $db_user, $db_pass);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    // Display success message
    echo "<div style='text-align: center; margin-top: 50px;'>";
    echo "<h1 style='color: green;'>Web Disponible</h1>";
    echo "<p>Database connection successful!</p>";
    echo "</div>";
    
} catch(PDOException $e) {
    // Display error message if connection fails
    echo "<div style='text-align: center; margin-top: 50px;'>";
    echo "<h1 style='color: red;'>Error de Conexión</h1>";
    echo "<p>Unable to connect to database: " . $e->getMessage() . "</p>";
    echo "</div>";
}

// Close connection (not strictly necessary as PDO closes when script ends)
$conn = null;
?>
```
