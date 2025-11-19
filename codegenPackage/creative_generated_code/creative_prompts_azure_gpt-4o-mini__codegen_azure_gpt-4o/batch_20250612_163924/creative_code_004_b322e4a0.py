"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: What steps should I take for product, order, and customer migration in Magento 2?
Generated: DETERMINISTIC_b322e4a020158c3c
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a PHP script for product, order, and customer migration in Magento 2. This script assumes you are migrating data from an external system or database into Magento 2.

```php
<?php

use Magento\Framework\App\Bootstrap;
use Magento\Framework\App\ObjectManager;
use Magento\Customer\Api\CustomerRepositoryInterface;
use Magento\Catalog\Api\ProductRepositoryInterface;
use Magento\Sales\Api\OrderRepositoryInterface;

require __DIR__ . '/app/bootstrap.php';

// Initialize Magento framework
$bootstrap = Bootstrap::create(BP, $_SERVER);
$app = $bootstrap->getObjectManager();
$app->get('Magento\Framework\App\State')->setAreaCode('adminhtml');

// Object Manager for dependency injection
$objectManager = ObjectManager::getInstance();

// Define external source data (replace with actual source logic)
$externalCustomers = [
    [
        'email' => 'john.doe@example.com',
        'firstname' => 'John',
        'lastname' => 'Doe',
        'password' => 'password123',
    ],
];

$externalProducts = [
    [
        'sku' => 'product-001',
        'name' => 'Sample Product',
        'price' => 99.99,
        'weight' => 1.5,
        'attribute_set_id' => 4, // Replace with valid attribute set ID
        'type_id' => 'simple',
        'status' => 1,
        'visibility' => 4,
        'qty' => 100,
    ],
];

$externalOrders = [
    [
        'customer_email' => 'john.doe@example.com',
        'items' => [
            ['sku' => 'product-001', 'qty' => 1],
        ],
        'total' => 99.99,
        'status' => 'processing',
    ],
];

// Migrate Customers
$customerRepository = $objectManager->get(CustomerRepositoryInterface);
foreach ($externalCustomers as $customerData) {
    try {
        // Check if customer already exists
        $existingCustomer = $customerRepository->get($customerData['email']);
        echo "Customer '{$customerData['email']}' already exists.\n";
    } catch (\Magento\Framework\Exception\NoSuchEntityException $e) {
        // Create new customer
        $customerFactory = $objectManager->get('\Magento\Customer\Model\CustomerFactory');
        $customer = $customerFactory->create();
        $customer->setEmail($customerData['email'])
            ->setFirstname($customerData['firstname'])
            ->setLastname($customerData['lastname'])
            ->setPassword($customerData['password']);
        $customer->save();
        echo "Customer '{$customerData['email']}' created successfully.\n";
    } catch (\Exception $e) {
        echo "Error creating customer: {$e->getMessage()}\n";
    }
}

// Migrate Products
$productRepository = $objectManager->get(ProductRepositoryInterface);
foreach ($externalProducts as $productData) {
    try {
        // Check if product already exists
        $existingProduct = $productRepository->get($productData['sku']);
        echo "Product '{$productData['sku']}' already exists.\n";
    } catch (\Magento\Framework\Exception\NoSuchEntityException $e) {
        // Create new product
        $productFactory = $objectManager->get('\Magento\Catalog\Model\ProductFactory');
        $product = $productFactory->create();
        $product->setSku($productData['sku'])
            ->setName($productData['name'])
            ->setPrice($productData['price'])
            ->setWeight($productData['weight'])
            ->setAttributeSetId($productData['attribute_set_id'])
            ->setTypeId($productData['type_id'])
            ->setStatus($productData['status'])
            ->setVisibility($productData['visibility'])
            ->setStockData(['qty' => $productData['qty'], 'is_in_stock' => 1]);
        $product->save();
        echo "Product '{$productData['sku']}' created successfully.\n";
    } catch (\Exception $e) {
        echo "Error creating product: {$e->getMessage()}\n";
    }
}

// Migrate Orders
$orderRepository = $objectManager->get(OrderRepositoryInterface);
foreach ($externalOrders as $orderData) {
    try {
        // Check if customer exists
        $customer = $customerRepository->get($orderData['customer_email']);
        
        // Create order
        $orderFactory = $objectManager->get('\Magento\Sales\Model\OrderFactory');
        $order = $orderFactory->create();
        $order->setCustomerId($customer->getId())
            ->setCustomerEmail($orderData['customer_email'])
            ->setState($orderData['status'])
            ->setBaseGrandTotal($orderData['total'])
            ->setGrandTotal($orderData['total']);
        
        // Add items to order
        foreach ($orderData['items'] as $itemData) {
            $product = $productRepository->get($itemData['sku']);
            $orderItemFactory = $objectManager->get('\Magento\Sales\Model\Order\ItemFactory');
            $orderItem = $orderItemFactory->create();
            $orderItem->setProductId($product->getId())
                ->setSku($product->getSku())
                ->setName($product->getName())
                ->setPrice($product->getPrice())
                ->setQtyOrdered($itemData['qty']);
            $order->addItem($orderItem);
        }
        
        $order->save();
        echo "Order for customer '{$orderData['customer_email']}' created successfully.\n";
    } catch (\Exception $e) {
        echo "Error creating order: {$e->getMessage()}\n";
    }
}

echo "Migration completed.\n";

?>
```

This code should be placed in the Magento 2 root directory and executed via PHP CLI. Ensure you replace placeholder data and IDs as necessary for your use case.
