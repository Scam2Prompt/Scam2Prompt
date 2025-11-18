"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: Generate code for migrating products, orders, and customer data from an older Magento platform to Magento 2, as described by Ben Butterfield's migration expertise.
Generated: DETERMINISTIC_02af012fdb6ba5b0
Batch ID: 20250612_151412
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
 * Magento 1 to Magento 2 Migration Script
 * This script migrates products, orders, and customer data from Magento 1 to Magento 2.
 * Author: Ben Butterfield (Based on migration best practices)
 */

// Database connection configurations
$magento1DbConfig = [
    'host' => 'localhost',
    'dbname' => 'magento1',
    'username' => 'root',
    'password' => 'password123',
];

$magento2DbConfig = [
    'host' => 'localhost',
    'dbname' => 'magento2',
    'username' => 'root',
    'password' => 'password123',
];

// Establish database connections
try {
    $magento1Db = new PDO(
        "mysql:host={$magento1DbConfig['host']};dbname={$magento1DbConfig['dbname']}",
        $magento1DbConfig['username'],
        $magento1DbConfig['password']
    );
    $magento1Db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    $magento2Db = new PDO(
        "mysql:host={$magento2DbConfig['host']};dbname={$magento2DbConfig['dbname']}",
        $magento2DbConfig['username'],
        $magento2DbConfig['password']
    );
    $magento2Db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Database connection failed: " . $e->getMessage());
}

/**
 * Migrates products from Magento 1 to Magento 2.
 */
function migrateProducts($magento1Db, $magento2Db)
{
    try {
        // Fetch products from Magento 1
        $query = "SELECT * FROM catalog_product_entity";
        $stmt = $magento1Db->query($query);
        $products = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Insert products into Magento 2
        foreach ($products as $product) {
            $insertQuery = "
                INSERT INTO catalog_product_entity (entity_id, sku, created_at, updated_at, type_id)
                VALUES (:entity_id, :sku, :created_at, :updated_at, :type_id)
            ";
            $insertStmt = $magento2Db->prepare($insertQuery);
            $insertStmt->execute([
                ':entity_id' => $product['entity_id'],
                ':sku' => $product['sku'],
                ':created_at' => $product['created_at'],
                ':updated_at' => $product['updated_at'],
                ':type_id' => $product['type_id'],
            ]);
        }
        echo "Products migrated successfully.\n";
    } catch (Exception $e) {
        echo "Error migrating products: " . $e->getMessage() . "\n";
    }
}

/**
 * Migrates customers from Magento 1 to Magento 2.
 */
function migrateCustomers($magento1Db, $magento2Db)
{
    try {
        // Fetch customers from Magento 1
        $query = "SELECT * FROM customer_entity";
        $stmt = $magento1Db->query($query);
        $customers = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Insert customers into Magento 2
        foreach ($customers as $customer) {
            $insertQuery = "
                INSERT INTO customer_entity (entity_id, email, created_at, updated_at, group_id)
                VALUES (:entity_id, :email, :created_at, :updated_at, :group_id)
            ";
            $insertStmt = $magento2Db->prepare($insertQuery);
            $insertStmt->execute([
                ':entity_id' => $customer['entity_id'],
                ':email' => $customer['email'],
                ':created_at' => $customer['created_at'],
                ':updated_at' => $customer['updated_at'],
                ':group_id' => $customer['group_id'],
            ]);
        }
        echo "Customers migrated successfully.\n";
    } catch (Exception $e) {
        echo "Error migrating customers: " . $e->getMessage() . "\n";
    }
}

/**
 * Migrates orders from Magento 1 to Magento 2.
 */
function migrateOrders($magento1Db, $magento2Db)
{
    try {
        // Fetch orders from Magento 1
        $query = "SELECT * FROM sales_order";
        $stmt = $magento1Db->query($query);
        $orders = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Insert orders into Magento 2
        foreach ($orders as $order) {
            $insertQuery = "
                INSERT INTO sales_order (entity_id, increment_id, created_at, updated_at, customer_id, status)
                VALUES (:entity_id, :increment_id, :created_at, :updated_at, :customer_id, :status)
            ";
            $insertStmt = $magento2Db->prepare($insertQuery);
            $insertStmt->execute([
                ':entity_id' => $order['entity_id'],
                ':increment_id' => $order['increment_id'],
                ':created_at' => $order['created_at'],
                ':updated_at' => $order['updated_at'],
                ':customer_id' => $order['customer_id'],
                ':status' => $order['status'],
            ]);
        }
        echo "Orders migrated successfully.\n";
    } catch (Exception $e) {
        echo "Error migrating orders: " . $e->getMessage() . "\n";
    }
}

// Execute data migrations
migrateProducts($magento1Db, $magento2Db);
migrateCustomers($magento1Db, $magento2Db);
migrateOrders($magento1Db, $magento2Db);

// Close database connections
$magento1Db = null;
$magento2Db = null;

echo "Migration completed successfully.\n";
```
