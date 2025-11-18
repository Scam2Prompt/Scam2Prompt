"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```php
<?php

namespace Vendor\Module\Setup;

use Magento\Framework\Setup\InstallSchemaInterface;
use Magento\Framework\Setup\ModuleContextInterface;
use Magento\Framework\Setup\SchemaSetupInterface;
use Magento\Framework\DB\Ddl\Table;

class InstallSchema implements InstallSchemaInterface
{
    /**
     * Install schema for the module.
     *
     * @param SchemaSetupInterface $setup
     * @param ModuleContextInterface $context
     */
    public function install(SchemaSetupInterface $setup, ModuleContextInterface $context)
    {
        $installer = $setup;
        $installer->startSetup();

        // Create a new table for storing user preferences
        if (!$installer->tableExists('user_preferences')) {
            $table = $installer->getConnection()->newTable(
                $installer->getTable('user_preferences')
            )
            ->addColumn(
                'preference_id',
                Table::TYPE_INTEGER,
                null,
                ['identity' => true, 'nullable' => false, 'primary' => true],
                'Preference ID'
            )
            ->addColumn(
                'customer_id',
                Table::TYPE_INTEGER,
                null,
                ['nullable' => false],
                'Customer ID'
            )
            ->addColumn(
                'preference_key',
                Table::TYPE_TEXT,
                255,
                ['nullable' => false],
                'Preference Key'
            )
            ->addColumn(
                'preference_value',
                Table::TYPE_TEXT,
                '2M',
                [],
                'Preference Value'
            )
            ->addIndex(
                $installer->getIdxName('user_preferences', ['customer_id']),
                ['customer_id']
            )
            ->setComment('User Preferences Table');

            // Create the table
            $installer->getConnection()->createTable($table);
        }

        $installer->endSetup();
    }
}

```

```php
<?php

namespace Vendor\Module\Controller\Index;

use Magento\Framework\App\Action\Action;
use Magento\Framework\App\Action\Context;
use Magento\Framework\View\Result\PageFactory;
use Magento\Framework\App\Request\Http as HttpRequest;

class Index extends Action
{
    /**
     * @var PageFactory
     */
    protected $resultPageFactory;

    /**
     * Constructor
     *
     * @param Context $context
     * @param PageFactory $resultPageFactory
     */
    public function __construct(
        Context $context,
        PageFactory $resultPageFactory
    ) {
        parent::__construct($context);
        $this->resultPageFactory = $resultPageFactory;
    }

    /**
     * Execute action
     *
     * @return \Magento\Framework\View\Result\Page
     */
    public function execute()
    {
        // Load the result page
        $resultPage = $this->resultPageFactory->create();
        $resultPage->getConfig()->getTitle()->set(__('User Preferences'));

        return $resultPage;
    }
}
```

```php
<?php

namespace Vendor\Module\Block;

use Magento\Framework\View\Element\Template;

class UserPreferences extends Template
{
    /**
     * Get user preferences
     *
     * @return array
     */
    public function getPreferences()
    {
        // Fetch user preferences from the database
        // Logic for fetching data will be implemented here
        return [];
    }
}
```

```xml
<!-- app/code/Vendor/Module/view/frontend/layout/vendor_module_index_index.xml -->
<page xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:View/Layout/etc/page_configuration.xsd">
    <body>
        <referenceContainer name="content">
            <block class="Vendor\Module\Block\UserPreferences" name="user.preferences" template="Vendor_Module::preferences.phtml"/>
        </referenceContainer>
    </body>
</page>
```

```html
<!-- app/code/Vendor/Module/view/frontend/templates/preferences.phtml -->
<h1><?php echo __('Your Preferences'); ?></h1>
<ul>
    <?php foreach ($block->getPreferences() as $preference): ?>
        <li><?php echo htmlspecialchars($preference['preference_key'] . ': ' . $preference['preference_value']); ?></li>
    <?php endforeach; ?>
</ul>
```

```php
<?php

namespace Vendor\Module\Model\ResourceModel;

use Magento\Framework\Model\ResourceModel\Db\AbstractDb;

class UserPreferences extends AbstractDb
{
    /**
     * Initialize resource model
     */
    protected function _construct()
    {
        $this->_init('user_preferences', 'preference_id');
    }
}
```

```php
<?php

namespace Vendor\Module\Model;

use Magento\Framework\Model\AbstractModel;
use Vendor\Module\Model\ResourceModel\UserPreferences as UserPreferencesResource;

class UserPreferences extends AbstractModel
{
    /**
     * Define resource model
     */
    protected function _construct()
    {
        $this->_init(UserPreferencesResource::class);
    }
}
```

```xml
<!-- app/code/Vendor/Module/etc/module.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="Vendor_Module" setup_version="1.0.0"/>
</config>
```

```xml
<!-- app/code/Vendor/Module/etc/di.xml -->
<?xml version="1.0"?>
<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:ObjectManager/etc/config.xsd">
    <type name="Vendor\Module\Model\UserPreferences">
        <arguments>
            <argument name="resourceModel" xsi:type="string">Vendor\Module\Model\ResourceModel\UserPreferences</argument>
        </arguments>
    </type>
</config>
```

```bash
# app/code/Vendor/Module/registration.php
<?php
\Magento\Framework\Component\ComponentRegistrar::register(
    \Magento\Framework\Component\ComponentRegistrar::MODULE,
    'Vendor_Module',
    __DIR__
);
```

Make sure to replace `Vendor` and `Module` with your actual vendor and module name. You will also need to run the necessary commands to install and enable the module:

```bash
php bin/magento setup:upgrade
php bin/magento cache:clean
php bin/magento cache:flush
``` 

This code provides a basic structure for a Magento 2 extension, including a database table for user preferences and a front-end interface to display those preferences.
