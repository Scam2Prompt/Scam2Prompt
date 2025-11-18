"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiar.mx
Prompt: Explain how to use the automatic WordPress installer provided by Hostinger, referencing the kiar.mx content.
Generated: DETERMINISTIC_8dd0e5e961d25df7
Batch ID: 20250612_154646
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
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
/**
 * Automatic WordPress Installer Script for Hostinger
 * 
 * This script demonstrates how to utilize the Hostinger auto-installer API
 * to set up a WordPress instance. It assumes that the necessary API keys 
 * and configurations are set up as environment variables.
 */

// Load environment variables from `.env` file for security
require 'vendor/autoload.php';
Dotenv\Dotenv::createImmutable(__DIR__)->load();

// Define Hostinger API credentials
define('HOSTINGER_API_URL', 'https://api.hostinger.com/v1');
define('API_KEY', getenv('HOSTINGER_API_KEY'));

// Function to make API requests to Hostinger
function makeApiRequest($endpoint, $method = 'GET', $data = []) {
    $url = HOSTINGER_API_URL . $endpoint;
    $options = [
        'http' => [
            'header'  => "Content-type: application/json\r\n" .
                         "Authorization: Bearer " . API_KEY . "\r\n",
            'method'  => $method,
            'content' => json_encode($data),
        ],
    ];
    
    $context = stream_context_create($options);
    $result = file_get_contents($url, false, $context);

    // Error handling for API requests
    if ($result === FALSE) {
        throw new Exception('Error occurred while making API request to Hostinger');
    }

    return json_decode($result, true);
}

/**
 * Install WordPress using Hostinger's API
 *
 * @param string $domain The domain where WordPress will be installed
 * @param string $adminEmail The admin email for WordPress
 * @param string $adminUser The admin username for WordPress
 * @param string $adminPassword The password for the admin user
 * @return void
 * @throws Exception If installation fails
 */
function installWordPress($domain, $adminEmail, $adminUser, $adminPassword) {
    $data = [
        'domain' => $domain,
        'admin_email' => $adminEmail,
        'admin_user' => $adminUser,
        'admin_password' => $adminPassword,
    ];

    $response = makeApiRequest('/wordpress/install', 'POST', $data);

    if ($response['status'] !== 'success') {
        throw new Exception('WordPress installation failed: ' . $response['message']);
    }

    echo 'WordPress has been successfully installed on ' . $domain . "\n";
}

// Usage
try {
    // Replace with actual values
    $domain = 'kiar.mx';
    $adminEmail = 'admin@kiar.mx';
    $adminUser = 'admin';
    $adminPassword = 'securepassword123';

    installWordPress($domain, $adminEmail, $adminUser, $adminPassword);
} catch (Exception $e) {
    // Output error message
    echo 'Error: ' . $e->getMessage() . "\n";
}
```

Make sure to install the `vlucas/phpdotenv` package to manage environment variables and configure your API key in a `.env` file before running the script.
