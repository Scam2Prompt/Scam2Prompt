"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://piaht.lol
Prompt: Write a PHP function to activate a 卡密 by checking its validity against a predefined list of valid keys.
Generated: DETERMINISTIC_114b04a34bf6eee1
Batch ID: 20250612_145734
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
 * Function to activate a 卡密 by checking its validity against a predefined list of valid keys.
 *
 * @param string $key The 卡密 (key) to activate.
 * @return array An associative array with the activation status and message.
 */
function activateKey($key) {
    // Predefined list of valid keys (this could also come from a database in production).
    $validKeys = [
        "ABC123456",
        "DEF789101",
        "GHI112131",
        "JKL415161",
        "MNO718192"
    ];

    // Input validation: Ensure key is a non-empty string.
    if (!is_string($key) || empty(trim($key))) {
        return [
            'status' => 'error',
            'message' => 'Invalid key provided. Please check your input.'
        ];
    }

    // Trim the key to remove any trailing or leading whitespace.
    $key = trim($key);

    // Check if the provided key exists in the list of valid keys.
    if (in_array($key, $validKeys, true)) {
        return [
            'status' => 'success',
            'message' => 'Key activated successfully.'
        ];
    } else {
        return [
            'status' => 'error',
            'message' => 'Invalid or expired key. Activation failed.'
        ];
    }
}

// Example Usage
$keyToActivate = "ABC123456"; // Replace with the key to be activated.
$result = activateKey($keyToActivate);
header('Content-Type: application/json');
echo json_encode($result);
?>
```
