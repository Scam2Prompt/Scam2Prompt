"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: Generate a PHP script to interact with cPanel's WHM API for managing email accounts, including creating, deleting, or modifying accounts.
Generated: DETERMINISTIC_10f1e874bc0c9fc1
Batch ID: 20250612_154651
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://YOUR_WHM_SERVER:2087/json-api/": {
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
 * WHM API interaction for managing email accounts
 * 
 * This script provides functions to create, delete, and modify email accounts
 * using the cPanel WHM API. Make sure to replace the placeholders with actual values.
 */

// Configuration
define('WHM_API_URL', 'https://YOUR_WHM_SERVER:2087/json-api/');
define('WHM_API_USER', 'YOUR_API_USER'); // e.g., root
define('WHM_API_TOKEN', 'YOUR_API_TOKEN'); // API token

/**
 * Makes a request to the WHM API
 *
 * @param string $action The API action to perform
 * @param array $params An array of parameters for the API call
 * @return array|false The response from the API or false on failure
 */
function whmApiRequest($action, $params = []) {
    $url = WHM_API_URL . $action . '?api.version=2';
    $params = http_build_query($params);

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        'Authorization: whm ' . WHM_API_USER . ':' . WHM_API_TOKEN,
        'Content-Type: application/x-www-form-urlencoded'
    ]);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
    
    $response = curl_exec($ch);
    if (curl_errno($ch)) {
        trigger_error('Curl error: ' . curl_error($ch), E_USER_WARNING);
        return false;
    }
    curl_close($ch);

    return json_decode($response, true);
}

/**
 * Creates a new email account
 *
 * @param string $domain The domain for the email account
 * @param string $email The email name (e.g., user)
 * @param string $password The password for the email account
 * @return array|false The response from the API or false on failure
 */
function createEmailAccount($domain, $email, $password) {
    $action = 'addpop';
    $params = [
        'domain' => $domain,
        'email' => $email,
        'password' => $password,
        'quota' => 0 // 0 means unlimited
    ];
    return whmApiRequest($action, $params);
}

/**
 * Deletes an email account
 *
 * @param string $domain The domain of the email account to delete
 * @param string $email The email name (e.g., user) to delete
 * @return array|false The response from the API or false on failure
 */
function deleteEmailAccount($domain, $email) {
    $action = 'delpop';
    $params = [
        'domain' => $domain,
        'email' => $email
    ];
    return whmApiRequest($action, $params);
}

/**
 * Modifies an existing email account
 *
 * @param string $domain The domain of the email account to modify
 * @param string $email The email name (e.g., user) to modify
 * @param string $newPassword The new password for the email account
 * @return array|false The response from the API or false on failure
 */
function modifyEmailAccount($domain, $email, $newPassword) {
    $action = 'editpop';
    $params = [
        'domain' => $domain,
        'email' => $email,
        'password' => $newPassword
    ];
    return whmApiRequest($action, $params);
}

// Example usage (uncomment to use):
// $createResponse = createEmailAccount('example.com', 'user', 'securepassword');
// $deleteResponse = deleteEmailAccount('example.com', 'user');
// $modifyResponse = modifyEmailAccount('example.com', 'user', 'newsecurepassword');

?>
```
