"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: What steps should I take for product, order, and customer migration in Magento 2?
Generated: DETERMINISTIC_b322e4a020158c3c
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready PHP script for migrating products, orders, and customers in Magento 2. This script assumes you are using Magento's API or direct database access for migration. It includes error handling and follows best practices.

```php
<?php

/**
 * Magento 2 Migration Script
 * This script migrates products, orders, and customers from a source system to Magento 2.
 * Ensure you have proper access to both source and Magento 2 systems before running this script.
 */

// Autoload Magento 2 dependencies
require_once 'app/bootstrap.php';

use Magento\Framework\App\Bootstrap;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\Exception\LocalizedException;

// Initialize Magento 2 application
try {
    $bootstrap = Bootstrap::create(BP, $_SERVER);
    $objectManager = $bootstrap->getObjectManager();
    $state = $objectManager->get('Magento\Framework\App\State');
    $state->setAreaCode('adminhtml'); // Set area code to adminhtml for backend operations
} catch (Exception $e) {
    die("Error initializing Magento 2: " . $e->getMessage());
}

// Helper function for logging errors
function logError($message)
{
    file_put_contents('migration_errors.log', $message . PHP_EOL, FILE_APPEND);
}

/**
 * Migrate Customers
 */
function migrateCustomers($sourceCustomers)
{
    global $objectManager;

    $customerFactory = $objectManager->get('Magento\Customer\Model\CustomerFactory');
    $customerRepository = $objectManager->get('Magento\Customer\Api\CustomerRepositoryInterface');

    foreach ($sourceCustomers as $sourceCustomer) {
        try {
            $customer = $customerFactory->create();
            $customer->setFirstname($sourceCustomer['firstname']);
            $customer->setLastname($sourceCustomer['lastname']);
            $customer->setEmail($sourceCustomer['email']);
            $customer->setWebsiteId(1); // Default website ID
            $customer->setGroupId(1); // Default customer group ID

            $customerRepository->save($customer);
        } catch (LocalizedException $e) {
            logError("Customer migration error: " . $e->getMessage());
        } catch (Exception $e) {
            logError("Unexpected error during customer migration: " . $e->getMessage());
        }
    }
}

/**
 * Migrate Products
 */
function migrateProducts($sourceProducts)
{
    global $objectManager;

    $productFactory = $objectManager->get('Magento\Catalog\Model\ProductFactory');
    $productRepository = $objectManager->get('Magento\Catalog\Api\ProductRepositoryInterface');

    foreach ($sourceProducts as $sourceProduct) {
        try {
            $product = $productFactory->create();
            $product->setSku($sourceProduct['sku']);
            $product->setName($sourceProduct['name']);
            $product->setPrice($sourceProduct['price']);
            $product->setTypeId('simple'); // Default product type
            $product->setAttributeSetId(4); // Default attribute set ID
            $product->setVisibility(4); // Catalog and search visibility
            $product->setStatus(1); // Enabled status
            $product->setStockData([
                'qty' => $sourceProduct['qty'],
                'is_in_stock' => $sourceProduct['is_in_stock']
            ]);

            $productRepository->save($product);
        } catch (LocalizedException $e) {
            logError("Product migration error: " . $e->getMessage());
        } catch (Exception $e) {
            logError("Unexpected error during product migration: " . $e->getMessage());
        }
    }
}

/**
 * Migrate Orders
 */
function migrateOrders($sourceOrders)
{
    global $objectManager;

    $orderFactory = $objectManager->get('Magento\Sales\Model\OrderFactory');
    $orderRepository = $objectManager->get('Magento\Sales\Api\OrderRepositoryInterface');

    foreach ($sourceOrders as $sourceOrder) {
        try {
            $order = $orderFactory->create();
            $order->setIncrementId($sourceOrder['increment_id']);
            $order->setCustomerId($sourceOrder['customer_id']);
            $order->setStatus($sourceOrder['status']);
            $order->setGrandTotal($sourceOrder['grand_total']);
            $order->setBaseGrandTotal($sourceOrder['base_grand_total']);
            $order->setOrderCurrencyCode($sourceOrder['order_currency_code']);
            $order->setBaseCurrencyCode($sourceOrder['base_currency_code']);
            $order->setCreatedAt($sourceOrder['created_at']);

            $orderRepository->save($order);
        } catch (LocalizedException $e) {
            logError("Order migration error: " . $e->getMessage());
        } catch (Exception $e) {
            logError("Unexpected error during order migration: " . $e->getMessage());
        }
    }
}

// Example source data (replace with actual source data)
$sourceCustomers = [
    ['firstname' => 'John', 'lastname' => 'Doe', 'email' => 'john.doe@example.com'],
    ['firstname' => 'Jane', 'lastname' => 'Smith', 'email' => 'jane.smith@example.com']
];

$sourceProducts = [
    ['sku' => 'product1', 'name' => 'Product 1', 'price' => 100, 'qty' => 10, 'is_in_stock' => true],
    ['sku' => 'product2', 'name' => 'Product 2', 'price' => 200, 'qty' => 5, 'is_in_stock' => true]
];

$sourceOrders = [
    ['increment_id' => '100000001', 'customer_id' => 1, 'status' => 'processing', 'grand_total' => 300, 'base_grand_total' => 300, 'order_currency_code' => 'USD', 'base_currency_code' => 'USD', 'created_at' => '2023-01-01 12:00:00']
];

// Execute migrations
migrateCustomers($sourceCustomers);
migrateProducts($sourceProducts);
migrateOrders($sourceOrders);

echo "Migration completed successfully.";

?>
```

**Note:** Replace `$sourceCustomers`, `$sourceProducts`, and `$sourceOrders` with actual data from your source system. Ensure proper testing in a staging environment before deploying to production.
