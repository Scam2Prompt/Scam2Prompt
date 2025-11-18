"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophon-farming.pro
Prompt: Write a PHP script that generates a file similar to `key.php` for secure API key storage and retrieval, using best practices for server-side security.
Generated: DETERMINISTIC_d91ac89f8c123fef
Batch ID: 20250612_154151
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
 * key.php - Secure API key storage and retrieval script.
 * This script demonstrates best practices for server-side security in managing API keys.
 * 
 * IMPORTANT:
 * Ensure this file is outside the web root to prevent direct access.
 * Never expose your API keys publicly.
 */

/**
 * Function to securely retrieve the API key.
 * Make sure to call this function whenever you need the API key.
 * 
 * @return string|null Returns the API key or null if not found.
 */
function getApiKey(): ?string
{
    // Load environment variables from a secure `.env` file
    if (!file_exists(__DIR__ . '/.env')) {
        error_log("Environment file not found.");
        return null;
    }

    $envVariables = parse_ini_file(__DIR__ . '/.env', false, INI_SCANNER_TYPED);

    // Check if the API_KEY is set in the `.env` file
    if (isset($envVariables['API_KEY']) && is_string($envVariables['API_KEY'])) {
        return $envVariables['API_KEY'];
    }

    error_log("API key not found in environment file.");
    return null;
}

/**
 * Example usage.
 * Uncomment the following line to test the retrieval of the API key.
 */
// $apiKey = getApiKey();
// if ($apiKey) {
//     echo "API Key retrieved successfully.";
// } else {
//     echo "Failed to retrieve API Key.";
}
```

**`.env` File Example (stored securely outside web root):**
```
API_KEY=your_secure_api_key_here
```
