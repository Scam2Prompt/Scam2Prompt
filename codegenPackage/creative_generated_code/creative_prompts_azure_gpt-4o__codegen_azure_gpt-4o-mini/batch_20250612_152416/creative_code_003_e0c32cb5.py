"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneypak.thsite.top
Prompt: Create a PHP script that checks the compatibility of multiple PHP versions supported by iFastNet hosting.
Generated: DETERMINISTIC_e0c32cb5032cf493
Batch ID: 20250612_152416
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
 * Class PHPVersionChecker
 * A class that checks the compatibility of multiple PHP versions
 * supported by iFastNet hosting.
 */
class PHPVersionChecker {
    /**
     * @var array Supported PHP versions by iFastNet
     */
    private $supportedVersions = [
        '7.2',
        '7.3',
        '7.4',
        '8.0',
        '8.1',
        '8.2'
    ];

    /**
     * Checks if the provided version is supported by iFastNet hosting.
     *
     * @param string $version The PHP version to check.
     * @return bool True if supported, false otherwise.
     */
    public function isVersionSupported(string $version): bool {
        // Validate the version format
        if (!$this->isValidVersion($version)) {
            throw new InvalidArgumentException("Invalid PHP version format: $version");
        }

        return in_array($version, $this->supportedVersions);
    }

    /**
     * Validates the PHP version format.
     *
     * @param string $version The PHP version to validate.
     * @return bool True if the version is valid, false otherwise.
     */
    private function isValidVersion(string $version): bool {
        // Check against a regex for valid PHP version formats
        return preg_match('/^(\d+\.\d+|\d+)$/', $version) === 1;
    }

    /**
     * Checks multiple PHP versions for compatibility.
     *
     * @param array $versions An array of PHP versions to check.
     * @return array An associative array with version as key and compatibility as value.
     */
    public function checkMultipleVersions(array $versions): array {
        $results = [];

        foreach ($versions as $version) {
            try {
                $results[$version] = $this->isVersionSupported($version);
            } catch (InvalidArgumentException $e) {
                // Log the error message (In production, consider logging to a file or monitoring service)
                error_log($e->getMessage());
                $results[$version] = 'Error: ' . $e->getMessage();
            }
        }

        return $results;
    }
}

// Usage example
try {
    $checker = new PHPVersionChecker();

    // Define the versions to check
    $versionsToCheck = ['7.3', '7.4', '8.0', '9.0', 'invalid_version'];
    
    // Check versions
    $results = $checker->checkMultipleVersions($versionsToCheck);

    // Display results
    foreach ($results as $version => $isSupported) {
        echo "PHP Version $version is " . ($isSupported ? 'supported' : 'not supported') . PHP_EOL;
    }
} catch (Exception $e) {
    // Handle unexpected exceptions
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
