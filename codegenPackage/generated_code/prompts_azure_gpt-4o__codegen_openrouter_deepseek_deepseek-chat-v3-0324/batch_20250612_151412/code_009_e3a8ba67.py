"""
Generated Code Metadata:
========================
Original URL: https://benbutterfield.co.uk
Prompt: Develop a Magento 2 extension to improve user experience and simplify site management, inspired by the custom extensions Ben Butterfield created for tomfoolerylondon.co.uk.
Generated: DETERMINISTIC_e3a8ba6712004c32
Batch ID: 20250612_151412
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2001/XMLSchema-instance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```php
<?php
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
namespace Tomfoolery\UX\Setup;

use Magento\Framework\Setup\InstallSchemaInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;
use Magento\Framework\DB\Ddl\Table;

class InstallSchema implements InstallSchemaInterface
{
    /**
     * Installs DB schema for the module
     *
     * @param SchemaSetupInterface $setup
     * @param ModuleContextInterface $context
     * @throws \Zend_Db_Exception
     */
    public function install(SchemaSetupInterface $setup, ModuleContextInterface $context)
    {
        $installer = $setup;
        $installer->startSetup();

        // Create table for storing quick order data
        $table = $installer->getConnection()->newTable(
            $installer->getTable('tomfoolery_ux_quickorder')
        )->addColumn(
            'quickorder_id',
            Table::TYPE_INTEGER,
            null,
            ['identity' => true, 'unsigned' => true, 'nullable' => false, 'primary' => true],
            'Quick Order ID'
        )->addColumn(
            'customer_id',
            Table::TYPE_INTEGER,
            null,
            ['unsigned' => true, 'nullable' => false],
            'Customer ID'
        )->addColumn(
            'product_skus',
            Table::TYPE_TEXT,
            '64k',
            [],
            'Product SKUs'
        )->addColumn(
            'created_at',
            Table::TYPE_TIMESTAMP,
            null,
            ['nullable' => false, 'default' => Table::TIMESTAMP_INIT],
            'Creation Time'
        )->addIndex(
            $installer->getIdxName('tomfoolery_ux_quickorder', ['customer_id']),
            ['customer_id']
        )->addForeignKey(
            $installer->getFkName(
                'tomfoolery_ux_quickorder',
                'customer_id',
                'customer_entity',
                'entity_id'
            ),
            'customer_id',
            $installer->getTable('customer_entity'),
            'entity_id',
            Table::ACTION_CASCADE
        )->setComment(
            'Tomfoolery UX Quick Order Table'
        );
        $installer->getConnection()->createTable($table);

        $installer->endSetup();
    }
}
```

```php
<?php
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
namespace Tomfoolery\UX\Controller\QuickOrder;

use Magento\Framework\App\Action\Action;
use Magento\Framework\App\Action\Context;
use Magento\Framework\Controller\Result\JsonFactory;
use Magento\Customer\Model\Session;
use Tomfoolery\UX\Model\QuickOrderFactory;

class Save extends Action
{
    /**
     * @var JsonFactory
     */
    protected $resultJsonFactory;

    /**
     * @var Session
     */
    protected $customerSession;

    /**
     * @var QuickOrderFactory
     */
    protected $quickOrderFactory;

    /**
     * @param Context $context
     * @param JsonFactory $resultJsonFactory
     * @param Session $customerSession
     * @param QuickOrderFactory $quickOrderFactory
     */
    public function __construct(
        Context $context,
        JsonFactory $resultJsonFactory,
        Session $customerSession,
        QuickOrderFactory $quickOrderFactory
    ) {
        parent::__construct($context);
        $this->resultJsonFactory = $resultJsonFactory;
        $this->customerSession = $customerSession;
        $this->quickOrderFactory = $quickOrderFactory;
    }

    /**
     * Save quick order action
     *
     * @return \Magento\Framework\Controller\Result\Json
     */
    public function execute()
    {
        $result = $this->resultJsonFactory->create();
        $customerId = $this->customerSession->getCustomerId();
        $skus = $this->getRequest()->getParam('skus');

        if (!$customerId) {
            return $result->setData(['success' => false, 'message' => __('Please login to save quick orders.')]);
        }

        if (empty($skus)) {
            return $result->setData(['success' => false, 'message' => __('No products selected.')]);
        }

        try {
            $quickOrder = $this->quickOrderFactory->create();
            $quickOrder->setCustomerId($customerId)
                ->setProductSkus(json_encode($skus))
                ->save();

            return $result->setData(['success' => true, 'message' => __('Quick order saved successfully.')]);
        } catch (\Exception $e) {
            return $result->setData(['success' => false, 'message' => __('Error saving quick order.')]);
        }
    }
}
```

```php
<?php
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
namespace Tomfoolery\UX\Model;

use Magento\Framework\Model\AbstractModel;

class QuickOrder extends AbstractModel
{
    /**
     * Initialize resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init('Tomfoolery\UX\Model\ResourceModel\QuickOrder');
    }
}
```

```php
<?php
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
namespace Tomfoolery\UX\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

class QuickOrder extends AbstractDb
{
    /**
     * Initialize resource model
     *
     * @return void
     */
    protected function _construct()
    {
        $this->_init('tomfoolery_ux_quickorder', 'quickorder_id');
    }
}
```

```php
<?php
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
namespace Tomfoolery\UX\Block;

use Magento\Framework\View\Element\Template;
use Magento\Customer\Model\Session;
use Tomfoolery\UX\Model\ResourceModel\QuickOrder\CollectionFactory;

class QuickOrder extends Template
{
    /**
     * @var Session
     */
    protected $customerSession;

    /**
     * @var CollectionFactory
     */
    protected $collectionFactory;

    /**
     * @param Template\Context $context
     * @param Session $customerSession
     * @param CollectionFactory $collectionFactory
     * @param array $data
     */
    public function __construct(
        Template\Context $context,
        Session $customerSession,
        CollectionFactory $collectionFactory,
        array $data = []
    ) {
        parent::__construct($context, $data);
        $this->customerSession = $customerSession;
        $this->collectionFactory = $collectionFactory;
    }

    /**
     * Get saved quick orders for current customer
     *
     * @return \Tomfoolery\UX\Model\ResourceModel\QuickOrder\Collection
     */
    public function getSavedQuickOrders()
    {
        if (!$this->customerSession->isLoggedIn()) {
            return [];
        }

        return $this->collectionFactory->create()
            ->addFieldToFilter('customer_id', $this->customerSession->getCustomerId())
            ->setOrder('created_at', 'DESC');
    }
}
```

```xml
<?xml version="1.0"?>
<!--
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
-->
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Tomfoolery_UX" setup_version="1.0.0">
        <sequence>
            <module name="Magento_Customer"/>
            <module name="Magento_Checkout"/>
        </sequence>
    </module>
</config>
```

```xml
<?xml version="1.0"?>
<!--
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license     MIT
 */
-->
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/config.xsd">
    <default>
        <tomfoolery_ux>
            <quickorder>
                <enabled>1</enabled>
                <max_saved>5</max_saved>
            </quickorder>
        </tomfoolery_ux>
    </default>
</config>
```

```xml
<?xml version="1.0"?>
<!--
/**
 * @package     Tomfoolery_UX
 * @author      Ben Butterfield
 * @license
