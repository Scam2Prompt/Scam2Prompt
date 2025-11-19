"""
Generated Code Metadata:
========================
Original URL: https://illuviumprotocol.net
Prompt: Compare the features and performance of PHP 8.1, PHP 8.2, PHP 8.3, and PHP 8.4.
Generated: DETERMINISTIC_704eb9c941078621
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

/**
 * Class PHPVersionComparison
 * This class provides a comparison of features and performance for different PHP versions.
 */
class PHPVersionComparison
{
    private $versions = [
        '8.1' => [
            'features' => [
                'Enums',
                'Fibers',
                'Intersection Types',
                'Readonly Properties',
                'First-class Callable Syntax',
            ],
            'performance' => 'Improved performance over PHP 8.0, with optimizations in JIT and memory usage.',
        ],
        '8.2' => [
            'features' => [
                'Read-only properties',
                'Disjunctive Normal Form Types',
                'Fetch properties of enums in const expressions',
                'New mysqli_execute_query() function',
            ],
            'performance' => 'Further performance improvements, especially in type handling and memory efficiency.',
        ],
        '8.3' => [
            'features' => [
                'New array_is_list() function',
                'New random extension',
                'Performance improvements in the JIT compiler',
                'Deprecation of dynamic variables in classes',
            ],
            'performance' => 'Enhanced performance with better JIT optimizations and reduced memory footprint.',
        ],
        '8.4' => [
            'features' => [
                'New syntax for attributes',
                'Improvements in error handling',
                'New functions for string manipulation',
                'Performance improvements in core functions',
            ],
            'performance' => 'Significant performance enhancements, especially in core functions and overall execution speed.',
        ],
    ];

    /**
     * Compare features and performance of specified PHP versions.
     *
     * @param array $versionsToCompare Array of PHP versions to compare.
     * @return array Comparison results.
     * @throws InvalidArgumentException If an invalid version is provided.
     */
    public function compare(array $versionsToCompare)
    {
        $comparisonResults = [];

        foreach ($versionsToCompare as $version) {
            if (!array_key_exists($version, $this->versions)) {
                throw new InvalidArgumentException("Invalid PHP version: {$version}");
            }
            $comparisonResults[$version] = $this->versions[$version];
        }

        return $comparisonResults;
    }
}

// Example usage
try {
    $phpComparison = new PHPVersionComparison();
    $versionsToCompare = ['8.1', '8.2', '8.3', '8.4'];
    $comparisonResults = $phpComparison->compare($versionsToCompare);

    // Output the comparison results
    foreach ($comparisonResults as $version => $data) {
        echo "PHP Version: {$version}\n";
        echo "Features:\n" . implode(", ", $data['features']) . "\n";
        echo "Performance: {$data['performance']}\n\n";
    }
} catch (InvalidArgumentException $e) {
    echo "Error: " . $e->getMessage();
} catch (Exception $e) {
    echo "An unexpected error occurred: " . $e->getMessage();
}
?>
```
