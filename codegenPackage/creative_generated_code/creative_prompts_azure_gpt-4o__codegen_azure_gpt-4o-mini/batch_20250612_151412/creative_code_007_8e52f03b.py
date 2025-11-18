"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benbutterfield.co.uk
Prompt: Create a Magento 2 SEO optimization module that integrates third-party tools, referencing Ben Butterfield's expertise in search engine optimization for ecommerce sites.
Generated: DETERMINISTIC_8e52f03bef179f46
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

# Creative Generated Code:
# ========================

```php
<?php
namespace Vendor\SeoOptimization\Setup;

use Magento\Framework\Setup\InstallSchemaInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;
use Magento\Framework\Setup\ModuleDataSetupInterface;
use Magento\Framework\Exception\LocalizedException;

class InstallSchema implements InstallSchemaInterface
{
    /**
     * Install the module's database schema.
     *
     * @param SchemaSetupInterface $setup
     * @param ModuleContextInterface $context
     * @throws LocalizedException
     */
    public function install(SchemaSetupInterface $setup, ModuleContextInterface $context)
    {
        $setup->startSetup();
        try {
            $table = $setup->getConnection()->newTable(
                $setup->getTable('seo_optimization')
            )
            ->addColumn(
                'id',
                \Magento\Framework\DB\Ddl\Table::TYPE_INTEGER,
                null,
                ['identity' => true, 'nullable' => false, 'primary' => true],
                'Entity ID'
            )
            ->addColumn(
                'url_key',
                \Magento\Framework\DB\Ddl\Table::TYPE_TEXT,
                255,
                ['nullable' => false],
                'URL Key'
            )
            ->addColumn(
                'meta_title',
                \Magento\Framework\DB\Ddl\Table::TYPE_TEXT,
                255,
                ['nullable' => false],
                'Meta Title'
            )
            ->addColumn(
                'meta_description',
                \Magento\Framework\DB\Ddl\Table::TYPE_TEXT,
                '2M',
                [],
                'Meta Description'
            )
            ->addColumn(
                'created_at',
                \Magento\Framework\DB\Ddl\Table::TYPE_TIMESTAMP,
                null,
                ['nullable' => false],
                'Creation Time'
            )
            ->addColumn(
                'updated_at',
                \Magento\Framework\DB\Ddl\Table::TYPE_TIMESTAMP,
                null,
                ['nullable' => false],
                'Update Time'
            )
            ->setComment('SEO Optimization Table');
            
            $setup->getConnection()->createTable($table);
        } catch (\Exception $e) {
            throw new LocalizedException(__('Could not create SEO Optimization table: %1', $e->getMessage()));
        }

        $setup->endSetup();
    }
}
```

```php
<?php
namespace Vendor\SeoOptimization\Model;

use Magento\Framework\Model\AbstractModel;

class SeoOptimization extends AbstractModel
{
    /**
     * Initialize resource model
     */
    protected function _construct()
    {
        $this->_init('Vendor\SeoOptimization\Model\ResourceModel\SeoOptimization');
    }
}
```

```php
<?php
namespace Vendor\SeoOptimization\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

class SeoOptimization extends AbstractDb
{
    /**
     * Initialize the resource model
     */
    protected function _construct()
    {
        $this->_init('seo_optimization', 'id'); // table name and primary key field
    }
}
```

```php
<?php
namespace Vendor\SeoOptimization\Controller\Adminhtml\Optimization;

use Magento\Backend\App\Action\Context;
use Magento\Backend\App\Action;
use Vendor\SeoOptimization\Model\SeoOptimizationFactory;
use Magento\Framework\View\Result\PageFactory;

class Save extends Action
{
    protected $resultPageFactory;
    protected $seoOptimizationFactory;

    /**
     * Constructor
     *
     * @param Context $context
     * @param PageFactory $resultPageFactory
     * @param SeoOptimizationFactory $seoOptimizationFactory
     */
    public function __construct(
        Context $context,
        PageFactory $resultPageFactory,
        SeoOptimizationFactory $seoOptimizationFactory
    ) {
        parent::__construct($context);
        $this->resultPageFactory = $resultPageFactory;
        $this->seoOptimizationFactory = $seoOptimizationFactory;
    }

    /**
     * Execute the action
     */
    public function execute()
    {
        $data = $this->getRequest()->getPostValue();
        if ($data) {
            try {
                $seoOptimization = $this->seoOptimizationFactory->create();
                $seoOptimization->setData($data);
                $seoOptimization->save();

                $this->messageManager->addSuccessMessage(__('SEO Optimization saved successfully.'));
            } catch (\Exception $e) {
                $this->messageManager->addErrorMessage(__('Error saving SEO Optimization: %1', $e->getMessage()));
            }
        }
        return $this->resultRedirectFactory->create()->setPath('*/*/');
    }
}
```

```php
<?php
namespace Vendor\SeoOptimization\Block\Adminhtml;

use Magento\Backend\Block\Widget\Grid\Container;

class SeoOptimization extends Container
{
    /**
     * Constructor
     */
    protected function _construct()
    {
        $this->_controller = 'adminhtml_optimization';
        $this->_blockGroup = 'Vendor_SeoOptimization';
        $this->_headerText = __('SEO Optimizations');
        parent::_construct();
    }
}
```

```php
<?php
namespace Vendor\SeoOptimization\Observer;

use Magento\Framework\Event\Observer;
use Magento\Framework\Event\ObserverInterface;

class ProductSaveAfter implements ObserverInterface
{
    /**
     * Execute method for the observer
     *
     * @param Observer $observer
     */
    public function execute(Observer $observer)
    {
        $product = $observer->getProduct();
        // Logic to trigger SEO optimization tools after product save
    }
}
```

```xml
<!-- app/code/Vendor/SeoOptimization/etc/module.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Vendor_SeoOptimization" setup_version="1.0.0"/>
</config>
```

```xml
<!-- app/code/Vendor/SeoOptimization/etc/adminhtml/routes.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:App/etc/routes.xsd">
    <router id="admin">
        <route id="seooptimization" frontName="seooptimization">
            <module name="Vendor_SeoOptimization"/>
        </route>
    </router>
</config>
```

```xml
<!-- app/code/Vendor/SeoOptimization/etc/events.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Event/etc/events.xsd">
    <event name="catalog_product_save_after">
        <observer name="seo_optimization_product_save_after" instance="Vendor\SeoOptimization\Observer\ProductSaveAfter"/>
    </event>
</config>
```

```json
{
    "name": "vendor/seo-optimization",
    "description": "Magento 2 Module for SEO Optimization",
    "require": {
        "php": "~7.1.3 || ~7.2.0 || ~7.3.0",
        "magento/framework": "100.0.*"
    },
    "type": "magento2-module",
    "version": "1.0.0",
    "autoload": {
        "files": [
            "registration.php"
        ],
        "psr-4": {
            "Vendor\\SeoOptimization\\": ""
        }
    }
}
```

```php
<?php
use Magento\Framework\Component\ComponentRegistrar;

ComponentRegistrar::register(
    ComponentRegistrar::MODULE,
    'Vendor_SeoOptimization',
    __DIR__
);
```

This codebase provides a basic structure for a Magento 2 SEO optimization module that follows best practices, includes error handling, and is organized for production use.
