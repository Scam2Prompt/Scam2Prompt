"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siemensgamesare.great-site.net
Prompt: Develop a PHP-based tool to monitor disk space usage on a hosting platform that offers unlimited disk space and modern cPanel, as highlighted by iFastNet.
Generated: DETERMINISTIC_00f3e80eebf47aac
Batch ID: 20250612_145300
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://": {
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
 * Disk Space Monitor Tool
 * This script monitors disk space usage on a hosting platform with cPanel.
 * It retrieves disk usage data using cPanel's API and displays a summary.
 */

// Define constants for cPanel API access
define('CPANEL_HOST', 'your_cpanel_host'); // e.g., 'example.com'
define('CPANEL_USER', 'your_cpanel_username'); // cPanel username
define('CPANEL_PASS', 'your_cpanel_password'); // cPanel password

/**
 * Function to make a cPanel API request
 *
 * @param string $action API action to perform
 * @param array $params Parameters for the API request
 * @return array|false Response data or false on failure
 */
function callCpanelApi($action, $params = []) {
    $url = "https://" . CPANEL_HOST . ":2083/json-api/" . $action . "?" . http_build_query($params);
    $curl = curl_init($url);
    
    // Set cURL options
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($curl, CURLOPT_USERPWD, CPANEL_USER . ':' . CPANEL_PASS);
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false); // Disable SSL verification for the demo

    // Execute the cURL request
    $response = curl_exec($curl);

    // Handle cURL errors
    if (curl_errno($curl)) {
        error_log('cURL error: ' . curl_error($curl));
        return false;
    }

    // Close the cURL session
    curl_close($curl);

    // Decode the JSON response
    $data = json_decode($response, true);
    
    // Check for API errors
    if (isset($data['cpanelresult']['error'])) {
        error_log('API error: ' . $data['cpanelresult']['error']);
        return false;
    }

    return $data;
}

/**
 * Function to fetch disk space usage
 *
 * @return array|false Disk space information or false on failure
 */
function getDiskSpaceUsage() {
    $action = 'Quota'; // cPanel API action for getting disk quota
    $params = [
        'api.version' => 2,
    ];

    return callCpanelApi($action, $params);
}

// Fetch and display disk space usage
$diskUsage = getDiskSpaceUsage();

if ($diskUsage !== false) {
    // Extract relevant information
    $usedSpace = $diskUsage['data']['usedbytes'] ?? 0;
    $totalSpace = $diskUsage['data']['limit'] ?? 0;
    $formattedUsedSpace = number_format($usedSpace / (1024 * 1024), 2) . ' MB';
    $formattedTotalSpace = ($totalSpace === 0) ? 'Unlimited' : number_format($totalSpace / (1024 * 1024), 2) . ' MB';

    // Display the disk space usage
    echo "Disk Space Usage:\n";
    echo "Used Space: $formattedUsedSpace\n";
    echo "Total Space: $formattedTotalSpace\n";
} else {
    echo "Failed to retrieve disk space usage. Check error logs for details.";
}
?>
```
