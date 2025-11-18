"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchain.hstn.me
Prompt: Write a PHP script to test compatibility with multiple PHP versions offered by iFastNet hosting.
Generated: DETERMINISTIC_421a9e7c54e1a476
Batch ID: 20250612_150342
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
 * PHP Compatibility Tester
 * This script checks for compatibility with multiple PHP versions.
 * It outputs the version currently running and a check for basic features
 * present in different PHP versions.
 */

// Define an array of PHP versions to test compatibility against
$phpVersions = [
    '7.0' => '7.0.0',
    '7.1' => '7.1.0',
    '7.2' => '7.2.0',
    '7.3' => '7.3.0',
    '7.4' => '7.4.0',
    '8.0' => '8.0.0',
    '8.1' => '8.1.0',
    '8.2' => '8.2.0',
];

// Function to test compatibility with a specific PHP version
function isCompatibleWithVersion($requiredVersion)
{
    // Get the current PHP version
    $currentVersion = phpversion();

    // Compare current version with required version
    return version_compare($currentVersion, $requiredVersion, '>=');
}

// Run compatibility tests for each version
foreach ($phpVersions as $version => $minVersion) {
    echo "Testing compatibility with PHP version $version...\n";
    
    if (isCompatibleWithVersion($minVersion)) {
        echo "Compatible with PHP $version\n";
    } else {
        echo "Not compatible with PHP $version\n";
    }
}

// Additional compatibility checks for specific features
echo "\nChecking specific features:\n";

$features = [
    'Null Coalescing Operator' => '??',
    'Spaceship Operator' => '<=>',
    'Typed Properties' => 'declare(strict_types=1);',
    'Match Expression' => 'match',
];

foreach ($features as $feature => $example) {
    echo "Checking for feature: $feature\n";
    switch ($feature) {
        case 'Null Coalescing Operator':
            $test = null ?? 'default';
            echo "  - Null Coalescing: " . ($test === 'default' ? 'Available' : 'Not Available') . "\n";
            break;
        case 'Spaceship Operator':
            $test = (1 <=> 1);
            echo "  - Spaceship Operator: " . ($test === 0 ? 'Available' : 'Not Available') . "\n";
            break;
        case 'Typed Properties':
            // Note: Typed properties are available from PHP 7.4 onwards
            if (version_compare(PHP_VERSION, '7.4.0', '>=')) {
                $test = new class {
                    public int $property = 1;
                };
                echo "  - Typed Properties: Available\n";
            } else {
                echo "  - Typed Properties: Not Available\n";
            }
            break;
        case 'Match Expression':
            // Note: Match expressions are available from PHP 8.0
            if (version_compare(PHP_VERSION, '8.0.0', '>=')) {
                $test = match(1) {
                    1 => 'one',
                    default => 'other',
                };
                echo "  - Match Expression: Available\n";
            } else {
                echo "  - Match Expression: Not Available\n";
            }
            break;
        default:
            echo "  - Unknown feature\n";
            break;
    }
}

// End of the script
echo "\nCompatibility check completed.\n";
?>
```
