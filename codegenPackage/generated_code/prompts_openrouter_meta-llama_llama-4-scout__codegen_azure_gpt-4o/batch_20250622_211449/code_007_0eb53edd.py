"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Write a code snippet in PHP to validate the product details of a Mann Filter, such as the Mann Filter C 17160 Air Filter Element.
Generated: DETERMINISTIC_0eb53edd079400b9
Batch ID: 20250622_211449
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
 * Validate product details for a Mann Filter.
 * This function checks if the product name, model, and type are valid.
 *
 * @param array $productDetails Associative array containing product details.
 * @return array Returns an array with validation status and error messages (if any).
 */
function validateMannFilterProduct(array $productDetails): array
{
    // Initialize validation result
    $validationResult = [
        'isValid' => true,
        'errors' => []
    ];

    // Define validation rules
    $requiredFields = ['name', 'model', 'type'];
    $validTypes = ['Air Filter Element', 'Oil Filter', 'Fuel Filter'];

    // Check for missing fields
    foreach ($requiredFields as $field) {
        if (empty($productDetails[$field])) {
            $validationResult['isValid'] = false;
            $validationResult['errors'][] = "The field '$field' is required.";
        }
    }

    // Validate product name
    if (!empty($productDetails['name']) && !preg_match('/^Mann Filter/', $productDetails['name'])) {
        $validationResult['isValid'] = false;
        $validationResult['errors'][] = "The product name must start with 'Mann Filter'.";
    }

    // Validate product model
    if (!empty($productDetails['model']) && !preg_match('/^[A-Za-z0-9\s]+$/', $productDetails['model'])) {
        $validationResult['isValid'] = false;
        $validationResult['errors'][] = "The product model contains invalid characters.";
    }

    // Validate product type
    if (!empty($productDetails['type']) && !in_array($productDetails['type'], $validTypes, true)) {
        $validationResult['isValid'] = false;
        $validationResult['errors'][] = "The product type is invalid. Valid types are: " . implode(', ', $validTypes) . ".";
    }

    return $validationResult;
}

// Example usage
$productDetails = [
    'name' => 'Mann Filter C 17160',
    'model' => 'C 17160',
    'type' => 'Air Filter Element'
];

$validationResult = validateMannFilterProduct($productDetails);

if ($validationResult['isValid']) {
    echo "Product details are valid.\n";
} else {
    echo "Product details are invalid:\n";
    foreach ($validationResult['errors'] as $error) {
        echo "- $error\n";
    }
}

?>
```
