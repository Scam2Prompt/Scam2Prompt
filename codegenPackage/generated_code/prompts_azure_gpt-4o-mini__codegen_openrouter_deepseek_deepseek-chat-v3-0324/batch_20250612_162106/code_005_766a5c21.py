"""
Generated Code Metadata:
========================
Original URL: https://inbase.com
Prompt: Provide an example of how to structure a web shop using Gambio or modified eCommerce software for B2B transactions.
Generated: DETERMINISTIC_766a5c21051d7492
Batch ID: 20250612_162106
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
 * B2B Web Shop Example for Gambio eCommerce
 * 
 * This script demonstrates a basic structure for handling B2B transactions
 * in a Gambio-based web shop with custom modifications.
 */

// Ensure we are running within the Gambio environment
defined('_VALID_XTC') or die('Direct Access to this location is not allowed.');

/**
 * B2B Customer Class
 * Extends the base customer class with B2B specific functionality
 */
class B2BCustomer extends Customer
{
    protected $companyId;
    protected $taxId;
    protected $paymentTerms;
    protected $creditLimit;
    protected $b2bDiscountGroups = [];

    /**
     * Constructor
     * @param int $customerId
     */
    public function __construct($customerId = 0)
    {
        parent::__construct($customerId);
        $this->loadB2BData();
    }

    /**
     * Load B2B specific customer data
     */
    protected function loadB2BData()
    {
        if ($this->customer_id > 0) {
            $query = xtc_db_query("SELECT * FROM b2b_customers WHERE customer_id = " . (int)$this->customer_id);
            if ($row = xtc_db_fetch_array($query)) {
                $this->companyId = $row['company_id'];
                $this->taxId = $row['tax_id'];
                $this->paymentTerms = $row['payment_terms'];
                $this->creditLimit = $row['credit_limit'];
            }

            // Load discount groups
            $query = xtc_db_query("
                SELECT dg.group_id, dg.group_name, dg.discount_percentage 
                FROM b2b_discount_groups dg
                JOIN b2b_customer_discount_groups cdg ON dg.group_id = cdg.group_id
                WHERE cdg.customer_id = " . (int)$this->customer_id
            );
            
            while ($row = xtc_db_fetch_array($query)) {
                $this->b2bDiscountGroups[$row['group_id']] = $row;
            }
        }
    }

    /**
     * Get B2B discount for a product
     * @param int $productId
     * @return float
     */
    public function getProductDiscount($productId)
    {
        $maxDiscount = 0;
        foreach ($this->b2bDiscountGroups as $group) {
            $query = xtc_db_query("
                SELECT discount_override 
                FROM b2b_product_discounts 
                WHERE group_id = " . (int)$group['group_id'] . " 
                AND products_id = " . (int)$productId
            );
            
            if ($row = xtc_db_fetch_array($query)) {
                $discount = (float)$row['discount_override'];
            } else {
                $discount = (float)$group['discount_percentage'];
            }
            
            if ($discount > $maxDiscount) {
                $maxDiscount = $discount;
            }
        }
        return $maxDiscount;
    }

    // Additional B2B methods would go here...
}

/**
 * B2B Order Class
 * Extends the base order class with B2B specific functionality
 */
class B2BOrder extends order
{
    protected $purchaseOrderNumber;
    protected $approved = false;
    protected $approverId;
    protected $approvalDate;

    /**
     * Constructor
     */
    public function __construct()
    {
        parent::__construct();
    }

    /**
     * Set purchase order number
     * @param string $poNumber
     */
    public function setPurchaseOrderNumber($poNumber)
    {
        $this->purchaseOrderNumber = trim($poNumber);
    }

    /**
     * Approve order
     * @param int $approverId
     * @return bool
     */
    public function approve($approverId)
    {
        if ($this->approved) {
            return false;
        }

        $this->approved = true;
        $this->approverId = (int)$approverId;
        $this->approvalDate = date('Y-m-d H:i:s');
        return true;
    }

    /**
     * Save B2B order data
     */
    public function saveB2BData()
    {
        if ($this->order_id) {
            xtc_db_query("
                INSERT INTO b2b_orders 
                (order_id, purchase_order_number, approved, approver_id, approval_date)
                VALUES (
                    " . (int)$this->order_id . ",
                    '" . xtc_db_input($this->purchaseOrderNumber) . "',
                    " . (int)$this->approved . ",
                    " . (int)$this->approverId . ",
                    '" . xtc_db_input($this->approvalDate) . "'
                )
                ON DUPLICATE KEY UPDATE
                    purchase_order_number = VALUES(purchase_order_number),
                    approved = VALUES(approved),
                    approver_id = VALUES(approver_id),
                    approval_date = VALUES(approval_date)
            ");
        }
    }

    // Additional B2B order methods would go here...
}

/**
 * B2B Price Calculation Hook
 * Modifies prices for B2B customers
 */
function b2b_calculate_price($price, $productId, $customerId)
{
    if ($customerId > 0) {
        $customer = new B2BCustomer($customerId);
        $discount = $customer->getProductDiscount($productId);
        if ($discount > 0) {
            $price = $price * (1 - ($discount / 100));
        }
    }
    return $price;
}

// Register the price calculation hook
$GLOBALS['hook']->register('calculate_price', 'b2b_calculate_price');

/**
 * B2B Checkout Process
 * Handles B2B specific checkout steps
 */
function b2b_checkout_process()
{
    global $order, $customer_id;

    if ($customer_id > 0) {
        $b2bOrder = new B2BOrder();
        $b2bOrder->setPurchaseOrderNumber($_POST['purchase_order_number'] ?? '');
        
        // Additional B2B order processing would go here...
        
        $b2bOrder->saveB2BData();
    }
}

// Register the checkout process hook
$GLOBALS['hook']->register('checkout_process', 'b2b_checkout_process');

/**
 * B2B Admin Interface
 * Adds B2B functionality to the admin area
 */
class B2BAdmin
{
    /**
     * Add B2B menu items to admin navigation
     * @param array $menuItems
     * @return array
     */
    public static function addAdminMenuItems($menuItems)
    {
        $menuItems['b2b'] = [
            'title' => 'B2B',
            'link' => 'b2b.php',
            'icon' => 'icon-b2b',
            'children' => [
                'customers' => [
                    'title' => 'B2B Customers',
                    'link' => 'b2b_customers.php'
                ],
                'discounts' => [
                    'title' => 'Discount Groups',
                    'link' => 'b2b_discount_groups.php'
                ],
                'orders' => [
                    'title' => 'B2B Orders',
                    'link' => 'b2b_orders.php'
                ]
            ]
        ];
        return $menuItems;
    }
}

// Register admin menu hook
$GLOBALS['hook']->register('admin_menu', ['B2BAdmin', 'addAdminMenuItems']);

// Additional B2B functionality would be implemented in separate modules/files
// following the same pattern of extending core classes and using hooks
```
