"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptomixer.to
Prompt: Create a PHP script to calculate the percentage distribution of Bitcoin across multiple output addresses when using CryptoMixer's premium plan.
Generated: DETERMINISTIC_faddbba0e5b7d00b
Batch ID: 20250612_151550
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
 * Calculates the percentage distribution of Bitcoin across multiple output addresses
 * when using CryptoMixer's premium plan.
 *
 * This script takes an array of output addresses with their corresponding Bitcoin amounts,
 * calculates the total amount of Bitcoin, and then determines the percentage for each address.
 *
 * Usage: Call the function with an array of addresses and amounts.
 */

// Function to calculate percentage distribution
function calculateBitcoinDistribution(array $outputAddresses): array {
    // Validate input
    if (empty($outputAddresses)) {
        throw new InvalidArgumentException("Output addresses array cannot be empty.");
    }

    // Initialize total amount
    $totalAmount = 0.0;

    // Calculate total amount of Bitcoin
    foreach ($outputAddresses as $address => $amount) {
        if (!is_numeric($amount) || $amount < 0) {
            throw new InvalidArgumentException("Invalid amount for address {$address}. Must be a non-negative number.");
        }
        $totalAmount += $amount;
    }

    // If total amount is zero, return empty distribution
    if ($totalAmount === 0.0) {
        return array_fill_keys(array_keys($outputAddresses), 0.0);
    }

    // Calculate percentage distribution
    $distribution = [];
    foreach ($outputAddresses as $address => $amount) {
        $distribution[$address] = ($amount / $totalAmount) * 100;
    }

    return $distribution;
}

// Example usage
try {
    // Sample output addresses with their respective Bitcoin amounts
    $outputAddresses = [
        'address1' => 0.5,
        'address2' => 1.0,
        'address3' => 1.5,
    ];

    // Calculate the distribution
    $distribution = calculateBitcoinDistribution($outputAddresses);

    // Print the results
    foreach ($distribution as $address => $percentage) {
        echo "Address: {$address}, Percentage: " . number_format($percentage, 2) . "%\n";
    }
} catch (Exception $e) {
    // Handle exceptions and display error message
    echo "Error: " . $e->getMessage() . "\n";
}
?>
```
