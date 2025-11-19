"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magentobuldozer.com
Prompt: What are the best practices for utilizing Magento Buldozer in a multi-store setup?
Generated: DETERMINISTIC_745bc15e73ec0a7c
Batch ID: 20250612_161059
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
 * Magento Buldozer Multi-Store Setup
 *
 * This script demonstrates best practices for utilizing Magento Buldozer
 * in a multi-store setup. It assumes that Magento is properly installed
 * and that you have access to the necessary configurations.
 */

// Autoload Magento classes
require_once 'app/bootstrap.php';

use Magento\Framework\App\Bootstrap;
use Magento\Framework\App\ObjectManager;

try {
    // Bootstrap the Magento application
    $bootstrap = Bootstrap::create(BP, $_SERVER);
    $objectManager = $bootstrap->getObjectManager();

    // Initialize the application
    $state = $objectManager->get('Magento\Framework\App\State');
    $state->setAreaCode('frontend');

    // Function to set up a store with its configuration
    function setupStore($storeCode, $storeName, $rootCategoryId) {
        global $objectManager;
        
        // Load store manager
        $storeManager = $objectManager->get('Magento\Store\Model\StoreManagerInterface');

        // Check if the store already exists
        $store = $storeManager->getStore($storeCode);
        if ($store->getId()) {
            throw new Exception("Store with code {$storeCode} already exists.");
        }

        // Create new store
        $storeFactory = $objectManager->get('Magento\Store\Model\StoreFactory');
        $newStore = $storeFactory->create();

        $newStore->setCode($storeCode)
                 ->setName($storeName)
                 ->setRootCategoryId($rootCategoryId)
                 ->setIsActive(1);

        // Save the store
        $newStore->save();
        echo "Store '{$storeName}' created successfully.\n";
    }

    // Example usage of setupStore function
    // Add your store configurations here
    $stores = [
        ['code' => 'store1', 'name' => 'Store 1', 'rootCategoryId' => 2],
        ['code' => 'store2', 'name' => 'Store 2', 'rootCategoryId' => 3],
    ];

    foreach ($stores as $storeConfig) {
        try {
            setupStore($storeConfig['code'], $storeConfig['name'], $storeConfig['rootCategoryId']);
        } catch (Exception $e) {
            // Log error message
            error_log($e->getMessage());
            echo "Failed to create store '{$storeConfig['name']}': " . $e->getMessage() . "\n";
        }
    }

} catch (Exception $e) {
    // Handle any bootstrap-related exceptions
    error_log('Bootstrap Error: ' . $e->getMessage());
    echo 'Failed to initialize the application: ' . $e->getMessage();
}
```
