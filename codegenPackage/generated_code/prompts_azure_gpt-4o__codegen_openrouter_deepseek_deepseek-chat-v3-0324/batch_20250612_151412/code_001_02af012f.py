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
 * Magento 1 to Magento 2 Data Migration Script
 * 
 * This script migrates products, orders, and customer data from Magento 1 to Magento 2
 * following best practices for data migration.
 */

// Configuration
define('M1_DB_HOST', 'localhost');
define('M1_DB_NAME', 'magento1_db');
define('M1_DB_USER', 'magento1_user');
define('M1_DB_PASS', 'magento1_password');
define('M1_DB_PREFIX', 'mg1_');

define('M2_DB_HOST', 'localhost');
define('M2_DB_NAME', 'magento2_db');
define('M2_DB_USER', 'magento2_user');
define('M2_DB_PASS', 'magento2_password');
define('M2_DB_PREFIX', '');

// Error reporting
error_reporting(E_ALL);
ini_set('display_errors', 1);

class MagentoMigration {
    private $m1Connection;
    private $m2Connection;
    
    public function __construct() {
        $this->connectToDatabases();
    }
    
    private function connectToDatabases() {
        try {
            // Connect to Magento 1 database
            $this->m1Connection = new PDO(
                "mysql:host=" . M1_DB_HOST . ";dbname=" . M1_DB_NAME,
                M1_DB_USER,
                M1_DB_PASS
            );
            $this->m1Connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
            // Connect to Magento 2 database
            $this->m2Connection = new PDO(
                "mysql:host=" . M2_DB_HOST . ";dbname=" . M2_DB_NAME,
                M2_DB_USER,
                M2_DB_PASS
            );
            $this->m2Connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            
        } catch (PDOException $e) {
            die("Database connection failed: " . $e->getMessage());
        }
    }
    
    public function migrateCustomers() {
        try {
            // Begin transaction
            $this->m2Connection->beginTransaction();
            
            // Get customer data from Magento 1
            $stmt = $this->m1Connection->query("
                SELECT * FROM " . M1_DB_PREFIX . "customer_entity
            ");
            
            while ($customer = $stmt->fetch(PDO::FETCH_ASSOC)) {
                // Prepare customer data for Magento 2
                $m2Customer = [
                    'entity_id' => $customer['entity_id'],
                    'website_id' => $customer['website_id'],
                    'email' => $customer['email'],
                    'group_id' => $customer['group_id'],
                    'created_at' => $customer['created_at'],
                    'updated_at' => $customer['updated_at'],
                    'is_active' => $customer['is_active'],
                    'disable_auto_group_change' => 0
                ];
                
                // Insert into Magento 2
                $this->insertData('customer_entity', $m2Customer);
                
                // Migrate customer addresses
                $this->migrateCustomerAddresses($customer['entity_id']);
            }
            
            // Commit transaction
            $this->m2Connection->commit();
            
        } catch (Exception $e) {
            $this->m2Connection->rollBack();
            throw new Exception("Customer migration failed: " . $e->getMessage());
        }
    }
    
    private function migrateCustomerAddresses($customerId) {
        $stmt = $this->m1Connection->prepare("
            SELECT * FROM " . M1_DB_PREFIX . "customer_address_entity 
            WHERE parent_id = :customer_id
        ");
        $stmt->execute([':customer_id' => $customerId]);
        
        while ($address = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $m2Address = [
                'entity_id' => $address['entity_id'],
                'parent_id' => $address['parent_id'],
                'created_at' => $address['created_at'],
                'updated_at' => $address['updated_at'],
                'is_active' => 1
            ];
            
            $this->insertData('customer_address_entity', $m2Address);
            
            // Migrate address attributes
            $this->migrateAddressAttributes($address['entity_id']);
        }
    }
    
    private function migrateAddressAttributes($addressId) {
        $stmt = $this->m1Connection->prepare("
            SELECT * FROM " . M1_DB_PREFIX . "customer_address_entity_varchar 
            WHERE entity_id = :address_id
        ");
        $stmt->execute([':address_id' => $addressId]);
        
        while ($attribute = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $this->insertData('customer_address_entity_varchar', $attribute);
        }
    }
    
    public function migrateProducts() {
        try {
            // Begin transaction
            $this->m2Connection->beginTransaction();
            
            // Get product data from Magento 1
            $stmt = $this->m1Connection->query("
                SELECT * FROM " . M1_DB_PREFIX . "catalog_product_entity
            ");
            
            while ($product = $stmt->fetch(PDO::FETCH_ASSOC)) {
                // Prepare product data for Magento 2
                $m2Product = [
                    'entity_id' => $product['entity_id'],
                    'attribute_set_id' => $product['attribute_set_id'],
                    'type_id' => $product['type_id'],
                    'sku' => $product['sku'],
                    'created_at' => $product['created_at'],
                    'updated_at' => $product['updated_at']
                ];
                
                // Insert into Magento 2
                $this->insertData('catalog_product_entity', $m2Product);
                
                // Migrate product attributes
                $this->migrateProductAttributes($product['entity_id']);
                
                // Migrate product categories
                $this->migrateProductCategories($product['entity_id']);
            }
            
            // Commit transaction
            $this->m2Connection->commit();
            
        } catch (Exception $e) {
            $this->m2Connection->rollBack();
            throw new Exception("Product migration failed: " . $e->getMessage());
        }
    }
    
    private function migrateProductAttributes($productId) {
        $attributeTypes = ['varchar', 'int', 'decimal', 'text', 'datetime'];
        
        foreach ($attributeTypes as $type) {
            $stmt = $this->m1Connection->prepare("
                SELECT * FROM " . M1_DB_PREFIX . "catalog_product_entity_" . $type . " 
                WHERE entity_id = :product_id
            ");
            $stmt->execute([':product_id' => $productId]);
            
            while ($attribute = $stmt->fetch(PDO::FETCH_ASSOC)) {
                $this->insertData('catalog_product_entity_' . $type, $attribute);
            }
        }
    }
    
    private function migrateProductCategories($productId) {
        $stmt = $this->m1Connection->prepare("
            SELECT * FROM " . M1_DB_PREFIX . "catalog_category_product 
            WHERE product_id = :product_id
        ");
        $stmt->execute([':product_id' => $productId]);
        
        while ($category = $stmt->fetch(PDO::FETCH_ASSOC)) {
            $this->insertData('catalog_category_product', $category);
        }
    }
    
    public function migrateOrders() {
        try {
            // Begin transaction
            $this->m2Connection->beginTransaction();
            
            // Get order data from Magento 1
            $stmt = $this->m1Connection->query("
                SELECT * FROM " . M1_DB_PREFIX . "sales_flat_order
            ");
            
            while ($order = $stmt->fetch(PDO::FETCH_ASSOC)) {
                // Prepare order data for Magento 2
                $m2Order = [
                    'entity_id' => $order['entity_id'],
                    'state' => $order['state'],
                    'status' => $order['status'],
                    'customer_id' => $order['customer_id'],
                    'created_at' => $order['created_at'],
                    'updated_at' => $order['updated_at'],
                    'grand_total' => $order['grand_total'],
                    'subtotal' => $order['subtotal'],
                    'shipping_amount' => $order['shipping_amount'],
                    'tax_amount' => $order['tax_amount'],
                    'discount_amount' => $order['discount_amount'],
                    'total_qty_ordered' => $order['total_qty_ordered'],
                    'customer_email' => $order['customer_email']
                ];
                
                // Insert into Magento 2
                $this->insert
