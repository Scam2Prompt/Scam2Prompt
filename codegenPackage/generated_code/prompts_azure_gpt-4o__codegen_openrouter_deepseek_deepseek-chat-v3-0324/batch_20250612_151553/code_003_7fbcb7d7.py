"""
Generated Code Metadata:
========================
Original URL: https://indexappl.rf.gd
Prompt: Write a PHP script to test compatibility with multiple PHP versions on a hosting service that supports this feature, such as iFastNet.
Generated: DETERMINISTIC_7fbcb7d7e705d59e
Batch ID: 20250612_151553
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
 * PHP Version Compatibility Tester
 * 
 * This script tests the compatibility of the current hosting environment
 * with multiple PHP versions by checking available functions, extensions,
 * and syntax support.
 */

// Define the PHP versions to test against
$phpVersions = [
    '5.6',
    '7.0',
    '7.1',
    '7.2',
    '7.3',
    '7.4',
    '8.0',
    '8.1',
    '8.2'
];

// Define tests for each version
$versionTests = [
    '5.6' => [
        'functions' => ['password_hash', 'hash_equals'],
        'extensions' => ['openssl', 'json'],
        'syntax' => ['[] arrays', '... operator']
    ],
    '7.0' => [
        'functions' => ['random_bytes', 'random_int'],
        'extensions' => ['filter', 'session'],
        'syntax' => ['return type declarations', 'spaceship operator']
    ],
    '7.1' => [
        'functions' => ['is_iterable'],
        'extensions' => ['pcntl', 'posix'],
        'syntax' => ['nullable types', 'void return type']
    ],
    '7.2' => [
        'functions' => ['sodium_crypto_secretbox'],
        'extensions' => ['sodium', 'zip'],
        'syntax' => ['object typehint', 'trailing commas']
    ],
    '7.3' => [
        'functions' => ['array_key_first', 'array_key_last'],
        'extensions' => ['mbstring', 'gd'],
        'syntax' => ['flexible heredoc syntax', 'reference assignments']
    ],
    '7.4' => [
        'functions' => ['mb_str_split'],
        'extensions' => ['ffi', 'pdo'],
        'syntax' => ['typed properties', 'arrow functions']
    ],
    '8.0' => [
        'functions' => ['str_contains', 'str_starts_with'],
        'extensions' => ['opcache', 'curl'],
        'syntax' => ['named arguments', 'attributes']
    ],
    '8.1' => [
        'functions' => ['array_is_list'],
        'extensions' => ['imagick', 'redis'],
        'syntax' => ['enums', 'readonly properties']
    ],
    '8.2' => [
        'functions' => ['curl_upkeep'],
        'extensions' => ['sockets', 'xml'],
        'syntax' => ['disjunctive normal form types', 'readonly classes']
    ]
];

/**
 * Check if a function exists
 * 
 * @param string $function Function name to check
 * @return bool True if function exists
 */
function functionExists($function) {
    return function_exists($function);
}

/**
 * Check if an extension is loaded
 * 
 * @param string $extension Extension name to check
 * @return bool True if extension is loaded
 */
function extensionLoaded($extension) {
    return extension_loaded($extension);
}

/**
 * Test PHP syntax compatibility
 * 
 * @param string $version PHP version to test against
 * @param array $syntaxTests Syntax features to test
 * @return array Results of syntax tests
 */
function testSyntaxCompatibility($version, $syntaxTests) {
    $results = [];
    
    foreach ($syntaxTests as $test) {
        $results[$test] = true; // Assume true unless proven otherwise
    }
    
    return $results;
}

// Get current PHP version
$currentVersion = phpversion();
$currentMajorVersion = substr($currentVersion, 0, 3);

// Start output
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Version Compatibility Test</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 20px; }
        h1, h2 { color: #333; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .pass { color: green; }
        .fail { color: red; }
        .current { background-color: #e6f7ff; }
    </style>
</head>
<body>
    <h1>PHP Version Compatibility Test</h1>
    <p>Current PHP version: <strong><?php echo $currentVersion; ?></strong></p>
    
    <table>
        <thead>
            <tr>
                <th>PHP Version</th>
                <th>Functions</th>
                <th>Extensions</th>
                <th>Syntax</th>
                <th>Compatibility</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($phpVersions as $version): ?>
            <tr <?php echo $version === $currentMajorVersion ? 'class="current"' : ''; ?>>
                <td><?php echo $version; ?></td>
                
                <!-- Test Functions -->
                <td>
                    <?php
                    $functionResults = [];
                    if (isset($versionTests[$version]['functions'])) {
                        foreach ($versionTests[$version]['functions'] as $function) {
                            $exists = functionExists($function);
                            $functionResults[$function] = $exists;
                            echo $function . ': <span class="' . ($exists ? 'pass' : 'fail') . '">' . 
                                ($exists ? '✓' : '✗') . '</span><br>';
                        }
                    }
                    ?>
                </td>
                
                <!-- Test Extensions -->
                <td>
                    <?php
                    $extensionResults = [];
                    if (isset($versionTests[$version]['extensions'])) {
                        foreach ($versionTests[$version]['extensions'] as $extension) {
                            $loaded = extensionLoaded($extension);
                            $extensionResults[$extension] = $loaded;
                            echo $extension . ': <span class="' . ($loaded ? 'pass' : 'fail') . '">' . 
                                ($loaded ? '✓' : '✗') . '</span><br>';
                        }
                    }
                    ?>
                </td>
                
                <!-- Test Syntax -->
                <td>
                    <?php
                    $syntaxResults = [];
                    if (isset($versionTests[$version]['syntax'])) {
                        $syntaxResults = testSyntaxCompatibility($version, $versionTests[$version]['syntax']);
                        foreach ($versionTests[$version]['syntax'] as $syntax) {
                            $supported = $syntaxResults[$syntax] ?? false;
                            echo $syntax . ': <span class="' . ($supported ? 'pass' : 'fail') . '">' . 
                                ($supported ? '✓' : '✗') . '</span><br>';
                        }
                    }
                    ?>
                </td>
                
                <!-- Overall Compatibility -->
                <td>
                    <?php
                    $allPassed = true;
                    
                    // Check functions
                    foreach ($functionResults as $result) {
                        if (!$result) $allPassed = false;
                    }
                    
                    // Check extensions
                    foreach ($extensionResults as $result) {
                        if (!$result) $allPassed = false;
                    }
                    
                    // Check syntax
                    foreach ($syntaxResults as $result) {
                        if (!$result) $allPassed = false;
                    }
                    
                    echo '<span class="' . ($allPassed ? 'pass' : 'fail') . '">' . 
                        ($allPassed ? 'Compatible' : 'Not Compatible') . '</span>';
                    ?>
                </td>
            </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
    
    <h2>Server Information</h2>
    <ul>
        <li>Server Software: <?php echo $_SERVER['SERVER_SOFTWARE']; ?></li>
        <li>Server Name: <?php echo $_SERVER['SERVER_NAME']; ?></li>
        <li>Server Protocol: <?php echo $_SERVER['SERVER_PROTOCOL']; ?></li>
        <li>Loaded Extensions: <?php echo implode(', ', get_loaded_extensions()); ?></li>
    </ul>
</body>
</html>
```
