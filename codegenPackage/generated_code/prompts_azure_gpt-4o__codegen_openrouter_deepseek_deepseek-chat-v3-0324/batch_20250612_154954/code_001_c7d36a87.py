"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: Generate code to develop a custom eCommerce solution using Magento with ERP software integration, as described on inbase.com.
Generated: DETERMINISTIC_c7d36a871e33210d
Batch ID: 20250612_154954
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
 * Magento ERP Integration Module
 * 
 * This module integrates Magento eCommerce with external ERP systems.
 * Features include product sync, order sync, inventory updates, and customer data exchange.
 */

// Ensure the script is not accessed directly
if (!defined('MAGENTO_ROOT')) {
    die('Direct access denied');
}

class Inbase_ErpIntegration_Model_Observer
{
    /**
     * Sync products from ERP to Magento
     * 
     * @param Varien_Event_Observer $observer
     * @throws Exception
     */
    public function syncProductsFromErp(Varien_Event_Observer $observer)
    {
        try {
            $erpClient = $this->_getErpClient();
            $products = $erpClient->getProducts();
            
            foreach ($products as $erpProduct) {
                $this->_createOrUpdateProduct($erpProduct);
            }
            
            Mage::log('Product sync completed successfully', null, 'erp_integration.log');
        } catch (Exception $e) {
            Mage::log('Product sync failed: ' . $e->getMessage(), null, 'erp_integration.log');
            throw $e;
        }
    }

    /**
     * Sync orders from Magento to ERP
     * 
     * @param Varien_Event_Observer $observer
     * @throws Exception
     */
    public function syncOrdersToErp(Varien_Event_Observer $observer)
    {
        try {
            $order = $observer->getEvent()->getOrder();
            $erpClient = $this->_getErpClient();
            
            $erpOrderData = $this->_prepareOrderData($order);
            $erpClient->createOrder($erpOrderData);
            
            Mage::log('Order #' . $order->getIncrementId() . ' synced to ERP', null, 'erp_integration.log');
        } catch (Exception $e) {
            Mage::log('Order sync failed: ' . $e->getMessage(), null, 'erp_integration.log');
            throw $e;
        }
    }

    /**
     * Get configured ERP client
     * 
     * @return Inbase_ErpIntegration_Model_Client_Abstract
     * @throws Exception
     */
    protected function _getErpClient()
    {
        $clientType = Mage::getStoreConfig('erp_integration/settings/client_type');
        $clientClass = 'Inbase_ErpIntegration_Model_Client_' . ucfirst($clientType);
        
        if (!class_exists($clientClass)) {
            throw new Exception('Invalid ERP client type configured');
        }
        
        return new $clientClass();
    }

    /**
     * Create or update Magento product from ERP data
     * 
     * @param array $erpProduct
     * @throws Exception
     */
    protected function _createOrUpdateProduct($erpProduct)
    {
        $product = Mage::getModel('catalog/product');
        $productId = $product->getIdBySku($erpProduct['sku']);
        
        if ($productId) {
            $product->load($productId);
        }
        
        try {
            $product->setSku($erpProduct['sku'])
                ->setName($erpProduct['name'])
                ->setDescription($erpProduct['description'])
                ->setShortDescription($erpProduct['short_description'])
                ->setPrice($erpProduct['price'])
                ->setWeight($erpProduct['weight'])
                ->setStatus(Mage_Catalog_Model_Product_Status::STATUS_ENABLED)
                ->setVisibility(Mage_Catalog_Model_Product_Visibility::VISIBILITY_BOTH)
                ->setTaxClassId($erpProduct['tax_class_id'])
                ->setStockData(array(
                    'qty' => $erpProduct['qty'],
                    'is_in_stock' => $erpProduct['qty'] > 0 ? 1 : 0
                ));
            
            // Handle categories
            if (isset($erpProduct['categories'])) {
                $categoryIds = $this->_getCategoryIds($erpProduct['categories']);
                $product->setCategoryIds($categoryIds);
            }
            
            $product->save();
        } catch (Exception $e) {
            Mage::log('Failed to save product SKU ' . $erpProduct['sku'] . ': ' . $e->getMessage(), null, 'erp_integration.log');
            throw $e;
        }
    }

    /**
     * Prepare order data for ERP system
     * 
     * @param Mage_Sales_Model_Order $order
     * @return array
     */
    protected function _prepareOrderData($order)
    {
        $items = array();
        foreach ($order->getAllVisibleItems() as $item) {
            $items[] = array(
                'sku' => $item->getSku(),
                'name' => $item->getName(),
                'qty' => $item->getQtyOrdered(),
                'price' => $item->getPrice()
            );
        }
        
        return array(
            'order_id' => $order->getIncrementId(),
            'customer_id' => $order->getCustomerId(),
            'customer_email' => $order->getCustomerEmail(),
            'billing_address' => $this->_prepareAddressData($order->getBillingAddress()),
            'shipping_address' => $this->_prepareAddressData($order->getShippingAddress()),
            'items' => $items,
            'subtotal' => $order->getSubtotal(),
            'shipping_amount' => $order->getShippingAmount(),
            'tax_amount' => $order->getTaxAmount(),
            'grand_total' => $order->getGrandTotal(),
            'payment_method' => $order->getPayment()->getMethod(),
            'created_at' => $order->getCreatedAt()
        );
    }

    /**
     * Prepare address data for ERP system
     * 
     * @param Mage_Sales_Model_Order_Address $address
     * @return array
     */
    protected function _prepareAddressData($address)
    {
        return array(
            'firstname' => $address->getFirstname(),
            'lastname' => $address->getLastname(),
            'street' => $address->getStreetFull(),
            'city' => $address->getCity(),
            'region' => $address->getRegion(),
            'postcode' => $address->getPostcode(),
            'country_id' => $address->getCountryId(),
            'telephone' => $address->getTelephone()
        );
    }

    /**
     * Get category IDs from ERP category names
     * 
     * @param array $categoryNames
     * @return array
     */
    protected function _getCategoryIds($categoryNames)
    {
        $categoryIds = array();
        foreach ($categoryNames as $name) {
            $category = Mage::getModel('catalog/category')->loadByAttribute('name', $name);
            if ($category && $category->getId()) {
                $categoryIds[] = $category->getId();
            }
        }
        return $categoryIds;
    }
}

/**
 * Abstract ERP Client
 */
abstract class Inbase_ErpIntegration_Model_Client_Abstract
{
    /**
     * Get products from ERP
     * 
     * @return array
     */
    abstract public function getProducts();

    /**
     * Create order in ERP
     * 
     * @param array $orderData
     * @return bool
     */
    abstract public function createOrder($orderData);

    /**
     * Update inventory in ERP
     * 
     * @param array $inventoryData
     * @return bool
     */
    abstract public function updateInventory($inventoryData);
}

/**
 * System configuration
 */
class Inbase_ErpIntegration_Model_System_Config_Source_Client
{
    /**
     * Options getter
     *
     * @return array
     */
    public function toOptionArray()
    {
        return array(
            array('value' => 'sap', 'label' => Mage::helper('erp_integration')->__('SAP')),
            array('value' => 'oracle', 'label' => Mage::helper('erp_integration')->__('Oracle')),
            array('value' => 'netsuite', 'label' => Mage::helper('erp_integration')->__('NetSuite')),
            array('value' => 'custom', 'label' => Mage::helper('erp_integration')->__('Custom'))
        );
    }
}
```
