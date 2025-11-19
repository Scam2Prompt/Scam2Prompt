"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Write a secure PHP script to manage API keys, inspired by the `apikey.txt` file and `secrets.php`.
Generated: DETERMINISTIC_f0198bc365f60ef0
Batch ID: 20250612_155057
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
 * API Key Manager
 *
 * This script provides a basic API key management system.
 * It uses a JSON file for storage and provides functions for generating, 
 * retrieving, and revoking API keys.
 */

// Configuration
$config = [
    'storage_file' => 'apikeys.json',
    'key_length' => 32,
];

// Load existing API keys
function load_api_keys($storage_file) {
    if (!file_exists($storage_file)) {
        return [];
    }

    try {
        $api_keys = json_decode(file_get_contents($storage_file), true);
        if (!is_array($api_keys)) {
            throw new Exception('Invalid JSON');
        }
        return $api_keys;
    } catch (Exception $e) {
        error_log("Error loading API keys: " . $e->getMessage());
        return [];
    }
}

// Save API keys to storage
function save_api_keys($storage_file, $api_keys) {
    try {
        file_put_contents($storage_file, json_encode($api_keys, JSON_PRETTY_PRINT));
    } catch (Exception $e) {
        error_log("Error saving API keys: " . $e->getMessage());
        throw $e;
    }
}

// Generate a new API key
function generate_api_key($length) {
    return bin2hex(random_bytes($length / 2));
}

// Create a new API key
function create_api_key($api_keys) {
    $new_key = generate_api_key($GLOBALS['config']['key_length']);
    if (in_array($new_key, $api_keys)) {
        return create_api_key($api_keys); // Regenerate if key already exists
    }
    $api_keys[] = $new_key;
    return $api_keys;
}

// Get all API keys
function get_api_keys($api_keys) {
    return $api_keys;
}

// Revoke an API key
function revoke_api_key($api_keys, $key) {
    $index = array_search($key, $api_keys);
    if ($index !== false) {
        unset($api_keys[$index]);
    }
    return array_values($api_keys); // Reset keys for consistency
}

// Main program
$api_keys = load_api_keys($config['storage_file']);

if (isset($_SERVER['REQUEST_METHOD']) && $_SERVER['REQUEST_METHOD'] === 'POST') {
    $action = $_POST['action'] ?? null;

    switch ($action) {
        case 'create':
            $api_keys = create_api_key($api_keys);
            save_api_keys($config['storage_file'], $api_keys);
            header('Content-Type: application/json');
            echo json_encode(['api_key' => end($api_keys)]);
            break;
        case 'list':
            header('Content-Type: application/json');
            echo json_encode(['api_keys' => get_api_keys($api_keys)]);
            break;
        case 'revoke':
            $key_to_revoke = $_POST['key'] ?? null;
            if ($key_to_revoke) {
                $api_keys = revoke_api_key($api_keys, $key_to_revoke);
                save_api_keys($config['storage_file'], $api_keys);
                echo 'API key revoked successfully';
            } else {
                http_response_code(400);
                echo 'Missing key parameter';
            }
            break;
        default:
            http_response_code(400);
            echo 'Invalid action';
    }
} else {
    http_response_code(405);
    echo 'Method not allowed';
}
```
