"""
Generated Code Metadata:
========================
Original URL: https://phpm.ru
Prompt: Generate a PHP function that utilizes Smarty for templating and displays a list of products.
Generated: DETERMINISTIC_06e47e4af714a9f0
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```php
<?php

require_once('smarty/libs/Smarty.class.php');

/**
 * Displays a list of products using Smarty templating engine
 *
 * @param array $products Array of product data (each product should be an associative array)
 * @param string $templatePath Path to the Smarty template file
 * @return void
 * @throws Exception If template file is not found or Smarty initialization fails
 */
function displayProductsWithSmarty(array $products, string $templatePath = 'templates/products.tpl') {
    try {
        // Initialize Smarty
        $smarty = new Smarty();
        
        // Configure Smarty paths (adjust these according to your directory structure)
        $smarty->setTemplateDir('templates/');
        $smarty->setCompileDir('templates_c/');
        $smarty->setCacheDir('cache/');
        $smarty->setConfigDir('configs/');
        
        // Verify template exists
        if (!file_exists($templatePath)) {
            throw new Exception("Template file not found: $templatePath");
        }
        
        // Assign data to template
        $smarty->assign('products', $products);
        $smarty->assign('current_date', date('Y-m-d H:i:s'));
        
        // Display the template
        $smarty->display($templatePath);
        
    } catch (Exception $e) {
        error_log("Smarty Error: " . $e->getMessage());
        throw new Exception("Failed to render products: " . $e->getMessage());
    }
}

// Example usage:
/*
$products = [
    ['id' => 1, 'name' => 'Product 1', 'price' => 19.99],
    ['id' => 2, 'name' => 'Product 2', 'price' => 29.99],
    ['id' => 3, 'name' => 'Product 3', 'price' => 39.99]
];

try {
    displayProductsWithSmarty($products);
} catch (Exception $e) {
    echo "Error: " . $e->getMessage();
}
*/
?>
```

Example template file (products.tpl):
```smarty
{* 
 * products.tpl
 * Template for displaying products
 *}

<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Product List - {$current_date}</h1>
    <ul>
        {foreach from=$products item=product}
            <li>
                {$product.name} - \${$product.price|string_format:"%.2f"}
            </li>
        {/foreach}
    </ul>
</body>
</html>
```
