"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thg-awardprogram.epizy.com
Prompt: Create a PHP script that demonstrates how to manage multiple email accounts on iFastNet web hosting.
Generated: DETERMINISTIC_5deb5eb35ddde5d0
Batch ID: 20250612_155306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com": {
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

// Script to manage multiple email accounts on iFastNet web hosting
// Ensure you have access credentials and the hosting control panel API enabled.

// Configuration Section
$apiEndpoint = "https://api.ifastnet.com"; // Replace with actual API endpoint
$apiKey = "your_api_key"; // Replace with your API key
$accountName = "your_account_name"; // Replace with your hosting account name

/**
 * Function to make API requests to iFastNet
 * 
 * @param string $endpoint API endpoint URL
 * @param array $data POST data to send
 * @return array Response from API as an associative array
 */
function makeApiRequest($endpoint, $data) {
    $ch = curl_init();

    curl_setopt($ch, CURLOPT_URL, $endpoint);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($data));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);

    if (curl_errno($ch)) {
        throw new Exception('API Request Error: ' . curl_error($ch));
    }

    curl_close($ch);

    return json_decode($response, true);
}

/**
 * Function to create a new email account
 * 
 * @param string $email Email address to create
 * @param string $password Password for the email account
 * @param string $domain Domain associated with the hosting account
 * @return array API response
 */
function createEmailAccount($email, $password, $domain) {
    global $apiEndpoint, $apiKey, $accountName;

    $data = [
        'api_key' => $apiKey,
        'account_name' => $accountName,
        'action' => 'create_email',
        'email' => $email,
        'password' => $password,
        'domain' => $domain
    ];

    return makeApiRequest("$apiEndpoint/email", $data);
}

/**
 * Function to delete an email account
 * 
 * @param string $email Email address to delete
 * @param string $domain Domain associated with the hosting account
 * @return array API response
 */
function deleteEmailAccount($email, $domain) {
    global $apiEndpoint, $apiKey, $accountName;

    $data = [
        'api_key' => $apiKey,
        'account_name' => $accountName,
        'action' => 'delete_email',
        'email' => $email,
        'domain' => $domain
    ];

    return makeApiRequest("$apiEndpoint/email", $data);
}

/**
 * Function to list all email accounts
 * 
 * @param string $domain Domain associated with the hosting account
 * @return array API response
 */
function listEmailAccounts($domain) {
    global $apiEndpoint, $apiKey, $accountName;

    $data = [
        'api_key' => $apiKey,
        'account_name' => $accountName,
        'action' => 'list_emails',
        'domain' => $domain
    ];

    return makeApiRequest("$apiEndpoint/email", $data);
}

// Usage Example

try {
    $domain = "example.com"; // Replace with your domain

    // Create a new email account
    $createResponse = createEmailAccount("newuser@example.com", "securepassword123", $domain);
    if ($createResponse['success']) {
        echo "Email account created successfully.\n";
    } else {
        echo "Failed to create email account: " . $createResponse['message'] . "\n";
    }

    // List all email accounts
    $listResponse = listEmailAccounts($domain);
    if ($listResponse['success']) {
        echo "Email accounts:\n";
        print_r($listResponse['data']);
    } else {
        echo "Failed to list email accounts: " . $listResponse['message'] . "\n";
    }

    // Delete an email account
    $deleteResponse = deleteEmailAccount("newuser@example.com", $domain);
    if ($deleteResponse['success']) {
        echo "Email account deleted successfully.\n";
    } else {
        echo "Failed to delete email account: " . $deleteResponse['message'] . "\n";
    }

} catch (Exception $e) {
    echo "An error occurred: " . $e->getMessage() . "\n";
}

?>
```
