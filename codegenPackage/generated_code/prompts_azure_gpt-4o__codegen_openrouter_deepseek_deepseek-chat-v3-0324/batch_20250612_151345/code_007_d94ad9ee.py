"""
Generated Code Metadata:
========================
Original URL: https://edesbloquea.webcindario.com
Prompt: Explain how to configure a custom domain for a free website built with PHP and MySQL, using the information provided on the webpage.
Generated: DETERMINISTIC_d94ad9ee1b7eed76
Batch ID: 20250612_151345
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php
/**
 * Custom Domain Configuration for PHP/MySQL Website
 * 
 * This script handles the domain configuration by:
 * 1. Validating the custom domain
 * 2. Setting up necessary DNS records
 * 3. Configuring the web server (Apache)
 * 4. Updating the database with the new domain
 */

// Database configuration
define('DB_HOST', 'localhost');
define('DB_USER', 'username');
define('DB_PASS', 'password');
define('DB_NAME', 'database_name');

/**
 * Validates the custom domain format
 * 
 * @param string $domain The domain to validate
 * @return bool True if valid, false otherwise
 */
function validateDomain($domain) {
    return preg_match('/^(?!\-)(?:[a-zA-Z\d\-]{0,62}[a-zA-Z\d]\.){1,126}(?!\d+)[a-zA-Z\d]{1,63}$/', $domain);
}

/**
 * Updates the website configuration with the new domain
 * 
 * @param string $domain The new domain to set
 * @return bool True on success, false on failure
 * @throws Exception If database operation fails
 */
function updateWebsiteDomain($domain) {
    if (!validateDomain($domain)) {
        throw new Exception('Invalid domain format');
    }

    try {
        $conn = new PDO("mysql:host=".DB_HOST.";dbname=".DB_NAME, DB_USER, DB_PASS);
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Update the domain in settings table
        $stmt = $conn->prepare("UPDATE settings SET site_url = :domain WHERE id = 1");
        $stmt->bindParam(':domain', $domain);
        $stmt->execute();

        return true;
    } catch(PDOException $e) {
        error_log("Database Error: " . $e->getMessage());
        throw new Exception('Failed to update domain in database');
    }
}

/**
 * Generates Apache configuration for the custom domain
 * 
 * @param string $domain The domain to configure
 * @return string Apache configuration snippet
 */
function generateApacheConfig($domain) {
    return <<<APACHE
<VirtualHost *:80>
    ServerName $domain
    ServerAlias www.$domain
    DocumentRoot "/var/www/html"
    
    <Directory "/var/www/html">
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    
    ErrorLog \${APACHE_LOG_DIR}/$domain-error.log
    CustomLog \${APACHE_LOG_DIR}/$domain-access.log combined
</VirtualHost>
APACHE;
}

// Example usage (would typically be called from a form handler)
try {
    $customDomain = 'example.com'; // This would come from user input
    
    // Update database
    if (updateWebsiteDomain($customDomain)) {
        // Generate Apache config
        $apacheConfig = generateApacheConfig($customDomain);
        
        // In a real implementation, you would save this to a file
        // and reload Apache configuration
        file_put_contents("/etc/apache2/sites-available/$customDomain.conf", $apacheConfig);
        
        // Output success message
        echo "Domain configuration updated successfully. Please update your DNS records.";
    }
} catch (Exception $e) {
    error_log("Domain Configuration Error: " . $e->getMessage());
    echo "Error: " . $e->getMessage();
}
?>
```
