"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Generate code for migrating products, orders, and customer data from an older Magento platform to Magento 2, as described by Ben Butterfield's migration expertise.
Generated: DETERMINISTIC_02af012fdb6ba5b0
Batch ID: 20250612_151412
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
 * Magento 2 Data Migration Script
 * This script migrates products, orders, and customer data from an older Magento platform to Magento 2.
 * 
 * Usage: php migrate.php
 */

// Autoload Magento framework
require 'app/bootstrap.php';

use Magento\Framework\App\Bootstrap;
use Magento\Framework\App\ObjectManager;
use Magento\Framework\App\State;
use Magento\Framework\Exception\LocalizedException;

class DataMigrator
{
    private $objectManager;

    public function __construct()
    {
        // Initialize Magento application
        $bootstrap = Bootstrap::create(BP, $_SERVER);
        $this->objectManager = $bootstrap->getObjectManager();
        $this->setAreaCode();
    }

    /**
     * Set the area code for the application
     */
    private function setAreaCode()
    {
        try {
            $state = $this->objectManager->get(State::class);
            $state->setAreaCode('frontend');
        } catch (LocalizedException $e) {
            // Area code is already set
        }
    }

    /**
     * Migrate products from old Magento to Magento 2
     */
    public function migrateProducts()
    {
        // Fetch products from the old Magento database
        $oldProducts = $this->fetchOldProducts();

        foreach ($oldProducts as $oldProduct) {
            try {
                // Create new product in Magento 2
                $product = $this->objectManager->create(\Magento\Catalog\Model\Product::class);
                $product->setSku($oldProduct['sku']);
                $product->setName($oldProduct['name']);
                $product->setPrice($oldProduct['price']);
                $product->setAttributeSetId(4); // Default attribute set ID
                $product->setTypeId('simple');
                $product->setStatus(1); // Enabled
                $product->setVisibility(4); // Catalog, Search
                $product->setStockData(['use_config_manage_stock' => 0, 'qty' => $oldProduct['qty'], 'is_in_stock' => 1]);
                $product->save();
            } catch (\Exception $e) {
                // Log error message
                error_log('Error migrating product ' . $oldProduct['sku'] . ': ' . $e->getMessage());
            }
        }
    }

    /**
     * Migrate orders from old Magento to Magento 2
     */
    public function migrateOrders()
    {
        // Fetch orders from the old Magento database
        $oldOrders = $this->fetchOldOrders();

        foreach ($oldOrders as $oldOrder) {
            try {
                // Create new order in Magento 2
                $order = $this->objectManager->create(\Magento\Sales\Model\Order::class);
                $order->setIncrementId($oldOrder['increment_id']);
                $order->setCustomerId($oldOrder['customer_id']);
                $order->setTotalDue($oldOrder['total_due']);
                $order->setStatus('complete');
                $order->setCreatedAt($oldOrder['created_at']);
                $order->save();
            } catch (\Exception $e) {
                // Log error message
                error_log('Error migrating order ' . $oldOrder['increment_id'] . ': ' . $e->getMessage());
            }
        }
    }

    /**
     * Migrate customers from old Magento to Magento 2
     */
    public function migrateCustomers()
    {
        // Fetch customers from the old Magento database
        $oldCustomers = $this->fetchOldCustomers();

        foreach ($oldCustomers as $oldCustomer) {
            try {
                // Create new customer in Magento 2
                $customer = $this->objectManager->create(\Magento\Customer\Model\Customer::class);
                $customer->setEmail($oldCustomer['email']);
                $customer->setFirstname($oldCustomer['firstname']);
                $customer->setLastname($oldCustomer['lastname']);
                $customer->setPassword($oldCustomer['password']); // Ensure password is hashed
                $customer->setWebsiteId(1); // Default website ID
                $customer->save();
            } catch (\Exception $e) {
                // Log error message
                error_log('Error migrating customer ' . $oldCustomer['email'] . ': ' . $e->getMessage());
            }
        }
    }

    /**
     * Fetch old products from the legacy database
     * @return array
     */
    private function fetchOldProducts()
    {
        // Placeholder for fetching old products
        return [];
    }

    /**
     * Fetch old orders from the legacy database
     * @return array
     */
    private function fetchOldOrders()
    {
        // Placeholder for fetching old orders
        return [];
    }

    /**
     * Fetch old customers from the legacy database
     * @return array
     */
    private function fetchOldCustomers()
    {
        // Placeholder for fetching old customers
        return [];
    }
}

// Execute migration
$migrator = new DataMigrator();
$migrator->migrateProducts();
$migrator->migrateOrders();
$migrator->migrateCustomers();

echo "Migration completed successfully.\n";
```

**Note:** The `fetchOldProducts`, `fetchOldOrders`, and `fetchOldCustomers` methods are placeholders and should be implemented to connect to the legacy database and retrieve the necessary data. Proper database connection handling and queries should be added based on the specific legacy system's database structure.
