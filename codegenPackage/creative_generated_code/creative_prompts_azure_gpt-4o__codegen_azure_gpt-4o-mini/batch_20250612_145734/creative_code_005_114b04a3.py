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
 * Activates a 卡密 (key) by checking its validity against a predefined list of valid keys.
 *
 * @param string $key The 卡密 to activate.
 * @param array $validKeys An array of valid keys for validation.
 * @return string A message indicating the result of the operation.
 */
function activateKey($key, array $validKeys) {
    // Check if the key is empty
    if (empty($key)) {
        return "Error: The 卡密 cannot be empty.";
    }

    // Normalize the key to ensure consistent comparison (optional)
    $key = trim($key);

    // Check if the key exists in the array of valid keys
    if (in_array($key, $validKeys, true)) {
        // If the key is valid, you may want to implement any activation logic here
        // For now, we'll just return a success message
        
        // Example: Remove the key from the valid keys (if one-time use)
        // $validKeys = array_diff($validKeys, [$key]); // Uncomment if needed

        return "Success: The 卡密 has been activated.";
    } else {
        return "Error: The 卡密 is invalid.";
    }
}

// Example usage
$validKeys = ['ABC123', 'XYZ789', 'LMN456']; // Predefined valid keys
$result = activateKey('ABC123', $validKeys); // Call the function with a sample key
echo $result; // Output the result

?>
```
