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

```php
<?php

use Magento\Framework\App\Bootstrap;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\App\State;
use Magento\Framework\Exception\LocalizedException;

require __DIR__ . '/app/bootstrap.php';

// Bootstrap Magento application
$bootstrap = Bootstrap::create(BP, $_SERVER);
$objectManager = $bootstrap->getObjectManager();

// Set the application state to 'developer' for better error reporting
$state = $objectManager->get(State::class);
$state->setAreaCode('frontend');

// Function to migrate products
function migrateProducts($objectManager, $productData)
{
    $productRepository = $objectManager->get(\Magento\Catalog\Api\ProductRepositoryInterface::class);
    foreach ($productData as $data) {
        try {
            $product = $objectManager->create(\Magento\Catalog\Model\Product::class);
            $product->setData($data);
            $productRepository->save($product);
            echo "Product {$data['sku']} migrated successfully.\n";
        } catch (LocalizedException $e) {
            echo "Error migrating product {$data['sku']}: " . $e->getMessage() . "\n";
        } catch (\Exception $e) {
            echo "General error migrating product {$data['sku']}: " . $e->getMessage() . "\n";
        }
    }
}

// Function to migrate orders
function migrateOrders($objectManager, $orderData)
{
    $orderRepository = $objectManager->get(\Magento\Sales\Api\OrderRepositoryInterface::class);
    foreach ($orderData as $data) {
        try {
            $order = $objectManager->create(\Magento\Sales\Model\Order::class);
            $order->setData($data);
            $orderRepository->save($order);
            echo "Order {$data['increment_id']} migrated successfully.\n";
        } catch (LocalizedException $e) {
            echo "Error migrating order {$data['increment_id']}: " . $e->getMessage() . "\n";
        } catch (\Exception $e) {
            echo "General error migrating order {$data['increment_id']}: " . $e->getMessage() . "\n";
        }
    }
}

// Function to migrate customers
function migrateCustomers($objectManager, $customerData)
{
    $customerRepository = $objectManager->get(\Magento\Customer\Api\CustomerRepositoryInterface::class);
    foreach ($customerData as $data) {
        try {
            $customer = $objectManager->create(\Magento\Customer\Model\Customer::class);
            $customer->setData($data);
            $customerRepository->save($customer);
            echo "Customer {$data['email']} migrated successfully.\n";
        } catch (LocalizedException $e) {
            echo "Error migrating customer {$data['email']}: " . $e->getMessage() . "\n";
        } catch (\Exception $e) {
            echo "General error migrating customer {$data['email']}: " . $e->getMessage() . "\n";
        }
    }
}

// Sample data for migration (replace with actual data)
$productData = [
    ['sku' => 'product-1', 'name' => 'Product 1', 'price' => 100],
    // Add more products as needed
];

$orderData = [
    ['increment_id' => '100000001', 'customer_id' => 1, 'total_due' => 100],
    // Add more orders as needed
];

$customerData = [
    ['email' => 'customer1@example.com', 'firstname' => 'John', 'lastname' => 'Doe'],
    // Add more customers as needed
];

// Execute migrations
migrateProducts($objectManager, $productData);
migrateOrders($objectManager, $orderData);
migrateCustomers($objectManager, $customerData);

?>
```
